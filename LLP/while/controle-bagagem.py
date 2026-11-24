continuar = "S"
peso_total = 0
quantidade = 0
while continuar == "S":
    quantidade = quantidade + 1
    peso = float(input("Digite o valor do peso da mala: "))
    peso_total = peso_total + peso
    if quantidade > 3 or peso_total > 23:
        print("debug NOP")
        continuar = "N"
    else:
        print(f"O peso da mala é {peso}, o peso total nesse momento é {peso_total} e tem {quantidade} malas.")
        continuar = input("Deseja continuar? [S/N] ")