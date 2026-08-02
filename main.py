contactos = []

while True:

    print("=" * 30)
    print("GESTÃO DE CONTACTOS")
    print("=" * 30)

    print("1 - Adicionar contacto")
    print("2 - Listar contactos")
    print("3 - Procurar contacto")
    print("4 - Atualizar contacto")
    print("5 - Eliminar contacto")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":

        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")

        contacto = {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }

        contactos.append(contacto)

        print("\nContacto adicionado com sucesso!")

    elif opcao == "2":
        print("\nLista de contactos:")
        print(contactos)

    elif opcao == "3":
        print("\nProcurar contacto")

    elif opcao == "4":
        print("\nAtualizar contacto")

    elif opcao == "5":
        print("\nEliminar contacto")

    elif opcao == "6":
        print("\nPrograma terminado.")
        break

    else:
        print("\nOpção inválida!")