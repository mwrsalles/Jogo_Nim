
def computador_escolhe_jogada(n, m):
        pc_play = 1

        while pc_play != m:
                if (n - pc_play)%(m+1) == 0:
                        return pc_play
                else:
                        pc_play += 1

        return pc_play



def usuario_escolhe_jogada(n, m):
        valid_play = False
        while not valid_play:
                print("")
                user_play = int(input("\nQuantas peças você vai tirar? "))

    #Jogada inválida:
                if(user_play < 1 or user_play > m):
                        print("\nOops! Jogada inválida! Tente de novo.")
                        user_play = int(input("\nQuantas peças você vai tirar? "))
                else:
                        valid_play = True
                        
        return user_play
                    


def partida():
        n = int(input("\nQuantas peças você deseja utilizar no jogo? " ))
        m = int(input("\nQual será o limite de peças por jogada? " ))
        pc_turn = False
        
        #Se n e m forem inválidos
        while m > n or m == 0 or n == 0:
                print("\nValores inválidos.")
                n = int(input("\nQuantas peças deseja utilizar no jogo? " ))
                m = int(input("\nQual será o limite de peças por jogada? " ))
                
        #Se n e m foram válidos
        
        if n%(m+1) == 0:
                print("")
                print("\nVocê começa!")
        else:
                print("")
                print("\nO computador começa!")
                pc_turn = True
                
        while n > 0:
                if pc_turn:
                        pc_play = computador_escolhe_jogada(n, m)
                        n = n - pc_play
                        print("\nO computador retirou", pc_play, "peças.")
                        
                        pc_turn = False
                else:
                        user_play = usuario_escolhe_jogada(n, m)
                        n = n - user_play
                        print("\nVocê retirou", user_play, "peças.")
                        
                        pc_turn = True
                        
                if n == 1:
                        print("\nAgora resta apenas uma peça no tabuleiro.")
                else:
                        if n != 0:
                                print("\nAgora restam", n, "peças no tabuleiro.")
                                
        print("\nFim do jogo! O computador ganhou!")      


                               
def campeonato():
    print("")
    print("**** Rodada 1 ****")
    print("")
    partida()
    print("")
    print("**** Rodada 2 ****")
    print("")
    partida()
    print("")
    print("**** Rodada 3 ****")
    print("")
    partida()
    print("\nFim do campeonato!")
    print("\nPlacar: Você 0 X 3 Computador")
#anunciar o vencedor do campeonato 


#Menu de início    
print("Bem-vindo ao jogo do NIM! Escolha:\n")
print("1 - para jogar uma partida isolada\n")
print("2 - para jogar um campeonato \n")
tipo = input("Sua escolha: ")

#Tipo do jogo
if tipo == "1":
    print("\nVocê escolheu uma partida isolada!") 
    partida()
    
if tipo == "2":
    print("\nVocê escolheu um campeonato!")
    campeonato()

else:
    while tipo != "1" and tipo != "2":
        print("")
        print("Escolha 1 ou 2.")
        print("1 - para jogar uma partida isolada")
        print("2 - para jogar um campeonato ")
        tipo = input("Sua escolha: ")
        if tipo == "1":
            print("\nVocê escolheu uma partida!")
            partida()
            
        if tipo == "2":
            print("\nVocê escolheu um campeonato!")
            campeonato()
