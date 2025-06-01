# zeroes_relationship.py

import matplotlib.pyplot as plt
import numpy as np

def explain_zeroes_relationship(query: str):
    """
    Explains the relationship between zeroes and coefficients of a quadratic polynomial.
    Returns a list of explanation steps and saves a plot.
    """
    query = query.lower()

    if "relationship" in query and ("zero" in query or "zeroes" in query):
        # Let's use a sample quadratic: x² - 3x + 2
        a, b, c = 1, -3, 2
        x_vals = np.linspace(-1, 4, 400)
        y_vals = a * x_vals**2 + b * x_vals + c

        # Plot the graph
        plt.figure()
        plt.plot(x_vals, y_vals, label='y = x² - 3x + 2')
        plt.axhline(0, color='black', lw=1)
        plt.axvline(0, color='black', lw=1)
        plt.title("Graph of y = x² - 3x + 2")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.legend()
        plt.savefig("zeroes_plot.png")

        return [
            "We are given the quadratic polynomial: x² - 3x + 2.",
            "Let the zeroes be α and β.",
            "From the equation, α = 1 and β = 2 (since (x - 1)(x - 2) = 0).",
            "Sum of zeroes α + β = 1 + 2 = 3.",
            "Product of zeroes α × β = 1 × 2 = 2.",
            "Now, compare with the general form ax² + bx + c:",
            "Sum of zeroes = -b/a = -(-3)/1 = 3 ✔",
            "Product of zeroes = c/a = 2/1 = 2 ✔",
            "✅ Hence, verified: Sum = -b/a and Product = c/a.",
            "📊 A graph of the polynomial has been saved as `zeroes_plot.png`."
        ]

    return ["❌ Please enter a valid query like 'Relationship between zeroes and coefficients of x^2 - 3x + 2'."]
