import lexical


class SyntaxAnalysis:
    keywords = {"<semi>": 0, "<assign>": 1, "<addop>": 2, "<$LP>": 3, "<$RP>": 4, "<mop>": 5, 			"$IF": 6,
                "$THEN": 7, "$ODD": 8, "<relop>": 9, "<$LB>": 10, "<$RB>": 11, "$CALL": 12, 		"$WHILE": 13,
                "$DO": 14, "$ELSE": 15}

    OPTable = [
        [0, '<', 0, '<', 0, 0, '<', 0, 0, 0, 0, '>', 0, '<', 0, 0],
        ['>', 0, '<', '<', 0, '<', 0, 0, 0, 0, 0, 0, 0, 0, 0, '>'],
        ['>', 0, '>', '<', '>', '<', 0, '>', 0, '>', 0, 0, 0, 0, '>', '>'],
        [0, 0, '<', '<', '=', '<', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ['>', 0, '>', 0, '>', '>', 0, 0, 0, 0, 0, 0, 0, 0, 0, '>'],
        ['>', 0, '>', '<', '>', '>', 0, '>', 0, '>', 0, 0, 0, 0, '>', '>'],
        [0, 0, '<', '<', 0, '<', 0, '=', '<', '<', 0, 0, 0, 0, 0, 0],
        ['>', '<', 0, '<', 0, 0, '<', 0, 0, 0, '<', 0, '<', 0, 0, '='],
        [0, 0, '<', '<', 0, '<', 0, '>', 0, 0, 0, 0, 0, 0, 0, '>'],
        [0, 0, '<', '<', 0, '<', 0, '>', 0, 0, 0, 0, 0, 0, '>', '>'],
        [0, '<', 0, 0, 0, 0, '<', 0, 0, 0, '<', '=', '<', '<', 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, '<', '<', 0, '<', 0, 0, '<', '<', 0, 0, 0, 0, '=', 0],
        ['>', '<', 0, '<', 0, 0, 0, 0, 0, 0, '<', 0, '<', '<', 0, 0],
        ['>', '<', 0, '<', 0, 0, '<', 0, 0, 0, '<', 0, '<', 0, 0, 0]]

    def __init__(self, scanner1, symtable):
        self.scanner1 = scanner1
        self.symTable = symtable
        self.stList = []
        self.qlist = []
        self.labels = 1
        self.whiles = 1
        self.reads = []
        self.prints = []

    def getStatements(self):
        self.scanner1.scanner()
        self.scanner1.scanner()
        self.scanner1.scanner()
        while (self.scanner1.fileCounter < self.scanner1.fileLength):
            token = self.scanner1.scanner()
            statement = []
            numBrackets = 0
            if (token[1] == '$CONST') or (token[1] == '<$var>'):
                while token[1] != '<semi>':
                    token = self.scanner1.scanner()
            elif (token[0] == 'Read'):
                token = self.scanner1.scanner()
                statement = ['Read', str(token[0]), '-', '-']
                self.reads.append(statement)
                while token[1] != '<semi>':
                    token = self.scanner1.scanner()
            elif (token[0] == 'Print'):
                token = self.scanner1.scanner()
                statement = ['Print', str(token[0]), '-', '-']
                self.prints.append(statement)
                while token[1] != '<semi>':
                    token = self.scanner1.scanner()
            elif token[1] == '<var>':
                while token[1] != '<semi>':
                    statement.append(token)
                    token = self.scanner1.scanner()
                statement.append(token)
                self.stList.append(statement)

            elif token[1] == '$IF':
                while token[1] != '<semi>':
                    if token[1] == '<$LB>':
                        numBrackets += 1
                    statement.append(token)
                    token = self.scanner1.scanner()
                if numBrackets == 0:
                    statement.append(token)
                    self.stList.append(statement)
                    continue
                else:
                    while numBrackets != 0:
                        if token[1] == '<$LB>':
                            numBrackets += 1
                        if token[1] == '<$RB>':
                            numBrackets -= 1
                        statement.append(token)
                        if numBrackets != 0:
                            token = self.scanner1.scanner()
                    self.stList.append(statement)
            elif token[1] == '$ELSE':
                while token[1] != '<semi>':
                    if token[1] == '<$LB>':
                        numBrackets += 1
                    statement.append(token)
                    token = self.scanner1.scanner()
                if numBrackets == 0:
                    statement.append(token)
                    for i in range(len(statement)):
                        self.stList[-1].append(statement[i])
                    continue
                else:
                    while numBrackets != 0:
                        if token[1] == '<$LB>':
                            numBrackets += 1
                        if token[1] == '<$RB>':
                            numBrackets -= 1
                        statement.append(token)
                        if numBrackets != 0:
                            token = self.scanner1.scanner()
                    for i in range(len(statement)):
                        self.stList[-1].append(statement[i])
            elif token[1] == '$WHILE':
                while token[1] != '<semi>':
                    if token[1] == '<$LB>':
                        numBrackets += 1
                    statement.append(token)
                    token = self.scanner1.scanner()
                if numBrackets == 0:
                    statement.append(token)
                    self.stList.append(statement)
                    continue
                else:
                    while numBrackets != 0:
                        if token[1] == '<$LB>':
                            numBrackets += 1
                        if token[1] == '<$RB>':
                            numBrackets -= 1
                        statement.append(token)
                        if numBrackets != 0:
                            token = self.scanner1.scanner()
                    self.stList.append(statement)
            else:
                print('Error at ' + str(self.scanner1.fileCounter))
        print('--------------------------')
        for i in range(len(self.stList)):
            print(self.stList[i])

    def makeQuads(self):
        finishedQuad = []
        for i in range(len(self.stList)):
            stack = [(';', '<semi>')]
            previousOps = [(';', '<semi>')]
            tempGenerator = []
            fixups = 0
            curr_quad = []
            curr_quad_0 = '-'
            curr_quad_1 = '-'
            curr_quad_2 = '-'
            curr_quad_3 = '-'
            labelIfThen = []
            whileGen = []
            for j in range(len(self.stList[i])):
                currentToken = self.stList[i][j]
                if currentToken[1] not in self.keywords:
                    print(str(currentToken) + ' not in dictionary, is a non-term')
                    stack.append(currentToken)
                elif self.OPTable[self.keywords[previousOps[-1][1]]][self.keywords[currentToken[1]]] == '<':
                    stack.append(currentToken)
                    previousOps.append(currentToken)
                    if currentToken[1] == '$IF':
                        placeHolders = ('-', '-')
                        tupleForLabels = ('IF', '$IF')
                        finishedQuad.append([tupleForLabels, placeHolders, placeHolders, placeHolders])
                    if currentToken[1] == '$WHILE':
                        placeHolders = ('-', '-')
                        tupleForLabels = ('WHILE', '$WHILE')
                        whileGen.append('W' + str(self.whiles))
                        self.whiles += 1
                        finishedQuad.append([tupleForLabels, (whileGen[-1], '<whileLabel>'), placeHolders, placeHolders])
                elif self.OPTable[self.keywords[previousOps[-1][1]]][self.keywords[currentToken[1]]] == '>':
                    while self.OPTable[self.keywords[previousOps[-1][1]]][self.keywords[currentToken[1]]] == '>':
                        popped_op = previousOps.pop()
                        if popped_op[1] == '<addop>' or popped_op[1] == '<mop>':
                            curr_quad_2 = stack.pop()
                            stack.pop()
                            curr_quad_1 = stack.pop()
                            tempGenerator.append('T' + str(len(tempGenerator) + 1))
                            curr_quad_3 = (tempGenerator[-1], '$temp')
                            curr_quad = [popped_op, curr_quad_1, curr_quad_2, curr_quad_3]
                            finishedQuad.append(curr_quad)
                            stack.append(curr_quad_3)
                        elif popped_op[1] == '<assign>':
                            curr_quad_2 = stack.pop()
                            stack.pop()
                            curr_quad_1 = stack.pop()
                            curr_quad_3 = ('-', '-')
                            curr_quad = [popped_op, curr_quad_1, curr_quad_2, curr_quad_3]
                            finishedQuad.append(curr_quad)
                        elif popped_op[1] == '<relop>':
                            curr_quad_2 = stack.pop()
                            stack.pop()  # the relop
                            curr_quad_1 = stack.pop()
                            curr_quad_3 = ('-', '-')
                            curr_quad = [popped_op, curr_quad_1, curr_quad_2, curr_quad_3]
                            finishedQuad.append(curr_quad)
                        elif popped_op[1] == '$THEN':
                            previousOps.pop()
                            stack.pop()
                            stack.pop()
                            moreLabels = (labelIfThen[-1], '<label>')
                            morePlaceHolders = ('-', '-')
                            finishedQuad.append([moreLabels, morePlaceHolders, morePlaceHolders, morePlaceHolders])
                        elif popped_op[1] == '$ELSE':
                            previousOps.pop()
                            previousOps.pop()
                            stack.pop()
                            stack.pop()
                            stack.pop()
                            moreLabels = (labelIfThen[-1], '<label>')
                            morePlaceHolders = ('-', '-')
                            finishedQuad.append([moreLabels, morePlaceHolders, morePlaceHolders, morePlaceHolders])
                        elif popped_op[1] == '$DO':
                            previousOps.pop()
                            stack.pop()
                            stack.pop()
                            moreLabels = (labelIfThen[-1], '<label>')
                            theWhileLabel = (whileGen[-1], '<whileLabel>')
                            morePlaceHolders = ('-', '-')
                            finishedQuad.append([moreLabels, theWhileLabel, morePlaceHolders, morePlaceHolders])
                            labelIfThen.pop()
                            whileGen.pop()
                        elif popped_op[1] == '<semi>':
                            stack.pop()
                    stack.append(currentToken)
                    previousOps.append(currentToken)
                    if stack[-1][1] == '<$RB>':
                        stack.pop()
                        stack.pop()
                        previousOps.pop()
                        previousOps.pop()
                        if (j == (len(self.stList[i]) - 1)) and (previousOps[-1][1] == '$THEN'):
                            previousOps.pop()
                            previousOps.pop()
                            stack.pop()
                            stack.pop()
                            moreLabels = (labelIfThen[-1], '<label>')
                            morePlaceHolders = ('-', '-')
                            finishedQuad.append([moreLabels, morePlaceHolders, morePlaceHolders, morePlaceHolders])
                        if (j == (len(self.stList[i]) - 1)) and (previousOps[-1][1] == '$ELSE'):
                            previousOps.pop()
                            previousOps.pop()
                            stack.pop()
                            stack.pop()
                            stack.pop()
                            moreLabels = (labelIfThen[-1], '<label>')
                            morePlaceHolders = ('-', '-')
                            finishedQuad.append([moreLabels, morePlaceHolders, morePlaceHolders, morePlaceHolders])
                        if (j == (len(self.stList[i]) - 1)) and (previousOps[-1][1] == '$DO'):
                            previousOps.pop()
                            previousOps.pop()
                            stack.pop()
                            stack.pop()
                            moreLabels = (labelIfThen[-1], '<label>')
                            labelIfThen.pop()
                            theWhileLabel = (whileGen[-1], '<whileLabel>')
                            whileGen.pop()
                            morePlaceHolders = ('-', '-')
                            finishedQuad.append([moreLabels, theWhileLabel, morePlaceHolders, morePlaceHolders])
                    if currentToken[1] == '$THEN':
                        labelIfThen.append('L' + str(self.labels))
                        self.labels += 1
                        zero = ('THEN', '$THEN')
                        one = (labelIfThen[-1], '<label>')
                        three = ('-', '-')
                        if finishedQuad[-1][0][0] == '>':
                            two = ('LE', '<jumpCondition>')
                        elif finishedQuad[-1][0][0] == '>=':
                            two = ('L', '<jumpCondition>')
                        elif finishedQuad[-1][0][0] == '<':
                            two = ('GE', '<jumpCondition>')
                        elif finishedQuad[-1][0][0] == '<=':
                            two = ('G', '<jumpCondition>')
                        elif finishedQuad[-1][0][0] == '==':
                            two = ('NE', '<jumpCondition>')
                        elif finishedQuad[-1][0][0] == '!=':
                            two = ('E', '<jumpCondition>')
                        else:
                            print('THEN WAS PUSHED BUT COULDNT FIND THE RIGHT CONDITIONAL')
                            two = ('-', '<jumpCondition>')
                        finishedQuad.append([zero, one, two, three])
                    if currentToken[1] == '$ELSE':
                        labelIfThen.append('L' + str(self.labels))
                        self.labels += 1
                        zero = ('ELSE', '$ELSE')
                        one = (labelIfThen[-1], '<label>')
                        two = ('-', '-')
                        three = ('-', '-')
                        finishedQuad.append([zero, one, two, three])
                        moreLabels = (labelIfThen[fixups], '<label>')
                        morePlaceHolders = ('-', '-')
                        finishedQuad.append([moreLabels, morePlaceHolders, morePlaceHolders, morePlaceHolders])
                        fixups += 1
                    if currentToken[1] == '$DO':
                        labelIfThen.append('L' + str(self.labels))
                        self.labels += 1
                        zero = ('DO', '$DO')
                        one = (labelIfThen[-1], '<label>')
                        three = ('-', '-')
                        if finishedQuad[-1][0][0] == '>':
                            two = ('LE', '<jumpCondition>')
                        elif finishedQuad[-1][0][0] == '>=':
                            two = ('L', '<jumpCondition>')
                        elif finishedQuad[-1][0][0] == '<':
                            two = ('GE', '<jumpCondition>')
                        elif finishedQuad[-1][0][0] == '<=':
                            two = ('G', '<jumpCondition>')
                        elif finishedQuad[-1][0][0] == '==':
                            two = ('NE', '<jumpCondition>')
                        elif finishedQuad[-1][0][0] == '!=':
                            two = ('E', '<jumpCondition>')
                        else:
                            print('THEN WAS PUSHED BUT COULDNT FIND THE RIGHT CONDITIONAL')
                            two = ('-', '<jumpCondition>')
                        finishedQuad.append([zero, one, two, three])
                    if currentToken[1] == '<$RP>':
                        previousOps.pop()
                        previousOps.pop()
                        stack.pop()
                        meTemp = stack.pop()
                        if stack[-1][1] == '<$LP>':
                            stack.pop()
                        if meTemp[1] != '<$LP>':
                            stack.append(meTemp)
                    if currentToken[1] == '<semi>':
                        previousOps.pop()
                        stack.pop()
                elif self.OPTable[self.keywords[previousOps[-1][1]]][self.keywords[currentToken[1]]] == '=':
                    stack.append(currentToken)
                    previousOps.append(currentToken)
                    if currentToken[1] == '$ELSE':
                        labelIfThen.append('L' + str(self.labels))
                        self.labels += 1
                        zero = ('ELSE', '$ELSE')
                        one = (labelIfThen[-1], '<label>')
                        two = ('-', '-')
                        three = ('-', '-')
                        finishedQuad.append([zero, one, two, three])
                        moreLabels = (labelIfThen[fixups], '<label>')
                        morePlaceHolders = ('-', '-')
                        finishedQuad.append([moreLabels, morePlaceHolders, morePlaceHolders, morePlaceHolders])
                        fixups += 1
                    if stack[-1][1] == '<$RB>':
                        stack.pop()
                        stack.pop()
                        previousOps.pop()
                        previousOps.pop()
                        if stack[-1][1] == '$DO':
                            stack.pop()
                            stack.pop()
                            previousOps.pop()
                            previousOps.pop()
                            moreLabels = (labelIfThen[-1], '<label>')
                            theWhileLabel = (whileGen[-1], '<whileLabel>')
                            morePlaceHolders = ('-', '-')
                            finishedQuad.append([moreLabels, theWhileLabel, morePlaceHolders, morePlaceHolders])
                            labelIfThen.pop()
                            whileGen.pop()
                        if stack[-1][1] == '$ELSE':
                            stack.pop()
                            stack.pop()
                            stack.pop()
                            previousOps.pop()
                            previousOps.pop()
                            previousOps.pop()

                            moreLabels = (labelIfThen[-1], '<label>')
                            morePlaceHolders = ('-', '-')
                            finishedQuad.append([moreLabels, morePlaceHolders, morePlaceHolders, morePlaceHolders])
                            labelIfThen.pop()
                else:
                    print('no relation found.')
            print('stack after: ' + str(i))
            for x in range(len(stack)):
                print(stack[x])
            print('----------------------')
        self.qList = finishedQuad
        return finishedQuad

def main(fileName):
    file = open(str(fileName), "r")
    allit = file.read()
    finFile = allit
    file.close()

    scan1 = lexical.LexicalScanner(finFile)
    scan2 = lexical.LexicalScanner(finFile)
    thesymboltable = lexical.parser(scan2)
    syntaxanal = SyntaxAnalysis(scan1, thesymboltable)
    syntaxanal.getStatements()

    usequads = syntaxanal.makeQuads()
    for i in range(len(usequads)):
        print(usequads[i])

    writequads = open("quads.txt", mode="w")
    for i in range(len(syntaxanal.reads)):
        for j in range(3):
            writequads.write(str(syntaxanal.reads[i][j]) + " ")
        writequads.write(str(syntaxanal.reads[i][3]))
        writequads.write("\n")

    for i in range(len(usequads)):
        for j in range(3):
            if usequads[i][j][1] == "<int>":
                writequads.write("lit" + str(usequads[i][j][0]) + " ")
            else:
                writequads.write(str(usequads[i][j][0]) + " ")
        if usequads[i][3][1] == "<int>":
            writequads.write("lit" + str(usequads[i][3][0]))
        else:
            writequads.write(str(usequads[i][3][0]))
        writequads.write("\n")

    for i in range(len(syntaxanal.prints)):
        for j in range(3):
            writequads.write(str(syntaxanal.prints[i][j] + " "))
        writequads.write(str(syntaxanal.prints[i][3]))
        writequads.write("\n")
    writequads.close()

if __name__ == '__main__':
    main('testInput.txt')
