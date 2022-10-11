class LexicalScanner:
    tokenConverter = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0, 'h': 0, 'i': 0, 			       'j': 0, 'k': 0, 'l': 0,
                      'm': 0,
                      'n': 0, 'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0, 'v': 0, 			       'w': 0, 'x': 0, 'y': 0,
                      'z': 0,

                      'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 			       'J': 0, 'K': 0, 'L': 0,
                      'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 			       'V': 0, 'W': 0, 'X': 0,
                      'Y': 0, 'Z': 0,

                      '0': 1, '1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1, 			       '9': 1,

                      "+": 2, "-": 3, "*": 4, ",": 5, ";": 6, ")": 7, "(": 8, "{": 9, "}": 10,
                      "/": 11, "=": 12, "<": 13, ">": 14, "!": 15,

                      " ": 16, "\n": 16, "\t": 16, "\r": 16
                      }

    with open("fsatable.txt", "r") as file:
        FSA_table = [[int(x) for x in line.split()] for line in file]

    def __init__(self, file):
        self.file = file
        self.fileCounter = 0
        self.fileLength = len(self.file)
        self.tokenList = []

    def scanner(self):
        finished = False
        current = self.fileCounter
        token = ""
        tokenType = ""
        nextState = 0

        if (self.fileCounter >= self.fileLength):
            return
        while (not finished):
            if (nextState == 0):
                token = ""
                nextState = LexicalScanner.FSA_table[nextState][LexicalScanner.tokenConverter[self.file[current]]]
                if (nextState != 0):
                    token += self.file[current]
                current += 1
            elif (nextState == 1):
                print("error at " + str(current) + ". Character is " + str(self.file[current]) + ".")
                finished = True
                self.fileCounter = current
                return -1
            elif (nextState == 2):
                tokenType = "<addop>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 3):
                tokenType = "<addop>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 4):
                tokenType = "<mop>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 5):
                tokenType = "<comma>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 6):
                tokenType = "<semi>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 7):
                tokenType = "<$RP>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 8):
                tokenType = "<$LP>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 9):
                tokenType = "<$LB>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 10):
                tokenType = "<$RB>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 11):
                nextState = LexicalScanner.FSA_table[nextState][LexicalScanner.tokenConverter[self.file[current]]]
                if (nextState == 11):
                    token += self.file[current]
                    current += 1
            elif (nextState == 12):
                tokenType = "<int>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 13):
                nextState = LexicalScanner.FSA_table[nextState][LexicalScanner.tokenConverter[self.file[current]]]
                if (nextState == 13):
                    token += self.file[current]
                    current += 1
            elif (nextState == 14):
                if (token == "CONST"):
                    tokenType = "$CONST"
                    self.tokenList.append((token, tokenType))
                elif (token == "IF"):
                    tokenType = "$IF"
                    self.tokenList.append((token, tokenType))
                elif (token == "VAR"):
                    tokenType = "<$var>"
                    self.tokenList.append((token, tokenType))
                elif (token == "THEN"):
                    tokenType = "$THEN"
                    self.tokenList.append((token, tokenType))
                elif (token == "PROCEDURE"):
                    tokenType = "$PROCEDURE"
                    self.tokenList.append((token, tokenType))
                elif (token == "WHILE"):
                    tokenType = "$WHILE"
                    self.tokenList.append((token, tokenType))
                elif (token == "DO"):
                    tokenType = "$DO"
                    self.tokenList.append((token, tokenType))
                elif (token == "CALL"):
                    tokenType = "$CALL"
                    self.tokenList.append((token, tokenType))
                elif (token == "CLASS"):
                    tokenType = "$CLASS"
                    self.tokenList.append((token, tokenType))
                elif (token == "ELSE"):
                    tokenType = "$ELSE"
                    self.tokenList.append((token, tokenType))
                else:
                    tokenType = "<var>"
                    self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 15):
                nextState = LexicalScanner.FSA_table[nextState][LexicalScanner.tokenConverter[self.file[current]]]
                if (nextState == 17):
                    token += self.file[current]
                    current += 1
            elif (nextState == 16):
                tokenType = "<mop>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 17):
                if (self.file[current] == "*"):
                    nextState = LexicalScanner.FSA_table[nextState][LexicalScanner.tokenConverter[self.file[current]]]
                    current += 1
                else:
                    token += self.file[current]
                    current += 1
            elif (nextState == 18):
                if (self.file[current] == "/"):
                    nextState = LexicalScanner.FSA_table[nextState][LexicalScanner.tokenConverter[self.file[current]]]
                    current += 1
                else:
                    nextState = 17
                    token += self.file[current]
                    current += 1
            elif (nextState == 19):
                nextState = LexicalScanner.FSA_table[nextState][LexicalScanner.tokenConverter[self.file[current]]]
                if (nextState == 21):
                    token += self.file[current]
                    current += 1
            elif (nextState == 20):
                tokenType = "<assign>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 21):
                tokenType = "<relop>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 22):
                nextState = LexicalScanner.FSA_table[nextState][LexicalScanner.tokenConverter[self.file[current]]]
                if (nextState == 24):
                    token += self.file[current]
                    current += 1
            elif (nextState == 23):
                tokenType = "<relop>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 24):
                tokenType = "<relop>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 25):
                nextState = LexicalScanner.FSA_table[nextState][LexicalScanner.tokenConverter[self.file[current]]]
                if (nextState == 27):
                    token += self.file[current]
                    current += 1
            elif (nextState == 26):
                tokenType = "<relop>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 27):
                tokenType = "<relop>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            elif (nextState == 28):
                nextState = LexicalScanner.FSA_table[nextState][LexicalScanner.tokenConverter[self.file[current]]]
                if (nextState == 30):
                    token += self.file[current]
                    current += 1
            elif (nextState == 29):
                print("Error at " + str(current) + "." + " Char is " + str(self.file[current]))
                finished = True
                self.fileCounter = current
                return -1
            elif (nextState == 30):
                tokenType = "<relop>"
                self.tokenList.append((token, tokenType))
                finished = True
                self.fileCounter = current
                return (token, tokenType)
            else:
                print("error: state not caught")
                return -1


