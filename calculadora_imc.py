"""
Cálculadora IMC
Autor: Vando Rocha
Descrição: Trata-se de um programa que recebe do usuário o peso e altura e cálcula o índice de massa corporal
"""
#Receber valores
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))


imc = peso/(altura**2)

print(imc)
