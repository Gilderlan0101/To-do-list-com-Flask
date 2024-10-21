import os
from flask import flash

# Define o caminho para o diretório onde o arquivo será salvo
BASE_DIR = os.path.expanduser("~")  # Diretório home do usuário
DIRECTORY = os.path.join(BASE_DIR, "my_tasks")  # Cria um diretório chamado "my_tasks"
FILENAME = os.path.join(DIRECTORY, 'my_task.txt')  # Caminho completo do arquivo

def my_list(add):
    try:
        # Verifica se o diretório existe, se não, cria
        if not os.path.exists(DIRECTORY):
            os.makedirs(DIRECTORY)

        # Primeiro, adicione a nova tarefa ao arquivo
        with open(FILENAME, 'a') as file:
            file.write(add + '\n')

        # Em seguida, retorne todas as tarefas
        return display()  # Chame a função display para retornar a lista completa

    except Exception as e:
        print(f"Erro: {e}")
        return []  # Retorna uma lista vazia em caso de erro


def display():
    tarefas = []  # Lista para armazenar as tarefas
    try:
        with open(FILENAME, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                tarefas.append(linha.strip())  # Adiciona cada linha à lista de tarefas

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {FILENAME}. Um novo arquivo será criado na próxima execução.")
        return []  # Retorna uma lista vazia se o arquivo não existir
    except Exception as e:
        print(f"Erro: {e}")
        return []  # Retorna uma lista vazia em caso de erro
    
    return tarefas  # Retorna a lista completa de tarefas
