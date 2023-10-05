agenda = {
    "Gabriel": {"phone": 987960801}
}

while True:
    print("Escolha uma opção:")
    print("1. Exibir contatos")
    print("2. Adicionar novo contato")
    print("3. Listar contatos")
    print("4. Pesquisar contato")
    print("5. Sair")

    escolha = input("Opção: ")

    if escolha == "1":
        # Exibir contatos
        print(agenda)
    
    elif escolha == "2":
        # Adicionar novo contato
        name = input("Insira o nome do novo contato: ")
        number = input("Insira o número do novo contato: ")
        agenda[name] = {"phone": number}
    
    elif escolha == "3":
        # Listar contatos
        print("Contatos:")
        for key in agenda:
            print(key)

    elif escolha == "4":
        # Pesquisar contato
        name = input("Insira o contato que deseja pesquisar: ")
        if name in agenda:
            print(agenda[name])
        else:
            print("Contato não encontrado")

    elif escolha == "5":
        # Sair
        print("Programa encerrado.")
        break

    else: 
        print("Escolha inválida")
