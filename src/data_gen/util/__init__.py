"""Utility."""

from typing import Any, Callable, Union

ConvertToStrRules = list[tuple[Callable[..., bool], Callable[..., str]]]
DEFAULT_CONVERT_TO_STR_RULES: ConvertToStrRules = [
    (lambda x: isinstance(x, str), lambda x: x),
    (lambda x: isinstance(x, int), lambda x: str(x)),
]


def convert_list_to_str(
        row: list[Any],
        sep: str = ',',
        rules: ConvertToStrRules = DEFAULT_CONVERT_TO_STR_RULES) -> str:
    """Convert list to string.

    Args:
        row (list[Any]): Target row.
        sep (str): Separator.
        rules (ConvertToStrRules): Convert rules.

    Returns:
        str: Result.
    """
    for i, v in enumerate(row):
        for check, convert in rules:
            if check(v):
                row[i] = convert(v)
                break
        else:
            row[i] = str(v)
    return sep.join(row)


def convert_dict_to_list(d: dict, keys: list[Union[str,
                                                   list[str]]]) -> list[Any]:
    # TODO: implement
    return []
