#EXERCÍCIO 04
#Crie uma função chamada calcular_desconto(valor). A função deverá calcular o valor final de uma compra de acordo com as seguintes regras:
#Até R$ 100,00: sem desconto
#De R$ 100,01 até R$ 500,00: 5% de desconto
#Acima de R$ 500,00: 10% de desconto
#O programa deverá exibir o valor original da compra, o percentual de desconto, o valor do desconto e o valor final.
valor_inicial = float(input("Digite o valor: "))
valor_percentual = 0
def calcular_desconto(valor):
    if valor <= 100:
        return valor
    elif valor > 100 and valor <= 500:
        return valor * 0.95
    else:
        return valor * 0.90
valor_final = calcular_desconto(valor_inicial)
if valor_inicial > 100 and valor_inicial <= 500:
    valor_percentual = 5
elif valor_inicial > 500:
    valor_percentual = 10
print(f"Valor original: {valor_inicial}\nValor do desconto: {valor_inicial - valor_final}\nValor percentual de desconto: {valor_percentual}%\nValor final com desconto: {valor_final}")