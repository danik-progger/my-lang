# Generated from Expr.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
# if sys.version_info[1] > 5:
# 	from typing import TextIO
# else:
# 	from typing.io import TextIO


def serializedATN():
    return [
        4, 1, 16, 50, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
        0, 1, 0, 5, 0, 16, 8, 0, 10, 0, 12, 0, 19, 9, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3,
        1, 28, 8, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 3, 2, 37, 8, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 1, 2, 5, 2, 45, 8, 2, 10, 2, 12, 2, 48, 9, 2, 1, 2, 0, 1, 4, 3, 0, 2, 4, 0, 2, 1, 0, 7,
        8, 1, 0, 9, 10, 52, 0, 6, 1, 0, 0, 0, 2, 27, 1, 0, 0, 0, 4, 36, 1, 0, 0, 0, 6, 7, 5, 12, 0, 0,
        7, 8, 5, 13, 0, 0, 8, 9, 5, 1, 0, 0, 9, 10, 5, 2, 0, 0, 10, 11, 5, 3, 0, 0, 11, 17, 5, 14, 0,
        0, 12, 13, 3, 2, 1, 0, 13, 14, 5, 14, 0, 0, 14, 16, 1, 0, 0, 0, 15, 12, 1, 0, 0, 0, 16, 19,
        1, 0, 0, 0, 17, 15, 1, 0, 0, 0, 17, 18, 1, 0, 0, 0, 18, 20, 1, 0, 0, 0, 19, 17, 1, 0, 0, 0,
        20, 21, 5, 4, 0, 0, 21, 1, 1, 0, 0, 0, 22, 23, 5, 5, 0, 0, 23, 28, 3, 4, 2, 0, 24, 25, 5, 16,
        0, 0, 25, 26, 5, 6, 0, 0, 26, 28, 3, 4, 2, 0, 27, 22, 1, 0, 0, 0, 27, 24, 1, 0, 0, 0, 28, 3,
        1, 0, 0, 0, 29, 30, 6, 2, -
            1, 0, 30, 37, 5, 15, 0, 0, 31, 32, 5, 1, 0, 0, 32, 33, 3, 4, 2,
        0, 33, 34, 5, 2, 0, 0, 34, 37, 1, 0, 0, 0, 35, 37, 5, 16, 0, 0, 36, 29, 1, 0, 0, 0, 36, 31,
        1, 0, 0, 0, 36, 35, 1, 0, 0, 0, 37, 46, 1, 0, 0, 0, 38, 39, 10, 5, 0, 0, 39, 40, 7, 0, 0, 0,
        40, 45, 3, 4, 2, 6, 41, 42, 10, 4, 0, 0, 42, 43, 7, 1, 0, 0, 43, 45, 3, 4, 2, 5, 44, 38, 1,
        0, 0, 0, 44, 41, 1, 0, 0, 0, 45, 48, 1, 0, 0, 0, 46, 44, 1, 0, 0, 0, 46, 47, 1, 0, 0, 0, 47,
        5, 1, 0, 0, 0, 48, 46, 1, 0, 0, 0, 5, 17, 27, 36, 44, 46
    ]


class ExprParser (Parser):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'('", "')'", "'{'", "'}'", "'print'",
                     "'='", "'*'", "'/'", "'+'", "'-'", "<INVALID>", "<INVALID>",
                     "'main'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                      "<INVALID>", "<INVALID>", "<INVALID>", "SPACES", "FUN",
                      "MAIN", "NEWLINE", "INT", "IDENT"]

    RULE_prog = 0
    RULE_stmt = 1
    RULE_expr = 2

    ruleNames = ["prog", "stmt", "expr"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    SPACES = 11
    FUN = 12
    MAIN = 13
    NEWLINE = 14
    INT = 15
    IDENT = 16

    def __init__(self, input: TokenStream, output = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUN(self):
            return self.getToken(ExprParser.FUN, 0)

        def MAIN(self):
            return self.getToken(ExprParser.MAIN, 0)

        def NEWLINE(self, i: int = None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StmtContext)
            else:
                return self.getTypedRuleContext(ExprParser.StmtContext, i)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitProg"):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)

    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 6
            self.match(ExprParser.FUN)
            self.state = 7
            self.match(ExprParser.MAIN)
            self.state = 8
            self.match(ExprParser.T__0)
            self.state = 9
            self.match(ExprParser.T__1)
            self.state = 10
            self.match(ExprParser.T__2)
            self.state = 11
            self.match(ExprParser.NEWLINE)

            self.state = 17
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == 5 or _la == 16:
                self.state = 12
                self.stmt()
                self.state = 13
                self.match(ExprParser.NEWLINE)
                self.state = 19
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 20
            self.match(ExprParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.printexp = None  # ExprContext
            self.ident = None  # Token
            self.assign = None  # ExprContext

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext, 0)

        def IDENT(self):
            return self.getToken(ExprParser.IDENT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_stmt

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitStmt"):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)

    def stmt(self):

        localctx = ExprParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5]:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(ExprParser.T__4)
                self.state = 23
                localctx.printexp = self.expr(0)
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                localctx.ident = self.match(ExprParser.IDENT)

                self.state = 25
                self.match(ExprParser.T__5)
                self.state = 26
                localctx.assign = self.expr(0)
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

    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.left = None  # ExprContext
            self.value = None  # Token
            self.exp = None  # ExprContext
            self.ident = None  # Token
            self.op = None  # Token
            self.right = None  # ExprContext

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext, i)

        def IDENT(self):
            return self.getToken(ExprParser.IDENT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitExpr"):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)

    def expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.state = 30
                localctx.value = self.match(ExprParser.INT)
                pass
            elif token in [1]:
                self.state = 31
                self.match(ExprParser.T__0)
                self.state = 32
                localctx.exp = self.expr(0)
                self.state = 33
                self.match(ExprParser.T__1)
                pass
            elif token in [16]:
                self.state = 35
                localctx.ident = self.match(ExprParser.IDENT)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(
                        self._input, 3, self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(
                            self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_expr)
                        self.state = 38
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 5)")
                        self.state = 39
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not (_la == 7 or _la == 8):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 40
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(
                            self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(
                            localctx, _startState, self.RULE_expr)
                        self.state = 41
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(
                                self, "self.precpred(self._ctx, 4)")
                        self.state = 42
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not (_la == 9 or _la == 10):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 43
                        localctx.right = self.expr(5)
                        pass

                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx: ExprContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 5)

        if predIndex == 1:
            return self.precpred(self._ctx, 4)