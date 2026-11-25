#EXERCÍCIO 07
#Crie uma função chamada calcular_reajuste(salario). A função deverá calcular o reajuste salarial de acordo com as seguintes regras:
#Até R$ 2.000,00: aumento de 10%
#De R$ 2.000,01 até R$ 4.000,00: aumento de 7%
#Acima de R$ 4.000,00: aumento de 5%
#O programa deverá exibir o salário atual, o percentual de reajuste, o valor do aumento e o novo salário.
salario_input = float(input("Digite o salário atual: "))
percentual = 0
def calcular_reajuste(salario):
    if salario <= 2000:
        return salario * 1.10
    elif 2000.1 <= salario <= 5000:
        return salario * 1.07
    else:
        return salario * 1.05
salario_final = calcular_reajuste(salario_input)
if salario_input <= 2000:
    percentual = 10
elif 2000.1 <= salario_input <= 5000:
    percentual = 7
else:   
    percentual = 5
print(f"O salario atual é: R${salario_input}\nO percentual de readjuste é: {percentual}%\nO valor do aumento é: R${salario_final - salario_input}\nO novo salário é: R${salario_final}")