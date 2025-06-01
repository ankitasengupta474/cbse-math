import re
from sympy import symbols, Eq, factor, solveset, S, sympify, lambdify
import matplotlib.pyplot as plt
import numpy as np

x = symbols('x')

superscript_map = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴",
    "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹",
    "+": "⁺", "-": "⁻"
}

def to_superscript(expr: str) -> str:
    def replacer(match):
        power = match.group(1)
        return ''.join(superscript_map.get(ch, ch) for ch in power)
    return re.sub(r"\*\*(\d+)", replacer, expr)

def explain_polynomial_factors(query: str):
    try:
        # Extract polynomial expression
        match = re.search(r'([\-+xX^0-9\s]+)=?\s*0?', query)
        if not match:
            return ["❌ Could not find a valid polynomial expression in the query."]
        
        raw_expr = match.group(1).strip()

        # Clean up expression
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

        # Create function for plotting
        f = lambdify(x, expr, modules=['numpy'])
        x_vals = np.linspace(-10, 10, 400)
        y_vals = f(x_vals)

        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, label=f'y = {expr_str}', color='blue')
        plt.axhline(0, color='black', lw=1)
        plt.axvline(0, color='black', lw=1)

        # Highlight zeroes if any
        if zeroes:
            real_zeroes = [float(r.evalf()) for r in zeroes]
            for z in real_zeroes:
                plt.plot(z, 0, 'ro')
                plt.text(z, 0.5, f'{z:.2f}', ha='center', fontsize=8)

        plt.title(f"Graph of y = {expr_str}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.savefig("polynomial_plot.png")

        return steps

    except Exception as e:
        return [f"❌ Could not process polynomial. Error: {e}"]
