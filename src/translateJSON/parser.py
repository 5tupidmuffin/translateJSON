from typing import Dict, List, Tuple

from translateJSON.CONSTANTS import (
    CLOSING_BRACE,
    CLOSING_BRACKET,
    COLON,
    COMMA,
    OPENING_BRACE,
    OPENING_BRACKET,
)

JSON_Types = str | bool | float | int | None


def parser(
    tokens: list[JSON_Types],
) -> Tuple[JSON_Types | List | Dict, List[JSON_Types]]:
    """
    parse given list of `tokens` into sensible `Dict` or `List`
    """
    token = tokens[0]

    if token == OPENING_BRACKET:
        return parse_array(tokens[1:])
    elif token == OPENING_BRACE:
        return parse_object(tokens[1:])
    else:
        return token, tokens[1:]


def parse_array(
    tokens: list[JSON_Types],
) -> Tuple[List, List[JSON_Types]]:
    result_array = []
    token = tokens[0]

    if token == CLOSING_BRACKET:
        return result_array, tokens[1:]

    while True:
        value, tokens = parser(tokens)
        result_array.append(value)

        token = tokens[0]
        if token == CLOSING_BRACKET:
            return result_array, tokens[1:]
        elif token != COMMA:
            raise Exception(f"comma exprected while parsing array, got '{token}'")
        else:
            tokens = tokens[1:]

    raise Exception("end of array bracket expected")


def parse_object(
    tokens: list[JSON_Types],
) -> Tuple[Dict, List[JSON_Types]]:
    result_obj = {}
    token = tokens[0]

    if token == CLOSING_BRACE:
        return result_obj, tokens[1:]

    while True:
        key = tokens[0]
        if type(key) == str:
            tokens = tokens[1:]
        else:
            raise Exception(f"expected string key, got '{key}'")

        if tokens[0] != COLON:
            raise Exception(f"expected colon, got '{tokens[0]}'")

        value, tokens = parser(tokens[1:])

        result_obj[key] = value

        token = tokens[0]
        if token == CLOSING_BRACE:
            return result_obj, tokens[1:]
        elif token != COMMA:
            raise Exception(f"comma exprected white parsing object, got '{token}'")

        tokens = tokens[1:]

    raise Exception("end of object brace expected")
