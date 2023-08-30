default: 
		antlr4 -Dlanguage=Python3 -no-listener Funx.g
		antlr4 -Dlanguage=Python3 -no-listener -visitor Funx.g
 
	