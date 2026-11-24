continuar = "S"
total = 0

while continuar == "S":
    kilo_inicial = float(input("Digite a kilometragem inicial: "))
    kilo_final = float(input("Digite a kilometragem final: "))
    kilo_total = kilo_final - kilo_inicial
    custo_corrida = kilo_total * 2.30
    print(f"O custo da corrida é {custo_corrida}")
    total = total + custo_corrida
    continuar = input("Deseja continuar? (S/N) ")

print(f"O total de todas as corridas é {total}")