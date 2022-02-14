import sys

escolha=[]
cardapio = {"coxinha": 3, "pastel": 6,}
escolha.append(cardapio)

escolha2=[]
cardapio2 = {"coca": 4, "suco": 5}
escolha2.append(cardapio2)

itens=[] ## produtos
quantidade=[] ## quantidade dos itens
multi=[] ##valor do produto vezes a quantidade

print('')
print("-"*24,"LANCHONETE","-"*24)
print('')

while True:
    kkkk = str(input("     Voce quer comprar um lanche ou uma bebida?: "))
    if kkkk == "lanche":
        print('')
        print("*"*20,"CARDAPIO DE LANCHES","*"*20)
        print('')
        for cardapio in escolha:
            for a, b in cardapio.items():
                print("                        ",a + ": "+str(b))
                print(61*"-")
        try:
            while True:
                pedido = input("qual o lanche?: ")
                if pedido in cardapio:
                    itens.append(pedido)
                    print('-'*30)
                    break
                else:
                    ("tente ")

            while True:

                quan = int(input("quantidade?: "))
                if quan >0:
                    quantidade.append(quan)
                    break
    
                else:
                    ("Não é um valor valido, tente novamente:")        
            print('-'*30)

            pagar=cardapio[pedido] * quan
            multi.append(pagar)
            final=sum(multi)

            s_n=str(input('Deseja comprar algo mais?: [s|n]'))
            print(' ')
            if s_n == 'n':
                break
        except:
            ("")

    elif kkkk == "bebida":
        print('')
        print("*"*20,"CARDAPIO DE BEBIDAS","*"*20)
        print('')
        for cardapio2 in escolha2:
            for a, b in cardapio2.items():
                print("                        ",a + ": "+str(b))
                print(61*"-")
        try:
            while True:
                pedido = input("qual a bebida?: ")
                if pedido in cardapio2:
                    itens.append(pedido)
                    print('-'*30)
                    break
                else:
                    ("tente ")

            while True:

                quan = int(input("quantidade?: "))
                if quan >0:
                    quantidade.append(quan)
                    break
    
                else:
                    ("Não é um valor valido, tente novamente:")        
            print('-'*30)

            pagar=cardapio2[pedido] * quan
            multi.append(pagar)
            final=sum(multi)

            s_n=str(input('Deseja comprar algo mais?: [s|n]'))
            print(' ')
            if s_n == 'n':
                break
        except:
            ("")

print(' ')
print("*"*26,"Conta","*"*26)
print('-'*59)
print("Produto:          Quantidade:          Total de cada item:")
for x in range(len(itens)):
    print(itens[x],"            ",quantidade[x],"                  ", multi[x])

print('')
print('-'*59)
print(" "*18,"Valor total da conta: ")
print(" "*26,"R$",sum(multi))
print('-'*59)

 