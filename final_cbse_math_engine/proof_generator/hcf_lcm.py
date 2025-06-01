
from collections import Counter
from math import gcd
from functools import reduce

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

def factor_counter(n):
    return Counter(prime_factors(n))

def get_hcf_lcm(a, b):
    fa = factor_counter(a)
    fb = factor_counter(b)

    hcf = 1
    lcm = 1

    # HCF: Product of smallest powers of common primes
    for prime in (fa.keys() & fb.keys()):
        hcf *= prime ** min(fa[prime], fb[prime])

    # LCM: Product of greatest powers of all primes involved
    all_primes = fa.keys() | fb.keys()
    for prime in all_primes:
        lcm *= prime ** max(fa.get(prime, 0), fb.get(prime, 0))

    return hcf, lcm, fa, fb

def explain_hcf_lcm(a, b):
    hcf, lcm, fa, fb = get_hcf_lcm(a, b)
    steps = []
    steps.append(f"**Finding HCF and LCM of {a} and {b} using the Fundamental Theorem of Arithmetic**")
    steps.append(f"Step 1: Prime factorisation of {a} = " + " × ".join([f"{p}^{fa[p]}" for p in sorted(fa)]))
    steps.append(f"Step 2: Prime factorisation of {b} = " + " × ".join([f"{p}^{fb[p]}" for p in sorted(fb)]))
    steps.append(f"Step 3: HCF is the product of the smallest powers of common primes:")
    hcf_terms = [f"{p}^{min(fa[p], fb[p])}" for p in (fa.keys() & fb.keys())]
    steps.append(" ⇒ HCF = " + " × ".join(hcf_terms) + f" = {hcf}")
    steps.append(f"Step 4: LCM is the product of the greatest powers of all primes involved:")
    lcm_terms = [f"{p}^{max(fa.get(p, 0), fb.get(p, 0))}" for p in sorted(fa.keys() | fb.keys())]
    steps.append(" ⇒ LCM = " + " × ".join(lcm_terms) + f" = {lcm}")
    steps.append(f"✅ Final Answer: HCF = {hcf}, LCM = {lcm}")
    return steps
