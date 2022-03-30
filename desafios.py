# 000001
print('olá mundo')

#00002
n1 = str(input('digite seu nome: '))

print('boas-vindas' ,n1,'!')

#00003
ruth1= int(input('venha me diga um numero! '))
ruth2= int(input('diga outro pfvr! '))

som = ruth + ruth2

print('sua soma e igual a' ,som,'!')

#00004
a= input('digite algo:  ')
print('tipo primitivo é ',type(a))

print('olá professor!')

#00005
n = int(input('digite um numero! '))
a = n -1
s = n +1

print('analisando o valor {} seu antecessor é {} e o seu sucessor é {}'.format(n, a, s))

#00006
n = int(input('digite um numero pfvr! '))
d= n*2
t=n*3
r=n**(1/2)
print('o dobro de {} vale {}.'.format(n ,d))
print('o tiplo de {} vale {}.'.format(n, t))
print('raiz quadrada de {} vale {}.'.format(n, r))

#00007

a1= float(input('digite a primeira nota do aluno! '))
a2= float(input('digite segunda nota do aluno! '))
media= (a1 + a2)/2
print('a media entre {} é {} é igual a {}...'.format(a1 ,a2 ,media))

#00008
medida =float(input('distancia em metro: '))
cm= medida*100
mm= medida*1000
print('a media em {}m corresponde a {}cm e {}mm.'.format(medida ,cm ,mm))

#000009
#ta indo ...
abc= int(input('digite um numero pra ver sua tabuada: '))
print('{} x {} ={}'.format(abc, 1, abc*1))
print('{} x {} ={}'.format(abc, 2, abc*2))
print('{} x {} ={}'.format(abc, 3, abc*3))
print('{} x {} ={}'.format(abc, 4, abc*4))
print('{} x {} ={}'.format(abc, 5, abc*5))
print('{} x {} ={}'.format(abc, 6, abc*6))
print('{} x {} ={}'.format(abc, 7, abc*7))
print('{} x {} ={}'.format(abc, 8, abc*8))
print('{} x {} ={}'.format(abc, 9, abc*9))
print('{} x {} ={}'.format(abc, 10, abc*10))

print('até logo!')
#00010
real = float(input('quanto dinheiro você tem na carteira R$'))
dolar = real/1.00
print('com {} R$ você pode comprar {} US$'.format(real, dolar))

#00011
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {largura*altura}m².')
print(f'Para pintar essa parede, você precisará de {largura*(altura / 2)}L de tinta.')

print('oizin!')

#00012

p = float(input('Qual o preço do produto? '))
x = int(input('De quanto será o desconto? '))
d = (p/100) * x
v = p-d
print('O produto que custava R${:.2f}, com {}% de desconto vai custar R${:.2f}'.format(p, x, v))

#000013
p = float(input('Qual é seu salario? '))
x = int(input('De quanto será o aumento? '))
a = (p/100) * x
v = p+a
print('O seu salario que era de R${:.2f},agora com aumento de  {}%  vai fica R${:.2f}'.format(p, x, v))

#000014
c=float(input('Informe a temperatura em °C: '))
f=(c*1.8+32)
print('{}°C é equivalente a {}°F'.format(c,f))

#0000015

d = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos quilômetros você rodou com ele? '))
a = d * 60 + km * 0.15
print(f'Você deve R${a:.2f} de aluguel')

#0000016
num = float(input('Digite um valor:'))
print('O valor {} tem sua parte inteira {:.0f}'.format(num, num))
print('obrigadu!')

#000017
from math import sqrt
print('Calculando a Hipotenusa')
co = float(input('Insira o valor do cateto oposto: '))
ca = float(input('Insira o valor do cateto adjacente: '))

hi = (co ** 2) + (ca ** 2)

hi = sqrt(hi)
print('A hipotenusa desse triângulo é:{:.2f}'.format(hi))

#000018

import math
an = float(input('digite o angulo q deseja ? '))
r = math.radians(an)
s = math.sin(r)
c = math.cos(r)
t = math.tan(r)
print('se o angulo for {} \n o seno sera {:.3f} \n o coseno sera{:.3f} \n e a trangente sera {:.3f}'.format(an, s, c, t))
print('valeu !')

#000019

from random import choice
a = str(input("1°aluno Nome: "))
b = str(input("2° aluno Nome: "))
c = str(input("3° aluno Nome: "))
d = str(input("4° aluno Nome: "))
escolhido = (a, b, c, d)
print("A pessoa escolhida foi {}".format(choice(escolhido)))
print('ops vc não ser deu bem hehehe!')

#000020

