# LAB 3.1  Implement Program that identifies valid c identifiers.
import os

os.system("cls")

c_keywords = {
    "auto",
    "break",
    "case",
    "char",
    "const",
    "continue",
    "default",
    "do",
    "double",
    "else",
    "enum",
    "extern",
    "float",
    "for",
    "goto",
    "if",
    "int",
    "long",
    "register",
    "return",
    "short",
    "signed",
    "sizeof",
    "static",
    "struct",
    "switch",
    "typedef",
    "union",
    "unsigned",
    "void",
    "volatile",
    "while",
}

str = input("Enter an identifier to check: ")

if len(str) == 0:
    print("Invalid Identifier")

elif not (str[0].isalpha() or str[0] == "_"):
    print("Invalid Identifier")

elif not all(ch.isalnum() or ch == "_" for ch in str):
    print("Invalid Identifier")

elif str in c_keywords:
    print("It is a C keyword")

else:
    print("Valid identifier")
