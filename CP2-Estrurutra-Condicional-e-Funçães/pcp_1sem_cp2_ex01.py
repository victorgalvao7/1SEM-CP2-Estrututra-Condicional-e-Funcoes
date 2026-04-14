# Faça um programa que recebe:
# •o código do estado de origem da carga de um caminhão, supondo que é um número inteiro de 1 a 5•o peso da carga do caminhão em toneladas
# •o código da carga, supondo que é um número inteiro de 10 e 40Seu programa deve calcular:•o peso da carga do caminhão convertido em quilos
# •o preço da carga do caminhão•valor do imposto que écobrado com base no preço da carga e do estado de origem
# •o valor total transportado pelo caminhão (carga + impostos)Utilize as tabelas abaixo:Obs.: considere que o usuário irá digitar tudo corretamente.
codigo_estado = int(input("Qual codigo do estado: "))
peso_em_toneladas = float(input("Qual o peso da carga em toneladas: "))
codigo_carga = int(input("Qual o código da carga: "))
peso_em_kg = peso_em_toneladas * 1000
if codigo_carga >= 10 and codigo_estado <=20:
    perco_carga = 100*peso_em_kg
elif codigo_carga >= 21 and codigo_estado <=30:
    perco_carga = 250*peso_em_kg
elif codigo_carga >= 31 and codigo_estado <=40:
    perco_carga = 340*peso_em_kg
match codigo_estado:
    case 1:
        imposto = 35/100
    case 2:
        imposto = 35/100
    case 3:
        imposto = 35/100
    case 4:
        imposto = 35/100
    case 5:
        imposto = "Insento"
valor_total = perco_carga+perco_carga*imposto
print(f"O valor total da carga foi de R${valor_total:.2f}")
