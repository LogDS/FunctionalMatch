# Generated from MatchingLanguage.g4 by ANTLR 4.13.2
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
        4,1,36,212,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,4,0,26,8,0,11,0,
        12,0,27,1,1,3,1,31,8,1,1,1,1,1,1,1,1,1,1,1,1,1,5,1,39,8,1,10,1,12,
        1,42,9,1,1,1,3,1,45,8,1,1,1,1,1,1,1,1,1,5,1,51,8,1,10,1,12,1,54,
        9,1,1,1,3,1,57,8,1,1,1,1,1,3,1,61,8,1,1,1,1,1,1,1,1,1,1,1,3,1,68,
        8,1,1,2,1,2,1,2,5,2,73,8,2,10,2,12,2,76,9,2,1,2,1,2,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,91,8,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,5,3,126,8,3,10,3,12,
        3,129,9,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,4,5,140,8,5,11,5,12,
        5,141,1,5,1,5,3,5,146,8,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,4,5,158,8,5,11,5,12,5,159,1,5,1,5,1,5,1,5,3,5,166,8,5,1,5,1,5,
        1,5,1,5,1,5,3,5,173,8,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,5,8,188,8,8,10,8,12,8,191,9,8,1,8,1,8,1,9,1,9,1,9,1,
        9,1,9,1,9,3,9,201,8,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,3,10,210,
        8,10,1,10,0,1,6,11,0,2,4,6,8,10,12,14,16,18,20,0,1,1,0,3,4,239,0,
        25,1,0,0,0,2,30,1,0,0,0,4,74,1,0,0,0,6,90,1,0,0,0,8,130,1,0,0,0,
        10,172,1,0,0,0,12,174,1,0,0,0,14,177,1,0,0,0,16,182,1,0,0,0,18,200,
        1,0,0,0,20,209,1,0,0,0,22,23,3,2,1,0,23,24,5,1,0,0,24,26,1,0,0,0,
        25,22,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,1,1,0,
        0,0,29,31,5,8,0,0,30,29,1,0,0,0,30,31,1,0,0,0,31,32,1,0,0,0,32,33,
        5,7,0,0,33,44,3,4,2,0,34,40,5,10,0,0,35,36,3,8,4,0,36,37,5,2,0,0,
        37,39,1,0,0,0,38,35,1,0,0,0,39,42,1,0,0,0,40,38,1,0,0,0,40,41,1,
        0,0,0,41,43,1,0,0,0,42,40,1,0,0,0,43,45,3,8,4,0,44,34,1,0,0,0,44,
        45,1,0,0,0,45,56,1,0,0,0,46,52,5,11,0,0,47,48,3,18,9,0,48,49,5,2,
        0,0,49,51,1,0,0,0,50,47,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,
        1,0,0,0,53,55,1,0,0,0,54,52,1,0,0,0,55,57,3,18,9,0,56,46,1,0,0,0,
        56,57,1,0,0,0,57,60,1,0,0,0,58,59,5,9,0,0,59,61,3,6,3,0,60,58,1,
        0,0,0,60,61,1,0,0,0,61,62,1,0,0,0,62,67,5,5,0,0,63,68,3,10,5,0,64,
        68,3,14,7,0,65,68,3,12,6,0,66,68,3,16,8,0,67,63,1,0,0,0,67,64,1,
        0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,3,1,0,0,0,69,70,3,10,5,0,70,
        71,5,2,0,0,71,73,1,0,0,0,72,69,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,
        0,74,75,1,0,0,0,75,77,1,0,0,0,76,74,1,0,0,0,77,78,3,10,5,0,78,5,
        1,0,0,0,79,80,6,3,-1,0,80,81,5,22,0,0,81,82,3,6,3,0,82,83,5,23,0,
        0,83,91,1,0,0,0,84,85,5,25,0,0,85,91,3,6,3,12,86,91,3,14,7,0,87,
        91,3,12,6,0,88,89,5,30,0,0,89,91,5,33,0,0,90,79,1,0,0,0,90,84,1,
        0,0,0,90,86,1,0,0,0,90,87,1,0,0,0,90,88,1,0,0,0,91,127,1,0,0,0,92,
        93,10,15,0,0,93,94,5,15,0,0,94,126,3,6,3,16,95,96,10,14,0,0,96,97,
        5,16,0,0,97,126,3,6,3,15,98,99,10,13,0,0,99,100,5,21,0,0,100,126,
        3,6,3,14,101,102,10,10,0,0,102,103,5,26,0,0,103,126,3,6,3,11,104,
        105,10,9,0,0,105,106,5,24,0,0,106,126,3,6,3,10,107,108,10,8,0,0,
        108,109,5,17,0,0,109,126,3,6,3,9,110,111,10,7,0,0,111,112,5,19,0,
        0,112,126,3,6,3,8,113,114,10,6,0,0,114,115,5,18,0,0,115,126,3,6,
        3,7,116,117,10,5,0,0,117,118,5,20,0,0,118,126,3,6,3,6,119,120,10,
        4,0,0,120,121,5,27,0,0,121,126,3,6,3,5,122,123,10,11,0,0,123,124,
        5,26,0,0,124,126,5,28,0,0,125,92,1,0,0,0,125,95,1,0,0,0,125,98,1,
        0,0,0,125,101,1,0,0,0,125,104,1,0,0,0,125,107,1,0,0,0,125,110,1,
        0,0,0,125,113,1,0,0,0,125,116,1,0,0,0,125,119,1,0,0,0,125,122,1,
        0,0,0,126,129,1,0,0,0,127,125,1,0,0,0,127,128,1,0,0,0,128,7,1,0,
        0,0,129,127,1,0,0,0,130,131,5,33,0,0,131,132,5,14,0,0,132,133,5,
        33,0,0,133,9,1,0,0,0,134,135,5,31,0,0,135,145,5,22,0,0,136,137,3,
        10,5,0,137,138,5,2,0,0,138,140,1,0,0,0,139,136,1,0,0,0,140,141,1,
        0,0,0,141,139,1,0,0,0,141,142,1,0,0,0,142,143,1,0,0,0,143,144,3,
        10,5,0,144,146,1,0,0,0,145,139,1,0,0,0,145,146,1,0,0,0,146,147,1,
        0,0,0,147,148,5,23,0,0,148,149,5,14,0,0,149,173,5,33,0,0,150,151,
        5,31,0,0,151,165,5,22,0,0,152,153,5,33,0,0,153,154,5,26,0,0,154,
        155,3,10,5,0,155,156,5,2,0,0,156,158,1,0,0,0,157,152,1,0,0,0,158,
        159,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,161,1,0,0,0,161,
        162,5,33,0,0,162,163,5,26,0,0,163,164,3,10,5,0,164,166,1,0,0,0,165,
        157,1,0,0,0,165,166,1,0,0,0,166,167,1,0,0,0,167,168,5,23,0,0,168,
        169,5,14,0,0,169,173,5,33,0,0,170,173,3,14,7,0,171,173,5,32,0,0,
        172,134,1,0,0,0,172,150,1,0,0,0,172,170,1,0,0,0,172,171,1,0,0,0,
        173,11,1,0,0,0,174,175,5,29,0,0,175,176,5,33,0,0,176,13,1,0,0,0,
        177,178,5,6,0,0,178,179,5,22,0,0,179,180,5,31,0,0,180,181,5,23,0,
        0,181,15,1,0,0,0,182,183,7,0,0,0,183,189,5,12,0,0,184,185,3,20,10,
        0,185,186,5,2,0,0,186,188,1,0,0,0,187,184,1,0,0,0,188,191,1,0,0,
        0,189,187,1,0,0,0,189,190,1,0,0,0,190,192,1,0,0,0,191,189,1,0,0,
        0,192,193,3,20,10,0,193,17,1,0,0,0,194,195,3,14,7,0,195,196,5,13,
        0,0,196,197,3,10,5,0,197,201,1,0,0,0,198,201,3,14,7,0,199,201,3,
        12,6,0,200,194,1,0,0,0,200,198,1,0,0,0,200,199,1,0,0,0,201,19,1,
        0,0,0,202,210,3,14,7,0,203,204,3,12,6,0,204,205,5,5,0,0,205,206,
        3,10,5,0,206,210,1,0,0,0,207,210,3,14,7,0,208,210,3,12,6,0,209,202,
        1,0,0,0,209,203,1,0,0,0,209,207,1,0,0,0,209,208,1,0,0,0,210,21,1,
        0,0,0,20,27,30,40,44,52,56,60,67,74,90,125,127,141,145,159,165,172,
        189,200,209
    ]

