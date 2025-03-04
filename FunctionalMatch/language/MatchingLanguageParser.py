# Generated from MatchingLanguage.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,170,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,4,0,20,8,0,11,0,12,0,21,1,1,3,1,25,8,1,1,1,
        1,1,1,1,1,1,1,1,1,1,4,1,33,8,1,11,1,12,1,34,1,1,1,1,3,1,39,8,1,1,
        1,1,1,3,1,43,8,1,1,1,5,1,46,8,1,10,1,12,1,49,9,1,1,1,1,1,1,1,1,1,
        3,1,55,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,68,8,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,5,2,103,8,2,10,2,12,2,106,9,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,
        1,4,1,4,4,4,117,8,4,11,4,12,4,118,1,4,1,4,3,4,123,8,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,4,4,135,8,4,11,4,12,4,136,1,4,1,4,
        1,4,1,4,3,4,143,8,4,1,4,1,4,1,4,1,4,1,4,3,4,150,8,4,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,168,8,7,
        1,7,0,1,4,8,0,2,4,6,8,10,12,14,0,0,194,0,19,1,0,0,0,2,24,1,0,0,0,
        4,67,1,0,0,0,6,107,1,0,0,0,8,149,1,0,0,0,10,151,1,0,0,0,12,154,1,
        0,0,0,14,167,1,0,0,0,16,17,3,2,1,0,17,18,5,1,0,0,18,20,1,0,0,0,19,
        16,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,
        0,23,25,5,6,0,0,24,23,1,0,0,0,24,25,1,0,0,0,25,26,1,0,0,0,26,27,
        5,5,0,0,27,38,3,8,4,0,28,32,5,8,0,0,29,30,3,6,3,0,30,31,5,2,0,0,
        31,33,1,0,0,0,32,29,1,0,0,0,33,34,1,0,0,0,34,32,1,0,0,0,34,35,1,
        0,0,0,35,36,1,0,0,0,36,37,3,6,3,0,37,39,1,0,0,0,38,28,1,0,0,0,38,
        39,1,0,0,0,39,42,1,0,0,0,40,41,5,7,0,0,41,43,3,4,2,0,42,40,1,0,0,
        0,42,43,1,0,0,0,43,47,1,0,0,0,44,46,3,14,7,0,45,44,1,0,0,0,46,49,
        1,0,0,0,47,45,1,0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,
        50,54,5,3,0,0,51,55,3,8,4,0,52,55,3,12,6,0,53,55,3,10,5,0,54,51,
        1,0,0,0,54,52,1,0,0,0,54,53,1,0,0,0,55,3,1,0,0,0,56,57,6,2,-1,0,
        57,58,5,19,0,0,58,59,3,4,2,0,59,60,5,20,0,0,60,68,1,0,0,0,61,62,
        5,22,0,0,62,68,3,4,2,12,63,68,3,12,6,0,64,68,3,10,5,0,65,66,5,27,
        0,0,66,68,5,30,0,0,67,56,1,0,0,0,67,61,1,0,0,0,67,63,1,0,0,0,67,
        64,1,0,0,0,67,65,1,0,0,0,68,104,1,0,0,0,69,70,10,15,0,0,70,71,5,
        12,0,0,71,103,3,4,2,16,72,73,10,14,0,0,73,74,5,13,0,0,74,103,3,4,
        2,15,75,76,10,13,0,0,76,77,5,18,0,0,77,103,3,4,2,14,78,79,10,10,
        0,0,79,80,5,23,0,0,80,103,3,4,2,11,81,82,10,9,0,0,82,83,5,21,0,0,
        83,103,3,4,2,10,84,85,10,8,0,0,85,86,5,14,0,0,86,103,3,4,2,9,87,
        88,10,7,0,0,88,89,5,16,0,0,89,103,3,4,2,8,90,91,10,6,0,0,91,92,5,
        15,0,0,92,103,3,4,2,7,93,94,10,5,0,0,94,95,5,17,0,0,95,103,3,4,2,
        6,96,97,10,4,0,0,97,98,5,24,0,0,98,103,3,4,2,5,99,100,10,11,0,0,
        100,101,5,23,0,0,101,103,5,25,0,0,102,69,1,0,0,0,102,72,1,0,0,0,
        102,75,1,0,0,0,102,78,1,0,0,0,102,81,1,0,0,0,102,84,1,0,0,0,102,
        87,1,0,0,0,102,90,1,0,0,0,102,93,1,0,0,0,102,96,1,0,0,0,102,99,1,
        0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,104,105,1,0,0,0,105,5,1,0,
        0,0,106,104,1,0,0,0,107,108,5,30,0,0,108,109,5,11,0,0,109,110,5,
        30,0,0,110,7,1,0,0,0,111,112,5,28,0,0,112,122,5,19,0,0,113,114,3,
        8,4,0,114,115,5,2,0,0,115,117,1,0,0,0,116,113,1,0,0,0,117,118,1,
        0,0,0,118,116,1,0,0,0,118,119,1,0,0,0,119,120,1,0,0,0,120,121,3,
        8,4,0,121,123,1,0,0,0,122,116,1,0,0,0,122,123,1,0,0,0,123,124,1,
        0,0,0,124,125,5,20,0,0,125,126,5,11,0,0,126,150,5,30,0,0,127,128,
        5,28,0,0,128,142,5,19,0,0,129,130,5,30,0,0,130,131,5,23,0,0,131,
        132,3,8,4,0,132,133,5,2,0,0,133,135,1,0,0,0,134,129,1,0,0,0,135,
        136,1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,138,1,0,0,0,138,
        139,5,30,0,0,139,140,5,23,0,0,140,141,3,8,4,0,141,143,1,0,0,0,142,
        134,1,0,0,0,142,143,1,0,0,0,143,144,1,0,0,0,144,145,5,20,0,0,145,
        146,5,11,0,0,146,150,5,30,0,0,147,150,3,12,6,0,148,150,5,29,0,0,
        149,111,1,0,0,0,149,127,1,0,0,0,149,147,1,0,0,0,149,148,1,0,0,0,
        150,9,1,0,0,0,151,152,5,26,0,0,152,153,5,30,0,0,153,11,1,0,0,0,154,
        155,5,4,0,0,155,156,5,19,0,0,156,157,5,28,0,0,157,158,5,20,0,0,158,
        13,1,0,0,0,159,160,5,9,0,0,160,168,3,12,6,0,161,162,3,10,5,0,162,
        163,5,10,0,0,163,164,3,8,4,0,164,168,1,0,0,0,165,168,3,12,6,0,166,
        168,3,10,5,0,167,159,1,0,0,0,167,161,1,0,0,0,167,165,1,0,0,0,167,
        166,1,0,0,0,168,15,1,0,0,0,16,21,24,34,38,42,47,54,67,102,104,118,
        122,136,142,149,167
    ]

