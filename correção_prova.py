n = input("Digite o seu nome: ")

an = int( input("Digite o ano de nascimento: ") )

at = 2021

i = at - an

print ( "Olá ", n, ", você tem ", i, " anos" )

"""O sistema de avaliação é composto por 3 notas. A primeira tem peso 2, a segunda tem peso 4 e a terceira tem peso 6. Faça um algoritmo, em Python, que leia 3 notas informadas pelo usuário, calcule a média final do aluno e informe o valor final."""

n1 = input ( "Digite a nota 1" )
n2 = input ( "Digite a nota 2" )
n3 = input ( "Digite a nota 3" )

m = (float(n1) * 2 + float(n2) * 4 + float(n3) * 6 ) / ( 2 + 4 + 6 )

print ("A média final é ", m)

"""O custo ao consumidor de um carro novo é a soma do custo de fábrica com a percentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que a percentagem do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo que leia o custo de fábrica de um carro e escreva o custo ao consumidor. """

cf = float( input("Digite o custo de fábrica: ") )

imposto = 45 / 100

p_dist = 28 / 100

cc = cf + (cf * imposto)

print(cc)