import re
from sympy import symbols, Eq, factor, solveset, S, sympify
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x')

# Superscript mapping
superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴",
    "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹",
    "+": "⁺", "-": "⁻"
}

def to_superscript(expr: str) -> str:
    """
    Convert '**2' to '²', '**10' to '¹⁰', etc.
    """
    def replacer(match):
        power = match.group(1)
        return ''.join(superscript_map.get(ch, ch) for ch in power)
    
    return re.sub(r"\*\*(\d+)", replacer, expr)

def explain_polynomial_factors(query: str):
    try:
        # Extract polynomial expression using regex
        match = re.search(r'([\-+xX^0-9\s]+)=?\s*0?', query)
        if not match:
            return ["❌ Could not find a valid polynomial expression in the query."]
        
        raw_expr = match.group(1).strip()

        # Clean up: insert * and convert ^ to **
        cleaned = raw_expr.replace("^", "**")
        cleaned = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', cleaned)
        cleaned = re.sub(r'([a-zA-Z])(\d)', r'\1*\2', cleaned)

        expr = sympify(cleaned)
        factored = factor(expr)
        zeroes = solveset(Eq(expr, 0), x, domain=S.Reals)

        expr_str = to_superscript(str(expr))
        factored_str = to_superscript(str(factored))

        steps = [
            f"We are given the polynomial: {expr_str}",
            f"Factoring the polynomial gives: {factored_str}",
            f"The zeroes of the polynomial are: {sorted(list(zeroes)) if zeroes else 'No real zeroes'}"
        ]

        # Plot if quadratic
        coeffs = expr.as_poly().all_coeffs()
        if len(coeffs) == 3:
            a, b, c = [float(c) for c in coeffs]
        else:
            a, b, c = 1, 0, 0

        x_vals = np.linspace(-10, 10, 400)
        y_vals = a * x_vals**2 + b * x_vals + c

        plt.figure()
        plt.plot(x_vals, y_vals, label=f'y = {expr}')
        plt.axhline(0, color='black', lw=1)
        plt.axvline(0, color='black', lw=1)
        plt.title(f"Graph of y = {expr}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.savefig("polynomial_plot.png")

        return steps

    except Exception as e:
        return [f"❌ Could not process polynomial. Error: {e}"]
