estados = ["SP", "MG", "RJ", "BA", "PR", "RS", "PE", "CE", "PA", "SC", "GO", "MA", "AM",
           "PB", "ES", "MT", "RN", "PI", "AL", "DF", "MS", "SE", "RD", "TO", "AC", "AP", "RO"]
populacao = [46081801, 21393441, 17223547, 14870907, 11890517, 11233263, 9562007, 9268836,
             8711196, 8187029, 7423629, 7018211, 4321616, 4164468, 4126854, 3893659, 3455236,
             3384547, 3220848, 2996899, 2924631, 2299425, 1751950, 1586859, 884372, 806517,
             738772]
continuar = "S"
while continuar == "S":
    estado_selecionado = input("Informe o estado: ")
    for i in range(len(estados)):
        if estados[i] == estado_selecionado:
            print(f"Estado: {estados[i]} | População: {populacao[i]}")
            continuar = input("Deseja continuar? (S/N) ")