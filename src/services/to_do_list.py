import os
from flask import flash

# Configurações do diretório e arquivo
BASE_DIR = os.path.expanduser("~")  # Diretório home do usuário
DIRECTORY = os.path.join(BASE_DIR, "my_tasks")  # Cria um diretório chamado "my_tasks"
FILENAME = os.path.join(DIRECTORY, 'my_task.txt')

def path_univesal():
   'Função que cria um caminho completo'
   FILENAME = os.path.join(DIRECTORY, 'my_task.txt')

   return FILENAME


def my_list(add):
    try:
        # Verifica se o diretório existe, se não, cria
        if not os.path.exists(DIRECTORY):
            os.makedirs(DIRECTORY)

        # Se a tarefa for vazia ou composta apenas por espaços, não a adiciona
        if not add.strip():
            flash("A tarefa não pode ser vazia.", "error")
            return display()

        # Adiciona a nova tarefa ao arquivo
        with open(FILENAME, 'a') as file:
            file.write(add.strip() + '\n')  # Use strip() para evitar espaços em branco

    except Exception as e:
        print(f"Erro: {e}")
        flash("Erro ao adicionar a tarefa.", "error")

def display():
    tarefas = []
    try:
        with open(FILENAME, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                tarefas.insert(0, linha.strip()) 

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {FILENAME}. Um novo arquivo será criado na próxima execução.")
        return []
    except Exception as e:
        print(f"Erro: {e}")
        return []

    return tarefas