#EXERCÍCIO 03
#Crie uma função chamada comparar_numeros(a, b). A função deverá receber dois números e informar se o primeiro é maior que o segundo, se o segundo é maior que o primeiro ou se os dois números são iguais.
input_a = int(input("Digite o primeiro número: "))
input_b = int(input("Digite o segundo número: "))
def comparar_numeros(a, b):
    if a > b:
        return f"{a} é maior que {b}"
    elif a < b:
        return f"{a} é menor que {b}"
    else:
        return f"{a} é igual a {b}"
resultado_comparacao = comparar_numeros(input_a, input_b)
print(resultado_comparacao)