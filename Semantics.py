def main():
    infile = open("quads.txt", 'r')
    quadList = []

    for line in infile:
        line = line.strip('\n')
        line = line.split(" ")
        quadList.append(line)
    infile.close()

    outfile = open("tempAssembly.txt", "w")
    tStr = ""
    for i in range(len(quadList)):
        if quadList[i][0] == "=":
            tStr = "\tmov ax, [" + str(quadList[i][2]) + "]\n"
            tStr += "\tmov [" + str(quadList[i][1]) + "], ax\n"
            outfile.write(tStr)
        elif quadList[i][0] == "+":
            tStr = "\tmov ax, [" + str(quadList[i][1]) + "]\n"
            tStr += "\tadd ax, [" + str(quadList[i][2]) + "]\n"
            tStr += "\tmov [" + str(quadList[i][3]) + "], ax\n"
            outfile.write(tStr)
        elif quadList[i][0] == "-":
            tStr = "\tmov ax, [" + str(quadList[i][1]) + "]\n"
            tStr += "\tsub ax, [" + str(quadList[i][2]) + "]\n"
            tStr += "\tmov [" + str(quadList[i][3]) + "], ax\n"
            outfile.write(tStr)
        elif quadList[i][0] == "/":
            tStr += "\tmov ax, [" + str(quadList[i][1]) + "]\n"
            tStr += "\tmov bx, [" + str(quadList[i][2]) + "]\n"
            tStr += "\tdiv bx\n"
            tStr += "\tmov [" + str(quadList[i][3]) + "], ax\n"
            outfile.write(tStr)
        elif quadList[i][0] == "*":
            tStr = "\tmov ax, [" + str(quadList[i][1]) + "]\n"
            tStr += "\tmul word[" + str(quadList[i][2]) + "]\n"
            tStr += "\tmov [" + str(quadList[i][3]) + "], ax\n"
        elif quadList[i][0] == "IF":
            pass
        elif quadList[i][0] == "WHILE":
            tStr = quadList[i][1] + ":"
            outfile.write(tStr)
        elif ((quadList[i][0] == "<") or (quadList[i][0] == ">") or (quadList[i][0] == "<=") or (quadList[i][0] == ">=")):
            tStr = "\tmov ax, [" + str(quadList[i][1]) + "]\n"
            tStr += "\tcmp ax, [" + str(quadList[i][2]) + "]\n"
            outfile.write(tStr)
        elif quadList[i][0] == "THEN":
            tStr = "\tJ" + str(quadList[i][2])
            tStr += " " + str(quadList[i][1] + "\n")
            outfile.write(tStr)
        elif quadList[i][0] == "ELSE":
            tStr = "\tJMP " + str(quadList[i][1]) + "\n"
            outfile.write(tStr)
        elif quadList[i][0] == "DO":
            tStr = "\tJ" + str(quadList[i][2])
            tStr += "\tJ" + str(quadList[i][1]) + "\n"
            outfile.write(tStr)
        elif quadList[i][0][0] == "L" and quadList[i][1][0] == "W":
            tStr = "\tJMP " + str(quadList[i][1]) + "\n"
            tStr += str(quadList[i][0]) + ": nop\n"
            outfile.write(tStr)
        elif quadList[i][0][0] == "L":
            tStr = str(quadList[i][0]) + ":\tnop\n"
            outfile.write(tStr)
        elif quadList[i][0] == "Read":
            tStr = "\tcall PrintString\n"
            tStr += "\tcall GetAnInteger\n"
            tStr += "\tmov ax, [ReadInt]\n"
            tStr += "\tmov [" + str(quadList[i][1]) + "], ax\n"
            outfile.write(tStr)
        elif quadList[i][0] == "Print":
            tStr = "\tmov ax, [" + str(quadList[i][1]) + "]\n"
            tStr += "\tcall ConvertIntegerToString\n"
            tStr += "\tmov eax, 4\n"
            tStr += "\tmov ebx, 1\n"
            tStr += "\tmov ecx, Result\n"
            tStr += "\tmov edx, ResultEnd\n"
            tStr += "\tint 80h\n"
            outfile.write(tStr)
    outfile.close()
if __name__ == '__main__':
    main()
