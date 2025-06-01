from proof_generator import (
    prove_irrationality,
    explain_hcf_lcm,
    explain_polynomial_factors,
    explain_zeroes_relationship,
)

def handle_math_query(query):
    query = query.lower()

    if "irrational" in query or "prove root" in query:
        return "\n".join(prove_irrationality(query))

    elif "hcf" in query and "lcm" in query:
        numbers = [int(s) for s in query.split() if s.isdigit()]
        if len(numbers) == 2:
            return "\n".join(explain_hcf_lcm(numbers[0], numbers[1]))
        else:
            return "❌ Please provide exactly two numbers for HCF and LCM."

    elif "factor" in query:
        return explain_polynomial_factors(query)

    elif "zero" in query and "relationship" in query:
        return explain_zeroes_relationship(query)
    
    elif "quadratic" in query.lower() and "sum" in query.lower() and "product" in query.lower():
        from proof_generator.construct_from_roots import construct_quadratic_from_sum_product_extracted
        return construct_quadratic_from_sum_product_extracted(query)


    else:
        return "❓ Query not recognized. Try something like:\n- 'Prove root 5 is irrational'\n- 'HCF and LCM of 72 and 120'\n- 'Factor x² + 5x + 6'\n- 'Relationship between zeroes and coefficients'."
