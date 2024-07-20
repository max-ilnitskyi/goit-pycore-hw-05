from re import finditer
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator:
    pattern = r"\s[+-]?([0-9]*[.])?[0-9]+\s"
    for match in finditer(pattern, text):
        yield float(match.group().strip())


def sum_profit(text: str, func: Callable) -> float:
    result = sum(func(text))
    return result
