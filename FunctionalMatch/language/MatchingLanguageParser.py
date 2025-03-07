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
        4,1,38,240,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,5,0,
        28,8,0,10,0,12,0,31,9,0,1,0,1,0,1,0,4,0,36,8,0,11,0,12,0,37,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,48,8,1,1,2,3,2,51,8,2,1,2,1,2,1,
        2,1,2,1,2,1,2,5,2,59,8,2,10,2,12,2,62,9,2,1,2,3,2,65,8,2,1,2,1,2,
        1,2,1,2,5,2,71,8,2,10,2,12,2,74,9,2,1,2,3,2,77,8,2,1,2,1,2,3,2,81,
        8,2,1,2,1,2,1,2,1,2,1,2,3,2,88,8,2,1,3,1,3,1,3,5,3,93,8,3,10,3,12,
        3,96,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,3,4,
        111,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,
        1,4,1,4,1,4,5,4,146,8,4,10,4,12,4,149,9,4,1,5,1,5,1,5,4,5,154,8,
        5,11,5,12,5,155,3,5,158,8,5,1,6,1,6,1,6,1,6,1,6,4,6,165,8,6,11,6,
        12,6,166,1,6,1,6,3,6,171,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,4,6,
        181,8,6,11,6,12,6,182,1,6,1,6,1,6,1,6,3,6,189,8,6,1,6,1,6,1,6,3,
        6,194,8,6,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,5,
        9,209,8,9,10,9,12,9,212,9,9,1,9,1,9,1,10,1,10,1,10,3,10,219,8,10,
        1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,3,11,229,8,11,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,3,12,238,8,12,1,12,0,1,8,13,0,2,4,6,8,10,
        12,14,16,18,20,22,24,0,1,1,0,5,6,270,0,29,1,0,0,0,2,47,1,0,0,0,4,
        50,1,0,0,0,6,94,1,0,0,0,8,110,1,0,0,0,10,150,1,0,0,0,12,193,1,0,
        0,0,14,195,1,0,0,0,16,198,1,0,0,0,18,203,1,0,0,0,20,215,1,0,0,0,
        22,228,1,0,0,0,24,237,1,0,0,0,26,28,3,2,1,0,27,26,1,0,0,0,28,31,
        1,0,0,0,29,27,1,0,0,0,29,30,1,0,0,0,30,35,1,0,0,0,31,29,1,0,0,0,
        32,33,3,4,2,0,33,34,5,1,0,0,34,36,1,0,0,0,35,32,1,0,0,0,36,37,1,
        0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,1,1,0,0,0,39,40,5,4,0,0,40,
        41,5,35,0,0,41,42,5,16,0,0,42,48,5,35,0,0,43,44,5,4,0,0,44,45,5,
        33,0,0,45,46,5,16,0,0,46,48,5,35,0,0,47,39,1,0,0,0,47,43,1,0,0,0,
        48,3,1,0,0,0,49,51,5,10,0,0,50,49,1,0,0,0,50,51,1,0,0,0,51,52,1,
        0,0,0,52,53,5,9,0,0,53,64,3,6,3,0,54,60,5,12,0,0,55,56,3,10,5,0,
        56,57,5,2,0,0,57,59,1,0,0,0,58,55,1,0,0,0,59,62,1,0,0,0,60,58,1,
        0,0,0,60,61,1,0,0,0,61,63,1,0,0,0,62,60,1,0,0,0,63,65,3,10,5,0,64,
        54,1,0,0,0,64,65,1,0,0,0,65,76,1,0,0,0,66,72,5,13,0,0,67,68,3,22,
        11,0,68,69,5,2,0,0,69,71,1,0,0,0,70,67,1,0,0,0,71,74,1,0,0,0,72,
        70,1,0,0,0,72,73,1,0,0,0,73,75,1,0,0,0,74,72,1,0,0,0,75,77,3,22,
        11,0,76,66,1,0,0,0,76,77,1,0,0,0,77,80,1,0,0,0,78,79,5,11,0,0,79,
        81,3,8,4,0,80,78,1,0,0,0,80,81,1,0,0,0,81,82,1,0,0,0,82,87,5,7,0,
        0,83,88,3,12,6,0,84,88,3,16,8,0,85,88,3,14,7,0,86,88,3,18,9,0,87,
        83,1,0,0,0,87,84,1,0,0,0,87,85,1,0,0,0,87,86,1,0,0,0,88,5,1,0,0,
        0,89,90,3,12,6,0,90,91,5,2,0,0,91,93,1,0,0,0,92,89,1,0,0,0,93,96,
        1,0,0,0,94,92,1,0,0,0,94,95,1,0,0,0,95,97,1,0,0,0,96,94,1,0,0,0,
        97,98,3,12,6,0,98,7,1,0,0,0,99,100,6,4,-1,0,100,101,5,24,0,0,101,
        102,3,8,4,0,102,103,5,25,0,0,103,111,1,0,0,0,104,105,5,27,0,0,105,
        111,3,8,4,12,106,111,3,16,8,0,107,111,3,14,7,0,108,109,5,32,0,0,
        109,111,5,35,0,0,110,99,1,0,0,0,110,104,1,0,0,0,110,106,1,0,0,0,
        110,107,1,0,0,0,110,108,1,0,0,0,111,147,1,0,0,0,112,113,10,15,0,
        0,113,114,5,17,0,0,114,146,3,8,4,16,115,116,10,14,0,0,116,117,5,
        18,0,0,117,146,3,8,4,15,118,119,10,13,0,0,119,120,5,23,0,0,120,146,
        3,8,4,14,121,122,10,10,0,0,122,123,5,28,0,0,123,146,3,8,4,11,124,
        125,10,9,0,0,125,126,5,26,0,0,126,146,3,8,4,10,127,128,10,8,0,0,
        128,129,5,19,0,0,129,146,3,8,4,9,130,131,10,7,0,0,131,132,5,21,0,
        0,132,146,3,8,4,8,133,134,10,6,0,0,134,135,5,20,0,0,135,146,3,8,
        4,7,136,137,10,5,0,0,137,138,5,22,0,0,138,146,3,8,4,6,139,140,10,
        4,0,0,140,141,5,29,0,0,141,146,3,8,4,5,142,143,10,11,0,0,143,144,
        5,28,0,0,144,146,5,30,0,0,145,112,1,0,0,0,145,115,1,0,0,0,145,118,
        1,0,0,0,145,121,1,0,0,0,145,124,1,0,0,0,145,127,1,0,0,0,145,130,
        1,0,0,0,145,133,1,0,0,0,145,136,1,0,0,0,145,139,1,0,0,0,145,142,
        1,0,0,0,146,149,1,0,0,0,147,145,1,0,0,0,147,148,1,0,0,0,148,9,1,
        0,0,0,149,147,1,0,0,0,150,157,5,35,0,0,151,153,5,15,0,0,152,154,
        3,20,10,0,153,152,1,0,0,0,154,155,1,0,0,0,155,153,1,0,0,0,155,156,
        1,0,0,0,156,158,1,0,0,0,157,151,1,0,0,0,157,158,1,0,0,0,158,11,1,
        0,0,0,159,160,5,33,0,0,160,170,5,24,0,0,161,162,3,12,6,0,162,163,
        5,2,0,0,163,165,1,0,0,0,164,161,1,0,0,0,165,166,1,0,0,0,166,164,
        1,0,0,0,166,167,1,0,0,0,167,168,1,0,0,0,168,169,3,12,6,0,169,171,
        1,0,0,0,170,164,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,194,
        5,25,0,0,173,174,5,33,0,0,174,188,5,24,0,0,175,176,5,35,0,0,176,
        177,5,28,0,0,177,178,3,12,6,0,178,179,5,2,0,0,179,181,1,0,0,0,180,
        175,1,0,0,0,181,182,1,0,0,0,182,180,1,0,0,0,182,183,1,0,0,0,183,
        184,1,0,0,0,184,185,5,35,0,0,185,186,5,28,0,0,186,187,3,12,6,0,187,
        189,1,0,0,0,188,180,1,0,0,0,188,189,1,0,0,0,189,190,1,0,0,0,190,
        194,5,25,0,0,191,194,3,16,8,0,192,194,5,34,0,0,193,159,1,0,0,0,193,
        173,1,0,0,0,193,191,1,0,0,0,193,192,1,0,0,0,194,13,1,0,0,0,195,196,
        5,31,0,0,196,197,5,35,0,0,197,15,1,0,0,0,198,199,5,8,0,0,199,200,
        5,24,0,0,200,201,5,33,0,0,201,202,5,25,0,0,202,17,1,0,0,0,203,204,
        7,0,0,0,204,210,5,14,0,0,205,206,3,24,12,0,206,207,5,2,0,0,207,209,
        1,0,0,0,208,205,1,0,0,0,209,212,1,0,0,0,210,208,1,0,0,0,210,211,
        1,0,0,0,211,213,1,0,0,0,212,210,1,0,0,0,213,214,3,24,12,0,214,19,
        1,0,0,0,215,216,5,33,0,0,216,218,5,3,0,0,217,219,5,32,0,0,218,217,
        1,0,0,0,218,219,1,0,0,0,219,220,1,0,0,0,220,221,5,35,0,0,221,21,
        1,0,0,0,222,223,3,16,8,0,223,224,5,15,0,0,224,225,3,12,6,0,225,229,
        1,0,0,0,226,229,3,16,8,0,227,229,3,14,7,0,228,222,1,0,0,0,228,226,
        1,0,0,0,228,227,1,0,0,0,229,23,1,0,0,0,230,238,3,16,8,0,231,232,
        3,14,7,0,232,233,5,7,0,0,233,234,3,12,6,0,234,238,1,0,0,0,235,238,
        3,16,8,0,236,238,3,14,7,0,237,230,1,0,0,0,237,231,1,0,0,0,237,235,
        1,0,0,0,237,236,1,0,0,0,238,25,1,0,0,0,25,29,37,47,50,60,64,72,76,
        80,87,94,110,145,147,155,157,166,170,182,188,193,210,218,228,237
    ]

