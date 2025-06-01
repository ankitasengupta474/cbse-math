import re

def construct_quadratic_from_sum_product_extracted(query: str) -> list:
    try:
        query = query.lower()

        # Match phrases like:
        # "sum is 3", "sum of roots are 3", "sum equals 3", "sum = 3"
        sum_match = re.search(r"sum\s+(of\s+(the\s+)?roots\s*)?(is|equals|=|are|:)?\s*(-?\d+)", query)
        prod_match = re.search(r"product\s+(of\s+(the\s+)?roots\s*)?(is|equals|=|are|:)?\s*(-?\d+)", query)

        if not sum_match or not prod_match:
            return ["❌ Could not extract valid sum and product from the query."]

        s = int(sum_match.group(4))
        p = int(prod_match.group(4))

        steps = []
        steps.append("We are given:")
        steps.append(f"→ Sum of roots (α + β) = {s}")
        steps.append(f"→ Product of roots (α × β) = {p}")
        steps.append("From quadratic theory, the general form is:")
        steps.append("→ x² - (α + β)x + (α × β)")
        steps.append(f"✅ Final equation: x² - {s}x + {p}")

        return steps

    except Exception as e:
        return [f"❌ Error while processing quadratic construction: {e}"]
