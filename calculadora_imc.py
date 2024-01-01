"""
Cálculadora IMC
Autor: Vando Rocha
Descrição: Trata-se de um programa que recebe do usuário o peso e altura e cálcula o índice de massa corporal
"""
#Receber valores
peso = float(input("Digite seu peso: ").replace(",", "."))
altura = float(input("Digite sua altura: ").replace(",", "."))



imc = peso/(altura**2)

print("IMC = ", round(imc,2))

if imc <= 16.99:
    print("Você está muito abaixo do peso.")
    
elif imc > 16.99 and imc < 18.49:
    print("Você está abaixo do peso.")
    
elif imc > 18.49 and imc <= 24.99:
    print("Peso normal.")
    
elif imc > 24.99 and imc <= 29.99:
    print("Você está acima do peso.")
    
elif imc > 29.99 and imc <= 34.99:
    print("Obesidade grau I.")

elif imc > 34.99 and imc <= 39.99:
    print("Obesidade grau II.")

else:
    print("Obesidade grau III.")
