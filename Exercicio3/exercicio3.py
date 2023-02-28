import json

# Leitura do arquivo JSON
with open('dados.json') as file:
    dados = json.load(file)

# Cálculo do menor e maior valor de faturamento
valores = [dado['valor'] for dado in dados if dado['valor'] != 0.0]
minimo = min(valores)
maximo = max(valores)

# Cálculo da média mensal
soma = sum(valores)
media = soma / len(valores)

# Contagem de dias com faturamento diário superior à média
dias_acima_da_media = sum(dado['valor'] > media for dado in dados if dado['valor'] != 0.0)

# Impressão dos resultados
print(f"Menor valor de faturamento: R${minimo:.2f}")
print(f"Maior valor de faturamento: R${maximo:.2f}")
print(f"Dias com faturamento diário acima da média mensal: {dias_acima_da_media}")
