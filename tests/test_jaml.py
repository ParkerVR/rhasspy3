import io

from rhasspy3.util.jaml import safe_load

YAML = """
# Line comment
outer_a:  # Inline comment
  name: outer_a
  prop_int: 1
  prop_float: 1.23
  prop_bool: true
  prop_str_noquotes: hello: world
  prop_str_1quotes: 'hello: world'
  prop_str_2quotes: "hello: world"
  prop_str_literal: |
    hello:
    world
  inner_a:
    name: inner_a
  empty_string: ""

outer_b:
  name: inner_b
"""


def test_safe_load():
    with io.StringIO(YAML) as yaml:
        assert safe_load(yaml) == {
            "outer_a": {
                "name": "outer_a",
                "prop_int": 1,
                "prop_float": 1.23,
                "prop_bool": True,
                "prop_str_noquotes": "hello: world",
                "prop_str_1quotes": "hello: world",
                "prop_str_2quotes": "hello: world",
                "prop_str_literal": "hello:\nworld",
                "inner_a": {"name": "inner_a"},
                "empty_string": "",
            },
            "outer_b": {"name": "inner_b"},
        }
