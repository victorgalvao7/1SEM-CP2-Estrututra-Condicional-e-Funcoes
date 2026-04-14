def pode_aprovar(idade, renda, valor):
    return idade >= 18 and valor <= 20 * renda


def definir_taxa(parcelas):
    if 3 <= parcelas <= 6:
        return 0.05
    elif 7 <= parcelas <= 12:
        return 0.08
    elif 13 <= parcelas <= 24:
        return 0.10
    else:
        return None


def calcular_parcela(valor, taxa, parcelas):
    i = taxa
    n = parcelas
    if i == 0:
        return valor / n

    pmt = valor * (i * (1 + i) ** n) / ((1 + i) ** n - 1)
    return pmt


def calcular_total(parcela, parcelas):
    return parcela * parcelas


def calcular_juros(total, valor):
    return total - valor


def main():
    print("=== SISTEMA DE FINANCIAMENTO ===")

    nome = input("Nome do cliente: ")
    idade = int(input("Idade: "))
    renda = float(input("Renda mensal: "))
    valor = float(input("Valor do empréstimo: "))
    parcelas = int(input("Número de parcelas (3 a 24): "))

    aprovado = pode_aprovar(idade, renda, valor)
    taxa = definir_taxa(parcelas)

    if not aprovado or taxa is None:
        print("\nEMPRÉSTIMO NEGADO")
        return

    parcela = calcular_parcela(valor, taxa, parcelas)
    total = calcular_total(parcela, parcelas)
    juros = calcular_juros(total, valor)

    print("\nEMPRÉSTIMO APROVADO ✅")
    print(f"Nome: {nome}")
    print(f"Valor financiado: R$ {valor:.2f}")
    print(f"Taxa de juros: {taxa*100:.0f}% ao mês")
    print(f"Valor da parcela: R$ {parcela:.2f}")
    print(f"Total pago: R$ {total:.2f}")
    print(f"Juros pagos: R$ {juros:.2f}")


if __name__ == "__main__":
    main()
