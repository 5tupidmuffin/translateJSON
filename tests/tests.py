import unittest
import translateJSON


class TestTranslateJSON(unittest.TestCase):
    def test_empty_obj(self):
        self.assertEqual(translateJSON.parse("{}"), {})

    def test_simple_obj(self):
        self.assertEqual(translateJSON.parse('{"foo":"bar"}'), {"foo": "bar"})

    def test_empty_array(self):
        self.assertEqual(translateJSON.parse("[]"), [])

    def test_complex_obj(self):
        self.assertEqual(
            translateJSON.parse(
                """
                    {
                        "foo": "bar",
                        "random_values": [1, 42, null, true, "abc"],
                        "nested": {
                            "props1": ["more", "values"],
                            "props2": 99.2
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
