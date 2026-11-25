#EXERCÍCIO 08
#Crie uma função chamada converter_temperatura(valor, tipo). O programa deverá permitir que o usuário escolha entre duas opções de conversão:
#Celsius para Fahrenheit
#Utilize a seguinte fórmula:
#F = (C × 9 / 5) + 32
valor_input = float(input("Digite o valor da temperatura: "))
tipo_input = input("Digite o tipo de temperatura (C/F): ")
def converter_temperatura(valor, tipo):
    if tipo == "C":
        return (valor * 9/5) + 32 
    elif tipo == "F":
        return (valor - 32) * 5/9
temperatura = converter_temperatura(valor_input, tipo_input)
print(f"A temperatura convertida é: {temperatura}")