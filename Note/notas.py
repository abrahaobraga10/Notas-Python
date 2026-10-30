import sqlite3
from datetime import datetime

connection = sqlite3.connect("notas.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    titulo TEXT NOT NULL,
    dataEHora TEXT NOT NULL,
    texto TEXT NOT NULL
)
""")





while True:
    print(r"""
    ╔══════════════════════════════════════════╗
    ║                                          ║
    ║    _   _       _                         ║
    ║   | \ | | ___ | |_ __ _ ___              ║
    ║   |  \| |/ _ \| __/ _` / __|             ║
    ║   | |\  | (_) | || (_| \__ \             ║
    ║   |_| \_|\___/ \__\__,_|___/             ║
    ║                                          ║
    ╠══════════════════════════════════════════╣
    ║                                          ║
    ║     [1]  📝  Nova nota                   ║
    ║     [2]  📚  Ver notas anteriores        ║
    ║     [3]  🔍  Pesquisar nota              ║
    ║     [4]  🗑️  Apagar nota                  ║ 
    ║     [0]  🚪  Sair                        ║
    ║                                          ║
    ╚══════════════════════════════════════════╝
    """)

    option = input("Qual opção você deseja: ")

    if option == "1" :
        print("--- Nova Nota ---")
        name = input("Seu Nome: ")
        title = input("Crie um título pra sua nota: ")
        note_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        text = input("Escreva a nota: ")
        
        
        send = input("Digite E para enviar e C para cancelar: ")

        if send == "E":    
            cursor.execute("INSERT INTO quotes (nome, titulo, dataEHora, texto) VALUES (?, ?, ?, ?);", (name, title, note_date, text))

            connection.commit()

            print("Nota inserida com sucesso!")

        elif send == "C" :
            print("Cancelado")

        else:
            print("Inválido")
            break

        continue
    elif option == "2" :
        print("--- Notas Anteriores ---")
        cursor.execute("SELECT * FROM quotes")
        notes = cursor.fetchall()
        for id, nome, titulo, dataEHora, texto in notes:
            print(f"""
            Id: {id}
            Autor: {nome}
            Título: {titulo}
            Data e Hora: {dataEHora}

            {texto} """)
        print(notes)
        connection.commit()

        continue

    elif option == "3" :
        print("--- Pesquisar nota ---")
        print("""Escolha um filtro de pesquisa
        Autor-----Digite 1
        Título----Digite 2
        Data------Digite 3
        Texto-----DIgite 4""")

        search_filter = None

        user_filter = input("Digite seu filtro: ")
        user_search = input("Faça sua pesquisa: ")
        
        if user_filter == "1":
            search_filter = "nome"
        elif user_filter == "2":
            search_filter = "titulo"
        elif user_filter == "3":
            search_filter = "dataEHora"
        elif user_filter == "4":
            search_filter = "texto"
        else:
            print("Opção inválida")
            exit()
        
        cursor.execute(
            f"SELECT * FROM quotes WHERE {search_filter} LIKE ?",
            (f"%{user_search}%",)
        )
        search_result = cursor.fetchall()
        print("Resultado da busca:")
        for id, nome, titulo, dataEHora, texto in search_result:
            print(f"""
            Id: {id}
            Autor: {nome}
            Título: {titulo}
            Data e Hora: {dataEHora}
        
                {texto} """)
        print(search_result)
        
        continue
    elif option == "4" :
        print("---Apagar nota---")
        print("Digite somente números referentes a id's")
        note_for_delete = input("Digite o id da nota que você deseja deletar: ")

        cursor.execute(f"DELETE FROM quotes WHERE id = {note_for_delete}")
        connection.commit()

    elif option == "0" :
        print("Saindo...")
        connection.close()
        break


    else:
        print("Inválido")
        continue