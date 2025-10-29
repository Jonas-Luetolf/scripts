#!/bin/python3

import sys
from itertools import product

assert len(sys.argv) >= 2, "Usage: truth-table EXPRESSION"

func = " ".join(sys.argv[1:])

# aquivalents for not
func = func.replace("!", "not")

# aquivalents for and
func = func.replace("&", "and")
func = func.replace("*", "and")

# aquivalents for or
func = func.replace("|", "or")
func = func.replace("+", "or")

#TODO: check expression validity

# extract variables
vars = list(sorted(set(filter(lambda x: x.isupper(), func))))
print(f"Detected Vars: {vars}")

combinations = list(product([0, 1], repeat=len(vars)))

# print header
print(" ".join(vars) + " | Result")
print("-" * ((len(vars) - 1) * 3 + 9))

# print rows
for comb in combinations:
    local_vars = {var: bool(comb[i]) for i, var in enumerate(vars)}
    result = eval(func, {}, local_vars)

    print(" ".join(str(int(local_vars[var])) for var in vars) + f" | {int(result)}")
