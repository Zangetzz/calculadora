# Calculadora versão 3.0 by Jão


print("CALCULADORA -------1.1--------")


n1=int(input("Primeiro numero: "))
si=input("Operador: ")
n2=int(input("Segundo numero: "))
 

if si == "+" :
    r=(n1 + n2)

if si == "-":
    r=(n1 - n2)

if si == "/":
    r=(n1 / n2)

if si == "*":
    r=(n1 * n2)

if si == "**":
    r=(n1 ** n2)

if si == "//":
    r=(n1 // n2)

if si == "%":
    r=(n1 % n2)

print("O resultado é {}".format(r))