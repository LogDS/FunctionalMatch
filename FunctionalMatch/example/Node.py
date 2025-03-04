from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    val: object
    left: Optional['Node']
    right: Optional['Node']

    @staticmethod
    def leaf(val):
        return Node(val, None, None)