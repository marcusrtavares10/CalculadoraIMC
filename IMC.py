"""
Projeto IMC básico
"""
print('=-'*22)
print('Calculadora IMC - Índice de Massa Corporal')
print('=-'*22)
print()
peso = float(input('Digite seu peso atual em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / (altura * altura)

print('Seu IMC é de {:.2f}'.format(imc))

if imc < 18.5:
    print('Abaixo do peso.')
elif imc >= 18.5 and imc <= 24.9:
    print('Peso ideal.')
elif imc >= 25 and imc <= 29.9:
    print('Excesso de peso.')
elif imc >= 30 and imc <= 34.9:
    print('Obesidade classe I')
elif imc >= 35 and imc <= 39.9:
    print('Obesidade classe II')
else:
    print('Obesidade classe III - Obesidade Mórbida.')
