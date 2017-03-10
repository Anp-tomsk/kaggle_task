import unittest
from mapping.dict_mapper import Mapper


class MapperTests(unittest.TestCase):

    def test_default_mapping_return_same_dict(self):
        mapper = Mapper()
        result = mapper.map({"foo": "hey"})

        self.assertEqual({"foo": "hey"}, result)

    def test_default_mapping_ignore_defaults_empty_dict(self):
        mapper = Mapper().ignore_not_resolved()
        result = mapper.map({"foo": "hey"})

        self.assertEqual({}, result)

    def test_default_mapping_ignore_defaults_resolve_using(self):
        mapper = Mapper().ignore_not_resolved().for_key("foo", "foo")
        result = mapper.map({"foo": "hey"})

        self.assertEqual({"foo": "hey"}, result)

    def test_mapping_ignore_not_resolved_custom_value_resolved(self):
        mapper = Mapper().ignore_not_resolved().for_key("foo", "bar")
        result = mapper.map({"foo": "hey"})

        self.assertEqual({"bar": "hey"}, result)

    def test_mapping_resolved_custom_value_resolved(self):
        mapper = Mapper().for_key("foo", "bar")
        result = mapper.map({"foo": "hey"})

        self.assertEqual({"bar": "hey"}, result)

    def test_mapping_aggregate_keys_append_resolved(self):

        def foobar_resolver(foo, bar):
            return foo + bar

        mapper = Mapper().aggregate_keys(["foo", "bar"], "foobar", foobar_resolver)
        result = mapper.map({"foo": "foo", "bar": "bar"})

        self.assertEqual({"foobar": "foobar"}, result)

