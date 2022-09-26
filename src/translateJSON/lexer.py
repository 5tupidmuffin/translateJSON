from typing import List, Literal, Tuple
from translateJSON.CONSTANTS import (
    QUOTE,
    WHITESPACE,
    NEWLINE,
    SYNTAX,
    NULL,
    TRUE,
    FALSE,
)


def lex_string(string: str) -> Tuple[str | None, str]:
    if string[0] == QUOTE:
        string = string[1:]
    else:
        return None, string

    token = ""
    for char in string:
        if char == QUOTE:
            return token, string[len(token) + 1 :]
        else:
            token += char

    raise Exception("Error Parsing String Token")


def lex_number(string: str) -> Tuple[int | float | None, str]:
    token = ""
    nums_comparison = [str(num) for num in range(0, 10)] + ["e", "-", "."]

    for char in string:
        if char in nums_comparison:
            token += char
        else:
            break

    if not len(token):
        return None, string

    if "." in token:
        return float(token), string[len(token) :]

    return int(token), string[len(token) :]


def lex_bool(string: str) -> Tuple[bool | None, str]:
    if len(string) >= len(TRUE) and string[: len(TRUE)] == TRUE:
        return True, string[len(TRUE) :]
    elif len(string) >= len(FALSE) and string[: len(FALSE)] == FALSE:
        return False, string[len(FALSE) :]
    else:
        return None, string


def lex_null(string: str) -> Tuple[Literal[True] | None, str]:
    if len(string) >= len(NULL) and string[: len(NULL)] == NULL:
        return None, string[len(NULL) :]
    else:
        return True, string


def lexer(input_string: str) -> List[str | bool | float | int | None]:
    """
    generate list of `tokens` from given `input_string`
    """
    tokens = []

    while len(input_string):
        # quoted strings
        str_token, input_string = lex_string(input_string)
        if str_token is not None:
            tokens.append(str_token)
            continue

        # numbers
        num_token, input_string = lex_number(input_string)
        if num_token is not None:
            tokens.append(num_token)
            continue

        # booleans
        bool_token, input_string = lex_bool(input_string)
        if bool_token is not None:
            tokens.append(bool_token)

        # null
        null_token, input_string = lex_null(input_string)
        if null_token is None:
            tokens.append(null_token)
            continue

        # syntactical punctuations
        if input_string[0] == WHITESPACE or input_string[0] == NEWLINE:
            input_string = input_string[1:]
        elif input_string[0] in SYNTAX:
            tokens.append(input_string[0])
            input_string = input_string[1:]
        else:

            raise Exception(f"unexpected character: '{input_string[0]}'")

    return tokens
