#EXERCÍCIO 02
#Crie uma função chamada verificar_numero(n). A função deverá receber um número e informar se ele é positivo, negativo ou zero. Caso seja diferente de zero, também deverá informar se o número é par ou ímpar.
numero_input = int(input("Digite um numero: "))
def verificar_numero(n):
    if n % 2 == 0:
        return "O número é par."
    else:
        return "O número é ímpar."
numero_final = verificar_numero(numero_input)
if numero_input == 0:
    print(f"O numero é zero")
else:
    print(numero_final)