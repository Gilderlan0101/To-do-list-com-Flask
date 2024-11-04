import requests
from flask import Blueprint, render_template, request, flash, url_for, redirect

# Configuração do Blueprint
home = Blueprint('home', __name__, template_folder='templates')

# URL base da API
API_BASE_URL = "https://api-para-to-do-list.onrender.com/task"

@home.route('/', methods=['POST', 'GET'])
def page_inicial():
    # Obtendo a lista de tarefas via GET na API
    try:
        response = requests.get(API_BASE_URL)
        response.raise_for_status()
        viws_task = response.json()  # Lista de tarefas
    except requests.exceptions.RequestException as e:
        flash("Erro ao carregar as tarefas.", 'error')
        viws_task = []

    # Caso o método seja POST, uma nova tarefa será enviada para a API
    if request.method == 'POST':
        task = request.form.get('task')
        if task:
            try:
                # Envia a nova tarefa para a API usando POST
                response = requests.post(API_BASE_URL, json={'task': task})
                response.raise_for_status()
                flash('Tarefa adicionada com sucesso!', 'success')
            except requests.exceptions.RequestException as e:
                flash('Erro ao adicionar a tarefa.', 'error')

            # Redireciona para a página inicial para evitar reenvio do formulário
            return redirect(url_for('home.page_inicial'))

    # Renderiza a página com a lista atual de tarefas
    return render_template('home.html', viws_task=viws_task)

@home.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    # Deleta a tarefa enviando uma requisição DELETE para a API
    try:
        response = requests.delete(f"{API_BASE_URL}/{task_id}")
        response.raise_for_status()
        flash('Tarefa removida com sucesso!', 'success')
    except requests.exceptions.RequestException as e:
        flash('Erro ao remover a tarefa.', 'error')

    return redirect(url_for('home.page_inicial'))
