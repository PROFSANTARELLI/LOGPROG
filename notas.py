#notas
nota1 = float(input("Digite a nota 1: ")) #variável que recebe a primeira nota
nota2 = float(input("Digite a nota 2: ")) #variável que recebe a segunda nota
media = (nota1 + nota2)/2 #Calculo da média das duas notas

print(f"Média: {media:.2}") #Apresentação da nota média

if media >= 6:
    print("Você está aprovado")

else:
    print("Você está reprovado")