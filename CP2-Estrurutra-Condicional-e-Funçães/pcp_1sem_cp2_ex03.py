'''03. (2,0 pontos)
Uma instituição de ensino avalia seus alunos ao longo do semestre com base em
diferentes atividades.

Requisitos:
1. O programa deve solicitar:
- Nota do Checkpoint 1 (cp1)
- Nota do Checkpoint 2 (cp2)
- Nota do Checkpoint 3 (cp3)
- Nota da Sprint 1 (sp1)
- Nota da Sprint 2 (sp2)
- Nota da Global Solution (gs)

2. O programa deve solicitar:
- Todas as notas variam de 0 a 10 e podem ser decimais
- O sistema deve identificar a menor nota entre os três checkpoints
- A menor nota deve ser desconsiderada no cálculo

3. A composição da média segue os seguintes pesos:
- 40% → média dos 2 maiores Checkpoints + 2 Sprints
- 60% → nota da Global Solution
- 40% → média do 1º semestre

4. Cálculo da média:
A média do semestre deve ser calculada utilizando:
- As duas maiores notas dos checkpoints
- As duas notas das sprints
- A nota da Global Solution
FÓRMULA:
media = ((cp1+cp2-cp3-menor+sp1+sp2)/4)*0,4 + gs*0,6
MÉDIA COM PESO:
mediaPeso = media*0,4

5. O sistema deve:
o Mostrar:
- Média do semestre (sem peso)
- Média do semestre com peso

6. Regras de implementação:
- Utilizar estruturas condicionais
- Não utilizar funções prontas como min()
- Trabalhar com valores decimais
- Implementar manualmente a lógica para encontrar a menor nota

7. Dica:
- Primeiro encontre a menor nota entre os checkpoints
- Depois aplique a fórmula removendo essa nota
- Por fim, calcule as médias e exiba com 1 casa decima'''


'''03. (2,0 pontos)
Uma instituição de ensino avalia seus alunos ao longo do semestre com base em
diferentes atividades.

Requisitos:
1. O programa deve solicitar:
- Nota do Checkpoint 1 (cp1)
- Nota do Checkpoint 2 (cp2)
- Nota do Checkpoint 3 (cp3)
- Nota da Sprint 1 (sp1)
- Nota da Sprint 2 (sp2)
- Nota da Global Solution (gs)

2. O programa deve solicitar:
- Todas as notas variam de 0 a 10 e podem ser decimais
- O sistema deve identificar a menor nota entre os três checkpoints
- A menor nota deve ser desconsiderada no cálculo

3. A composição da média segue os seguintes pesos:
- 40% → média dos 2 maiores Checkpoints + 2 Sprints
- 60% → nota da Global Solution
- 40% → média do 1º semestre

4. Cálculo da média:
A média do semestre deve ser calculada utilizando:
- As duas maiores notas dos checkpoints
- As duas notas das sprints
- A nota da Global Solution
FÓRMULA:
media = ((cp1+cp2-cp3-menor+sp1+sp2)/4)*0,4 + gs*0,6
MÉDIA COM PESO:
mediaPeso = media*0,4

5. O sistema deve mostrar:
- Média do semestre (sem peso)
- Média do semestre com peso

6. Regras de implementação:
- Utilizar estruturas condicionais
- Não utilizar funções prontas como min()
- Trabalhar com valores decimais
- Implementar manualmente a lógica para encontrar a menor nota

7. Dica:
- Primeiro encontre a menor nota entre os checkpoints
- Depois aplique a fórmula removendo essa nota
- Por fim, calcule as médias e exiba com 1 casa decimal'''

#Solicitando as notas da CP1, CP2, CP3, Sp1, Sp2, Gs
CP1 = float(input("Digite a nota do Checkpoint 1: "))
CP2 = float(input("Digite a nota do Checkpoint 2: "))
CP3 = float(input("Digite a nota do Checkpoint 3: "))
Sp1 = float(input("Digite a nota da Sprint 1: "))
Sp2 = float(input("Digite a nota da Sprint 2: "))
Gs = float(input("Digite a nota da Global Solution: "))

#Identificando quais notas da CP devem ser consideradas para o cálculo da média
menor_nota = 0
nota_desconsiderada = ""
if (CP1 < CP2) and (CP1 < CP3):
    menor_nota = CP1
    nota_desconsiderada = "CP1"
elif (CP2 < CP1) and (CP2 < CP3):
    menor_nota = CP2
    nota_desconsiderada = "CP2"
else:
    menor_nota = CP3
    nota_desconsiderada = "CP3"

#Cálculo da média do semestre:
#40% → média dos 2 maiores Checkpoints + 2 Sprints
#60% → nota da Global Solution
media = 0
if nota_desconsiderada == "CP1":
    #cálculo da média quando a menor nota for da CP1
    media = round((((CP1 + CP2 + CP3 - menor_nota + Sp1 + Sp2)/4)*0.4 + Gs * 0.6), 1) #round 1 para uma casa após a vírgula
elif nota_desconsiderada == "CP2":
    #cálculo da média quando a menor nota for da CP2
    media = round((((CP1 + CP2 + CP3 - menor_nota + Sp1 + Sp2)/4)*0.4 + Gs * 0.6), 1)
else:
    # cálculo da média quando a menor nota for da CP3
    media = round((((CP1 + CP2 +CP3 - menor_nota + Sp1 + Sp2)/4)*0.4 + Gs * 0.6), 1)

#Cálculo da média do semestre com peso (a média semestral vale 40% da média anual):
media_com_peso = round((media * 0.4), 1) #round 1 para uma casa após a vírgula

#Mostrar a média do semestre (sem peso) e a média do semestre com peso:
print(f"A média semestral do aluno é {media}. E sua média com peso é {media_com_peso}.")