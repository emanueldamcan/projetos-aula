def celsius_farenheit(c):
    f = c * 1.8 + 32
    return f
celsius = int(input("Digite um valor C: "))
print(celsius_farenheit(celsius))