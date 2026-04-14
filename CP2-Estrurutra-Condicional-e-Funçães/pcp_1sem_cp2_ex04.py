nome = input("Qual o seu nome? ")
while True:
    cargo = int(input("Qual opção corresponde ao seu cargo? \n1) Gerente \n2) Analista \n3) Assistente \n4) Estagiário \nDigite o número: "))
    if cargo > 4 or cargo < 1:
        print("Essa opção não está disponível!")
    else:
        break
salario_base = float(input("Qual o valor do seu salário base: "))
horas = int(input("Quantas horas extras foram trabalhadas? "))
faltas = int(input("Qual o total de faltas durante o mês? "))
recebeu_bonus = input("Recebeu bônus por desempenho? Sim/Não: ")

def calcular_horas_extras(salario_base, horas):
    return salario_base* 0.015 * horas

def calcular_descontos_faltas(salario_base, faltas):
    return salario_base * 0.02 * faltas

def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus.lower() != 'Sim':
        return 0
    if cargo == 1:
        return 1000
    elif cargo == 2:
        return 500
    elif cargo == 3:
        return 300
    elif cargo == 4:
        return 100
    else:
        return 0

print(f"Esses é o cálculo do seu salário final, {nome}: ")
print(f"Salário bruto: {salario_base}")
print(f"Total dos acréscimos (horas extras + bônus): {calcular_horas_extras(salario_base, horas)+calcular_bonus(cargo, recebeu_bonus)}")
print(f"Total dos descontos: {calcular_descontos_faltas(salario_base, faltas)}")
print(f"O seu salário a receber é de: {salario_base + calcular_horas_extras(salario_base, horas)+calcular_bonus(cargo, recebeu_bonus) - calcular_descontos_faltas(salario_base, faltas)}")
print(f"Obrigado pelos serviços prestados, {nome}!")


