produto = input("Digite o nome do produto: ")
valor = float(input("Digite o valor do produto: "))
representante = input("Voce é representante? (S/N) ")

print(f"Nome do produto: {produto}")
print(f"Valor do produto: {valor}")
if representante == "S":
    valor = valor - (0.18 * valor)
    print(f"Valor do produto com desconto: {valor}")
elif representante == "N":
    valor = valor - (0.05 * valor)
    print(f"Valor do produto com desconto: {valor}")