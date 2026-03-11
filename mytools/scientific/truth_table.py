from itertools import product
from mytools.resources.argparser import parse_args

AND_AQUIVALENTS = ["&", "*", "^", "&&"]
OR_AQUIVALENTS = ["|", "+", "v", "||"]
NOT_AQUIVALENTS = ["!"]


def parse_expression(func: str):
    """
    Normalize a logical expression so it can be evaluated by Python.

    Replaces supported logical operator equivalents with Python's
    "not", "and", and "or", and extracts sorted uppercase variables.

    Args:
        func (str): Logical expression containing uppercase variables.

    Returns:
        tuple[str, list[str]]: Normalized expression and sorted variables.
    """
    for not_equiv in NOT_AQUIVALENTS:
        func = func.replace(not_equiv, "not ")

    for and_equiv in AND_AQUIVALENTS:
        func = func.replace(and_equiv, " and ")

    for or_equiv in OR_AQUIVALENTS:
        func = func.replace(or_equiv, " or ")

    vars = list(sorted(set(filter(lambda x: x.isupper(), func))))
    return func, vars


def evaluate_expression(func: str, vars: dict) -> bool:
    """
    Evaluate a logical expression for all boolean combinations.

    Args:
        func (str): Python-compatible logical expression.
        vars (list[str]): Variables used in the expression.

    Returns:
        dict[tuple[int, ...], bool]: Mapping of input combinations to
        evaluation results.
    """
    results = {}
    combinations = list(product([0, 1], repeat=len(vars)))

    for comb in combinations:
        local_vars = {var: bool(comb[i]) for i, var in enumerate(vars)}
        results.update({comb: eval(func, {}, local_vars)})

    return results

def generate_truth_table(expression: str) -> [dict, str, vars]:
    """
    Generate the truth table for a logical expression.

    Args:
        expression (str): Logical expression string.

    Returns:
        tuple[dict, str, list[str]]: Truth table, normalized expression,
        and sorted variables.
    """
    func, vars = parse_expression(expression)
    return evaluate_expression(func, vars), func, vars

def main():
    args, _ = parse_args()
    assert len(args) >= 1, "Usage: truth-table <EXPRESSION>"

    results, func, vars = generate_truth_table(" ".join(args))

    # print header
    print(f"Parsed Function: {func}")
    print(" ".join(vars) + " | Result")
    print("-" * ((len(vars) - 1) * 3 + 9))

    # print rows
    for comb, result in results.items():
        print(f"{" ".join(map(str, comb))} | {int(result)}")


if __name__ == "__main__":
    main()