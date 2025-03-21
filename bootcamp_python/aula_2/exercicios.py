# #### Inteiros (`int`)

## 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
#num1 = int(input("Digite o primeiro numero inteiro: "))
#num2 = int(input("Digite o segundo numero inteiro: "))
#resultado_soma = num1 + num2
#print("A soma é:", resultado_soma)

## 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
#num = int(input("Digite um numero:"))
#resultado_resto = num % 5
#print(" O resultado da divisao por 5 é:", resultado_resto)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
#num1 = int(input("Digite o primeiro numero inteiro: "))
#num2 = int(input("Digite o segundo numero inteiro: "))
#resultado_multiplicacao = num1 * num2
#print("O resultado da multiplicação é:", resultado_multiplicacao)

## 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
#num1 = int(input("Digite o primeiro numero inteiro: "))
#num2 = int(input("Digite o segundo numero inteiro: "))
#resultado_divisao_inteira = num1 / num2
#print("o resultado da divisão inteira é:", resultado_divisao_inteira)


# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
#num = int(input("Digite um numero: "))
#resultado_quadrado = num ** 2
#print("O quadrado do numero é:", resultado_quadrado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
#num1 = float(input("Digite o primeiro numero flutuante: "))
#num2 = float(input("Digite o segundo numero flutuante: "))
#resultado_soma = num1 + num2
#print("A soma é:", resultado_soma)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário"
#num1 = float(input("Digite o primeiro numero flutuante:"))
#num2 = float(input("Digite o segundo numero flutuante: "))
#media = (num1 + num2) / 2
#print(f"A media é: {media:.2f}")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário.
#base = float(input("Digite o numero da base: "))
#expoente =  float(input("Digiteo o numero do expoente: "))
#potencia = base ** expoente
#print(f"O resultado da potencia é: {potencia:.2f}")

## 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
#Celsius =  float(input("Digite a temperatura em Celsius: "))
#Fahrenheit = (Celsius * 9/5) + 32
#print(f"{Celsius}ºC é igual a {Fahrenheit}ºF")


# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
#import math

#raio_do_circulo = float(input("Digite o raio do circulo: "))
#area_do_circulo = math.pi *  raio_do_circulo ** 2
#print(f"A área do círculo é {area_do_circulo:.2f}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
#texto = input("Digite um texto: ")
#texto_maiusculas = texto.upper()
#print("Texto em maiúsculas:", texto_maiusculas)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
#nome_completo = input("Digite o nome completo: ")
#nome_minusculas = nome_completo.lower()
#print("Nome em minúsculas:", nome_minusculas)

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
#frase = input("Digite uma frase: ")
#frase_sem_espacos = frase.strip()
#print("Frase sem espaços em brancos:", frase_sem_espacos)

## 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
#data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
#lista_de_dia_mes_ano = data_do_usuario.split("/")
#print(f"O dia é: {lista_de_dia_mes_ano[0]}")
#print(f"O mês é: {lista_de_dia_mes_ano[1]}")
#print(f"O ano é: {lista_de_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
#parte1 = input("Digite a primeira parte do texto: ")
#parte2 = input("Digite a segunda parte do texto: ")
#texto_concatenado =  parte1 + parte2
#print("Texto concatenado:", texto_concatenado)


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
#valor1 = input("Digite true ou false para a primeira expressão: ").strip().lower() == "true"
#valor2 = input("Digite true ou false para a segunda expressão: ").strip().lower() == "true"   
#resultado_and = valor1 and valor2
#print("Resultando do AND logico:", resultado_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
#valor1 = input("Digite True ou False para a primeira expressão: ").strip().lower() == "true"
#valor2 = input("Digite True ou False para a segunda expressão: ").strip().lower() == "true"
#resultado_or =  valor1 or valor2
#print("Resultado do OR lógico:", resultado_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
#valor = input("Digite True ou False: ").strip().lower() == "true" 
#valor_invertido = not valor
#print("Valor invertido:", valor_invertido)



## 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
#num1 = int(input("Digite o primeiro numero: "))
#num2 = int(input("Digite o segundo numero: "))

#if num1 == num2:
    #print("Os numeros são iguais.")
#else:
    #print("Os numeros são diferentes.")

## 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
#num1 = int(input("Digite o primeiro numero: "))
#num2 = int(input("Digite o segundo numero: "))
#resultado_diferenca = (num1 != num2)
#print("Resultado da diferença:", resultado_diferenca)

# #### try-except e if

# 21: Conversor de Temperatura
try:
    fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}ºF é igual a {celsius:.2f}ºC")

    if celsius >0:
        print("A temperatura é positiva.")
    elif celsius ==0:
        print("A temperatura é zero.")
    else:
        print("A temperatura é negativa. ")


except ValueError:
    print("Erro: Digite um número válido.")

# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação