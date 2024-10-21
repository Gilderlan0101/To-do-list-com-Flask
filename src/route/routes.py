from flask import Blueprint, render_template, request, redirect, flash
from src.services.to_do_list import my_list, display
import os

home = Blueprint('home', __name__, template_folder='templates')
FILENAME = 'src/services/my_task.txt'

@home.route('/', methods=['POST', 'GET'])
def page_inicial():
    
    if request.method == 'POST':
        task = request.form.get('task')  # Use get() para evitar KeyError

        if task:
            add_task = my_list(task)  # Aqui você adiciona a tarefa
            if add_task is None:
                print("Erro ao adicionar a tarefa.")
            if add_task == [ ]:
                flash('Sua lista esta vazinha')    
            

    # Aqui, chame a função display() para obter todas as tarefas
    viws_task = display()
    
    return render_template('home.html', viws_task=viws_task)


FILENAME = os.path.join(os.path.expanduser("~"), "my_tasks.txt")  # Salva o arquivo no diretório home do usuário

@home.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    try:
        # Lê as tarefas atuais
        tarefas = display()  # Chama a função display para obter a lista de tarefas

        # Verifica se o ID da tarefa está dentro do intervalo válido
        if 0 <= task_id < len(tarefas):
            # Remove a tarefa selecionada
            tarefas.pop(task_id)

            # Escreve as tarefas atualizadas de volta ao arquivo
            with open(FILENAME, 'w') as file:
                for tarefa in tarefas:
                    file.write(tarefa + '\n')

            flash('Tarefa removida com sucesso!', 'success')  # Adiciona uma mensagem de sucesso
        else:
            flash('ID da tarefa inválido.', 'error')  # Mensagem de erro se o ID for inválido

    except Exception as e:
        print(f"Erro ao deletar tarefa: {e}")
        flash('Erro ao remover a tarefa.', 'error')  # Mensagem de erro em caso de exceção

    return redirect('/')  # Redireciona para a página inicial
