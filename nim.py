#jogo NIM - desafio 
def computador_escolhe_jogada (n,m):
  if n%(m+1)==0 or n%(m+1)>m:
    print("O computador tirou", m, "peças.")
    return m
  else:
    print("O computador tirou", n%(m+1), "peças.")
    return n%(m+1)

def usuario_escolhe_jogada (n,m):
  jogadavalida = False
  while not jogadavalida:
    i= int(input("Quantas peças você vai tirar?"))
    if i>0 and i<=m:
      jogadavalida = True 
    else:
      print("Oops! Jogada inválida! Tente de novo.")
  print("Voce tirou", i, "peças.")
  return i

def partida ():
  n = int(input("Quantas peças?"))
  m = int(input('Limite de peças por jogada?'))
  if n%(m+1)==0:
    print("Você começa!")
    while n>0:
     n = n-usuario_escolhe_jogada(n,m)
     if n==0:
       print("Você ganhou!")
     else:
        print("Agora restam", n, "peças no tabuleiro")
     n = n-computador_escolhe_jogada(n,m)
     if n==0:
       print("O computador ganhou!")
     else:
        print("Agora restam", n, "peças no tabuleiro")

  else:
    print("Computador começa!")
    while n>0:
      n= n-computador_escolhe_jogada(n,m)
      if n==0:
        print("O computador ganhou!")
      else:
        print("Agora restam", n, "peças no tabuleiro")
        n = n-usuario_escolhe_jogada(n,m)
        if n==0:
          print("Você ganhou!")
        else:
          print("Agora restam", n, "peças no tabuleiro")
    
def campeonato():
   print("**** Rodada 1 ****")
   partida()
   print("**** Rodada 2 ****")
   partida()
   print("**** Rodada 3 ****")
   partida()
   print("**** Final do campeonato! ****")
   print('Placar: Você 0 X 3 Computador')

def main():
  print("Bem-vindo ao jogo do NIM! Escolha:")
  escolha = int(input("1 - para jogar uma partida isolada 2 - para jogar um campeonato"))
  if escolha == 1:
    partida()
  else:
    if escolha == 2:
      campeonato()

if __name__ == '__main__': 
  main()