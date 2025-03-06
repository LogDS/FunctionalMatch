from dataclasses import dataclass
from typing import Optional

def example_ext(d):
    return d.update("genoveffo", "blue")

@dataclass(frozen=True, order=True, unsafe_hash=True, eq=True)
class Node:
    val: object
    left: Optional['Node']
    right: Optional['Node']

    @staticmethod
    def leaf(val):
        return Node(val, None, None)