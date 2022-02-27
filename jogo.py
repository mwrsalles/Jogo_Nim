
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
                user_play = int(input("Quantas peças você vai tirar? "))

    #Jogada inválida:
                if(user_play < 1 or user_play > m):
                        print("Oops! Jogada inválida! Tente de novo.")
                        print("")
                        user_play = int(input("Quantas peças você vai tirar? "))
                else:
                        valid_play = True
                        
        return user_play
                    


def partida():
        n = int(input("Quantas peças? " ))
        m = int(input("Limite de peças por jogada? " ))
        pc_turn = False
        
        #Se n e m forem inválidos
        while m > n or m == 0 or n == 0:
                print("Valores inválidos.")
                n = int(input("Quantas peças? " ))
                m = int(input("Limite de peças por jogada? " ))
                
        #Se n e m foram válidos
        
        if n%(m+1) == 0:
                print("")
                print("Você começa!")
        else:
                print("")
                print("O computador começa!")
                pc_turn = True
                
        while n > 0:
                if pc_turn:
                        pc_play = computador_escolhe_jogada(n, m)
                        n = n - pc_play
                        print("")
                        print("O computador retirou", pc_play, "peças.")
                        
                        pc_turn = False
                else:
                        user_play = usuario_escolhe_jogada(n, m)
                        n = n - user_play
                        print("")
                        print("Você retirou", user_play, "peças.")
                        
                        pc_turn = True
                        
                if n == 1:
                        print("Agora resta apenas uma peça no tabuleiro.")
                        print("")
                else:
                        if n != 0:
                                print("Agora restam", n, "peças no tabuleiro.")
                                print("")
                                
        print("Fim do jogo! O computador ganhou!")      


                               
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
    print("Final do campeonato!")
    print("Placar: Você 0 X 3 Computador")
#anunciar o vencedor do campeonato 


#Menu de início    
print("Bem-vindo ao jogo do NIM! Escolha:")
print("")
print("1 - para jogar uma partida isolada")
tipo = input("2 - para jogar um campeonato ")

#Tipo do jogo
if tipo == "1":
    print("")
    print("Você escolheu uma partida isolada!") 
    partida()
    
if tipo == "2":
    print("")
    print("Você escolheu um campeonato!")
    campeonato()

else:
    while tipo != "1" and tipo != "2":
        print("")
        print("Escolha 1 ou 2.")
        print("1 - para jogar uma partida isolada")
        tipo = input("2 - para jogar um campeonato ")
        if tipo == "1":
            print("")
            print("Você escolheu uma partida!")
            partida()
            
        if tipo == "2":
            print("")
            print("Você escolheu um campeonato!")
            campeonato()
