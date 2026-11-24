cliente = ["Maria","Manoel","José"]
saldo_anterior = [1000, 1200, 950]
imposto = []
saque = [950.00, 25.60, 2.00]
saldo = []
def imposto_calc(valor_saque):
    return valor_saque * 0.016
def saldo_calc(sal_ant, val_saque, val_imp):
    return sal_ant - val_saque - val_imp
for i in range(len(cliente)):
    imp_calculado = imposto_calc(saque[i])
    imposto.append(imp_calculado)
    sld_calculado = saldo_calc(saldo_anterior[i], saque[i], imp_calculado)
    saldo.append(sld_calculado)
for i in range(len(cliente)):
    print(f"{cliente[i]}|{saldo_anterior[i]}|{imposto[i]}|{saque[i]}|{saldo[i]}")