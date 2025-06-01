import re

def prove_irrationality(query: str) -> list:
    # Normalize input: replace "root" with sqrt notation
    query = query.lower().replace(" ", "").replace("root", "√")

    # Match patterns: 3√2, √5+3, √7
    match = re.match(r".*?(?:(\d+)?√(\d+))([+-]\d+)?", query)
    if not match:
        return ["❌ Could not parse a square root expression like √n, √n ± k, or r√n."]

    multiplier = match.group(1)  # may be None
    root_val = int(match.group(2))
    offset = match.group(3)      # may be None

    sqrt_expr = f"√{root_val}"
    steps = []

    # Case 1: r * √n
    if multiplier and not offset:
        r = int(multiplier)
        expr = f"{r}√{root_val}"
        steps.append(f"**Proving that {expr} is irrational**\n")
        steps.append(f"Step 1:\nAssume that {expr} is rational.\n")
        steps.append(f"Step 2:\nThen {sqrt_expr} = (a/b)/{r} = a/({r}b), which is rational.\n")
        steps.append(f"Step 3:\nBut {sqrt_expr} is irrational, so this is a contradiction.\n")
        steps.append(f"✅ Therefore, {expr} is irrational.")

    # Case 2: √n ± k
    elif offset:
        sign = "+" if "+" in offset else "-"
        k = int(offset)
        expr = f"{sqrt_expr}{offset}"
        steps.append(f"**Proving that {expr} is irrational**\n")
        steps.append(f"Step 1:\nAssume that {expr} is rational.\n")
        steps.append(f"Step 2:\nThen {sqrt_expr} = (a/b) {'-' if sign == '+' else '+'} {abs(k)}\n")
        steps.append(f"Step 3:\nSince (a/b) {'-' if sign == '+' else '+'} {abs(k)} is rational, this implies {sqrt_expr} is rational.\n")
        steps.append(f"Step 4:\nBut {sqrt_expr} is irrational — contradiction.\n")
        steps.append(f"✅ Hence, our assumption is false. {expr} is irrational.")

    # Case 3: √n only
    else:
        expr = sqrt_expr
        steps.append(f"**Proving that {expr} is irrational**\n")
        steps.append(f"Step 1:\nAssume {expr} is rational. That is, {expr} = a/b where a and b are coprime integers and b ≠ 0.\n")
        steps.append(f"Step 2:\nSquaring both sides, we get: {root_val} = a² / b² => a² = {root_val} * b²\n")
        steps.append(f"Step 3:\nSo a² is divisible by {root_val} => a is divisible by {root_val}\n")
        steps.append(f"Step 4:\nLet a = {root_val} * c. Then a² = {root_val}² * c² => a² = {root_val} * b² => b² = {root_val} * c²\n")
        steps.append(f"Step 5:\nSo b is also divisible by {root_val}\n")
        steps.append(f"Step 6:\nThen a and b have a common factor {root_val} — contradiction.\n")
        steps.append(f"✅ Therefore, {expr} is irrational.")

    return steps
