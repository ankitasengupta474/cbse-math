# classX5m.py — Fully patched with:
# ✅ Dynamic path fix
# ✅ Proper import
# ✅ Plot reset fix

import streamlit as st
import sys
import os

# Ensure root path is available for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../")))

from cbse_maths.final_cbse_math_engine.math_engine1 import handle_math_query

st.set_page_config(page_title="CBSE Class X Math Reasoning", layout="wide")

st.title("🧠 CBSE Class X Math Reasoning Assistant")
st.markdown("This app helps understand **Real Numbers** and **Polynomials** through symbolic logic, LLM, and visual graphs.")

query = st.text_input("🔍 Enter your math query (e.g., 'Prove √7 is irrational', 'HCF and LCM of 72 and 120', 'Factor x² + 5x + 6'):")

if st.button("Get Answer"):
    if query.strip():
        with st.spinner("🔎 Thinking..."):
            # Remove old plot if exists
            if os.path.exists("polynomial_plot.png"):
                os.remove("polynomial_plot.png")

            result = handle_math_query(query)

            st.markdown("### 📘 Explanation")
            if isinstance(result, list):
                for line in result:
                    st.markdown(f"- {line}")
            else:
                st.markdown(result)

            if os.path.exists("polynomial_plot.png"):
                st.image("polynomial_plot.png", caption="Polynomial Graph", use_column_width=True)
    else:
        st.warning("Please enter a valid query.")
