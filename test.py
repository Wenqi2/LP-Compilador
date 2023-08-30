from antlr4 import *
from FunxLexer import FunxLexer
from FunxParser import FunxParser
from FunxVisitor import FunxVisitor
import sys

input_stream = FileStream(sys.argv[1], encoding='utf-8')
lexer = FunxLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = FunxParser(token_stream)
tree = parser.root()
visitor = FunxVisitor()
visitor.visit(tree)

