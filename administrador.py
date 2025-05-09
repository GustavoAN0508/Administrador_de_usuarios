import os

def limparConsole() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

name, age, email= [], [], []

lista = {
        "nome" : name,
        "idade": age,
        "email": email
        }

def cadastrarUsuario() -> None: 
    #o uso de -> de versões recentes, permite definir o tipo do retorno
    global name, age, email, lista #todas as variáveis estão sendo devidamente atribuidas como globais em prol da usabilidade
    
    while True:
        escolha = int(input("Deseja adicionar usuário?\n1. Sim\n2. Não\n"))

        if escolha == 1:
            nome = input("Nome: ")
            idade = int(input("Idade: "))
            caixaPostal = input("Email: ")

            name.append(nome)
            age.append(idade)
            email.append(caixaPostal)

            print("\nUsuário adicionado com sucesso!\n")
            input("Aperte Enter para continuar...")
            limparConsole()
        else:
            print("\nProcesso de cadastro encerrado.\n")
            input("Aperte Enter para continuar...")
            limparConsole()
            break

def listagensDeUsuario ()-> None:

    global name, age, email, lista
    coluna1, coluna2, coluna3  = [], [], []

    for campos, itens in lista.items(): 
    #assim como forEach em PHP serve para dicionários, a função for com o adendo de .itens() no final auxilia com campos e keys
        if (campos == "nome"):
            for nomes in name:
                coluna1.append(nomes)

        if (campos == "idade"):
            for idades in age:
                coluna2.append(idades)

        if (campos == "email"):
            for emails in email:
                coluna3.append(emails)

    for i in range(len(coluna1)): #ele usou o tamanho de uma coluna somente
        print(f"{coluna1[i]:<15} | {coluna2[i]:<10} | {coluna3[i]:<30}") #os dois pontos servem para formatação de largura entre textos à direita
        

def buscaDeUsuario (nomeacao: str) -> None:
    global name, age, email, lista

    qtd = len(name)

    for elemento in range(0, qtd, 1): 
        if(nomeacao == name[elemento]):
            print(f"Usuário encontrado!!! \nsegue informações abaixo:\n\n")
            print(f"{name[elemento]}   |   {age[elemento]}   |   {email[elemento]}") 
            #aqui é onde o conceito anterior é utilizado, porque se fosse fazer de outra forma, poderia dar problemas
            print(f"Busca terminada!")
            
            input("Aperte Enter para continuar...")
            limparConsole()
            break
                


while True:
    print(f"Olá, bem-vindo ao console. O que deseja fazer? (favor preencher tudo numéricamente)")
    try:
        console = int(input("1. Cadastro de usuário\n2. Verificar listagem\n3. Realizar busca de usuário\n\n(Outro número para sair):\n\n "))
    except ValueError:
        print("Entrada inválida. Digite um número.")#o uso de try e except é necessário para caso haja erro no console, apenas dar essa mensagem 
        pausar()
        continue

    if(console == 1):
        print(f"insira nome, idade e email respectivamente (favor colocar somente numeros em idade)")
        cadastrarUsuario()
        input("Aperte Enter para continuar...")
        limparConsole()


    elif(console == 2):
        print(f"Aqui está a listagem de usuários!")
        listagensDeUsuario()
        input("Aperte Enter para continuar...")
        limparConsole()

    elif(console == 3):
        nomeacao = input(f"Insira o nome do usuario que deseja buscar aqui:\n")
        buscaDeUsuario(nomeacao)
        input("Aperte Enter para continuar...")
        limparConsole()
    
    else:
        print(f"saindo...")
        limparConsole()
        break
