import collections
import copy


class FrozenDict(collections.abc.Mapping):
    """author: https://stackoverflow.com/a/2704866/1376095"""

    def __init__(self, *args, **kwargs):
        self._d = dict(*args, **kwargs)
        self._hash = None

    @staticmethod
    def from_dictionary(d):
        return FrozenDict(**d)

    def __contains__(self, key):
        return key in self._d

    def __iter__(self):
        return iter(self._d)

    def items(self):
        return self._d.items()

    def __len__(self):
        return len(self._d)

    def __getitem__(self, key):
        return self._d[key]

    def update(self, key, value):
        j = copy.deepcopy(self._d)
        j[key] = value
        return FrozenDict(**j)

    def __contains__(self, item):
        return item in self._d

    def get(self, key, value=None):
        return self._d.get(key, value)

    def __hash__(self):
        # It would have been simpler and maybe more obvious to
        # use hash(tuple(sorted(self._d.iteritems()))) from this discussion
        # so far, but this solution is O(n). I don't know what kind of
        # n we are going to run into, but sometimes it's hard to resist the
        # urge to optimize when it will gain improved algorithmic performance.
        if self._hash is None:
            hash_ = 0
            for pair in self.items():
                hash_ ^= hash(pair)
            self._hash = hash_
        return self._hash
