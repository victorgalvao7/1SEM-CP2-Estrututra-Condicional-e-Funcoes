# Faça um programa que recebe:
# •o código do estado de origem da carga de um caminhão, supondo que é um número inteiro de 1 a 5•o peso da carga do caminhão em toneladas
# •o código da carga, supondo que é um número inteiro de 10 e 40Seu programa deve calcular:•o peso da carga do caminhão convertido em quilos
# •o preço da carga do caminhão•valor do imposto que écobrado com base no preço da carga e do estado de origem
# •o valor total transportado pelo caminhão (carga + impostos)Utilize as tabelas abaixo:Obs.: considere que o usuário irá digitar tudo corretamente.
codigo_estado = int(input("Qual codigo do estado: "))
peso = float(input("Qual o pesso da carga em toneladas: "))
if peso >= 10 and peso <= 20:
    perco = peso * 100 * 1000
elif peso >= 21 and peso <= 30:
    perco = peso * 250 * 1000
elif peso >= 31 and peso <= 40:
    perco = peso * 340 * 1000
if codigo_estado == 1:
    peso_com_imposto = perco *135
elif codigo_estado == 2:
    peso_com_imposto = perco *125
elif codigo_estado == 3:
    peso_com_imposto = perco *115
elif codigo_estado == 4:
    peso_com_imposto = perco *105
elif codigo_estado == 5:
    peso_com_imposto = perco 
print(f"O peso da carga do caminhao em quilos é {peso*1000}kg \nOperço da carga foi de {perco:.2f}\n O valor do imposto cobrado foi de {int((peso_com_imposto-peso)/peso*100)}% ou R${peso_com_imposto-perco:.2f} \nO valor total foi de {peso_com_imposto}")