# app.py
import streamlit as st
from final_cbse_math_engine.math_engine import handle_math_query

st.set_page_config(page_title="CBSE Math Engine", layout="centered")

st.title("📚 CBSE Math Query Solver")

query = st.text_input("🔍 Enter your math question")

if st.button("🧠 Solve") and query:
    response = handle_math_query(query)
    st.markdown("### ✅ Answer:")
    st.write(response)

    # Optional: show graph if generated
    import os
    if os.path.exists("final_cbse_math_engine/polynomial_plot.png"):
        st.image("final_cbse_math_engine/polynomial_plot.png", caption="📈 Polynomial Plot")