from random import shuffle
p = input('Digite o nome do 1° aluno: ')
s = input('Digite o nome do 2° aluno: ')
t = input('Digite o nome do 3° aluno: ')
q = input('Digite o nome do 4° aluno: ')
lista = [p, s, t, q]
emb = shuffle(lista)
print('a ordem foi {}'.format(lista))
print('valeu!')
#000021
#não conseguir...


#000022



nome = input('Ingresse seu nome completo : ')
print('Seu nome completo é : {}'.format(nome))
print('Seu nome em maiúsculas : {}'.format(nome.upper()))
print('Seu nome em minúsculas : {}'.format(nome.lower()))
# Forma 1
separado = nome.split() # lo separo
print(separado) # lo muestro separado
print(''.join(separado)) #lo muestro unido (sem espacios)
print('O cumprimento do nome sem espacios é: {}'.format(len(''.join(separado))))
# Forma 2
print('Cumprimento {}'.format(len(nome.replace(' ',''))))

# Quantas letras tem o primeiro nome
print('Quantidade letras o 1er nome é: {}'.format(len(separado[0])))

#000023

n = int(input('Digite um número entre 0 e 9999: '))
n2 = str(int(10000 + n))
print('O número {} possui, {} milhares.'.format(n, n2[1]))
print('O número {} possui, {} centenas. '.format(n, n2[2]))
print('O número {} possui, {} dezenas. '.format(n, n2[3]))
print('O número {} possui, {} unidades.'.format(n, n2[4]))

#000024

nome=str(input("Introduza o nome da cidade: ")).strip()
print("santo" in nome.lower())

#000025

nome=str(input("diga seu nome completo: ")).strip()
print("silva" in nome.lower())
print('valeu!')

#000026

frase = str(input('digite uma frase: ')).strip().lower()
print('a letra a (sem acento) aparece',frase.count('a'),'vezes na frase.')
print('a posição que o a está é',frase.find('a')+1)
print('a letra a apareceu por ultimo na posição',frase.rfind('a')+1)

#00027
nome = str(input('digite seu nome: ')).strip().lower()
print('seu nome (sem acento) aparece',nome.count('nome'),'vezes na frase.')
print('a posição que o nome está é',nome.find('a')+1)
print('seu nome apareceu por ultimo na posição',nome.rfind('nome')+1)


#028
from random import randint
from time import sleep
comp = randint (0, 5)
print('vou pensar em um numero de 0 a 5 adivinhe!')
jogador =int(input('em que numero eu pensei ? '))
print('calma processando...')
sleep(3)
if jogador == comp:
 print('parabens você ganhou !')
else:
 print('vc perdeu hehehe!')

#00029

velo = int(input('Velocidade(Km/h): '))
print(f'MULTADO! Você excedeu o limite de 80Km/h e agora deve pagar uma multa de R${(velo - 80)*7:.2f}!' if velo > 80 else 'Dentro dos limites de velocidade!')
print('Dirija com cuidado!')

#000030

número = int(input('me diga um número qualquer: '))
if número % 2 == 0:
    print(número,'é par.')
else:
    print(número,'é impar.')

#000031

km = float(input('Qual a distância em (Km) você deseja percorrer? '))
if km <= 200:
    print('Sua passagem vai custar {} reais. '.format(km * 0.5))
else:
    print('Sua passagem vai custar {} reais. '.format(km * 0.45))

#000032

import calendar
ano = int(input('Digite o ano: '))
ano6 = calendar.isleap(ano)
if ano6 is True:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')

#00033

primeiro = int(input('Digite o primeiro número: 3'))
segundo = int(input('Digite o segundo número:'))
terceiro = int(input('Digite o terceiro número:'))
numeros = [primeiro, segundo, terceiro]

print('O maior valor digitado foi {}'.format(max(numeros)))
print('O menor valor digitado foi {}'.format(min(numeros)))


#00034

salario = float(input('Informe o salário do funcionário: '))
if salario <=1250:
    print('Seu salário terá um aumento de 15%!!')
    print(f'O valor do seu salario era {salario} e agora será de R${(salario*0.15)+salario:.2f}')
else:
    print('Seu salário terá um aumento de 10%!!')
    print(f'O valor do seu salario era {salario} e agora será de R$ {(salario*0.10)+salario:.2f}')


#000035

a = float(input('Coloque o valor de um lado: '))
b = float(input('Coloque o valor de outro lado: '))
c = float(input('Coloque o valor de outro lado: '))

if abs( b - c) < a <  b + c and abs( a - c ) < b < a + c and abs( a - b ) < c < a + b:
    print('Os lados {}, {} e {} podem formar triângulo.'.format(a,b,c))
else:
    print('Os lados {}, {} e {} não podem formar triângulo.'.format(a,b,c))


#finalmente terminei eeeee ....