def parser(scannerObject):
    parsingConverter = {"$CLASS": 0, "<var>": 1, "<$LB>": 2, "$CONST": 3, "<assign>": 4, "<int>": 5,
        "<comma>": 6, "<semi>": 7, "<$var>": 8, "$IF": 9, "$THEN": 10, "$PROCEDURE": 11, "$WHILE": 12,
        "$CALL": 13, "$DO": 14, "$ODD": 15}


    with open("parseTable.txt", "r") as file:
        parseTable = [[int(x) for x in line.split()] for line in file]

    symtable = []
    nextState = 0
    prevVar = ''
    codeSeg = 0
    dataSeg = 0
    output = None

    while (scannerObject.fileCounter < scannerObject.fileLength):
        currToken = scannerObject.scanner()
        if (nextState == 0):
            nextState = parseTable[nextState][parsingConverter[currToken[1]]]
            if (currToken[1] == '<var>'):
                prevVar = currToken[0]
        elif (nextState == 1):
            nextState = parseTable[nextState][parsingConverter[currToken[1]]]
            if (currToken[1] == '<var>'):
                prevVar = currToken[0]
                output = [str(currToken[0]), "<Program Name>", " ", 0, "CS"]
                symtable.append(output)
                codeSeg += 2
        elif (nextState == 2):
            nextState = parseTable[nextState][parsingConverter[currToken[1]]]
            if (currToken[1] == '<var>'):
                prevVar = currToken[0]
        elif (nextState == 3):
            nextState = parseTable[nextState][parsingConverter[currToken[1]]]
            if (currToken[1] == '<var>'):
                prevVar = currToken[0]
        elif (nextState == 4):
            nextState = parseTable[nextState][parsingConverter[currToken[1]]]
            if (currToken[1] == '<var>'):
                prevVar = currToken[0]
        elif (nextState == 5):
            nextState = parseTable[nextState][parsingConverter[currToken[1]]]
            if (currToken[1] == '<var>'):
                prevVar = currToken[0]
        elif (nextState == 6):
            nextState = parseTable[nextState][parsingConverter[currToken[1]]]
            if (currToken[1] == '<var>'):
                prevVar = currToken[0]
            output = [prevVar, "<$var>", currToken[0], dataSeg, "DS"]
            symtable.append(output)
            dataSeg += 2
        elif (nextState == 7):
            nextState = parseTable[nextState][parsingConverter[currToken[1]]]
            if (currToken[1] == '<var>'):
                prevVar = currToken[0]
        elif (nextState == 8):
            nextState = parseTable[nextState][parsingConverter[currToken[1]]]
            output = [currToken[0], "<var>", "-", dataSeg, "DS"]
            symtable.append(output)
            dataSeg += 2
            if (currToken[1] == '<var>'):
                prevVar = currToken[0]
        elif (nextState == 9):
            nextState = parseTable[nextState][parsingConverter[currToken[1]]]
            if (currToken[1] == '<var>'):
                prevVar = currToken[0]
        elif (nextState == 10):
            if currToken[1] in parsingConverter:
                nextState = parseTable[nextState][parsingConverter[currToken[1]]]
            else:
                nextState = 10
            if (nextState == 11):
                isdupe = False
                for i in range(len(symtable)):
                    if (symtable[i][0] == currToken[0]):
                        isdupe = True
                if not isdupe:
                    output = [currToken[0], "$NUMLIT", currToken[0], dataSeg, "DS"]
                    symtable.append(output)
                    dataSeg += 2
        elif (nextState == 11):
            nextState = 10
    for i in range(10):
        temp = "T" + str(i + 1)
        currOutput = [temp, "$TEMP", "-", dataSeg, "DS"]
        symtable.append(currOutput)
        dataSeg += 2
    return symtable


def main(inputFile):
    inFile = open(str(inputFile), 'r')
    readFile = inFile.read()
    myFile = readFile
    inFile.close()

    outFile = open("tokens.txt", 'w')
    sc = LexicalScanner(myFile)
    while (sc.fileCounter < sc.fileLength):
        token = sc.scanner()
        outFile.write(str(token[0]) + " " + str(token[1]) + '\n')
    outFile.close()

    sc2 = LexicalScanner(myFile)
    symbols = parser(sc2)
    symbolOut = open("SymTable.txt", "w")
    for i in range(len(symbols)):
        for j in range(len(symbols[i])):
            symbolOut.write(str(symbols[i][j]) + " ")
        symbolOut.write("\n")


if __name__ == "__main__":
    main("testInput.txt")
