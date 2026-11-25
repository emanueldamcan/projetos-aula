#EXERCÍCIO 05
#Crie uma função chamada classificar_idade(idade). A função deverá receber a idade de uma pessoa e retornar sua classificação.
#0 a 12 anos: Criança
#13 a 17 anos: Adolescente
#18 a 59 anos: Adulto
#60 anos ou mais: Idoso
idade_input = int(input("Digite a idade: "))
def classificar_idade(idade):
    if idade >= 0 and idade <= 12:
        return "Criança"
    elif idade >= 13 and idade <= 17:
        return "Adolescente"
    elif idade >= 18 and idade <= 59:
        return "Adulto"
    else:
        return "Idoso"
idade_func = classificar_idade(idade_input)
print(f"A classificação da idade {idade_input} é: {idade_func}")