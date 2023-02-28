num = int(input("Digite um número: "))

# Definindo os primeiros valores da sequência
fib1, fib2 = 0, 1

# Loop para calcular a sequência até o número desejado ou exceder ele
while fib2 < num:
    fib1, fib2 = fib2, fib1 + fib2

# Verificando se o número está presente na sequência
if fib2 == num:
    print(num, "pertence à sequência de Fibonacci")
else:
    print(num, "não pertence à sequência de Fibonacci")