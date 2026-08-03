import customtkinter as ctk
from tkinter import messagebox

from contactos import (
    carregar_contactos,
    guardar_contactos,
    adicionar_contacto as guardar_novo_contacto
)


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

contactos = carregar_contactos()


def limpar_campos():
    entrada_nome.delete(0, "end")
    entrada_telefone.delete(0, "end")
    entrada_email.delete(0, "end")


def atualizar_lista_contactos():
    caixa_contactos.configure(state="normal")
    caixa_contactos.delete("1.0", "end")

    if len(contactos) == 0:
        caixa_contactos.insert(
            "end",
            "Não existem contactos guardados."
        )

    else:
        contactos_ordenados = sorted(
            contactos,
            key=lambda contacto: contacto["nome"].lower()
        )

        for numero, contacto in enumerate(
            contactos_ordenados,
            start=1
        ):
            caixa_contactos.insert(
                "end",
                f"Contacto {numero}\n"
                f"Nome: {contacto['nome']}\n"
                f"Telefone: {contacto['telefone']}\n"
                f"Email: {contacto['email']}\n"
                f"{'-' * 40}\n"
            )

    caixa_contactos.configure(state="disabled")


def adicionar_contacto():
    nome = entrada_nome.get()
    telefone = entrada_telefone.get()
    email = entrada_email.get()

    sucesso, mensagem = guardar_novo_contacto(
        contactos,
        nome,
        telefone,
        email
    )

    if sucesso:
        label_mensagem.configure(
            text=mensagem,
            text_color="green"
        )

        limpar_campos()
        atualizar_lista_contactos()

    else:
        label_mensagem.configure(
            text=mensagem,
            text_color="red"
        )


def procurar_contacto():
    nome_pesquisado = entrada_nome.get().strip()

    if nome_pesquisado == "":
        label_mensagem.configure(
            text="Introduz o nome do contacto a procurar.",
            text_color="red"
        )
        return

    for contacto in contactos:
        if contacto["nome"].lower() == nome_pesquisado.lower():

            entrada_nome.delete(0, "end")
            entrada_nome.insert(
                0,
                contacto["nome"]
            )

            entrada_telefone.delete(0, "end")
            entrada_telefone.insert(
                0,
                contacto["telefone"]
            )

            entrada_email.delete(0, "end")
            entrada_email.insert(
                0,
                contacto["email"]
            )

            label_mensagem.configure(
                text="Contacto encontrado.",
                text_color="green"
            )

            return

    label_mensagem.configure(
        text="Contacto não encontrado.",
        text_color="red"
    )


def atualizar_contacto():
    nome_pesquisado = entrada_nome.get().strip()
    novo_telefone = entrada_telefone.get().strip()
    novo_email = entrada_email.get().strip()

    if nome_pesquisado == "":
        label_mensagem.configure(
            text="Introduz o nome do contacto a atualizar.",
            text_color="red"
        )
        return

    if novo_telefone == "" or novo_email == "":
        label_mensagem.configure(
            text="Procura primeiro o contacto e preenche todos os campos.",
            text_color="red"
        )
        return

    if not novo_telefone.isdigit():
        label_mensagem.configure(
            text="O telefone deve conter apenas números.",
            text_color="red"
        )
        return

    if len(novo_telefone) < 9:
        label_mensagem.configure(
            text="O telefone deve ter pelo menos 9 dígitos.",
            text_color="red"
        )
        return

    if "@" not in novo_email or "." not in novo_email:
        label_mensagem.configure(
            text="Introduz um email válido.",
            text_color="red"
        )
        return

    for contacto in contactos:
        if contacto["nome"].lower() == nome_pesquisado.lower():

            contacto["telefone"] = novo_telefone
            contacto["email"] = novo_email

            if guardar_contactos(contactos):
                label_mensagem.configure(
                    text="Contacto atualizado com sucesso!",
                    text_color="green"
                )

                atualizar_lista_contactos()

            else:
                label_mensagem.configure(
                    text="Não foi possível guardar as alterações.",
                    text_color="red"
                )

            return

    label_mensagem.configure(
        text="Contacto não encontrado.",
        text_color="red"
    )


