total = 0
continuar = "S"
while continuar == "S":
    idade = int(input("Digite uma idade: "))
    total = total + idade
    continuar = input("Deseja continuar? (S/N) ")
print(f"A soma total das idades é: {total}")