class MatchingLanguageParser ( Parser ):

    grammarFileName = "MatchingLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "'shallow'", "'deep'", "'as'", 
                     "'var'", "'match'", "'nested'", "'where'", "'extend-with'", 
                     "'replace'", "'rewrite'", "'with'", "'in-module'", 
                     "'&&'", "'||'", "<INVALID>", "<INVALID>", "'<'", "'>'", 
                     "'\\u2192'", "'('", "')'", "'\\u2260'", "'!'", "'='", 
                     "'\\u2208'", "'\\u2205'", "'jsonpath'", "'python'", 
                     "<INVALID>", "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "SHALLOW", 
                      "DEEP", "AS", "VAR", "MATCHING", "NESTED", "WHERE", 
                      "EXTEND", "REPLACE", "REWRITE", "WITH", "OVERMODULE", 
                      "AND", "OR", "LEQ", "GEQ", "LT", "GT", "IMPL", "LPAR", 
                      "RPAR", "NEQ", "NOT", "EQ", "ISIN", "EMPTY", "JSONPATH", 
                      "PYTHON", "ALPHANAME", "IGNORE", "STRING", "SPACE", 
                      "COMMENT", "LINE_COMMENT" ]

    RULE_language = 0
    RULE_rule = 1
    RULE_match_multiobj = 2
    RULE_prop = 3
    RULE_extension = 4
    RULE_object = 5
    RULE_jpath = 6
    RULE_variable = 7
    RULE_rewrite_list = 8
    RULE_replacement = 9
    RULE_rewrite = 10

    ruleNames =  [ "language", "rule", "match_multiobj", "prop", "extension", 
                   "object", "jpath", "variable", "rewrite_list", "replacement", 
                   "rewrite" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    SHALLOW=3
    DEEP=4
    AS=5
    VAR=6
    MATCHING=7
    NESTED=8
    WHERE=9
    EXTEND=10
    REPLACE=11
    REWRITE=12
    WITH=13
    OVERMODULE=14
    AND=15
    OR=16
    LEQ=17
    GEQ=18
    LT=19
    GT=20
    IMPL=21
    LPAR=22
    RPAR=23
    NEQ=24
    NOT=25
    EQ=26
    ISIN=27
    EMPTY=28
    JSONPATH=29
    PYTHON=30
    ALPHANAME=31
    IGNORE=32
    STRING=33
    SPACE=34
    COMMENT=35
    LINE_COMMENT=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
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
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.rule_()
                self.state = 23
                self.match(MatchingLanguageParser.T__0)
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7 or _la==8):
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
            self.query = None # Match_multiobjContext
            self.rewriting = None # ObjectContext

        def MATCHING(self):
            return self.getToken(MatchingLanguageParser.MATCHING, 0)

        def AS(self):
            return self.getToken(MatchingLanguageParser.AS, 0)

        def match_multiobj(self):
            return self.getTypedRuleContext(MatchingLanguageParser.Match_multiobjContext,0)


        def variable(self):
            return self.getTypedRuleContext(MatchingLanguageParser.VariableContext,0)


        def jpath(self):
            return self.getTypedRuleContext(MatchingLanguageParser.JpathContext,0)


        def rewrite_list(self):
            return self.getTypedRuleContext(MatchingLanguageParser.Rewrite_listContext,0)


        def NESTED(self):
            return self.getToken(MatchingLanguageParser.NESTED, 0)

        def EXTEND(self):
            return self.getToken(MatchingLanguageParser.EXTEND, 0)

        def extension(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.ExtensionContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.ExtensionContext,i)


        def REPLACE(self):
            return self.getToken(MatchingLanguageParser.REPLACE, 0)

        def replacement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.ReplacementContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.ReplacementContext,i)


        def WHERE(self):
            return self.getToken(MatchingLanguageParser.WHERE, 0)

        def prop(self):
            return self.getTypedRuleContext(MatchingLanguageParser.PropContext,0)


        def object_(self):
            return self.getTypedRuleContext(MatchingLanguageParser.ObjectContext,0)


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
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 29
                self.match(MatchingLanguageParser.NESTED)


            self.state = 32
            self.match(MatchingLanguageParser.MATCHING)
            self.state = 33
            localctx.query = self.match_multiobj()
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 34
                self.match(MatchingLanguageParser.EXTEND)
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 35
                        self.extension()
                        self.state = 36
                        self.match(MatchingLanguageParser.T__1) 
                    self.state = 42
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

                self.state = 43
                self.extension()


            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 46
                self.match(MatchingLanguageParser.REPLACE)
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 47
                        self.replacement()
                        self.state = 48
                        self.match(MatchingLanguageParser.T__1) 
                    self.state = 54
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 55
                self.replacement()


            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 58
                self.match(MatchingLanguageParser.WHERE)
                self.state = 59
                self.prop(0)


            self.state = 62
            self.match(MatchingLanguageParser.AS)
            self.state = 67
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 63
                localctx.rewriting = self.object_()
                pass

            elif la_ == 2:
                self.state = 64
                self.variable()
                pass

            elif la_ == 3:
                self.state = 65
                self.jpath()
                pass

            elif la_ == 4:
                self.state = 66
                self.rewrite_list()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Match_multiobjContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def object_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.ObjectContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.ObjectContext,i)


        def getRuleIndex(self):
            return MatchingLanguageParser.RULE_match_multiobj

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatch_multiobj" ):
                listener.enterMatch_multiobj(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatch_multiobj" ):
                listener.exitMatch_multiobj(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatch_multiobj" ):
                return visitor.visitMatch_multiobj(self)
            else:
                return visitor.visitChildren(self)




    def match_multiobj(self):

        localctx = MatchingLanguageParser.Match_multiobjContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_match_multiobj)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 69
                    self.object_()
                    self.state = 70
                    self.match(MatchingLanguageParser.T__1) 
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 77
            self.object_()
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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_prop, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [22]:
                localctx = MatchingLanguageParser.P_parContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 80
                self.match(MatchingLanguageParser.LPAR)
                self.state = 81
                self.prop(0)
                self.state = 82
                self.match(MatchingLanguageParser.RPAR)
                pass
            elif token in [25]:
                localctx = MatchingLanguageParser.P_notContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 84
                self.match(MatchingLanguageParser.NOT)
                self.state = 85
                self.prop(12)
                pass
            elif token in [6]:
                localctx = MatchingLanguageParser.P_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 86
                self.variable()
                pass
            elif token in [29]:
                localctx = MatchingLanguageParser.P_jpathContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 87
                self.jpath()
                pass
            elif token in [30]:
                localctx = MatchingLanguageParser.P_jsonContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 88
                self.match(MatchingLanguageParser.PYTHON)
                self.state = 89
                self.match(MatchingLanguageParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 127
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 125
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = MatchingLanguageParser.P_andContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 92
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 93
                        self.match(MatchingLanguageParser.AND)
                        self.state = 94
                        self.prop(16)
                        pass

                    elif la_ == 2:
                        localctx = MatchingLanguageParser.P_orContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 95
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 96
                        self.match(MatchingLanguageParser.OR)
                        self.state = 97
                        self.prop(15)
                        pass

                    elif la_ == 3:
                        localctx = MatchingLanguageParser.P_implContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 98
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 99
                        self.match(MatchingLanguageParser.IMPL)
                        self.state = 100
                        self.prop(14)
                        pass

                    elif la_ == 4:
                        localctx = MatchingLanguageParser.P_eqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 101
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 102
                        self.match(MatchingLanguageParser.EQ)
                        self.state = 103
                        self.prop(11)
                        pass

                    elif la_ == 5:
                        localctx = MatchingLanguageParser.P_neqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 104
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 105
                        self.match(MatchingLanguageParser.NEQ)
                        self.state = 106
                        self.prop(10)
                        pass

                    elif la_ == 6:
                        localctx = MatchingLanguageParser.P_leqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 107
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 108
                        self.match(MatchingLanguageParser.LEQ)
                        self.state = 109
                        self.prop(9)
                        pass

                    elif la_ == 7:
                        localctx = MatchingLanguageParser.P_ltContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 110
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 111
                        self.match(MatchingLanguageParser.LT)
                        self.state = 112
                        self.prop(8)
                        pass

                    elif la_ == 8:
                        localctx = MatchingLanguageParser.P_geqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 113
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 114
                        self.match(MatchingLanguageParser.GEQ)
                        self.state = 115
                        self.prop(7)
                        pass

                    elif la_ == 9:
                        localctx = MatchingLanguageParser.P_gtContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 116
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 117
                        self.match(MatchingLanguageParser.GT)
                        self.state = 118
                        self.prop(6)
                        pass

                    elif la_ == 10:
                        localctx = MatchingLanguageParser.P_gtContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 119
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 120
                        self.match(MatchingLanguageParser.ISIN)
                        self.state = 121
                        self.prop(5)
                        pass

                    elif la_ == 11:
                        localctx = MatchingLanguageParser.P_isemptyContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 122
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 123
                        self.match(MatchingLanguageParser.EQ)
                        self.state = 124
                        self.match(MatchingLanguageParser.EMPTY)
                        pass

             
                self.state = 129
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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
        self.enterRule(localctx, 8, self.RULE_extension)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            localctx.fun = self.match(MatchingLanguageParser.STRING)
            self.state = 131
            self.match(MatchingLanguageParser.OVERMODULE)
            self.state = 132
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
        self.enterRule(localctx, 10, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.state = 172
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = MatchingLanguageParser.Actual_objectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.match(MatchingLanguageParser.ALPHANAME)
                self.state = 135
                self.match(MatchingLanguageParser.LPAR)
                self.state = 145
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6442451008) != 0):
                    self.state = 139 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 136
                            self.object_()
                            self.state = 137
                            self.match(MatchingLanguageParser.T__1)

                        else:
                            raise NoViableAltException(self)
                        self.state = 141 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                    self.state = 143
                    self.object_()


                self.state = 147
                self.match(MatchingLanguageParser.RPAR)
                self.state = 148
                self.match(MatchingLanguageParser.OVERMODULE)
                self.state = 149
                localctx.module = self.match(MatchingLanguageParser.STRING)
                pass

            elif la_ == 2:
                localctx = MatchingLanguageParser.Actual_tuple_of_type_and_argsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.match(MatchingLanguageParser.ALPHANAME)
                self.state = 151
                self.match(MatchingLanguageParser.LPAR)
                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==33:
                    self.state = 157 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 152
                            self.match(MatchingLanguageParser.STRING)
                            self.state = 153
                            self.match(MatchingLanguageParser.EQ)
                            self.state = 154
                            self.object_()
                            self.state = 155
                            self.match(MatchingLanguageParser.T__1)

                        else:
                            raise NoViableAltException(self)
                        self.state = 159 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

                    self.state = 161
                    self.match(MatchingLanguageParser.STRING)
                    self.state = 162
                    self.match(MatchingLanguageParser.EQ)
                    self.state = 163
                    self.object_()


                self.state = 167
                self.match(MatchingLanguageParser.RPAR)
                self.state = 168
                self.match(MatchingLanguageParser.OVERMODULE)
                self.state = 169
                localctx.module = self.match(MatchingLanguageParser.STRING)
                pass

            elif la_ == 3:
                localctx = MatchingLanguageParser.Actual_variableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.variable()
                pass

            elif la_ == 4:
                localctx = MatchingLanguageParser.Ignoring_argumentContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 171
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
        self.enterRule(localctx, 12, self.RULE_jpath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.match(MatchingLanguageParser.JSONPATH)
            self.state = 175
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
        self.enterRule(localctx, 14, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 177
            self.match(MatchingLanguageParser.VAR)
            self.state = 178
            self.match(MatchingLanguageParser.LPAR)
            self.state = 179
            self.match(MatchingLanguageParser.ALPHANAME)
            self.state = 180
            self.match(MatchingLanguageParser.RPAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Rewrite_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REWRITE(self):
            return self.getToken(MatchingLanguageParser.REWRITE, 0)

        def rewrite(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.RewriteContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.RewriteContext,i)


        def SHALLOW(self):
            return self.getToken(MatchingLanguageParser.SHALLOW, 0)

        def DEEP(self):
            return self.getToken(MatchingLanguageParser.DEEP, 0)

        def getRuleIndex(self):
            return MatchingLanguageParser.RULE_rewrite_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRewrite_list" ):
                listener.enterRewrite_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRewrite_list" ):
                listener.exitRewrite_list(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRewrite_list" ):
                return visitor.visitRewrite_list(self)
            else:
                return visitor.visitChildren(self)




    def rewrite_list(self):

        localctx = MatchingLanguageParser.Rewrite_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_rewrite_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            _la = self._input.LA(1)
            if not(_la==3 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 183
            self.match(MatchingLanguageParser.REWRITE)
            self.state = 189
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 184
                    self.rewrite()
                    self.state = 185
                    self.match(MatchingLanguageParser.T__1) 
                self.state = 191
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

            self.state = 192
            self.rewrite()
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
            self.as_ = None # ObjectContext

        def variable(self):
            return self.getTypedRuleContext(MatchingLanguageParser.VariableContext,0)


        def WITH(self):
            return self.getToken(MatchingLanguageParser.WITH, 0)

        def object_(self):
            return self.getTypedRuleContext(MatchingLanguageParser.ObjectContext,0)


        def jpath(self):
            return self.getTypedRuleContext(MatchingLanguageParser.JpathContext,0)


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
        self.enterRule(localctx, 18, self.RULE_replacement)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.variable()
                self.state = 195
                self.match(MatchingLanguageParser.WITH)
                self.state = 196
                localctx.as_ = self.object_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.jpath()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RewriteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.repl = None # VariableContext
            self.as_ = None # ObjectContext

        def variable(self):
            return self.getTypedRuleContext(MatchingLanguageParser.VariableContext,0)


        def jpath(self):
            return self.getTypedRuleContext(MatchingLanguageParser.JpathContext,0)


        def AS(self):
            return self.getToken(MatchingLanguageParser.AS, 0)

        def object_(self):
            return self.getTypedRuleContext(MatchingLanguageParser.ObjectContext,0)


        def getRuleIndex(self):
            return MatchingLanguageParser.RULE_rewrite

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRewrite" ):
                listener.enterRewrite(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRewrite" ):
                listener.exitRewrite(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRewrite" ):
                return visitor.visitRewrite(self)
            else:
                return visitor.visitChildren(self)




    def rewrite(self):

        localctx = MatchingLanguageParser.RewriteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_rewrite)
        try:
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                localctx.repl = self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 203
                self.jpath()
                self.state = 204
                self.match(MatchingLanguageParser.AS)
                self.state = 205
                localctx.as_ = self.object_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 207
                self.variable()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 208
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
        self._predicates[3] = self.prop_sempred
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
         




