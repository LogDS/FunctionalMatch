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
        4,1,39,263,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,5,0,32,8,0,10,0,12,0,35,9,0,1,0,1,0,1,0,4,0,40,8,0,
        11,0,12,0,41,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,52,8,1,1,2,3,2,
        55,8,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,63,8,2,10,2,12,2,66,9,2,1,2,3,
        2,69,8,2,1,2,1,2,1,2,1,2,5,2,75,8,2,10,2,12,2,78,9,2,1,2,3,2,81,
        8,2,1,2,1,2,3,2,85,8,2,1,2,1,2,1,2,1,2,1,2,3,2,92,8,2,1,3,1,3,1,
        3,5,3,97,8,3,10,3,12,3,100,9,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,3,4,115,8,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,1,4,5,4,150,8,4,10,4,12,4,153,9,4,
        1,5,1,5,1,5,4,5,158,8,5,11,5,12,5,159,3,5,162,8,5,1,6,1,6,1,6,1,
        6,1,6,4,6,169,8,6,11,6,12,6,170,1,6,1,6,3,6,175,8,6,1,6,1,6,1,6,
        1,6,1,6,1,6,1,6,1,6,4,6,185,8,6,11,6,12,6,186,1,6,1,6,1,6,1,6,3,
        6,193,8,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,4,6,203,8,6,11,6,12,6,
        204,3,6,207,8,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,215,8,6,1,7,1,7,1,7,
        1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,5,9,230,8,9,10,9,12,9,233,
        9,9,1,9,1,9,1,10,1,10,1,10,1,10,3,10,241,8,10,1,10,3,10,244,8,10,
        1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,12,1,13,1,13,1,13,3,13,257,
        8,13,1,14,1,14,3,14,261,8,14,1,14,0,1,8,15,0,2,4,6,8,10,12,14,16,
        18,20,22,24,26,28,0,1,1,0,5,6,295,0,33,1,0,0,0,2,51,1,0,0,0,4,54,
        1,0,0,0,6,98,1,0,0,0,8,114,1,0,0,0,10,154,1,0,0,0,12,214,1,0,0,0,
        14,216,1,0,0,0,16,219,1,0,0,0,18,224,1,0,0,0,20,236,1,0,0,0,22,245,
        1,0,0,0,24,249,1,0,0,0,26,256,1,0,0,0,28,260,1,0,0,0,30,32,3,2,1,
        0,31,30,1,0,0,0,32,35,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,39,
        1,0,0,0,35,33,1,0,0,0,36,37,3,4,2,0,37,38,5,1,0,0,38,40,1,0,0,0,
        39,36,1,0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,1,1,0,
        0,0,43,44,5,4,0,0,44,45,5,36,0,0,45,46,5,17,0,0,46,52,5,36,0,0,47,
        48,5,4,0,0,48,49,5,34,0,0,49,50,5,17,0,0,50,52,5,36,0,0,51,43,1,
        0,0,0,51,47,1,0,0,0,52,3,1,0,0,0,53,55,5,11,0,0,54,53,1,0,0,0,54,
        55,1,0,0,0,55,56,1,0,0,0,56,57,5,10,0,0,57,68,3,6,3,0,58,64,5,14,
        0,0,59,60,3,22,11,0,60,61,5,2,0,0,61,63,1,0,0,0,62,59,1,0,0,0,63,
        66,1,0,0,0,64,62,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,64,1,0,0,
        0,67,69,3,22,11,0,68,58,1,0,0,0,68,69,1,0,0,0,69,80,1,0,0,0,70,76,
        5,13,0,0,71,72,3,10,5,0,72,73,5,2,0,0,73,75,1,0,0,0,74,71,1,0,0,
        0,75,78,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,
        1,0,0,0,79,81,3,10,5,0,80,70,1,0,0,0,80,81,1,0,0,0,81,84,1,0,0,0,
        82,83,5,12,0,0,83,85,3,8,4,0,84,82,1,0,0,0,84,85,1,0,0,0,85,86,1,
        0,0,0,86,91,5,7,0,0,87,92,3,12,6,0,88,92,3,16,8,0,89,92,3,14,7,0,
        90,92,3,18,9,0,91,87,1,0,0,0,91,88,1,0,0,0,91,89,1,0,0,0,91,90,1,
        0,0,0,92,5,1,0,0,0,93,94,3,12,6,0,94,95,5,2,0,0,95,97,1,0,0,0,96,
        93,1,0,0,0,97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,101,1,0,
        0,0,100,98,1,0,0,0,101,102,3,12,6,0,102,7,1,0,0,0,103,104,6,4,-1,
        0,104,105,5,25,0,0,105,106,3,8,4,0,106,107,5,26,0,0,107,115,1,0,
        0,0,108,109,5,28,0,0,109,115,3,8,4,12,110,115,3,16,8,0,111,115,3,
        14,7,0,112,113,5,33,0,0,113,115,5,36,0,0,114,103,1,0,0,0,114,108,
        1,0,0,0,114,110,1,0,0,0,114,111,1,0,0,0,114,112,1,0,0,0,115,151,
        1,0,0,0,116,117,10,15,0,0,117,118,5,18,0,0,118,150,3,8,4,16,119,
        120,10,14,0,0,120,121,5,19,0,0,121,150,3,8,4,15,122,123,10,13,0,
        0,123,124,5,24,0,0,124,150,3,8,4,14,125,126,10,10,0,0,126,127,5,
        29,0,0,127,150,3,8,4,11,128,129,10,9,0,0,129,130,5,27,0,0,130,150,
        3,8,4,10,131,132,10,8,0,0,132,133,5,20,0,0,133,150,3,8,4,9,134,135,
        10,7,0,0,135,136,5,22,0,0,136,150,3,8,4,8,137,138,10,6,0,0,138,139,
        5,21,0,0,139,150,3,8,4,7,140,141,10,5,0,0,141,142,5,23,0,0,142,150,
        3,8,4,6,143,144,10,4,0,0,144,145,5,30,0,0,145,150,3,8,4,5,146,147,
        10,11,0,0,147,148,5,29,0,0,148,150,5,31,0,0,149,116,1,0,0,0,149,
        119,1,0,0,0,149,122,1,0,0,0,149,125,1,0,0,0,149,128,1,0,0,0,149,
        131,1,0,0,0,149,134,1,0,0,0,149,137,1,0,0,0,149,140,1,0,0,0,149,
        143,1,0,0,0,149,146,1,0,0,0,150,153,1,0,0,0,151,149,1,0,0,0,151,
        152,1,0,0,0,152,9,1,0,0,0,153,151,1,0,0,0,154,161,5,36,0,0,155,157,
        5,16,0,0,156,158,3,20,10,0,157,156,1,0,0,0,158,159,1,0,0,0,159,157,
        1,0,0,0,159,160,1,0,0,0,160,162,1,0,0,0,161,155,1,0,0,0,161,162,
        1,0,0,0,162,11,1,0,0,0,163,164,5,34,0,0,164,174,5,25,0,0,165,166,
        3,12,6,0,166,167,5,2,0,0,167,169,1,0,0,0,168,165,1,0,0,0,169,170,
        1,0,0,0,170,168,1,0,0,0,170,171,1,0,0,0,171,172,1,0,0,0,172,173,
        3,12,6,0,173,175,1,0,0,0,174,168,1,0,0,0,174,175,1,0,0,0,175,176,
        1,0,0,0,176,215,5,26,0,0,177,178,5,34,0,0,178,192,5,25,0,0,179,180,
        5,36,0,0,180,181,5,29,0,0,181,182,3,12,6,0,182,183,5,2,0,0,183,185,
        1,0,0,0,184,179,1,0,0,0,185,186,1,0,0,0,186,184,1,0,0,0,186,187,
        1,0,0,0,187,188,1,0,0,0,188,189,5,36,0,0,189,190,5,29,0,0,190,191,
        3,12,6,0,191,193,1,0,0,0,192,184,1,0,0,0,192,193,1,0,0,0,193,194,
        1,0,0,0,194,215,5,26,0,0,195,215,3,16,8,0,196,197,5,36,0,0,197,198,
        5,25,0,0,198,199,3,12,6,0,199,206,5,26,0,0,200,202,5,16,0,0,201,
        203,3,20,10,0,202,201,1,0,0,0,203,204,1,0,0,0,204,202,1,0,0,0,204,
        205,1,0,0,0,205,207,1,0,0,0,206,200,1,0,0,0,206,207,1,0,0,0,207,
        215,1,0,0,0,208,215,5,35,0,0,209,210,5,25,0,0,210,211,3,12,6,0,211,
        212,5,26,0,0,212,215,1,0,0,0,213,215,5,36,0,0,214,163,1,0,0,0,214,
        177,1,0,0,0,214,195,1,0,0,0,214,196,1,0,0,0,214,208,1,0,0,0,214,
        209,1,0,0,0,214,213,1,0,0,0,215,13,1,0,0,0,216,217,5,32,0,0,217,
        218,5,36,0,0,218,15,1,0,0,0,219,220,5,9,0,0,220,221,5,25,0,0,221,
        222,5,34,0,0,222,223,5,26,0,0,223,17,1,0,0,0,224,225,7,0,0,0,225,
        231,5,15,0,0,226,227,3,24,12,0,227,228,5,2,0,0,228,230,1,0,0,0,229,
        226,1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,
        234,1,0,0,0,233,231,1,0,0,0,234,235,3,24,12,0,235,19,1,0,0,0,236,
        237,5,34,0,0,237,243,5,3,0,0,238,244,3,16,8,0,239,241,5,33,0,0,240,
        239,1,0,0,0,240,241,1,0,0,0,241,242,1,0,0,0,242,244,5,36,0,0,243,
        238,1,0,0,0,243,240,1,0,0,0,244,21,1,0,0,0,245,246,3,16,8,0,246,
        247,5,16,0,0,247,248,3,26,13,0,248,23,1,0,0,0,249,250,3,28,14,0,
        250,251,5,8,0,0,251,252,3,26,13,0,252,25,1,0,0,0,253,257,3,14,7,
        0,254,257,3,12,6,0,255,257,3,16,8,0,256,253,1,0,0,0,256,254,1,0,
        0,0,256,255,1,0,0,0,257,27,1,0,0,0,258,261,3,16,8,0,259,261,3,14,
        7,0,260,258,1,0,0,0,260,259,1,0,0,0,261,29,1,0,0,0,28,33,41,51,54,
        64,68,76,80,84,91,98,114,149,151,159,161,170,174,186,192,204,206,
        214,231,240,243,256,260
    ]

