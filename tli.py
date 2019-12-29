import sys
import re

class Expr:

    def evalExpr(strExpr):
        solvedExpr = eval(strExpr)

        return solvedExpr

    def printExpr(expression, ST, LT):
        oprList = ["+", "-", "*", "/", "<", ">", "<=", ">=", "==", "!=", ",", "="]

        strExpr = ' '.join(expression)
        commaSepList = strExpr.split(',')

        for index, elm in enumerate(expression):
            if (elm in oprList or elm.isnumeric()): continue
            if ("\'" in elm) or ('"' in elm): continue
            
            expression[index] = str(ST.get(elm))
            postStrExpr = ' '.join(expression)
 
        tempV = str(eval(postStrExpr))
        tempV = tempV.replace('(','').replace(')','').replace(',', '')
        return tempV


    def parseExpr(expression, ST, LT):
        oprList = ["+", "-", "*", "/", "<", ">", "<=", ">=", "==", "!="]
        doNothing = 0

        if (str(expression[0]).isdigit() != True and len(expression) == 1):
            return(ST.get(expression[0])) 
        for index, elm in enumerate(expression):
            if (str(elm).isdigit() != True) and (elm not in oprList):
                expression[index] = ST.get(elm)

      #  print('expression2: ', expression)
        for index, elm in enumerate(expression):
           # print(elm)
            expression[index] = str(elm)
            
        return (eval(str(' '.join(expression))))
        

class Stmts:

    # retrieve an if statements var value before passing it to parseExpr from perform
    def perform(lines, ST, LT):

        oprList = ["+", "-", "*", "/", "<", ">", "<=", ">=", "==", "!="]
        printVal = ""
        index = 0

        while index < len(lines):


            word = lines[index].split(' ')

            if (':' in word[0]):
                word[0] = word[0].split('\t', 1)[-1]

            if (word[0] == "print"):
                printVal = Expr.printExpr(word[1:],ST,LT)
                print(printVal)

            if word[0] == "if":
                # if the first word is a variable
                if (word[1].isdigit != True):
                    word[1] = ST.get(word[1])

                if (word[3].isdigit != True):
                    word[3] = ST.get(word[3])              
                boolVal = Expr.parseExpr(word[1:4], ST, LT)

                (newIndex) = LT.get(word[-1])
                if boolVal: 
                    index = newIndex
                    continue
                else: 
                    index = index + 1
                    continue

            if word[0] == "input": 
                ST[word[1]] = input()
                index = index + 1
                continue

            if word[0] == "let":
                if '"' in word[3]:
                    ST[word[1]] = word[3]
                else: 

                    ST[word[1]] = Expr.parseExpr(word[3:], ST, LT)

                index = index + 1
                continue
            else: 
                index = index + 1
                continue

    def fillLT(lines, labelTable):
        for index, element in enumerate(lines):
            if ':' in element:
                label = element.split(':')[0]
                labelTable[label] = (index)
        return labelTable
    def parseStmt(lines, ST, LT):

        returnLines = []

        for line in lines:
            line = line.strip()

            if len(line) < 2:
                lines.remove(line)

            returnLines.append(line)
        return returnLines
    def __init__(self, lines, ST, LT):
        symTable = {}
        labelTable = {}
        Stmts.fillLT(lines, labelTable)
        lines = Stmts.parseStmt(lines, symTable, labelTable)

        Stmts.perform(lines, symTable, labelTable)
def main():
    symTable = {}
    labelTable = {}
    argLines = []
    inputFile = open(sys.argv[1], 'r')
    fileContents = inputFile.read()

    fileLines = fileContents.split('\n')

    arrStmt = fileLines

    arrTerms = []
    for x in fileContents.split(' '): arrTerms.append(x.rstrip())
    Stmts(fileLines, symTable, labelTable)

if __name__ == "__main__":
    main()

