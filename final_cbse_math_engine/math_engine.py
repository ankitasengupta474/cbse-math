# STEP 1: Add this to `math_engine.py`

import json
from os import getenv
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
groq_llm = Groq(api_key=getenv("GROQ_API_KEY"))


def interpret_query_with_llm(query: str) -> dict:
    prompt = f"""
    You are a CBSE math query parser.
    Given a user query, output its structured intent and any numbers it refers to.

    If the query is like:
    "Find a quadratic polynomial whose sum and product of roots are -3 and 2 respectively."
    then respond strictly in this JSON format:

    {{
      "intent": "construct_quadratic_from_roots",
      "sum": -3,
      "product": 2
    }}

    If it is not this kind of query, then reply:
    {{ "intent": "unknown" }}

    Query: "{query}"

    ONLY reply with the JSON. Do not explain anything.
    """

    response = groq_llm.chat.completions.create(
        model="llama3-8b-8192",
        messages=[{"role": "user", "content": prompt}]
    )
    try:
        return json.loads(response.choices[0].message.content.strip())
    except Exception as e:
        return {"intent": "unknown", "error": str(e)}


# STEP 2: Patch inside handle_math_query(query)

def handle_math_query(query: str):
    query = query.strip().lower()

    if "factor" in query:
        from proof_generator.polynomial_factors import explain_polynomial_factors
        return explain_polynomial_factors(query)

    elif "irrational" in query or "prove" in query and "root" in query:
        from proof_generator.irrationality import prove_irrationality
        return prove_irrationality(query)

    elif "relationship" in query and "zero" in query:
        from proof_generator.zeroes_relationship import explain_zeroes_relationship
        return explain_zeroes_relationship(query)

    elif "hcf" in query or "lcm" in query:
        from proof_generator.hcf_lcm import explain_hcf_lcm
        import re 
        nums = list(map(int, re.findall(r"\d+", query)))
        if len(nums) >= 2:
            return explain_hcf_lcm(nums[0], nums[1])
        else:
            return ["❌ Couldn't extract two numbers for HCF/LCM."]
        

    elif "quadratic" in query and "sum" in query and "product" in query:
        from proof_generator.construct_from_roots import construct_quadratic_from_sum_product_extracted
        return construct_quadratic_from_sum_product_extracted(query)

    else:
        # fallback to LLM parser
        parsed = interpret_query_with_llm(query)
        if parsed.get("intent") == "construct_quadratic_from_roots":
            from proof_generator.construct_from_roots import construct_quadratic_from_sum_product_extracted
            # build fake input query
            return [
                "LLM parsed intent: construct_quadratic_from_roots",
                f"Sum = {parsed.get('sum')}, Product = {parsed.get('product')}",
                f"→ x² - ({parsed['sum']})x + ({parsed['product']})"
            ]

        return ["❌ Sorry, I couldn't understand the query."]


# STEP 3: Patch zeroes_relationship.py condition

# Old:
# if "relationship" in query and ("zero" in query or "zeroes" in query):

# New:
# if "relationship" in query and re.search(r"x\\s*\\^?2", query):
