condicao_saude = input("Você está em boas condições de saúde? (S/N) ")
peso = float(input("Digite o seu peso: "))
alimentado = input("Você está alimentado? (S/N) ")
dormido = int(input("Quantas horas você dormiu nas ultimas 24 horas? "))

if condicao_saude == "S" and peso >= 50 and alimentado == "S" and dormido >= 6:
    print("Parabens! Você pode doar sangue!")
else:
    print("Sentimos muito, nesse momento você não doar.")