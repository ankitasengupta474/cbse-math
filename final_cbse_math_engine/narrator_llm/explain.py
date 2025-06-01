
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.expanduser(r"C:\Users\ADMIN\Desktop\cbse_maths\.env"))
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def explain_math_proof(logic_type, steps):
    prompt = f"Explain the following {logic_type} proof in CBSE Class X style:\n\n" + "\n".join(steps)
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"LLM Error: {e}"
