This is a Python interpreter for a syntax-restricted tiny language.
It will read in a text file argument containing pseudocode-like statements
of code, parse this file to read in labels and variables(symbols) to
store in the Label Table hashmap and Symbol Table hashmap for later reference.

There will be four types of statements in the specified format: 
/***************************************************/
let	variableName	=	expression
if	expression	goto	label
print	expression1,	expression2,	...
input	variableName
/***************************************************/

Running instructions:
This program can be run by typing
    'python3 tli.py prog*.txt'
where prog*.txt is the file name of any text file containing statements
to be parsed and resolved by our interpreter.

*** STILL A WORK IN PROGRESS ***
Further updates will be coming for text parsing error message provision,
increased flexiblility of statement syntax, and proper type casting.