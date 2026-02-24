from itertools import product
from mytools.resources.argparser import parse_args

AND_AQUIVALENTS = ["&", "*", "^"]
OR_AQUIVALENTS = ["|", "+", "v"]
NOT_AQUIVALENTS = ["!"]


def parse_expression(func: str):
    # aquivalents for not
    for not_equiv in NOT_AQUIVALENTS:
        func = func.replace(not_equiv, "not ")

    for and_equiv in AND_AQUIVALENTS:
        func = func.replace(and_equiv, " and ")

    for or_equiv in OR_AQUIVALENTS:
        func = func.replace(or_equiv, " or ")

    vars = list(sorted(set(filter(lambda x: x.isupper(), func))))
    return func, vars


def evaluate_expression(func: str, vars: dict) -> bool:
    results = {}
    combinations = list(product([0, 1], repeat=len(vars)))

    for comb in combinations:
        local_vars = {var: bool(comb[i]) for i, var in enumerate(vars)}
        results.update({comb: eval(func, {}, local_vars)})
    return results


def main():
    args, _ = parse_args()
    assert len(args) >= 1, "Usage: truth-table EXPRESSION"

    print(args)
    # extract variables
    func, vars = parse_expression(" ".join(args))

    print(f"Detected Vars: {vars}")

    # print header
    print(" ".join(vars) + " | Result")
    print("-" * ((len(vars) - 1) * 3 + 9))

    results = evaluate_expression(func, vars)
    # print rows
    for comb, result in results.items():
        print(f"{" ".join(map(str, comb))} | {int(result)}")


if __name__ == "__main__":
    main()
