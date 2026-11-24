continuar = "S"
preco_total = 0
quantidade_produto = 0
while continuar == "S":
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input("Digite o valor do produto: "))
    percentual_desconto_produto = float(input("Digite o percentual de desconto: "))
    if percentual_desconto_produto > 15:
        percentual_desconto_produto = 0
    preco_venda = preco_produto - (preco_produto * (percentual_desconto_produto / 100))
    preco_total = preco_total + preco_venda
    quantidade_produto = quantidade_produto + 1
    continuar = input("Deseja continuar? (S/N) ")
print(f"A soma dos valores é {preco_total}, e a quantidade de produtos é {quantidade_produto}")