import os
from flask import Blueprint, render_template, request, redirect, flash
from src.services.to_do_list import my_list, display, path_univesal
home = Blueprint('home', __name__, template_folder='templates')


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
    caminho_creat_path = path_univesal() 
    try:
        tarefas = display()  # Chama a função display para obter a lista de tarefas
        if 0 <= task_id < len(tarefas):
            tarefas.pop(task_id)  # Remove a tarefa selecionada

            # Escreve as tarefas atualizadas de volta ao arquivo
            with open(caminho_creat_path, 'w') as file:
                for tarefa in tarefas:
                    file.write(tarefa + '\n')

            flash('Tarefa removida com sucesso!', 'success')
        else:
            flash('ID da tarefa inválido.', 'error')

    except Exception as e:
        print(f"Erro ao deletar tarefa: {e}")
        flash('Erro ao remover a tarefa.', 'error')

    return redirect('/')  # Redireciona para a página inicial