class MatchingLanguageParser ( Parser ):

    grammarFileName = "MatchingLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "':'", "'import'", "'shallow'", 
                     "'deep'", "'as'", "'var'", "'match'", "'nested'", "'where'", 
                     "'extend-with'", "'replace'", "'rewrite'", "'with'", 
                     "'in-module'", "'&&'", "'||'", "<INVALID>", "<INVALID>", 
                     "'<'", "'>'", "'\\u2192'", "'('", "')'", "'\\u2260'", 
                     "'!'", "'='", "'\\u2208'", "'\\u2205'", "'jsonpath'", 
                     "'python'", "<INVALID>", "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IMPORT", "SHALLOW", "DEEP", "AS", "VAR", "MATCHING", 
                      "NESTED", "WHERE", "EXTEND", "REPLACE", "REWRITE", 
                      "WITH", "OVERMODULE", "AND", "OR", "LEQ", "GEQ", "LT", 
                      "GT", "IMPL", "LPAR", "RPAR", "NEQ", "NOT", "EQ", 
                      "ISIN", "EMPTY", "JSONPATH", "PYTHON", "ALPHANAME", 
                      "IGNORE", "STRING", "SPACE", "COMMENT", "LINE_COMMENT" ]

    RULE_language = 0
    RULE_import_statement = 1
    RULE_rule = 2
    RULE_match_multiobj = 3
    RULE_prop = 4
    RULE_extension = 5
    RULE_object = 6
    RULE_jpath = 7
    RULE_variable = 8
    RULE_rewrite_list = 9
    RULE_funarg = 10
    RULE_replacement = 11
    RULE_rewrite = 12

    ruleNames =  [ "language", "import_statement", "rule", "match_multiobj", 
                   "prop", "extension", "object", "jpath", "variable", "rewrite_list", 
                   "funarg", "replacement", "rewrite" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    IMPORT=4
    SHALLOW=5
    DEEP=6
    AS=7
    VAR=8
    MATCHING=9
    NESTED=10
    WHERE=11
    EXTEND=12
    REPLACE=13
    REWRITE=14
    WITH=15
    OVERMODULE=16
    AND=17
    OR=18
    LEQ=19
    GEQ=20
    LT=21
    GT=22
    IMPL=23
    LPAR=24
    RPAR=25
    NEQ=26
    NOT=27
    EQ=28
    ISIN=29
    EMPTY=30
    JSONPATH=31
    PYTHON=32
    ALPHANAME=33
    IGNORE=34
    STRING=35
    SPACE=36
    COMMENT=37
    LINE_COMMENT=38

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

        def import_statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.Import_statementContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.Import_statementContext,i)


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
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 26
                self.import_statement()
                self.state = 31
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 35 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 32
                self.rule_()
                self.state = 33
                self.match(MatchingLanguageParser.T__0)
                self.state = 37 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==9 or _la==10):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Import_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return MatchingLanguageParser.RULE_import_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Function_importContext(Import_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.Import_statementContext
            super().__init__(parser)
            self.fun = None # Token
            self.module = None # Token
            self.copyFrom(ctx)

        def IMPORT(self):
            return self.getToken(MatchingLanguageParser.IMPORT, 0)
        def OVERMODULE(self):
            return self.getToken(MatchingLanguageParser.OVERMODULE, 0)
        def STRING(self, i:int=None):
            if i is None:
                return self.getTokens(MatchingLanguageParser.STRING)
            else:
                return self.getToken(MatchingLanguageParser.STRING, i)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_import" ):
                listener.enterFunction_import(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_import" ):
                listener.exitFunction_import(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_import" ):
                return visitor.visitFunction_import(self)
            else:
                return visitor.visitChildren(self)


    class Class_importContext(Import_statementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.Import_statementContext
            super().__init__(parser)
            self.module = None # Token
            self.copyFrom(ctx)

        def IMPORT(self):
            return self.getToken(MatchingLanguageParser.IMPORT, 0)
        def ALPHANAME(self):
            return self.getToken(MatchingLanguageParser.ALPHANAME, 0)
        def OVERMODULE(self):
            return self.getToken(MatchingLanguageParser.OVERMODULE, 0)
        def STRING(self):
            return self.getToken(MatchingLanguageParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClass_import" ):
                listener.enterClass_import(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClass_import" ):
                listener.exitClass_import(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_import" ):
                return visitor.visitClass_import(self)
            else:
                return visitor.visitChildren(self)



    def import_statement(self):

        localctx = MatchingLanguageParser.Import_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_import_statement)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = MatchingLanguageParser.Function_importContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 39
                self.match(MatchingLanguageParser.IMPORT)
                self.state = 40
                localctx.fun = self.match(MatchingLanguageParser.STRING)
                self.state = 41
                self.match(MatchingLanguageParser.OVERMODULE)
                self.state = 42
                localctx.module = self.match(MatchingLanguageParser.STRING)
                pass

            elif la_ == 2:
                localctx = MatchingLanguageParser.Class_importContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.match(MatchingLanguageParser.IMPORT)
                self.state = 44
                self.match(MatchingLanguageParser.ALPHANAME)
                self.state = 45
                self.match(MatchingLanguageParser.OVERMODULE)
                self.state = 46
                localctx.module = self.match(MatchingLanguageParser.STRING)
                pass


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
        self.enterRule(localctx, 4, self.RULE_rule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 49
                self.match(MatchingLanguageParser.NESTED)


            self.state = 52
            self.match(MatchingLanguageParser.MATCHING)
            self.state = 53
            localctx.query = self.match_multiobj()
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 54
                self.match(MatchingLanguageParser.EXTEND)
                self.state = 60
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 55
                        self.extension()
                        self.state = 56
                        self.match(MatchingLanguageParser.T__1) 
                    self.state = 62
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 63
                self.extension()


            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 66
                self.match(MatchingLanguageParser.REPLACE)
                self.state = 72
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 67
                        self.replacement()
                        self.state = 68
                        self.match(MatchingLanguageParser.T__1) 
                    self.state = 74
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                self.state = 75
                self.replacement()


            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 78
                self.match(MatchingLanguageParser.WHERE)
                self.state = 79
                self.prop(0)


            self.state = 82
            self.match(MatchingLanguageParser.AS)
            self.state = 87
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 83
                localctx.rewriting = self.object_()
                pass

            elif la_ == 2:
                self.state = 84
                self.variable()
                pass

            elif la_ == 3:
                self.state = 85
                self.jpath()
                pass

            elif la_ == 4:
                self.state = 86
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
        self.enterRule(localctx, 6, self.RULE_match_multiobj)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 89
                    self.object_()
                    self.state = 90
                    self.match(MatchingLanguageParser.T__1) 
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 97
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
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_prop, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [24]:
                localctx = MatchingLanguageParser.P_parContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 100
                self.match(MatchingLanguageParser.LPAR)
                self.state = 101
                self.prop(0)
                self.state = 102
                self.match(MatchingLanguageParser.RPAR)
                pass
            elif token in [27]:
                localctx = MatchingLanguageParser.P_notContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 104
                self.match(MatchingLanguageParser.NOT)
                self.state = 105
                self.prop(12)
                pass
            elif token in [8]:
                localctx = MatchingLanguageParser.P_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 106
                self.variable()
                pass
            elif token in [31]:
                localctx = MatchingLanguageParser.P_jpathContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 107
                self.jpath()
                pass
            elif token in [32]:
                localctx = MatchingLanguageParser.P_jsonContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(MatchingLanguageParser.PYTHON)
                self.state = 109
                self.match(MatchingLanguageParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 147
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 145
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = MatchingLanguageParser.P_andContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 112
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 113
                        self.match(MatchingLanguageParser.AND)
                        self.state = 114
                        self.prop(16)
                        pass

                    elif la_ == 2:
                        localctx = MatchingLanguageParser.P_orContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 115
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 116
                        self.match(MatchingLanguageParser.OR)
                        self.state = 117
                        self.prop(15)
                        pass

                    elif la_ == 3:
                        localctx = MatchingLanguageParser.P_implContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 118
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 119
                        self.match(MatchingLanguageParser.IMPL)
                        self.state = 120
                        self.prop(14)
                        pass

                    elif la_ == 4:
                        localctx = MatchingLanguageParser.P_eqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 121
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 122
                        self.match(MatchingLanguageParser.EQ)
                        self.state = 123
                        self.prop(11)
                        pass

                    elif la_ == 5:
                        localctx = MatchingLanguageParser.P_neqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 124
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 125
                        self.match(MatchingLanguageParser.NEQ)
                        self.state = 126
                        self.prop(10)
                        pass

                    elif la_ == 6:
                        localctx = MatchingLanguageParser.P_leqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 127
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 128
                        self.match(MatchingLanguageParser.LEQ)
                        self.state = 129
                        self.prop(9)
                        pass

                    elif la_ == 7:
                        localctx = MatchingLanguageParser.P_ltContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 130
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 131
                        self.match(MatchingLanguageParser.LT)
                        self.state = 132
                        self.prop(8)
                        pass

                    elif la_ == 8:
                        localctx = MatchingLanguageParser.P_geqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 133
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 134
                        self.match(MatchingLanguageParser.GEQ)
                        self.state = 135
                        self.prop(7)
                        pass

                    elif la_ == 9:
                        localctx = MatchingLanguageParser.P_gtContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 136
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 137
                        self.match(MatchingLanguageParser.GT)
                        self.state = 138
                        self.prop(6)
                        pass

                    elif la_ == 10:
                        localctx = MatchingLanguageParser.P_gtContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 139
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 140
                        self.match(MatchingLanguageParser.ISIN)
                        self.state = 141
                        self.prop(5)
                        pass

                    elif la_ == 11:
                        localctx = MatchingLanguageParser.P_isemptyContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 142
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 143
                        self.match(MatchingLanguageParser.EQ)
                        self.state = 144
                        self.match(MatchingLanguageParser.EMPTY)
                        pass

             
                self.state = 149
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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

        def STRING(self):
            return self.getToken(MatchingLanguageParser.STRING, 0)

        def WITH(self):
            return self.getToken(MatchingLanguageParser.WITH, 0)

        def funarg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.FunargContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.FunargContext,i)


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
        self.enterRule(localctx, 10, self.RULE_extension)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            localctx.fun = self.match(MatchingLanguageParser.STRING)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 151
                self.match(MatchingLanguageParser.WITH)
                self.state = 153 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 152
                    self.funarg()
                    self.state = 155 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==33):
                        break



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
            self.copyFrom(ctx)

        def ALPHANAME(self):
            return self.getToken(MatchingLanguageParser.ALPHANAME, 0)
        def LPAR(self):
            return self.getToken(MatchingLanguageParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(MatchingLanguageParser.RPAR, 0)
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
            self.copyFrom(ctx)

        def ALPHANAME(self):
            return self.getToken(MatchingLanguageParser.ALPHANAME, 0)
        def LPAR(self):
            return self.getToken(MatchingLanguageParser.LPAR, 0)
        def RPAR(self):
            return self.getToken(MatchingLanguageParser.RPAR, 0)
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
        self.enterRule(localctx, 12, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.state = 193
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                localctx = MatchingLanguageParser.Actual_objectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 159
                self.match(MatchingLanguageParser.ALPHANAME)
                self.state = 160
                self.match(MatchingLanguageParser.LPAR)
                self.state = 170
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 25769804032) != 0):
                    self.state = 164 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 161
                            self.object_()
                            self.state = 162
                            self.match(MatchingLanguageParser.T__1)

                        else:
                            raise NoViableAltException(self)
                        self.state = 166 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                    self.state = 168
                    self.object_()


                self.state = 172
                self.match(MatchingLanguageParser.RPAR)
                pass

            elif la_ == 2:
                localctx = MatchingLanguageParser.Actual_tuple_of_type_and_argsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 173
                self.match(MatchingLanguageParser.ALPHANAME)
                self.state = 174
                self.match(MatchingLanguageParser.LPAR)
                self.state = 188
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==35:
                    self.state = 180 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 175
                            self.match(MatchingLanguageParser.STRING)
                            self.state = 176
                            self.match(MatchingLanguageParser.EQ)
                            self.state = 177
                            self.object_()
                            self.state = 178
                            self.match(MatchingLanguageParser.T__1)

                        else:
                            raise NoViableAltException(self)
                        self.state = 182 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                    self.state = 184
                    self.match(MatchingLanguageParser.STRING)
                    self.state = 185
                    self.match(MatchingLanguageParser.EQ)
                    self.state = 186
                    self.object_()


                self.state = 190
                self.match(MatchingLanguageParser.RPAR)
                pass

            elif la_ == 3:
                localctx = MatchingLanguageParser.Actual_variableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 191
                self.variable()
                pass

            elif la_ == 4:
                localctx = MatchingLanguageParser.Ignoring_argumentContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 192
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
        self.enterRule(localctx, 14, self.RULE_jpath)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(MatchingLanguageParser.JSONPATH)
            self.state = 196
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
        self.enterRule(localctx, 16, self.RULE_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(MatchingLanguageParser.VAR)
            self.state = 199
            self.match(MatchingLanguageParser.LPAR)
            self.state = 200
            self.match(MatchingLanguageParser.ALPHANAME)
            self.state = 201
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
        self.enterRule(localctx, 18, self.RULE_rewrite_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 204
            self.match(MatchingLanguageParser.REWRITE)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 205
                    self.rewrite()
                    self.state = 206
                    self.match(MatchingLanguageParser.T__1) 
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

            self.state = 213
            self.rewrite()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunargContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ALPHANAME(self):
            return self.getToken(MatchingLanguageParser.ALPHANAME, 0)

        def STRING(self):
            return self.getToken(MatchingLanguageParser.STRING, 0)

        def PYTHON(self):
            return self.getToken(MatchingLanguageParser.PYTHON, 0)

        def getRuleIndex(self):
            return MatchingLanguageParser.RULE_funarg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunarg" ):
                listener.enterFunarg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunarg" ):
                listener.exitFunarg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunarg" ):
                return visitor.visitFunarg(self)
            else:
                return visitor.visitChildren(self)




    def funarg(self):

        localctx = MatchingLanguageParser.FunargContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_funarg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.match(MatchingLanguageParser.ALPHANAME)
            self.state = 216
            self.match(MatchingLanguageParser.T__2)

            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==32:
                self.state = 217
                self.match(MatchingLanguageParser.PYTHON)


            self.state = 220
            self.match(MatchingLanguageParser.STRING)
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
        self.enterRule(localctx, 22, self.RULE_replacement)
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.variable()
                self.state = 223
                self.match(MatchingLanguageParser.WITH)
                self.state = 224
                localctx.as_ = self.object_()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.variable()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
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
        self.enterRule(localctx, 24, self.RULE_rewrite)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 230
                localctx.repl = self.variable()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 231
                self.jpath()
                self.state = 232
                self.match(MatchingLanguageParser.AS)
                self.state = 233
                localctx.as_ = self.object_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 235
                self.variable()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 236
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
        self._predicates[4] = self.prop_sempred
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
         




