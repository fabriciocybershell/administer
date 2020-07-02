#! bin/bash/python3
# -*- coding: UTF-8 -*-
'''
AUTOR:Fabrício
OBJETIVO: gerenciar o seu dinheiro para manter um equilíbrio
entre o que você pode e não pode gastar, usando uma metodologia 
que visa ajudalo a não ficar sem dinheiro como que você realmente 
precisa, uma ferramenta que sabe dar prioridade para o que 
realmente é escencial para sua vivência equilibrada.
STATUS: em desenvolvimento ...
DEPENDÊNCIAS:
python3, numpy
'''
import os
import sys
import time
import matplotlib.pyplot as plt
import numpy as np

os.system('clear')

def menu():
  print (30*"-","MENU",30*"-")
  print("[1] para adicionar salario adquirido")
  print("[2] para ver gráfico para gastos")
  print("[3] para subtrair valores de tópico")
  print("[4] para ver a percentagem de cada tópico")
  print("[5] para sair")
  print("[6] resetar banco de dados")
  print(60*"-")

def logo():
  print('  %%%%  %%%%%   %%   %%  %%%%%%  %%  %%  %%%%%%   %%%%   %%%%%%  %%%%%%  %%%%%  ')
  print(' %%  %% %%  %%  %%% %%%    %%    %%% %%    %%    %%        %%    %%      %%  %% ')
  print(' %%%%%% %%  %%  %% % %%    %%    %% %%%    %%     %%%%     %%    %%%%    %%%%%  ')
  print(' %%  %% %%  %%  %%   %%    %%    %%  %%    %%        %%    %%    %%      %%  %% ')
  print(' %%  %% %%%%%   %%   %%  %%%%%%  %%  %%  %%%%%%   %%%%     %%    %%%%%%  %%  %% ')
  print('.................................................................................')

arquivo = open('imp.gener','a')
arquivo.write(str(0))
arquivo.close()
arquivo = open('apn.gener','a')
arquivo.write(str(0))
arquivo.close()
arquivo = open('dis.gener','a')
arquivo.write(str(0))
arquivo.close()

def recalcsaldo():
  arquivo = open('imp.gener','r')
  imp=arquivo.read()
  arquivo.close()

  arquivo = open('apn.gener','r')
  apn=arquivo.read()
  arquivo.close()

  arquivo = open('dis.gener','r')
  dis=arquivo.read()
  arquivo.close()

  return float(imp)+float(apn)+float(dis)

laço=True

