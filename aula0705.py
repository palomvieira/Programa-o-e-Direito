# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Nome: Alice - Idade: 25 - Cidade: São Paulo!
def questao1(nome, idade, cidade):
    print("Nome: ", nome, end=" - ")
    print("Idade: ", idade, end=" - ")
    print("Cidade: ", cidade, end="!\n")
    
questao1("Paloma", 20, "Rio de Janeiro")
questao1("Joana", 25, "Tijuca")

def questao2():
    n1 = float(input("Entre com o primeiro número: "))
    n2 = float(input("Entre com o segundo número: "))
    op = input("Entre com a operação (+, -, *, /): ")
    
    if op == '+':
        print(n1 + n2)
    elif op == '-':
        print(n1 - n2)
    elif op == '*':
        print(n1 * n2)
    elif op == '/':
        print(n1 / n2)
    else:
        print('Operador desconhecido')

def questao3():
    texto = input("Entre com os ítens de uma lista de compras, separados por vírgulas: ")
    
    lista = texto.split(',')
    
    contador = 1
    for item in lista:
        print("Item", contador, ":", item)
        contador += 1
        
def questao4():
    texto = input("Entre com a temperatura em Celsius: ")
    celsius = float(texto)
    
    f = (celsius * 9/5) + 32
    print("A temperatura em Fahrenheit é", f)
    
def questao5():
    print("Entre com nomes. Digite sair para terminar.")
    
    nomes = []
    
    while True:
        entrada = input()
        
        if entrada.lower() == 'sair':
            break
        else:
            nomes.append(entrada)
            
    for nome in nomes:
        print(nome)
    
