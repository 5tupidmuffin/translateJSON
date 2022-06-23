import unittest
import translateJSON


class Tests(unittest.TestCase):
    def empty_obj(self):
        self.assertEqual(translateJSON.parse("{}"), {})

    def simple_obj(self):
        self.assertEqual(translateJSON.parse('{"foo":"bar"}'), {"foo": "bar"})

    def empty_array(self):
        self.assertEqual(translateJSON.parse("[]"), [])

    def complex_obj(self):
        self.assertEqual(
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
            {
                "foo": "bar",
                "random_values": [1, 42, None, True, "abc"],
                "nested": {"props1": ["more", "values"], "props2": 99.2},
            },
        )


if __name__ == "__main__":
    unittest.main()
