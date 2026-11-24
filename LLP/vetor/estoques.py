produtos = [ "Computador Desktop", "Laptop", "Monitor LED",
             "Teclado Mecânico", "Mouse Óptico", "Impressora Multifuncional",
             "Webcam", "Fone de Ouvido com Microfone", "Pendrive",
             "HD Externo", "Roteador Wi-Fi", "Placa de Vídeo", "Memória RAM",
             "Fonte de Alimentação", "Gabinete" ]
estoques = [ 487, 434, 1, 3, 332, 123, 23, 2, 3, 44, 343, 6, 777, 56 , 4 ]
print("*************************************\n"
      "CONTROLE DE ESTOQUE\n"
      "*************************************\n"
      "Situação: [baixo]")

for i in range(len(produtos)):
    if estoques[i] < 5:
        print(f"-{produtos[i]}: {estoques[i]}-{10 - estoques[i]}")
