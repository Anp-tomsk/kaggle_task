from mapping.resolvers import *


class Mapper:

    def __init__(self):
        self.mapping_dict = dict()
        self.ignored_keys = []
        self.ignore_default = False

    def for_key(self, key, resolving_key, resolver=default_resolver):
        self.mapping_dict[resolving_key] = (key, resolver)
        return self

    def ignore_not_resolved(self):
        self.ignore_default = True
        return self

    def aggregate_keys(self, keys, resolving_key, resolver):
        self.mapping_dict[resolving_key] = (keys, resolver)
        return self

    def ignore_key(self, key):
        self.ignored_keys.append(key)
        return self

    def map(self, in_dict):
        result = {}
        if self.ignore_default:
            for resolving_key, value in self.mapping_dict.items():
                key, resolver = value
                source = in_dict[key]
                result[resolving_key] = resolver(source)
            return result

        for resolving_key, value in self.mapping_dict.items():
            key, resolver = value

            if type(key) is list:
                arg_dict = {}
                for sub_key in key:
                    arg_dict[sub_key] = in_dict[sub_key]
                    self.ignored_keys.append(sub_key)
                result[resolving_key] = resolver(**arg_dict)
            else:
                source = in_dict[key]
                result[resolving_key] = resolver(source)
                self.ignored_keys.append(key)

        for key, value in in_dict.items():
            if key not in self.ignored_keys:
                result[key] = default_resolver(value)

        return result


class DictToArrMapper:

    def __init__(self):
        self.keys_resolvers = []
        self.ignored_keys = []
        self.ignore_defaults = False

    def for_key(self, key, resolver=default_resolver):
        self.keys_resolvers.append((key, resolver))
        return self

    def ignore_not_resolved(self):
        self.ignore_defaults = True
        return self

    def ignore_key(self, key):
        self.ignored_keys.append(key)
        return self

    def map(self, in_dict):
        result = []
        for key, resolver in self.keys_resolvers:
            if type(key) is list:
                arg_dict = {}
                for sub_key in key:
                    arg_dict[sub_key] = in_dict[sub_key]
                    self.ignored_keys.append(sub_key)

                resolved_value = resolver(**arg_dict)
                if type(resolved_value) is list:
                    result.extend(resolved_value)
                else:
                    result.append(resolved_value)
            else:
                value = in_dict[key]

                resolved_value = resolver(value)
                if type(resolved_value) is list:
                    result.extend(resolved_value)
                else:
                    result.append(resolved_value)

                self.ignored_keys.append(key)

        for key, value in in_dict.items():
            if key not in self.ignored_keys:
                resolved_value = default_resolver(value)
                if type(resolved_value) is list:
                    result.extend(resolved_value)
                else:
                    result.append(resolved_value)

        return result


