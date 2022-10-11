import lexical
import Syntax
import Semantics
import CodeGen

def main():
    inputFile = input("Enter file name: ")

    lexical.main(inputFile)
    Syntax.main(inputFile)
    Semantics.main()
    CodeGen.main()

if __name__ == "__main__":
    main()