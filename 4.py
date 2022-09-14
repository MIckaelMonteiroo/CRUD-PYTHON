#Nome: MICKAEL MONTEIRO DA ROSA
#RU :   4233306

dado = {'id':'','nome':'','fabricante':'','valor':''}
lista_items = []

def cadastrarProduto():
    id = 0
    while True:
        nome = input('Nome do Produto: ')
        fabricante = input('Fabricante do Produto: ')
        valor = input('valor do Produto: ')

        id +=1
        dado ['id'] = str(id)
        dado['nome'] = nome
        dado['fabricante'] = fabricante
        dado['valor'] = valor
        lista_items.append(dado.copy())

        escolha = input('deseja cadastrar mais? [S/N] ')
        if(escolha.upper() != 'S'):
            break
      

def Consulta_produto():
    while True:
        print('(1) - Consultar Todos')
        print('(2) - Consultar por codigo')
        print('(3) - Consultar por Fabricante')
        print('(4) - Voltar')
        escolha = int(input('Escolha uma Opção: '))
        if(escolha == 1):
            for item in lista_items:   
                print('ID - ',item['id'])
                print('Nome - ',item['nome'])
                print('Fabricante - ',item['fabricante'])
                print('Valor - ',item['valor'])
                print('\n')

        if (escolha == 2):        
            a = int(input('digite o codigo do produto : '))
            for item in lista_items:   
                if(item['id'] == str(a)):
                    print('Nome - ',item['nome'])
                    print('Fabricante - ',item['fabricante'])
                    print('Valor - ',item['valor'])
                    print('\n')
                    break
        if(escolha == 3):
            a = input('digite o nome do Fabricante : ')

            item_encontrado = False

            for item in lista_items:  
                if(item['fabricante'] == a): 
                    print('ID - ',item['id'])
                    print('Nome - ',item['nome'])
                    print('Fabricante - ',item['fabricante'])
                    print('Valor - ',item['valor'])
                    item_encontrado = True 
                    

            if(not item_encontrado ):
                print('Fabricante não encontrado!')        
                
        if(escolha == 4):
            break            
                   
def Remover_produto():
    a = int(input('digite o ID para remover o produto : '))
    for item in lista_items:   
        if(int(item['id']) == a):
            lista_items.remove(item)

            break

def Menu():
    while True:
        print('(1) - Cadastrar Produto')
        print('(2) - consultar produto')
        print('(3) - Remover Produto')
        print('(4) - Sair')
        escolha = int(input('Faça uma escolha: '))
        if(escolha == 1):
            cadastrarProduto()
        if(escolha == 2):
            Consulta_produto()
        if(escolha == 3):
            Remover_produto()        
            
        if(escolha == 4):
            print('Saindo do sistema!')
            break  
Menu()



             

