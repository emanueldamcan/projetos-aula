# while loop
continuar = "S"
while continuar == "S":
    # values for coefficients a, b, and c
    valor_a = float(input("Digite o valor do variavel a: "))
    valor_b = float(input("Digite o valor do variavel b: "))
    valor_c = float(input("Digite o valor do variavel c: "))
    # calculating Δ (b² - 4ac)
    def delta_calc(a, b, c):
        return (b * b) - (4 * a * c)
    valor_delta = delta_calc(valor_a, valor_b, valor_c)
    # solving for x (-b ± Δ / 2a)
    def x_calc(a, b, delta):
        return (f"Valor x’: {(-b + delta ** 0.5) / (2 * a)}\n"
                f"Valor x’’: {(-b - delta ** 0.5) / (2 * a)}")
    valor_x = x_calc(valor_a, valor_b, valor_delta)
    # if Δ is a negative value, do not print x
    if valor_delta > 0:
        print("Duas raízes reais e distantes")
        print(valor_x)
    elif valor_delta == 0:
        print("Duas raízes reais e iguais")
        print(valor_x)
    else:
        print("Duas raízes complexas")
    # repeat
    continuar = input("Deseja calcular mais uma equação do 2º grau? (S/N): ")