#EXERCÍCIO 01
#Crie uma função chamada verificar_media(nota1, nota2, nota3). A função deverá receber três notas, calcular a média do aluno e retornar a situação correspondente.
#Média ≥ 6: Aprovado
#Média ≥ 3 e < 6: Recuperação
#Média < 3: Reprovado
#O programa deverá solicitar as três notas e exibir a média final e a situação do aluno.

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))
def verificar_media(nota1, nota2, nota3):
    return (nota1 + nota2 + nota3) / 3
media = verificar_media(n1, n2, n3)
if media >= 6:
    print("Aprovado")
elif media >= 3 and media < 6:
    print("Recuperação")
else:
    print("Reprovado")
print(f"Primeira nota: {n1}\nSegunda nota: {n2}\nTerceira nota: {n3}\nMédia: {media}")