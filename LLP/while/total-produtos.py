continuar = "S"
total = 0

while continuar == "S":
    nome_produto = input("Digite o nome do produto: ")
    valor_produto = float(input("Digite o valor do produto: "))
    total = total + valor_produto
    continuar = input("Deseja continuar?")

print(f"O valor total de todos os produtos é: {total}")