class MatchingLanguageParser ( Parser ):

    grammarFileName = "MatchingLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'as'", "'var'", "'match'", 
                     "'nested'", "'where'", "'extend-with'", "'replace'", 
                     "'with'", "'in-module'", "'&&'", "'||'", "<INVALID>", 
                     "<INVALID>", "'<'", "'>'", "'\\u2192'", "'('", "')'", 
                     "'\\u2260'", "'!'", "'='", "'\\u2208'", "'\\u2205'", 
                     "'jsonpath'", "'python'", "<INVALID>", "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "AS", "VAR", 
                      "MATCHING", "NESTED", "WHERE", "EXTEND", "REPLACE", 
                      "WITH", "OVERMODULE", "AND", "OR", "LEQ", "GEQ", "LT", 
                      "GT", "IMPL", "LPAR", "RPAR", "NEQ", "NOT", "EQ", 
                      "ISIN", "EMPTY", "JSONPATH", "PYTHON", "ALPHANAME", 
                      "IGNORE", "STRING", "SPACE", "COMMENT", "LINE_COMMENT" ]

    RULE_language = 0
    RULE_rule = 1
    RULE_prop = 2
    RULE_extension = 3
    RULE_object = 4
    RULE_jpath = 5
    RULE_variable = 6
    RULE_replacement = 7

    ruleNames =  [ "language", "rule", "prop", "extension", "object", "jpath", 
                   "variable", "replacement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    AS=3
    VAR=4
    MATCHING=5
    NESTED=6
    WHERE=7
    EXTEND=8
    REPLACE=9
    WITH=10
    OVERMODULE=11
    AND=12
    OR=13
    LEQ=14
    GEQ=15
    LT=16
    GT=17
    IMPL=18
    LPAR=19
    RPAR=20
    NEQ=21
    NOT=22
    EQ=23
    ISIN=24
    EMPTY=25
    JSONPATH=26
    PYTHON=27
    ALPHANAME=28
    IGNORE=29
    STRING=30
    SPACE=31
    COMMENT=32
    LINE_COMMENT=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class LanguageContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def rule_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.RuleContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.RuleContext,i)


        def getRuleIndex(self):
            return MatchingLanguageParser.RULE_language

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLanguage" ):
                listener.enterLanguage(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLanguage" ):
                listener.exitLanguage(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLanguage" ):
                return visitor.visitLanguage(self)
            else:
                return visitor.visitChildren(self)




    def language(self):

        localctx = MatchingLanguageParser.LanguageContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_language)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.rule_()
                self.state = 17
                self.match(MatchingLanguageParser.T__0)
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==6):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.query = None # ObjectContext
            self.rewriting = None # ObjectContext

        def MATCHING(self):
            return self.getToken(MatchingLanguageParser.MATCHING, 0)

        def AS(self):
            return self.getToken(MatchingLanguageParser.AS, 0)

        def object_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.ObjectContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.ObjectContext,i)


        def variable(self):
            return self.getTypedRuleContext(MatchingLanguageParser.VariableContext,0)


        def jpath(self):
            return self.getTypedRuleContext(MatchingLanguageParser.JpathContext,0)


        def NESTED(self):
            return self.getToken(MatchingLanguageParser.NESTED, 0)

        def EXTEND(self):
            return self.getToken(MatchingLanguageParser.EXTEND, 0)

        def extension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.ExtensionContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.ExtensionContext,i)


        def WHERE(self):
            return self.getToken(MatchingLanguageParser.WHERE, 0)

        def prop(self):
            return self.getTypedRuleContext(MatchingLanguageParser.PropContext,0)


        def replacement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.ReplacementContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.ReplacementContext,i)


        def getRuleIndex(self):
            return MatchingLanguageParser.RULE_rule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRule" ):
                listener.enterRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRule" ):
                listener.exitRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRule" ):
                return visitor.visitRule(self)
            else:
                return visitor.visitChildren(self)




    def rule_(self):

        localctx = MatchingLanguageParser.RuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 23
                self.match(MatchingLanguageParser.NESTED)


            self.state = 26
            self.match(MatchingLanguageParser.MATCHING)
            self.state = 27
            localctx.query = self.object_()
            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 28
                self.match(MatchingLanguageParser.EXTEND)
                self.state = 32 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 29
                        self.extension()
                        self.state = 30
                        self.match(MatchingLanguageParser.T__1)

                    else:
                        raise NoViableAltException(self)
                    self.state = 34 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 36
                self.extension()


            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 40
                self.match(MatchingLanguageParser.WHERE)
                self.state = 41
                self.prop(0)


            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 67109392) != 0):
                self.state = 44
                self.replacement()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
            self.match(MatchingLanguageParser.AS)
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.state = 51
                localctx.rewriting = self.object_()
                pass

            elif la_ == 2:
                self.state = 52
                self.variable()
                pass

            elif la_ == 3:
                self.state = 53
                self.jpath()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PropContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MatchingLanguageParser.RULE_prop

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class P_jpathContext(PropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.PropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def jpath(self):
            return self.getTypedRuleContext(MatchingLanguageParser.JpathContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_jpath" ):
                listener.enterP_jpath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_jpath" ):
                listener.exitP_jpath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_jpath" ):
                return visitor.visitP_jpath(self)
            else:
                return visitor.visitChildren(self)


    class P_ltContext(PropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.PropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def prop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.PropContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.PropContext,i)

        def LT(self):
            return self.getToken(MatchingLanguageParser.LT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_lt" ):
                listener.enterP_lt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_lt" ):
                listener.exitP_lt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_lt" ):
                return visitor.visitP_lt(self)
            else:
                return visitor.visitChildren(self)


    class P_parContext(PropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.PropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(MatchingLanguageParser.LPAR, 0)
        def prop(self):
            return self.getTypedRuleContext(MatchingLanguageParser.PropContext,0)

        def RPAR(self):
            return self.getToken(MatchingLanguageParser.RPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_par" ):
                listener.enterP_par(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_par" ):
                listener.exitP_par(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_par" ):
                return visitor.visitP_par(self)
            else:
                return visitor.visitChildren(self)


    class P_implContext(PropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.PropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def prop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.PropContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.PropContext,i)

        def IMPL(self):
            return self.getToken(MatchingLanguageParser.IMPL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_impl" ):
                listener.enterP_impl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_impl" ):
                listener.exitP_impl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_impl" ):
                return visitor.visitP_impl(self)
            else:
                return visitor.visitChildren(self)


    class P_orContext(PropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.PropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def prop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.PropContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.PropContext,i)

        def OR(self):
            return self.getToken(MatchingLanguageParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_or" ):
                listener.enterP_or(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_or" ):
                listener.exitP_or(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_or" ):
                return visitor.visitP_or(self)
            else:
                return visitor.visitChildren(self)


    class P_gtContext(PropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.PropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def prop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.PropContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.PropContext,i)

        def GT(self):
            return self.getToken(MatchingLanguageParser.GT, 0)
        def ISIN(self):
            return self.getToken(MatchingLanguageParser.ISIN, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_gt" ):
                listener.enterP_gt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_gt" ):
                listener.exitP_gt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_gt" ):
                return visitor.visitP_gt(self)
            else:
                return visitor.visitChildren(self)


    class P_varContext(PropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.PropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(MatchingLanguageParser.VariableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_var" ):
                listener.enterP_var(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_var" ):
                listener.exitP_var(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_var" ):
                return visitor.visitP_var(self)
            else:
                return visitor.visitChildren(self)


    class P_eqContext(PropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.PropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def prop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.PropContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.PropContext,i)

        def EQ(self):
            return self.getToken(MatchingLanguageParser.EQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_eq" ):
                listener.enterP_eq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_eq" ):
                listener.exitP_eq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_eq" ):
                return visitor.visitP_eq(self)
            else:
                return visitor.visitChildren(self)


    class P_notContext(PropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.PropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NOT(self):
            return self.getToken(MatchingLanguageParser.NOT, 0)
        def prop(self):
            return self.getTypedRuleContext(MatchingLanguageParser.PropContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_not" ):
                listener.enterP_not(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_not" ):
                listener.exitP_not(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_not" ):
                return visitor.visitP_not(self)
            else:
                return visitor.visitChildren(self)


    class P_geqContext(PropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.PropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def prop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.PropContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.PropContext,i)

        def GEQ(self):
            return self.getToken(MatchingLanguageParser.GEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_geq" ):
                listener.enterP_geq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_geq" ):
                listener.exitP_geq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_geq" ):
                return visitor.visitP_geq(self)
            else:
                return visitor.visitChildren(self)


    class P_isemptyContext(PropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.PropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def prop(self):
            return self.getTypedRuleContext(MatchingLanguageParser.PropContext,0)

        def EQ(self):
            return self.getToken(MatchingLanguageParser.EQ, 0)
        def EMPTY(self):
            return self.getToken(MatchingLanguageParser.EMPTY, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_isempty" ):
                listener.enterP_isempty(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_isempty" ):
                listener.exitP_isempty(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_isempty" ):
                return visitor.visitP_isempty(self)
            else:
                return visitor.visitChildren(self)


    class P_jsonContext(PropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.PropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def PYTHON(self):
            return self.getToken(MatchingLanguageParser.PYTHON, 0)
        def STRING(self):
            return self.getToken(MatchingLanguageParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_json" ):
                listener.enterP_json(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_json" ):
                listener.exitP_json(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_json" ):
                return visitor.visitP_json(self)
            else:
                return visitor.visitChildren(self)


    class P_neqContext(PropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.PropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def prop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.PropContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.PropContext,i)

        def NEQ(self):
            return self.getToken(MatchingLanguageParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_neq" ):
                listener.enterP_neq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_neq" ):
                listener.exitP_neq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_neq" ):
                return visitor.visitP_neq(self)
            else:
                return visitor.visitChildren(self)


    class P_andContext(PropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.PropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def prop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.PropContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.PropContext,i)

        def AND(self):
            return self.getToken(MatchingLanguageParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_and" ):
                listener.enterP_and(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_and" ):
                listener.exitP_and(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_and" ):
                return visitor.visitP_and(self)
            else:
                return visitor.visitChildren(self)


    class P_leqContext(PropContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.PropContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def prop(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.PropContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.PropContext,i)

        def LEQ(self):
            return self.getToken(MatchingLanguageParser.LEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterP_leq" ):
                listener.enterP_leq(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitP_leq" ):
                listener.exitP_leq(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitP_leq" ):
                return visitor.visitP_leq(self)
            else:
                return visitor.visitChildren(self)



    def prop(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MatchingLanguageParser.PropContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_prop, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                localctx = MatchingLanguageParser.P_parContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 57
                self.match(MatchingLanguageParser.LPAR)
                self.state = 58
                self.prop(0)
                self.state = 59
                self.match(MatchingLanguageParser.RPAR)
                pass
            elif token in [22]:
                localctx = MatchingLanguageParser.P_notContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 61
                self.match(MatchingLanguageParser.NOT)
                self.state = 62
                self.prop(12)
                pass
            elif token in [4]:
                localctx = MatchingLanguageParser.P_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 63
                self.variable()
                pass
            elif token in [26]:
                localctx = MatchingLanguageParser.P_jpathContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 64
                self.jpath()
                pass
            elif token in [27]:
                localctx = MatchingLanguageParser.P_jsonContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 65
                self.match(MatchingLanguageParser.PYTHON)
                self.state = 66
                self.match(MatchingLanguageParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 104
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 102
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = MatchingLanguageParser.P_andContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 69
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 70
                        self.match(MatchingLanguageParser.AND)
                        self.state = 71
                        self.prop(16)
                        pass

                    elif la_ == 2:
                        localctx = MatchingLanguageParser.P_orContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 72
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 73
                        self.match(MatchingLanguageParser.OR)
                        self.state = 74
                        self.prop(15)
                        pass

                    elif la_ == 3:
                        localctx = MatchingLanguageParser.P_implContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 75
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 76
                        self.match(MatchingLanguageParser.IMPL)
                        self.state = 77
                        self.prop(14)
                        pass

                    elif la_ == 4:
                        localctx = MatchingLanguageParser.P_eqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 78
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 79
                        self.match(MatchingLanguageParser.EQ)
                        self.state = 80
                        self.prop(11)
                        pass

                    elif la_ == 5:
                        localctx = MatchingLanguageParser.P_neqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 81
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 82
                        self.match(MatchingLanguageParser.NEQ)
                        self.state = 83
                        self.prop(10)
                        pass

                    elif la_ == 6:
                        localctx = MatchingLanguageParser.P_leqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 84
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 85
                        self.match(MatchingLanguageParser.LEQ)
                        self.state = 86
                        self.prop(9)
                        pass

                    elif la_ == 7:
                        localctx = MatchingLanguageParser.P_ltContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 87
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 88
                        self.match(MatchingLanguageParser.LT)
                        self.state = 89
                        self.prop(8)
                        pass

                    elif la_ == 8:
                        localctx = MatchingLanguageParser.P_geqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 90
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 91
                        self.match(MatchingLanguageParser.GEQ)
                        self.state = 92
                        self.prop(7)
                        pass

                    elif la_ == 9:
                        localctx = MatchingLanguageParser.P_gtContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 93
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 94
                        self.match(MatchingLanguageParser.GT)
                        self.state = 95
                        self.prop(6)
                        pass

                    elif la_ == 10:
                        localctx = MatchingLanguageParser.P_gtContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 96
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 97
                        self.match(MatchingLanguageParser.ISIN)
                        self.state = 98
                        self.prop(5)
                        pass

                    elif la_ == 11:
                        localctx = MatchingLanguageParser.P_isemptyContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 99
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 100
                        self.match(MatchingLanguageParser.EQ)
                        self.state = 101
                        self.match(MatchingLanguageParser.EMPTY)
                        pass

             
                self.state = 106
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExtensionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.fun = None # Token
            self.module = None # Token

        def OVERMODULE(self):
            return self.getToken(MatchingLanguageParser.OVERMODULE, 0)

        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MatchingLanguageParser.STRING)
            else:
                return self.getToken(MatchingLanguageParser.STRING, i)

        def getRuleIndex(self):
            return MatchingLanguageParser.RULE_extension

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtension" ):
                listener.enterExtension(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtension" ):
                listener.exitExtension(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtension" ):
                return visitor.visitExtension(self)
            else:
                return visitor.visitChildren(self)




    def extension(self):

        localctx = MatchingLanguageParser.ExtensionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_extension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            localctx.fun = self.match(MatchingLanguageParser.STRING)
            self.state = 108
            self.match(MatchingLanguageParser.OVERMODULE)
            self.state = 109
            localctx.module = self.match(MatchingLanguageParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MatchingLanguageParser.RULE_object

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Actual_objectContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.ObjectContext
            super().__init__(parser)
            self.module = None # Token
            self.copyFrom(ctx)

        def ALPHANAME(self):
            return self.getToken(MatchingLanguageParser.ALPHANAME, 0)
        def LPAR(self):
            return self.getToken(MatchingLanguageParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(MatchingLanguageParser.RPAR, 0)
        def OVERMODULE(self):
            return self.getToken(MatchingLanguageParser.OVERMODULE, 0)
        def STRING(self):
            return self.getToken(MatchingLanguageParser.STRING, 0)
        def object_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.ObjectContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.ObjectContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActual_object" ):
                listener.enterActual_object(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActual_object" ):
                listener.exitActual_object(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActual_object" ):
                return visitor.visitActual_object(self)
            else:
                return visitor.visitChildren(self)


    class Ignoring_argumentContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IGNORE(self):
            return self.getToken(MatchingLanguageParser.IGNORE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIgnoring_argument" ):
                listener.enterIgnoring_argument(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIgnoring_argument" ):
                listener.exitIgnoring_argument(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIgnoring_argument" ):
                return visitor.visitIgnoring_argument(self)
            else:
                return visitor.visitChildren(self)


    class Actual_variableContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def variable(self):
            return self.getTypedRuleContext(MatchingLanguageParser.VariableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActual_variable" ):
                listener.enterActual_variable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActual_variable" ):
                listener.exitActual_variable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActual_variable" ):
                return visitor.visitActual_variable(self)
            else:
                return visitor.visitChildren(self)


    class Actual_tuple_of_type_and_argsContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.ObjectContext
            super().__init__(parser)
            self.module = None # Token
            self.copyFrom(ctx)

        def ALPHANAME(self):
            return self.getToken(MatchingLanguageParser.ALPHANAME, 0)
        def LPAR(self):
            return self.getToken(MatchingLanguageParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(MatchingLanguageParser.RPAR, 0)
        def OVERMODULE(self):
            return self.getToken(MatchingLanguageParser.OVERMODULE, 0)
        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MatchingLanguageParser.STRING)
            else:
                return self.getToken(MatchingLanguageParser.STRING, i)
        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(MatchingLanguageParser.EQ)
            else:
                return self.getToken(MatchingLanguageParser.EQ, i)
        def object_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.ObjectContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.ObjectContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActual_tuple_of_type_and_args" ):
                listener.enterActual_tuple_of_type_and_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActual_tuple_of_type_and_args" ):
                listener.exitActual_tuple_of_type_and_args(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActual_tuple_of_type_and_args" ):
                return visitor.visitActual_tuple_of_type_and_args(self)
            else:
                return visitor.visitChildren(self)



    def object_(self):

        localctx = MatchingLanguageParser.ObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.state = 149
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                localctx = MatchingLanguageParser.Actual_objectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 111
                self.match(MatchingLanguageParser.ALPHANAME)
                self.state = 112
                self.match(MatchingLanguageParser.LPAR)
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 805306384) != 0):
                    self.state = 116 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 113
                            self.object_()
                            self.state = 114
                            self.match(MatchingLanguageParser.T__1)

                        else:
                            raise NoViableAltException(self)
                        self.state = 118 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                    self.state = 120
                    self.object_()


                self.state = 124
                self.match(MatchingLanguageParser.RPAR)
                self.state = 125
                self.match(MatchingLanguageParser.OVERMODULE)
                self.state = 126
                localctx.module = self.match(MatchingLanguageParser.STRING)
                pass

            elif la_ == 2:
                localctx = MatchingLanguageParser.Actual_tuple_of_type_and_argsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 127
                self.match(MatchingLanguageParser.ALPHANAME)
                self.state = 128
                self.match(MatchingLanguageParser.LPAR)
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==30:
                    self.state = 134 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 129
                            self.match(MatchingLanguageParser.STRING)
                            self.state = 130
                            self.match(MatchingLanguageParser.EQ)
                            self.state = 131
                            self.object_()
                            self.state = 132
                            self.match(MatchingLanguageParser.T__1)

                        else:
                            raise NoViableAltException(self)
                        self.state = 136 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                    self.state = 138
                    self.match(MatchingLanguageParser.STRING)
                    self.state = 139
                    self.match(MatchingLanguageParser.EQ)
                    self.state = 140
                    self.object_()


                self.state = 144
                self.match(MatchingLanguageParser.RPAR)
                self.state = 145
                self.match(MatchingLanguageParser.OVERMODULE)
                self.state = 146
                localctx.module = self.match(MatchingLanguageParser.STRING)
                pass

            elif la_ == 3:
                localctx = MatchingLanguageParser.Actual_variableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.variable()
                pass

            elif la_ == 4:
                localctx = MatchingLanguageParser.Ignoring_argumentContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.match(MatchingLanguageParser.IGNORE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class JpathContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JSONPATH(self):
            return self.getToken(MatchingLanguageParser.JSONPATH, 0)

        def STRING(self):
            return self.getToken(MatchingLanguageParser.STRING, 0)

        def getRuleIndex(self):
            return MatchingLanguageParser.RULE_jpath

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJpath" ):
                listener.enterJpath(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJpath" ):
                listener.exitJpath(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitJpath" ):
                return visitor.visitJpath(self)
            else:
                return visitor.visitChildren(self)




    def jpath(self):

        localctx = MatchingLanguageParser.JpathContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_jpath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(MatchingLanguageParser.JSONPATH)
            self.state = 152
            self.match(MatchingLanguageParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MatchingLanguageParser.VAR, 0)

        def LPAR(self):
            return self.getToken(MatchingLanguageParser.LPAR, 0)

        def ALPHANAME(self):
            return self.getToken(MatchingLanguageParser.ALPHANAME, 0)

        def RPAR(self):
            return self.getToken(MatchingLanguageParser.RPAR, 0)

        def getRuleIndex(self):
            return MatchingLanguageParser.RULE_variable

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariable" ):
                listener.enterVariable(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariable" ):
                listener.exitVariable(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)




    def variable(self):

        localctx = MatchingLanguageParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.match(MatchingLanguageParser.VAR)
            self.state = 155
            self.match(MatchingLanguageParser.LPAR)
            self.state = 156
            self.match(MatchingLanguageParser.ALPHANAME)
            self.state = 157
            self.match(MatchingLanguageParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReplacementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.repl = None # VariableContext
            self.as_ = None # ObjectContext

        def REPLACE(self):
            return self.getToken(MatchingLanguageParser.REPLACE, 0)

        def variable(self):
            return self.getTypedRuleContext(MatchingLanguageParser.VariableContext,0)


        def jpath(self):
            return self.getTypedRuleContext(MatchingLanguageParser.JpathContext,0)


        def WITH(self):
            return self.getToken(MatchingLanguageParser.WITH, 0)

        def object_(self):
            return self.getTypedRuleContext(MatchingLanguageParser.ObjectContext,0)


        def getRuleIndex(self):
            return MatchingLanguageParser.RULE_replacement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReplacement" ):
                listener.enterReplacement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReplacement" ):
                listener.exitReplacement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReplacement" ):
                return visitor.visitReplacement(self)
            else:
                return visitor.visitChildren(self)




    def replacement(self):

        localctx = MatchingLanguageParser.ReplacementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_replacement)
        try:
            self.state = 167
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(MatchingLanguageParser.REPLACE)
                self.state = 160
                localctx.repl = self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 161
                self.jpath()
                self.state = 162
                self.match(MatchingLanguageParser.WITH)
                self.state = 163
                localctx.as_ = self.object_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 165
                self.variable()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 166
                self.jpath()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.prop_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def prop_sempred(self, localctx:PropContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 15)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 14)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 13)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 10)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 9)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 8:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 10:
                return self.precpred(self._ctx, 11)
         




