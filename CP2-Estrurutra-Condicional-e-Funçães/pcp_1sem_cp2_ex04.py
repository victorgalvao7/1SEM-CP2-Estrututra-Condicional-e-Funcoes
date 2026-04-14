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
bonus = input("Recebeu bônus por desempenho? Sim/Não: ")

def calcular_horas_extras(salario_base, horas)

