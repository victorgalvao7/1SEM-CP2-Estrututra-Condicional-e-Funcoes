#Faça um programa que leia 3 valores que representam os lados de um triângulo A, B e C e ordene-os
#em ordem decrescente, de modo que o lado A representa o maior dos 3 lados. A seguir, determine o
#tipo de triângulo que estes três lados formam, com base nos seguintes casos:
#▪ Se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO;
#▪ Se A² = B² + C² , apresente a mensagem: TRIANGULO RETANGULO;
#▪ Se A² > B² + C² , apresente a mensagem: TRIANGULO OBTUSANGULO;
#▪ Se A² < B² + C² , apresente a mensagem: TRIANGULO ACUTANGULO;
#▪ Se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO;
#▪ Se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES;
l1 = int(input("Digite o primeiro lado: "))
l2 = int(input("Digite o segundo lado: "))
l3 = int(input("Digite o terceiro lado: "))
lados = [l1,l2,l3]
ordenado = sorted(lados)
if ordenado[1] >= (ordenado[2]+ordenado[3]):
    print("NÃO FORMA TRIANGULO")
elif ordenado[3] ** 2 == (ordenado[1]**2 + ordenado[2]**2):
    print("TRIANGULO RETANGULO")
elif ordenado[3] ** 2 > (ordenado[2]**2 + ordenado[1]**2):
    print("TRIANGULO OBTUSANGULO")
elif ordenado[3] ** 2 < (ordenado[2]**2 + ordenado[1]**2):
    print("TRIANGULO ACUTANGULO")
elif ordenado[3] == ordenado [2] and ordenado[3] == ordenado[1]:
    print("TRIANGULO EQUILATERO")
elif ordenado[3] == ordenado [2] or ordenado[3] == ordenado[1] or ordenado[2] == ordenado[1]:
    print("TRIANGULO ISOSCELES")