import pprint
import translateJSON

# simple
pprint.pprint(translateJSON.parse('{"foo": "bar"}'))
# {'foo': 'bar'}

# complex
pprint.pprint(
    translateJSON.parse(
        """
    {
        "foo": "bar",
        "random_values": [1, 42, null, true, "abc"],
        "nested": {
            "prop1": ["more", "values"],
            "prop2": 99.2
        }
    }
"""
    ),
    indent=2,
)
# { 'foo': 'bar',
#   'nested': {'prop1': ['more', 'values'], 'prop2': 99.2},
#   'random_values': [1, 42, None, True, 'abc']}
