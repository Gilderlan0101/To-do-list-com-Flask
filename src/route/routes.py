import os
from flask import Blueprint, render_template, request, redirect, flash

# Configurações do diretório e arquivo
BASE_DIR = os.path.expanduser("~")  # Diretório home do usuário
DIRECTORY = os.path.join(BASE_DIR, "my_tasks")  # Cria um diretório chamado "my_tasks"
FILENAME = os.path.join(DIRECTORY, 'my_task.txt')  # Caminho completo do arquivo

# Define o blueprint
home = Blueprint('home', __name__, template_folder='templates')

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
                tarefas.append(linha.strip())

    except FileNotFoundError:
        print(f"Arquivo não encontrado: {FILENAME}. Um novo arquivo será criado na próxima execução.")
        return []
    except Exception as e:
        print(f"Erro: {e}")
        return []

    return tarefas

@home.route('/', methods=['POST', 'GET'])
def page_inicial():
    viws_task = display()  # Chama a função display() para obter todas as tarefas

    if request.method == 'POST':
        task = request.form.get('task')  # Use get() para evitar KeyError
        if task:
            my_list(task)  # Adiciona a tarefa
            viws_task = display()  # Atualiza a lista de tarefas após adicionar

            if not viws_task:  # Se a lista de tarefas estiver vazia
                flash('Sua lista está vazia!', 'info')

    return render_template('home.html', viws_task=viws_task)

@home.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    try:
        tarefas = display()  # Chama a função display para obter a lista de tarefas
        if 0 <= task_id < len(tarefas):
            tarefas.pop(task_id)  # Remove a tarefa selecionada

            # Escreve as tarefas atualizadas de volta ao arquivo
            with open(FILENAME, 'w') as file:
                for tarefa in tarefas:
                    file.write(tarefa + '\n')

            flash('Tarefa removida com sucesso!', 'success')
        else:
            flash('ID da tarefa inválido.', 'error')

    except Exception as e:
        print(f"Erro ao deletar tarefa: {e}")
        flash('Erro ao remover a tarefa.', 'error')

    return redirect('/')  # Redireciona para a página inicial
