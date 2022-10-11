def main():
    infile = open("SymTable.txt", "r")
    symtable = []
    for i in infile:
        i = i.strip("\n")
        i = i.split(" ")
        symtable.append(i)
    infile.close()
    print(symtable)

    fileTo = open("NestIf2.asm", "w")
    temp1 = open("assemblytemp1.txt", "r")
    for i in temp1:
        fileTo.write(i)
    temp1.close()

    for i in range(len(symtable)):
        if symtable[i][1] == "$NUMLIT":
            theString = "\tlit" + str(symtable[i][0]) + "\tDW\t" + str(symtable[i][0]) + "\n"
            fileTo.write(theString)
        elif symtable[i][1] == "<$var>":
            theString = "\t" + str(symtable[i][0]) + "\tDW\t" + str(symtable[i][2]) + "\n"
            fileTo.write(theString)
        else:
            pass

    temp2 = open("assemblytemp2.txt", "r")
    for i in temp2:
        fileTo.write(i)
    temp2.close()

    for i in range(len(symtable)):
        if symtable[i][1] == "<var>":
            theString = "\t" + str(symtable[i][0]) + "\tRESW\t1\n"
            fileTo.write(theString)

    temp3 = open("assemblytemp3.txt", "r")
    for i in temp3:
        fileTo.write(i)
    temp3.close()

    assFromSemantics = open("tempAssembly.txt", "r")
    for i in assFromSemantics:
        fileTo.write(i)
    assFromSemantics.close()

    temp4 = open("assemblytemp4.txt", "r")
    for i in temp4:
        fileTo.write(i)
    temp4.close()

    fileTo.close()

if __name__ == "__main__":
    main()