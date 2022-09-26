from typing import Dict, List
from translateJSON.lexer import lexer
from translateJSON.parser import parser


def parse(json_string: str) -> Dict | List:
    """
    parse given `json_string` to equivalent `Dict` or `List`
    """
    tokens = lexer(json_string)
    return parser(tokens)[0]