while (laço):

  saldo=recalcsaldo()
  os.system('clear')
  logo()
  print('seu saldo atual:',"%.2f"%saldo,"R$")
  menu()

  opção=int(input('digite a opção desejada:'))

  if opção == 1 :
    adicional=input("digite aqui o valor adicional do seu saldo:")
    adicional2=input("agora, digite novamente para termos serteza antes de adicionar:")

    if adicional == adicional2:

      arquivo = open('imp.gener','r')
      imp=arquivo.read()
      arquivo.close()
      arquivo = open('apn.gener','r')
      apn=arquivo.read()
      arquivo.close()
      arquivo = open('dis.gener','r')
      dis=arquivo.read()
      arquivo.close()

      restrair1=float(imp)
      impres=restrair1+(float(adicional)*60)/100

      restrair2=float(apn)
      apenes=restrair2+(float(adicional)*30)/100

      restrair3=float(dis)
      dispen=restrair3+(float(adicional)*10)/100

      arquivo=open("imp.gener","w")
      arquivo.write(str(impres))
      arquivo.close()
      arquivo=open("apn.gener","w")
      arquivo.write(str(apenes))
      arquivo.close()
      arquivo=open("dis.gener","w")
      arquivo.write(str(dispen))
      arquivo.close()
      pass

      print("valor adicionado!")
      time.sleep(1)

    else :
      print("ERRO!. DIGITE O VALOR CORRETAMENTE")
      time.sleep(1)

  if opção == 2:

    arquivo = open('imp.gener','r')
    imp=arquivo.read()
    arquivo.close()
    arquivo = open('apn.gener','r')
    apn=arquivo.read()
    arquivo.close()
    arquivo = open('dis.gener','r')
    dis=arquivo.read()
    arquivo.close()

    
    luzagua=float(imp)*10/100
    comida=float(imp)*15/100
    aluguel=float(imp)*35/100

    apenas=float(apn)*3/100

    savel=float(dis)*10/100

    os.system('clear')
    print(60*"=")
    print("saldo atual:","%.2f"%saldo,"R$")
    print(60*"=")
    print("VALORES TOTAIS DOS TÓPICOS:")
    print(60*"*")
    print("IMPRESCINDÍVEIS TOTAl:",imp,"R$")
    print("SUBVALOR:")
    print("luz:","%.2f"%luzagua,"R$")
    print("água:","%.2f"%luzagua,"R$")
    print("comida:","%.2f"%comida,"R$")
    print("aluguel:","%.2f"%aluguel,"R$")
    print(60*"_")
    print("APENAS NECESSÁRIO TOTAl:",apn,"R$")
    print("SUBVALOR:")
    print("internet:","%.2f"%apenas,"R$")
    print("livros:","%.2f"%apenas,"R$")
    print("cursos:","%.2f"%apenas,"R$")
    print("laser:","%.2f"%apenas,"R$")
    print("investir:","%.2f"%apenas,"R$")
    print("reformas:","%.2f"%apenas,"R$")
    print("móveis:","%.2f"%apenas,"R$")
    print("férias:","%.2f"%apenas,"R$")
    print("celular:","%.2f"%apenas,"R$")
    print("compútador:","%.2f"%apenas,"R$")
    print(60*"_")
    print("DISPENSÁVEL TOTAl:",dis,"R$")
    print("SUBVALOR:")
    print("diversão 'sair no dia a dia':","%.2f"%savel,"R$")
    print("viagens:","%.2f"%savel,"R$")
    print("comprar besteiras:","%.2f"%savel,"R$")
    print(60*"_")
    print("\n")
    decid=str(input('você gostaria de um gráfico dos valores [s/n]?'))
    if decid == "s":
      print("plotando gráfico ...")


      plt.style.use('dark_background')
      x=[3,2,1]
      y=[dis,apn,imp]
      x1=[3,2,1]
      y1=[dis,apn,imp]
      x3=[3,2,1]
      y3=[0,0,imp]
      #plt.plot(0,4,0,saldo/(saldo*99/100))
      plt.title('equilibribrio de valores, quanto maior a  dobra, maior o desequilíbreo')
      plt.xlabel('imprescindivel =1   necessário=2   dispensável=3')
      plt.ylabel('valores em R$')
      plt.bar(x,y, label = 'valores', color='white')
      plt.plot(x1,y1, label = 'equilibrio', color='red')
      if float(imp) <= 200:
        plt.title('ALERTA! FALTA DE DINHEIRO PARA COISAS IMPRESCINDÍVEIS',color='red')
      plt.show()



  if opção == 3:
    os.system('clear')
    logo()
    print('selecione um tópico para subtrair:')
    print(60*"_")
    arquivo = open('imp.gener','r')
    imp=arquivo.read()
    arquivo.close()
    print("[1] IMPRESCINDÍVEIS:","%.2f"%float(imp),"R$")
    print(60*"_")
    arquivo = open('apn.gener','r')
    apn=arquivo.read()
    arquivo.close()
    print("[2] APENAS NECESSÁRIO:","%.2f"%float(apn),"R$")
    print(60*"_")
    arquivo = open('dis.gener','r')
    dis=arquivo.read()
    arquivo.close()
    print("[3] DISPENSÁVEL:","%.2f"%float(dis),"R$")
    print(60*"_")
    print("[4] sair")
    print("\n")

    op=int(input("digite a opção desejada:"))

    if op == 1:
      subop=int(input("digite o valor a retirar:"))
      registrar=float(imp)-float(subop)
      arquivo=open("imp.gener","w")
      arquivo.write(str(registrar))
      arquivo.close()
      print("RETIRADO!")
      time.sleep(1)

    if op == 2:
      subop=int(input("digite o valor a retirar:"))
      registrar=float(apn)-float(subop)
      arquivo=open("apn.gener","w")
      arquivo.write(str(registrar))
      arquivo.close()

      print("RETIRADO!")
      time.sleep(1)

    if op == 3:
      subop=int(input("digite o valor a retirar:"))
      registrar=float(dis)-float(subop)
      arquivo=open("dis.gener","w")
      arquivo.write(str(registrar))
      arquivo.close()

      print("RETIRADO!")
      time.sleep(1)

    if op == 4:
      print("SAINDO ...")
      time.sleep(1)


  if opção == 4:
    os.system('clear')
    print(60*"=")
    print("TÓPICOS:")
    print(60*"=")
    print("IMPRESCINDÍVEIS:60%")
    print(60*"_")
    print("luz:20%")
    print("água:20%")
    print("comida:15%")
    print("aluguel:35%")
    print("outros ...")
    print(60*"_")
    print("APENAS NECESSÁRIO:30%")
    print(60*"_")
    print("internet:3%")
    print("livros:3%")
    print("cursos:3%")
    print("laser:3%")
    print("investir:3%")
    print("reformas:3%")
    print("móveis:3%")
    print("férias:3%")
    print("celular:3%")
    print("compútador:3%")
    print(60*"_")
    print("DISPENSÁVEL:10%")
    print(60*"_")
    print("diversão 'sair no dia a dia':10%")
    print("viagens:10%")
    print("comprar besteiras:10%")
    print("\n")
    vari=input('dê ENTER para sair!')

  if opção == 5:
    laço=False

  if opção == 6:
    decid=str(input("deseja mesmo resetar o banco de dados [s/n] ?"))
    if decid == "s":
      print("resetando ...")
      arquivo=open("imp.gener","w")
      arquivo.write(str(0))
      arquivo.close()
      arquivo=open("apn.gener","w")
      arquivo.write(str(0))
      arquivo.close()
      arquivo=open("dis.gener","w")
      arquivo.write(str(0))
      arquivo.close()
      time.sleep(1)

    else:
      print("bye")
      time.sleep(1)