def eliminar_contacto():
    nome_pesquisado = entrada_nome.get().strip()

    if nome_pesquisado == "":
        label_mensagem.configure(
            text="Introduz o nome do contacto a eliminar.",
            text_color="red"
        )
        return

    for contacto in contactos:
        if contacto["nome"].lower() == nome_pesquisado.lower():

            confirmar = messagebox.askyesno(
                "Confirmar eliminação",
                f"Queres mesmo eliminar o contacto "
                f"{contacto['nome']}?"
            )

            if not confirmar:
                label_mensagem.configure(
                    text="Eliminação cancelada.",
                    text_color="orange"
                )
                return

            contactos.remove(contacto)

            if guardar_contactos(contactos):
                label_mensagem.configure(
                    text="Contacto eliminado com sucesso!",
                    text_color="green"
                )

                limpar_campos()
                atualizar_lista_contactos()

            else:
                label_mensagem.configure(
                    text="Não foi possível guardar a alteração.",
                    text_color="red"
                )

            return

    label_mensagem.configure(
        text="Contacto não encontrado.",
        text_color="red"
    )


janela = ctk.CTk()
janela.title("Gestão de Contactos")
janela.geometry("720x900")
janela.resizable(False, False)


titulo = ctk.CTkLabel(
    janela,
    text="GESTÃO DE CONTACTOS",
    font=ctk.CTkFont(
        size=24,
        weight="bold"
    )
)

titulo.pack(pady=(25, 15))


label_nome = ctk.CTkLabel(
    janela,
    text="Nome:"
)

label_nome.pack(pady=(5, 3))


entrada_nome = ctk.CTkEntry(
    janela,
    width=320,
    placeholder_text="Introduza o nome"
)

entrada_nome.pack(pady=(0, 10))


label_telefone = ctk.CTkLabel(
    janela,
    text="Telefone:"
)

label_telefone.pack(pady=(5, 3))


entrada_telefone = ctk.CTkEntry(
    janela,
    width=320,
    placeholder_text="Introduza o telefone"
)

entrada_telefone.pack(pady=(0, 10))


label_email = ctk.CTkLabel(
    janela,
    text="Email:"
)

label_email.pack(pady=(5, 3))


entrada_email = ctk.CTkEntry(
    janela,
    width=320,
    placeholder_text="Introduza o email"
)

entrada_email.pack(pady=(0, 10))


frame_botoes = ctk.CTkFrame(
    janela,
    fg_color="transparent"
)

frame_botoes.pack(pady=(20, 10))


botao_adicionar = ctk.CTkButton(
    frame_botoes,
    text="Adicionar Contacto",
    width=200,
    height=40,
    command=adicionar_contacto
)

botao_adicionar.grid(
    row=0,
    column=0,
    padx=10,
    pady=5
)


botao_procurar = ctk.CTkButton(
    frame_botoes,
    text="Procurar Contacto",
    width=200,
    height=40,
    command=procurar_contacto
)

botao_procurar.grid(
    row=0,
    column=1,
    padx=10,
    pady=5
)


botao_atualizar = ctk.CTkButton(
    frame_botoes,
    text="Atualizar Contacto",
    width=200,
    height=40,
    command=atualizar_contacto
)

botao_atualizar.grid(
    row=1,
    column=0,
    padx=10,
    pady=5
)


botao_eliminar = ctk.CTkButton(
    frame_botoes,
    text="Eliminar Contacto",
    width=200,
    height=40,
    fg_color="#B22222",
    hover_color="#8B0000",
    command=eliminar_contacto
)

botao_eliminar.grid(
    row=1,
    column=1,
    padx=10,
    pady=5
)


botao_limpar = ctk.CTkButton(
    janela,
    text="Limpar Campos",
    width=200,
    height=35,
    fg_color="gray40",
    hover_color="gray30",
    command=limpar_campos
)

botao_limpar.pack(pady=(5, 10))


label_mensagem = ctk.CTkLabel(
    janela,
    text=""
)

label_mensagem.pack(pady=5)


titulo_contactos = ctk.CTkLabel(
    janela,
    text="CONTACTOS GUARDADOS",
    font=ctk.CTkFont(
        size=18,
        weight="bold"
    )
)

titulo_contactos.pack(pady=(15, 5))


caixa_contactos = ctk.CTkTextbox(
    janela,
    width=520,
    height=230
)

caixa_contactos.pack(pady=(0, 20))


atualizar_lista_contactos()

janela.mainloop()