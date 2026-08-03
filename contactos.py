import json
import os

FICHEIRO = "contactos.json"


def carregar_contactos():
    if not os.path.exists(FICHEIRO):
        return []

    try:
        with open(FICHEIRO, "r", encoding="utf-8") as ficheiro:
            dados = json.load(ficheiro)

            if isinstance(dados, list):
                return dados

            return []

    except (json.JSONDecodeError, OSError):
        return []


def guardar_contactos(contactos):
    try:
        with open(FICHEIRO, "w", encoding="utf-8") as ficheiro:
            json.dump(
                contactos,
                ficheiro,
                ensure_ascii=False,
                indent=4
            )

        return True

    except OSError:
        return False


def validar_dados(nome, telefone, email):
    nome = nome.strip()
    telefone = telefone.strip()
    email = email.strip()

    if nome == "" or telefone == "" or email == "":
        return False, "Todos os campos são obrigatórios."

    if not telefone.isdigit():
        return False, "O telefone deve conter apenas números."

    if len(telefone) < 9:
        return False, "O telefone deve ter pelo menos 9 dígitos."

    if "@" not in email or "." not in email:
        return False, "Introduz um email válido."

    return True, ""


def adicionar_contacto(contactos, nome, telefone, email):
    nome = nome.strip()
    telefone = telefone.strip()
    email = email.strip()

    dados_validos, mensagem = validar_dados(
        nome,
        telefone,
        email
    )

    if not dados_validos:
        return False, mensagem

    for contacto in contactos:
        if contacto["nome"].lower() == nome.lower():
            return False, "Já existe um contacto com esse nome."

    novo_contacto = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    contactos.append(novo_contacto)

    if not guardar_contactos(contactos):
        contactos.remove(novo_contacto)
        return False, "Não foi possível guardar o contacto."

    return True, "Contacto adicionado com sucesso!"