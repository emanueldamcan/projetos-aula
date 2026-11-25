#EXERCÍCIO 06
#Crie uma função chamada calcular_imc(peso, altura). A função deverá calcular o IMC utilizando a fórmula:
#IMC = peso / (altura × altura)
#Após o cálculo, classifique o resultado da seguinte forma:
#Menor que 18,5: Abaixo do peso
#De 18,5 até 24,9: Peso normal
#De 25 até 29,9: Sobrepeso
#30 ou mais: Obesidade
#O programa deverá exibir o valor calculado do IMC e sua classificação.
peso_input = float(input("Digite o peso em kg: "))
altura_input = float(input("Digite a altura em metros: "))
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 24.9:
        return "Peso normal"
    elif 25 <= imc < 29.9:
        return "Sobrepeso"
    else:
        return "Obesidade"
imc_final = calcular_imc(peso_input, altura_input)
print(f"Seu IMC é: {imc_final}, e você está classificado como: {imc_final}.") 