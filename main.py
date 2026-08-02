import json
import os

FICHEIRO = "contactos.json"


# Carregar contactos guardados
if os.path.exists(FICHEIRO):
    try:
        with open(FICHEIRO, "r", encoding="utf-8") as ficheiro:
            contactos = json.load(ficheiro)

    except json.JSONDecodeError:
        contactos = []

else:
    contactos = []


while True:

    print("\n" + "=" * 40)
    print("        GESTÃO DE CONTACTOS")
    print("=" * 40)

    print("1 - Adicionar contacto")
    print("2 - Listar contactos")
    print("3 - Procurar contacto")
    print("4 - Atualizar contacto")
    print("5 - Eliminar contacto")
    print("6 - Sair")

    opcao = input("\nEscolha uma opção: ").strip()

    # Adicionar contacto
    if opcao == "1":

        print("\n===== ADICIONAR CONTACTO =====")

        nome = input("Nome: ").strip()
        telefone = input("Telefone: ").strip()
        email = input("Email: ").strip()

        if nome == "" or telefone == "" or email == "":
            print("\nTodos os campos são obrigatórios.")
            continue

        contacto_existente = False

        for contacto in contactos:
            if contacto["nome"].lower() == nome.lower():
                contacto_existente = True
                break

        if contacto_existente:
            print("\nJá existe um contacto com esse nome.")
            continue

        novo_contacto = {
            "nome": nome,
            "telefone": telefone,
            "email": email
        }

        contactos.append(novo_contacto)

        with open(FICHEIRO, "w", encoding="utf-8") as ficheiro:
            json.dump(
                contactos,
                ficheiro,
                ensure_ascii=False,
                indent=4
            )

        print("\nContacto adicionado com sucesso!")

    # Listar contactos
    elif opcao == "2":

        print("\n===== LISTA DE CONTACTOS =====")

        if len(contactos) == 0:
            print("Não existem contactos guardados.")

        else:
            contactos_ordenados = sorted(
                contactos,
                key=lambda contacto: contacto["nome"].lower()
            )

            for numero, contacto in enumerate(
                contactos_ordenados,
                start=1
            ):
                print(f"\nContacto {numero}")
                print(f"Nome: {contacto['nome']}")
                print(f"Telefone: {contacto['telefone']}")
                print(f"Email: {contacto['email']}")
                print("-" * 30)

    # Procurar contacto
    elif opcao == "3":

        print("\n===== PROCURAR CONTACTO =====")

        nome_pesquisado = input(
            "Nome do contacto: "
        ).strip()

        encontrado = False

        for contacto in contactos:

            if (
                contacto["nome"].lower()
                == nome_pesquisado.lower()
            ):

                print("\nContacto encontrado:")
                print(f"Nome: {contacto['nome']}")
                print(f"Telefone: {contacto['telefone']}")
                print(f"Email: {contacto['email']}")

                encontrado = True
                break

        if not encontrado:
            print("\nContacto não encontrado.")

    # Atualizar contacto
    elif opcao == "4":

        print("\n===== ATUALIZAR CONTACTO =====")

        nome_pesquisado = input(
            "Nome do contacto a atualizar: "
        ).strip()

        encontrado = False

        for contacto in contactos:

            if (
                contacto["nome"].lower()
                == nome_pesquisado.lower()
            ):

                print("\nDeixa o campo vazio para manter o valor atual.")

                novo_nome = input(
                    f"Novo nome [{contacto['nome']}]: "
                ).strip()

                novo_telefone = input(
                    f"Novo telefone [{contacto['telefone']}]: "
                ).strip()

                novo_email = input(
                    f"Novo email [{contacto['email']}]: "
                ).strip()

                if novo_nome != "":
                    contacto["nome"] = novo_nome

                if novo_telefone != "":
                    contacto["telefone"] = novo_telefone

                if novo_email != "":
                    contacto["email"] = novo_email

                with open(
                    FICHEIRO,
                    "w",
                    encoding="utf-8"
                ) as ficheiro:
                    json.dump(
                        contactos,
                        ficheiro,
                        ensure_ascii=False,
                        indent=4
                    )

                print("\nContacto atualizado com sucesso!")

                encontrado = True
                break

        if not encontrado:
            print("\nContacto não encontrado.")

    # Eliminar contacto
    elif opcao == "5":

        print("\n===== ELIMINAR CONTACTO =====")

        nome_pesquisado = input(
            "Nome do contacto a eliminar: "
        ).strip()

        encontrado = False

        for contacto in contactos:

            if (
                contacto["nome"].lower()
                == nome_pesquisado.lower()
            ):

                confirmacao = input(
                    f"Confirma a eliminação de "
                    f"{contacto['nome']}? (sim/não): "
                ).strip().lower()

                if confirmacao == "sim":
                    contactos.remove(contacto)

                    with open(
                        FICHEIRO,
                        "w",
                        encoding="utf-8"
                    ) as ficheiro:
                        json.dump(
                            contactos,
                            ficheiro,
                            ensure_ascii=False,
                            indent=4
                        )

                    print("\nContacto eliminado com sucesso!")

                else:
                    print("\nEliminação cancelada.")

                encontrado = True
                break

        if not encontrado:
            print("\nContacto não encontrado.")

    # Sair
    elif opcao == "6":

        print("\nPrograma terminado.")
        break

    # Opção inválida
    else:
        print("\nOpção inválida. Escolhe uma opção de 1 a 6.")