# El intérprete de funciones Funx

Es un proyecto sobre un pequeño intérprete de el lenguaje Funx. Que realiza una pequeña parte de trabajo de un compilador. El proyecto está escrito básicamente en python, antlr y html.

El proyecto está formado por:
* **Funx.g** que es la la gramática de Funx, creado con Antlr.
* **Funx.py** Es el interpretador de la gramática y backend de la página web.
* **base.html** Es la página web del intérprete.

## Ejecución de la programa 
Para poder ejecutar la programa, previamente hay que tener instalado los materiales necesarios como **flask**, **jinja2**, **antlr**.
Estos son los comandos necesario para generar ficheros necesario:
>antlr4 -Dlanguage=Python3 -no-listener Funx.g

>antlr4 -Dlanguage=Python3 -no-listener -visitor Funx.g

Para poder ejecutar la programa, necesita utilizar siguiente comando en el terminar:
>export FLASK_APP=funx

>flask run

La programa dará una página web donde puede entrar:
>http://127.0.0.1:5000/

## Uso de la programa 
En la página web puede encontrar una zona que se llama consola donde puede utilizar las expresiones que permite el lenguaje funx. 
como:
> 3 + 4 * 2
o
>DOS { 2 }
>Suma2 x { DOS + x }
>Suma2 3

En la zona de resultado se muestra el resultado de la expresión introducido. Y la zona de función se muestra la función que has introducido previamente.

## inconveniente 
Aunque hemos tratado los posibles errores, si el usuario no sigue la norma de funx el programa se dejará de funcionar. Por ejemplo, si escribe algo así:

> 3 */ 2
> 3 * 2 3