class MatchingLanguageParser ( Parser ):

    grammarFileName = "MatchingLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "','", "':'", "'import'", "'shallow'", 
                     "'deep'", "'as'", "'to'", "'var'", "'match'", "'nested'", 
                     "'where'", "'extend-with'", "'replace'", "'rewrite'", 
                     "'with'", "'in-module'", "'&&'", "'||'", "<INVALID>", 
                     "<INVALID>", "'<'", "'>'", "'\\u2192'", "'('", "')'", 
                     "'\\u2260'", "'!'", "'='", "'\\u2208'", "'\\u2205'", 
                     "'jsonpath'", "'python'", "<INVALID>", "'_'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IMPORT", "SHALLOW", "DEEP", "AS", "TO", "VAR", "MATCHING", 
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
    RULE_as = 13
    RULE_repl = 14

    ruleNames =  [ "language", "import_statement", "rule", "match_multiobj", 
                   "prop", "extension", "object", "jpath", "variable", "rewrite_list", 
                   "funarg", "replacement", "rewrite", "as", "repl" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    IMPORT=4
    SHALLOW=5
    DEEP=6
    AS=7
    TO=8
    VAR=9
    MATCHING=10
    NESTED=11
    WHERE=12
    EXTEND=13
    REPLACE=14
    REWRITE=15
    WITH=16
    OVERMODULE=17
    AND=18
    OR=19
    LEQ=20
    GEQ=21
    LT=22
    GT=23
    IMPL=24
    LPAR=25
    RPAR=26
    NEQ=27
    NOT=28
    EQ=29
    ISIN=30
    EMPTY=31
    JSONPATH=32
    PYTHON=33
    ALPHANAME=34
    IGNORE=35
    STRING=36
    SPACE=37
    COMMENT=38
    LINE_COMMENT=39

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
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==4:
                self.state = 30
                self.import_statement()
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 36
                self.rule_()
                self.state = 37
                self.match(MatchingLanguageParser.T__0)
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==10 or _la==11):
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
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = MatchingLanguageParser.Function_importContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.match(MatchingLanguageParser.IMPORT)
                self.state = 44
                localctx.fun = self.match(MatchingLanguageParser.STRING)
                self.state = 45
                self.match(MatchingLanguageParser.OVERMODULE)
                self.state = 46
                localctx.module = self.match(MatchingLanguageParser.STRING)
                pass

            elif la_ == 2:
                localctx = MatchingLanguageParser.Class_importContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.match(MatchingLanguageParser.IMPORT)
                self.state = 48
                self.match(MatchingLanguageParser.ALPHANAME)
                self.state = 49
                self.match(MatchingLanguageParser.OVERMODULE)
                self.state = 50
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

        def REPLACE(self):
            return self.getToken(MatchingLanguageParser.REPLACE, 0)

        def replacement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.ReplacementContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.ReplacementContext,i)


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
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 53
                self.match(MatchingLanguageParser.NESTED)


            self.state = 56
            self.match(MatchingLanguageParser.MATCHING)
            self.state = 57
            localctx.query = self.match_multiobj()
            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 58
                self.match(MatchingLanguageParser.REPLACE)
                self.state = 64
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 59
                        self.replacement()
                        self.state = 60
                        self.match(MatchingLanguageParser.T__1) 
                    self.state = 66
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

                self.state = 67
                self.replacement()


            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 70
                self.match(MatchingLanguageParser.EXTEND)
                self.state = 76
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 71
                        self.extension()
                        self.state = 72
                        self.match(MatchingLanguageParser.T__1) 
                    self.state = 78
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

                self.state = 79
                self.extension()


            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12:
                self.state = 82
                self.match(MatchingLanguageParser.WHERE)
                self.state = 83
                self.prop(0)


            self.state = 86
            self.match(MatchingLanguageParser.AS)
            self.state = 91
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 87
                localctx.rewriting = self.object_()
                pass

            elif la_ == 2:
                self.state = 88
                self.variable()
                pass

            elif la_ == 3:
                self.state = 89
                self.jpath()
                pass

            elif la_ == 4:
                self.state = 90
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
            self.state = 98
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 93
                    self.object_()
                    self.state = 94
                    self.match(MatchingLanguageParser.T__1) 
                self.state = 100
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

            self.state = 101
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
            self.state = 114
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                localctx = MatchingLanguageParser.P_parContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 104
                self.match(MatchingLanguageParser.LPAR)
                self.state = 105
                self.prop(0)
                self.state = 106
                self.match(MatchingLanguageParser.RPAR)
                pass
            elif token in [28]:
                localctx = MatchingLanguageParser.P_notContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 108
                self.match(MatchingLanguageParser.NOT)
                self.state = 109
                self.prop(12)
                pass
            elif token in [9]:
                localctx = MatchingLanguageParser.P_varContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 110
                self.variable()
                pass
            elif token in [32]:
                localctx = MatchingLanguageParser.P_jpathContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 111
                self.jpath()
                pass
            elif token in [33]:
                localctx = MatchingLanguageParser.P_jsonContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 112
                self.match(MatchingLanguageParser.PYTHON)
                self.state = 113
                self.match(MatchingLanguageParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 151
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 149
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = MatchingLanguageParser.P_andContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 116
                        if not self.precpred(self._ctx, 15):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 15)")
                        self.state = 117
                        self.match(MatchingLanguageParser.AND)
                        self.state = 118
                        self.prop(16)
                        pass

                    elif la_ == 2:
                        localctx = MatchingLanguageParser.P_orContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 119
                        if not self.precpred(self._ctx, 14):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 14)")
                        self.state = 120
                        self.match(MatchingLanguageParser.OR)
                        self.state = 121
                        self.prop(15)
                        pass

                    elif la_ == 3:
                        localctx = MatchingLanguageParser.P_implContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 122
                        if not self.precpred(self._ctx, 13):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 13)")
                        self.state = 123
                        self.match(MatchingLanguageParser.IMPL)
                        self.state = 124
                        self.prop(14)
                        pass

                    elif la_ == 4:
                        localctx = MatchingLanguageParser.P_eqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 125
                        if not self.precpred(self._ctx, 10):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 10)")
                        self.state = 126
                        self.match(MatchingLanguageParser.EQ)
                        self.state = 127
                        self.prop(11)
                        pass

                    elif la_ == 5:
                        localctx = MatchingLanguageParser.P_neqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 128
                        if not self.precpred(self._ctx, 9):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 9)")
                        self.state = 129
                        self.match(MatchingLanguageParser.NEQ)
                        self.state = 130
                        self.prop(10)
                        pass

                    elif la_ == 6:
                        localctx = MatchingLanguageParser.P_leqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 131
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 132
                        self.match(MatchingLanguageParser.LEQ)
                        self.state = 133
                        self.prop(9)
                        pass

                    elif la_ == 7:
                        localctx = MatchingLanguageParser.P_ltContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 134
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 135
                        self.match(MatchingLanguageParser.LT)
                        self.state = 136
                        self.prop(8)
                        pass

                    elif la_ == 8:
                        localctx = MatchingLanguageParser.P_geqContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 137
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 138
                        self.match(MatchingLanguageParser.GEQ)
                        self.state = 139
                        self.prop(7)
                        pass

                    elif la_ == 9:
                        localctx = MatchingLanguageParser.P_gtContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 140
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 141
                        self.match(MatchingLanguageParser.GT)
                        self.state = 142
                        self.prop(6)
                        pass

                    elif la_ == 10:
                        localctx = MatchingLanguageParser.P_gtContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 143
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 144
                        self.match(MatchingLanguageParser.ISIN)
                        self.state = 145
                        self.prop(5)
                        pass

                    elif la_ == 11:
                        localctx = MatchingLanguageParser.P_isemptyContext(self, MatchingLanguageParser.PropContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_prop)
                        self.state = 146
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 147
                        self.match(MatchingLanguageParser.EQ)
                        self.state = 148
                        self.match(MatchingLanguageParser.EMPTY)
                        pass

             
                self.state = 153
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
            self.state = 154
            localctx.fun = self.match(MatchingLanguageParser.STRING)
            self.state = 161
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 155
                self.match(MatchingLanguageParser.WITH)
                self.state = 157 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 156
                    self.funarg()
                    self.state = 159 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==34):
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



    class ParContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LPAR(self):
            return self.getToken(MatchingLanguageParser.LPAR, 0)
        def object_(self):
            return self.getTypedRuleContext(MatchingLanguageParser.ObjectContext,0)

        def RPAR(self):
            return self.getToken(MatchingLanguageParser.RPAR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPar" ):
                listener.enterPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPar" ):
                listener.exitPar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPar" ):
                return visitor.visitPar(self)
            else:
                return visitor.visitChildren(self)


    class Actual_unary_function_with_argsContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(MatchingLanguageParser.STRING, 0)
        def LPAR(self):
            return self.getToken(MatchingLanguageParser.LPAR, 0)
        def object_(self):
            return self.getTypedRuleContext(MatchingLanguageParser.ObjectContext,0)

        def RPAR(self):
            return self.getToken(MatchingLanguageParser.RPAR, 0)
        def WITH(self):
            return self.getToken(MatchingLanguageParser.WITH, 0)
        def funarg(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MatchingLanguageParser.FunargContext)
            else:
                return self.getTypedRuleContext(MatchingLanguageParser.FunargContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActual_unary_function_with_args" ):
                listener.enterActual_unary_function_with_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActual_unary_function_with_args" ):
                listener.exitActual_unary_function_with_args(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActual_unary_function_with_args" ):
                return visitor.visitActual_unary_function_with_args(self)
            else:
                return visitor.visitChildren(self)


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


    class Actual_stringContext(ObjectContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a MatchingLanguageParser.ObjectContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(MatchingLanguageParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterActual_string" ):
                listener.enterActual_string(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitActual_string" ):
                listener.exitActual_string(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitActual_string" ):
                return visitor.visitActual_string(self)
            else:
                return visitor.visitChildren(self)



    def object_(self):

        localctx = MatchingLanguageParser.ObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_object)
        self._la = 0 # Token type
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                localctx = MatchingLanguageParser.Actual_objectContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self.match(MatchingLanguageParser.ALPHANAME)
                self.state = 164
                self.match(MatchingLanguageParser.LPAR)
                self.state = 174
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 120292639232) != 0):
                    self.state = 168 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 165
                            self.object_()
                            self.state = 166
                            self.match(MatchingLanguageParser.T__1)

                        else:
                            raise NoViableAltException(self)
                        self.state = 170 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

                    self.state = 172
                    self.object_()


                self.state = 176
                self.match(MatchingLanguageParser.RPAR)
                pass

            elif la_ == 2:
                localctx = MatchingLanguageParser.Actual_tuple_of_type_and_argsContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(MatchingLanguageParser.ALPHANAME)
                self.state = 178
                self.match(MatchingLanguageParser.LPAR)
                self.state = 192
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==36:
                    self.state = 184 
                    self._errHandler.sync(self)
                    _alt = 1
                    while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                        if _alt == 1:
                            self.state = 179
                            self.match(MatchingLanguageParser.STRING)
                            self.state = 180
                            self.match(MatchingLanguageParser.EQ)
                            self.state = 181
                            self.object_()
                            self.state = 182
                            self.match(MatchingLanguageParser.T__1)

                        else:
                            raise NoViableAltException(self)
                        self.state = 186 
                        self._errHandler.sync(self)
                        _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

                    self.state = 188
                    self.match(MatchingLanguageParser.STRING)
                    self.state = 189
                    self.match(MatchingLanguageParser.EQ)
                    self.state = 190
                    self.object_()


                self.state = 194
                self.match(MatchingLanguageParser.RPAR)
                pass

            elif la_ == 3:
                localctx = MatchingLanguageParser.Actual_variableContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.variable()
                pass

            elif la_ == 4:
                localctx = MatchingLanguageParser.Actual_unary_function_with_argsContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.match(MatchingLanguageParser.STRING)
                self.state = 197
                self.match(MatchingLanguageParser.LPAR)
                self.state = 198
                self.object_()
                self.state = 199
                self.match(MatchingLanguageParser.RPAR)
                self.state = 206
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==16:
                    self.state = 200
                    self.match(MatchingLanguageParser.WITH)
                    self.state = 202 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while True:
                        self.state = 201
                        self.funarg()
                        self.state = 204 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if not (_la==34):
                            break



                pass

            elif la_ == 5:
                localctx = MatchingLanguageParser.Ignoring_argumentContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 208
                self.match(MatchingLanguageParser.IGNORE)
                pass

            elif la_ == 6:
                localctx = MatchingLanguageParser.ParContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 209
                self.match(MatchingLanguageParser.LPAR)
                self.state = 210
                self.object_()
                self.state = 211
                self.match(MatchingLanguageParser.RPAR)
                pass

            elif la_ == 7:
                localctx = MatchingLanguageParser.Actual_stringContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 213
                self.match(MatchingLanguageParser.STRING)
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
            self.state = 216
            self.match(MatchingLanguageParser.JSONPATH)
            self.state = 217
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
            self.state = 219
            self.match(MatchingLanguageParser.VAR)
            self.state = 220
            self.match(MatchingLanguageParser.LPAR)
            self.state = 221
            self.match(MatchingLanguageParser.ALPHANAME)
            self.state = 222
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
            self.state = 224
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 225
            self.match(MatchingLanguageParser.REWRITE)
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 226
                    self.rewrite()
                    self.state = 227
                    self.match(MatchingLanguageParser.T__1) 
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

            self.state = 234
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

        def variable(self):
            return self.getTypedRuleContext(MatchingLanguageParser.VariableContext,0)


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
            self.state = 236
            self.match(MatchingLanguageParser.ALPHANAME)
            self.state = 237
            self.match(MatchingLanguageParser.T__2)
            self.state = 243
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.state = 238
                self.variable()
                pass
            elif token in [33, 36]:
                self.state = 240
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==33:
                    self.state = 239
                    self.match(MatchingLanguageParser.PYTHON)


                self.state = 242
                self.match(MatchingLanguageParser.STRING)
                pass
            else:
                raise NoViableAltException(self)

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

        def variable(self):
            return self.getTypedRuleContext(MatchingLanguageParser.VariableContext,0)


        def WITH(self):
            return self.getToken(MatchingLanguageParser.WITH, 0)

        def as_(self):
            return self.getTypedRuleContext(MatchingLanguageParser.AsContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.variable()
            self.state = 246
            self.match(MatchingLanguageParser.WITH)
            self.state = 247
            self.as_()
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

        def repl(self):
            return self.getTypedRuleContext(MatchingLanguageParser.ReplContext,0)


        def TO(self):
            return self.getToken(MatchingLanguageParser.TO, 0)

        def as_(self):
            return self.getTypedRuleContext(MatchingLanguageParser.AsContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 249
            self.repl()
            self.state = 250
            self.match(MatchingLanguageParser.TO)
            self.state = 251
            self.as_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def jpath(self):
            return self.getTypedRuleContext(MatchingLanguageParser.JpathContext,0)


        def object_(self):
            return self.getTypedRuleContext(MatchingLanguageParser.ObjectContext,0)


        def variable(self):
            return self.getTypedRuleContext(MatchingLanguageParser.VariableContext,0)


        def getRuleIndex(self):
            return MatchingLanguageParser.RULE_as

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAs" ):
                listener.enterAs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAs" ):
                listener.exitAs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAs" ):
                return visitor.visitAs(self)
            else:
                return visitor.visitChildren(self)




    def as_(self):

        localctx = MatchingLanguageParser.AsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_as)
        try:
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.jpath()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.object_()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 255
                self.variable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReplContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(MatchingLanguageParser.VariableContext,0)


        def jpath(self):
            return self.getTypedRuleContext(MatchingLanguageParser.JpathContext,0)


        def getRuleIndex(self):
            return MatchingLanguageParser.RULE_repl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepl" ):
                listener.enterRepl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepl" ):
                listener.exitRepl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRepl" ):
                return visitor.visitRepl(self)
            else:
                return visitor.visitChildren(self)




    def repl(self):

        localctx = MatchingLanguageParser.ReplContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_repl)
        try:
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.variable()
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 259
                self.jpath()
                pass
            else:
                raise NoViableAltException(self)

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
         




