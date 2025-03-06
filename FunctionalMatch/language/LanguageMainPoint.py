__author__ = "Giacomo Bergami"
__copyright__ = "Copyright 2025, Functional Match"
__credits__ = ["Giacomo Bergami"]
__license__ = "GPLv3"
__version__ = "2.0"
__maintainer__ = "Giacomo Bergami"
__email__ = "bergamigiacomo@gmail.com"
__status__ = "Production"

import json
# from typing import override
import dacite
from antlr4 import *
import os

from FunctionalMatch.Query import Query
from FunctionalMatch.ReturningFirstObjects import FromJSONPath
from FunctionalMatch.TransformationResults import ReplaceWith
from FunctionalMatch.language.MatchingLanguageLexer import MatchingLanguageLexer
from FunctionalMatch.language.MatchingLanguageParser import MatchingLanguageParser
from FunctionalMatch.language.MatchingLanguageVisitor import MatchingLanguageVisitor
from FunctionalMatch.utils import FrozenDict


class MatchingLanguageVisitor2(MatchingLanguageVisitor):
    def visitP_json(self, ctx: MatchingLanguageParser.P_jsonContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING JObject")
        return json.loads(json.loads(ctx.STRING().getText()))

    def visitP_jpath(self, ctx: MatchingLanguageParser.P_jpathContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING JPath")
        return self.visit(ctx.jpath())

    
    def visitP_var(self, ctx: MatchingLanguageParser.P_varContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING Variable")
        return self.visit(ctx.variable())

    
    # Visit a parse tree produced by MatchingLanguageParser#language.
    def visitLanguage(self, ctx: MatchingLanguageParser.LanguageContext):
        if ctx is None:
            yield from []
        else:
            for child in ctx.rule_():
                result = self.visitRule(child)
                if result is not None:
                    yield result

    def visitMatch_multiobj(self, ctx: MatchingLanguageParser.Match_multiobjContext):
        if ctx is None:
            return []
        return [self.visit(x) for x in ctx.object_()]

    # Visit a parse tree produced by MatchingLanguageParser#match.
    def visitRule(self, ctx: MatchingLanguageParser.RuleContext):
        if ctx is None:
            return None
        nested = ctx.NESTED() is not None
        q = self.visit(ctx.query)
        extension = []
        if ctx.EXTEND() is not None:
            for child in ctx.extension():
                extension.append(self.visit(child))
        replacements = dict()
        if ctx.REPLACE() is not None:
            for child in ctx.replacement():
                k, v = self.visit(child)
                replacements[k] = v
        replacements = ReplaceWith(FrozenDict.from_dictionary(replacements))
        where = None
        if ctx.WHERE() is not None:
            where = self.visit(ctx.prop())
        ## TODO: perform the rest, according to the full query semantics!
        from FunctionalMatch.Match import Match
        query =  Match(q, nested, where, extension, replacements)
        as_ = None
        if ctx.rewriting is not None:
            from FunctionalMatch.ReturningFirstObjects import Invent
            as_ = Invent(self.visit(ctx.rewriting))
        elif ctx.variable() is not None:
            from FunctionalMatch.ReturningFirstObjects import FromVariable
            as_ = FromVariable(self.visit(ctx.variable()))
        elif ctx.jpath() is not None:
            as_ = FromJSONPath(self.visit(ctx.jpath()))
        return Query(query, as_)
    
    # Visit a parse tree produced by MatchingLanguageParser#p_not.
    def visitP_not(self, ctx: MatchingLanguageParser.P_notContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING Empty")
        from FunctionalMatch.PropositionalLogic import Not
        return Not(self.visit(ctx.prop()))

    
    # Visit a parse tree produced by MatchingLanguageParser#p_lt.
    def visitP_lt(self, ctx: MatchingLanguageParser.P_ltContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING Lt")
        from FunctionalMatch.PropositionalLogic import LT
        return LT(self.visit(ctx.prop(0)), self.visit(ctx.prop(1)))

    
    # Visit a parse tree produced by MatchingLanguageParser#p_geq.
    def visitP_geq(self, ctx: MatchingLanguageParser.P_geqContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING Geq")
        from FunctionalMatch.PropositionalLogic import GEq
        return GEq(self.visit(ctx.prop(0)), self.visit(ctx.prop(1)))

    
    # Visit a parse tree produced by MatchingLanguageParser#p_par.
    def visitP_par(self, ctx: MatchingLanguageParser.P_parContext):
        return self.visit(None if ctx is None else ctx.prop())

    
    # Visit a parse tree produced by MatchingLanguageParser#p_impl.
    def visitP_impl(self, ctx: MatchingLanguageParser.P_implContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING Impl")
        from FunctionalMatch.PropositionalLogic import Impl
        return Impl(self.visit(ctx.prop(0)), self.visit(ctx.prop(1)))

    
    # Visit a parse tree produced by MatchingLanguageParser#p_or.
    def visitP_or(self, ctx: MatchingLanguageParser.P_orContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING Or")
        from FunctionalMatch.PropositionalLogic import Or
        return Or(self.visit(ctx.prop(0)), self.visit(ctx.prop(1)))

    
    # Visit a parse tree produced by MatchingLanguageParser#p_gt.
    def visitP_gt(self, ctx: MatchingLanguageParser.P_gtContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING Gt")
        from FunctionalMatch.PropositionalLogic import GT
        return GT(self.visit(ctx.prop(0)), self.visit(ctx.prop(1)))

    
    # Visit a parse tree produced by MatchingLanguageParser#p_isempty.
    def visitP_isempty(self, ctx: MatchingLanguageParser.P_isemptyContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING Empty")
        from FunctionalMatch.PropositionalLogic import Empty
        return Empty(self.visit(ctx.prop()))

    
    # Visit a parse tree produced by MatchingLanguageParser#p_neq.
    def visitP_neq(self, ctx: MatchingLanguageParser.P_neqContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING NEq")
        from FunctionalMatch.PropositionalLogic import NEq
        return NEq(self.visit(ctx.prop(0)), self.visit(ctx.prop(1)))

    
    # Visit a parse tree produced by MatchingLanguageParser#p_and.
    def visitP_and(self, ctx: MatchingLanguageParser.P_andContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING AND")
        from FunctionalMatch.PropositionalLogic import And
        return And(self.visit(ctx.prop(0)), self.visit(ctx.prop(1)))

    
    # Visit a parse tree produced by MatchingLanguageParser#p_leq.
    def visitP_leq(self, ctx: MatchingLanguageParser.P_leqContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING LEQ")
        from FunctionalMatch.PropositionalLogic import LEq
        return LEq(self.visit(ctx.prop(0)), self.visit(ctx.prop(1)))

    
    # Visit a parse tree produced by MatchingLanguageParser#p_eq.
    def visitP_eq(self, ctx: MatchingLanguageParser.P_eqContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING EQUALITY")
        from FunctionalMatch.PropositionalLogic import Eq
        return Eq(self.visit(ctx.prop(0)), self.visit(ctx.prop(1)))

    
    # Visit a parse tree produced by MatchingLanguageParser#extension.
    def visitExtension(self, ctx: MatchingLanguageParser.ExtensionContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING extension")
        from FunctionalMatch.Match import ExternalMatchByExtesion
        return ExternalMatchByExtesion(json.loads(ctx.fun.text), json.loads(ctx.module.text))

    
    # Visit a parse tree produced by MatchingLanguageParser#actual_object.
    def visitActual_object(self, ctx: MatchingLanguageParser.Actual_objectContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING actual tuple")
        name = ctx.ALPHANAME().getText()
        module = json.loads(ctx.module.text)
        d = dict()
        ## TODO: get dataclass type associated with this
        import importlib
        mod = importlib.import_module(module)  # __import__(self.module)
        func = getattr(mod, name)
        args = [self.visit(x) for x in ctx.object_()]
        return func(*args)

    
    # Visit a parse tree produced by MatchingLanguageParser#actual_tuple_of_type_and_args.
    def visitActual_tuple_of_type_and_args(self, ctx: MatchingLanguageParser.Actual_tuple_of_type_and_argsContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING actual tuple")
        name = ctx.ALPHANAME().getText()
        module = json.loads(ctx.module.text)
        d = dict()
        import importlib
        mod = importlib.import_module(module)  # __import__(self.module)
        func = getattr(mod, name)
        ## TODO: get dataclass type associated with this
        type = None
        for key, value in zip(ctx.STRING(), ctx.object_()):
            key = json.loads(key.getText())
            d[key] = self.visit(value)
        return dacite.from_dict(func, d)

    
    # Visit a parse tree produced by MatchingLanguageParser#actual_variable.
    def visitActual_variable(self, ctx: MatchingLanguageParser.Actual_variableContext):
        return self.visitVariable(None if ctx is None else ctx.variable())

    
    # Visit a parse tree produced by MatchingLanguageParser#ignoring_argument.
    def visitIgnoring_argument(self, ctx: MatchingLanguageParser.Ignoring_argumentContext):
        from FunctionalMatch.functions.structural_match import ignore_instance
        return ignore_instance

    
    # Visit a parse tree produced by MatchingLanguageParser#jpath.
    def visitJpath(self, ctx: MatchingLanguageParser.JpathContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING JPath")
        from FunctionalMatch import JSONPath
        return JSONPath(json.loads(ctx.STRING().getText()))

    
    # Visit a parse tree produced by MatchingLanguageParser#variable.
    def visitVariable(self, ctx: MatchingLanguageParser.VariableContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING Variable")
        from FunctionalMatch import var
        return var(ctx.ALPHANAME().getText())

    
    # Visit a parse tree produced by MatchingLanguageParser#replacement.
    def visitReplacement(self, ctx: MatchingLanguageParser.ReplacementContext):
        if (ctx is None):
            raise RuntimeError("ERROR MATCHING replacement")
        premise = ctx.variable().ALPHANAME().getText()
        conseq = self.visit(ctx.as_)
        from FunctionalMatch.functions.structural_match import Variable
        if isinstance(conseq, Variable) or type(conseq).__name__ == "Variable":
            conseq = conseq.name
        return (premise, conseq)


def parse_query(filename:str):
    data = None
    if os.path.isfile(filename):
        with open(filename) as file:
            data = f'{file.read()}\n'
    else:
        data = filename
    input_stream = InputStream(data)
    lexer = MatchingLanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = MatchingLanguageParser(stream)
    result = [x for x in MatchingLanguageVisitor2().visitLanguage(parser.language())]
    return result