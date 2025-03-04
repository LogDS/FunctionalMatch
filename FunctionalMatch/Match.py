__author__ = "Giacomo Bergami"
__copyright__ = "Copyright 2025, Functional Match"
__credits__ = ["Giacomo Bergami"]
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Giacomo Bergami"
__email__ = "bergamigiacomo@gmail.com"
__status__ = "Production"

from dataclasses import dataclass
from typing import Optional, List
from FunctionalMatch import structural_match
from FunctionalMatch.PropositionalLogic import Prop

@dataclass(eq=True, order=True, frozen=True)
class ExternalMatchByExtesion:
    module: str
    function_name: str

    def __call__(self, x):
        import importlib
        mod = importlib.import_module(self.module) #__import__(self.module)
        func = getattr(mod, self.function_name)
        return func(x)

@dataclass(eq=True, order=True, frozen=True)
class Match:
    query: object
    nested: bool
    where: Optional[Prop]
    extension: List[ExternalMatchByExtesion]

    def __call__(self, x):
        if isinstance(x, list):
            return [structural_match(self.query, y, self.nested, self.where, self.extension) for y in x]
        elif isinstance(x, tuple):
            return (structural_match(self.query, y, self.nested, self.where, self.extension) for y in x)
        elif isinstance(x, set):
            return {structural_match(self.query, y, self.nested, self.where, self.extension) for y in x}
        elif isinstance(x, dict):
            return {k: structural_match(self.query, y, self.nested, self.where, self.extension) for k, y in x.items()}
        else:
            return structural_match(self.query, x, self.nested, self.where, self.extension)


