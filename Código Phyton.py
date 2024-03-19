#Seleciona números pares num conjunto numérico 

numeros = [1,2,3,4,5,6,7,8,9,10]
pares = []
for item in numeros:
    if(item%2 == 0):
        pares.append(item)
print(pares)


#Tabuada (Multiplicação) de 0 a 10

for i in range(0,10):
    print("\nTabuada (Multiplicação) por ", i)
    for j in range(0,10):
        print(i, "x", j, " = ", i*j)


#Calcula situação de aluno

nota1 = 6
nota2 = 7

media = (nota1 + nota2)/2 
if(media > 6):
    print("Aprovado")
else:
    if(media == 6):
        print("Recuperação")
    else:
        print("Reprovado")
