string_original = input("Digite uma string para ser invertida: ") # solicita a entrada do usuário

string_invertida = "" # inicializa a string invertida vazia

# percorre a string original de trás para frente, adicionando cada caractere à string invertida
for i in range(len(string_original)-1, -1, -1):
    string_invertida += string_original[i]

print("String original: ", string_original)
print("String invertida: ", string_invertida)