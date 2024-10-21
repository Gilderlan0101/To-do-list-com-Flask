from flask import Blueprint, render_template, request, redirect, flash
from src.services.to_do_list import my_list, display

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

@home.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    try:
        # Lê as tarefas atuais
        tarefas = display()
        if 0 <= task_id < len(tarefas):
            # Remove a tarefa selecionada
            tarefas.pop(task_id)


        
            # Escreve as tarefas atualizadas de volta ao arquivo
            with open(FILENAME, 'w') as file:
                for tarefa in tarefas:
                    file.write(tarefa + '\n')
            
                

    except Exception as e:
        print(f"Erro: {e}")

    return redirect('/')  # Redireciona para a página inicial


