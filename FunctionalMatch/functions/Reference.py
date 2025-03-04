import ctypes
from typing import Optional


def reference(obj):
    """Returning the pointer associated to the object"""
    return id(obj)

def dereference(ptr):
    """Returning the object the pointer is referring to"""
    return ctypes.cast(ptr, ctypes.py_object).value


from dataclasses import dataclass

@dataclass(frozen=True, eq=True, order=True, init=False)
class Reference:
    ref: Optional[int]

    @staticmethod
    def from_object(obj):
        return Reference(reference(obj))

    @staticmethod
    def null_ptr():
        return Reference(None)

    def get(self):
        return dereference(self.ref) if self.ref is not None else None