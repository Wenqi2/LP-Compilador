grammar Funx;
root : bloc EOF ;

bloc: instruccio* ;

instruccio
        : assig 
        | ifcondition
        | bucleWhile
        | function
        | expr
        ;

aplyfunction: ID expr*;

function:  ID  Minuscula*  '{' bloc '}';

assig: Minuscula '<-' expr;

expr : <assoc=right> '('expr ')'#Paren
    |expr '%' expr #Modul
    | expr '*' expr #Mul
    | expr '/' expr #Div
    | expr '+' expr #Suma
    | expr '-' expr #Res 
    | aplyfunction #Func
    | Minuscula #Varia
    | NUM #Num
    ;
    
bucleWhile : 'while' condition '{' bloc '}';

condition : expr ('='|'!='| '<'|'>'|'>='|'<=') expr;

ifcondition: 
            'if' condition '{' bloc '}' #Ifthen
            | 'if' condition '{' bloc '}' ('else''{' bloc '}')? #IfElse
            ; 

NUM : [0-9]+ ;
ID : [A-Z][a-zA-Z0-9]*;
Minuscula: [a-z0-9]+;
WS : [ \n]+ -> skip ;


COMENTARI : '#' ~[\r\n]* -> skip;