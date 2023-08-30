from flask import Flask, render_template, request
from antlr4 import *
from FunxLexer import FunxLexer
from FunxParser import FunxParser
import sys

if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
    from .FunxVisitor import FunxVisitor
else:
    from FunxParser import FunxParser
    from FunxVisitor import FunxVisitor


class Errores(Exception):
    def __init__(self, mensaje):
        self.mensaje = 'ERROR: ' + mensaje

# Definció d'una funcio


class Function:
    def __init__(self, nom, parametres, instrucions):
        self.nom = nom
        self.parametres = parametres
        self.instrucions = instrucions


class TreeVisitor(FunxVisitor):

    def __init__(self):
        self.nivell = 0
        self.taulaSimbols = [{}]  # La pila
        self.taulaFuncions = {}

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        resultat = self.visit(l[0])
        return resultat

    def visitBloc(self, ctx):
        l = list(ctx.getChildren())
        for i in range(len(l)):
            resultat = self.visit(l[i])
            if resultat != None:
                return resultat

    def visitAssig(self, ctx):
        l = list(ctx.getChildren())
        variable = l[0].getText()
        self.taulaSimbols[-1][variable] = self.visit(l[2])

    def visitFunction(self, ctx):
        l = list(ctx.getChildren())
        nom = l[0].getText()

        # Excepció funció ja estigui definit
        if nom in self.taulaFuncions:
            raise Errores("Funció " + nom + " ja està definit.")

        # Llegir els parametres de la funcio
        parametres = []
        param = l[1].getText()
        i = 1
        while param != '{':
            if param in parametres:
                raise Errores("Paràmetre duplicat en la funció " + nom)
            else:
                parametres.append(param)
            i += 1
            param = l[i].getText()

        # Afegim al diccionari de processos el procés llegit
        self.taulaFuncions[nom] = Function(nom, parametres, ctx.bloc())

    def visitAplyfunction(self, ctx):
        l = list(ctx.getChildren())
        nomF = l[0].getText()

        # Excepció en cas que la funció no esta definit
        if nomF not in self.taulaFuncions:
            raise Errores("funció " + nomF + " no està definit.")

        i = 1
        parametresE = []  # parametre d'entrada
        while i < len(l):
            parametresE.append(self.visit(l[i]))
            i += 1
        if len(self.taulaFuncions[nomF].parametres) != len(parametresE):
            raise Errores("Parametres d'entrada incorrecte")

        vars = {}
        # asignar cada parametre d'entrada amb el parametre d'entrada de la funcio
        for i in range(0, len(parametresE)):
            vars[self.taulaFuncions[nomF].parametres[i]] = parametresE[i]
        self.taulaSimbols.append(vars)
        resultat = self.visit(self.taulaFuncions[nomF].instrucions)

        # guardamos las variables locales en el índice -1 y las vamos eliminando
        self.taulaSimbols.pop()
        return resultat

    def visitIfthen(self, ctx):
        l = list(ctx.getChildren())
        if (self.visit(l[1])):  # si la condicion és True visito el bloc de instrucio
            return self.visit(l[3])

    def visitIfElse(self, ctx):
        l = list(ctx.getChildren())
        if (self.visit(l[1])):  # si la condicion és True visito el bloc de instrucio
            return self.visit(l[3])
        elif len(l) > 5:
            return self.visit(l[7])

    def visitBucleWhile(self, ctx):
        l = list(ctx.getChildren())
        while (self.visit(l[1])):
            self.visit(l[3])

    def visitModul(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[2]) == 0.0:
            raise Errores('Modul entre 0')
        elif len(l) == 1:
            return int(l[0].getText())
        else:  # len(l) == 3
            return self.visit(l[0]) % self.visit(l[2])

    def visitSuma(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            return int(l[0].getText())
        else:  # len(l) == 3
            return self.visit(l[0]) + self.visit(l[2])

    def visitMul(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            return int(l[0].getText())
        else:  # len(l) == 3
            return self.visit(l[0]) * self.visit(l[2])

    def visitDiv(self, ctx):
        l = list(ctx.getChildren())
        if self.visit(l[2]) == 0.0:
            raise Errores('Divisió entre 0')
        elif len(l) == 1:
            return int(l[0].getText())
        else:  # len(l) == 3
            return self.visit(l[0]) / self.visit(l[2])

    def visitRes(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            return int(l[0].getText())
        else:  # len(l) == 3
            return self.visit(l[0]) - self.visit(l[2])

    def visitParen(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            return int(l[0].getText())
        else:  # len(l) == 3
            return self.visit(l[1])

    def visitNum(self, ctx):
        l = list(ctx.getChildren())
        resultat = l[0].getText()
        return float(resultat)

    def visitVaria(self, ctx):
        l = list(ctx.getChildren())
        resultat = l[0].getText()
        return self.taulaSimbols[-1][resultat]

    def visitFunc(self, ctx):
        l = list(ctx.getChildren())
        resultat = l[0].getText()
        if resultat[0] >= 'A' and resultat[0] <= 'Z':
            return self.visit(l[0])

    def visitCondition(self, ctx):
        l = list(ctx.getChildren())
        if len(l) == 1:
            return self.visit(l[0])
        elif l[1].getText() == "<":  # MENOR
            return self.visit(l[0]) < self.visit(l[2])
        elif l[1].getText() == ">":  # MAJOR
            return self.visit(l[0]) > self.visit(l[2])
        elif l[1].getText() == ">=":  # MAJOR O IGUAL
            return self.visit(l[0]) >= self.visit(l[2])
        elif l[1].getText() == "<=":  # MENOR O IGUAL
            return self.visit(l[0]) <= self.visit(l[2])
        elif l[1].getText() == "=":  # EQUAL
            return self.visit(l[0]) == self.visit(l[2])
        elif l[1].getText() == "!=":  # NOT EQUAL
            return self.visit(l[0]) != self.visit(l[2])


contador = 0
operacions = []
resultatFuncio = {}
visitor = TreeVisitor()

app = Flask(__name__)


@app.route("/",)
def calcul():
    return render_template('base.html')


@app.route("/", methods=['POST', 'GET'])
def resultat():
    # LLegir el Input
    codi = InputStream(str(request.form["consola"]))
    lexer = FunxLexer(codi)
    token_stream = CommonTokenStream(lexer)
    parser = FunxParser(token_stream)
    tree = parser.root()
    global contador
    try:
        out = visitor.visit(tree)

        # Escriure el resultat de Input
        contador += 1
        input = f'{codi}'
        output = f'{out}'

        # Actualitzar el resulta de output, si és major que 5
        if len(operacions) == 5:
            operacions.pop(0)
            operacions.append((contador, input, output))
        else:
            operacions.append((contador, input, output))
        operacions2 = reversed(operacions)

        # Escriure el resultat de Funcio
        for key in visitor.taulaFuncions:
            if key not in resultatFuncio:
                func = key
                for parametre in visitor.taulaFuncions[key].parametres:
                    func += " " + parametre + " "
                resultatFuncio[key] = func

    except Errores as e:
        out = e.mensaje
        # Escriure el resultat de Input
        contador += 1
        input = f'{codi}'
        output = f'{out}'

        # Actualitzar el resulta de output, si és major que 5
        if len(operacions) == 5:
            operacions.pop(0)
            operacions.append((contador, input, output))
        else:
            operacions.append((contador, input, output))
        operacions2 = reversed(operacions)

    return render_template('base.html', operacio=operacions2, funciones=resultatFuncio)


if __name__ == "__main__":
    app.run()
