# Generated from Funx.g by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
else:
    from FunxParser import FunxParser

# This class defines a complete generic visitor for a parse tree produced by FunxParser.

class FunxVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FunxParser#root.
    def visitRoot(self, ctx:FunxParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#bloc.
    def visitBloc(self, ctx:FunxParser.BlocContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#instruccio.
    def visitInstruccio(self, ctx:FunxParser.InstruccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#aplyfunction.
    def visitAplyfunction(self, ctx:FunxParser.AplyfunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#function.
    def visitFunction(self, ctx:FunxParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#assig.
    def visitAssig(self, ctx:FunxParser.AssigContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Div.
    def visitDiv(self, ctx:FunxParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Suma.
    def visitSuma(self, ctx:FunxParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Res.
    def visitRes(self, ctx:FunxParser.ResContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Func.
    def visitFunc(self, ctx:FunxParser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Mul.
    def visitMul(self, ctx:FunxParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Varia.
    def visitVaria(self, ctx:FunxParser.VariaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Num.
    def visitNum(self, ctx:FunxParser.NumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Modul.
    def visitModul(self, ctx:FunxParser.ModulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Paren.
    def visitParen(self, ctx:FunxParser.ParenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#bucleWhile.
    def visitBucleWhile(self, ctx:FunxParser.BucleWhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#condition.
    def visitCondition(self, ctx:FunxParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Ifthen.
    def visitIfthen(self, ctx:FunxParser.IfthenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#IfElse.
    def visitIfElse(self, ctx:FunxParser.IfElseContext):
        return self.visitChildren(ctx)



del FunxParser