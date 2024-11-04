import requests
from flask import flash

# URL base da API
API_BASE_URL = "http://127.0.0.1:5000/task"
import requests
from flask import flash


def my_list(add):
    """
    Envia uma nova tarefa para a API.
    """
    if not add.strip():  # Verifica se a tarefa não está vazia
        flash("A tarefa não pode ser vazia.", "error")
        return display()  # Retorna a lista atualizada para exibição

    try:
        # Envia a tarefa com o nome correto do campo 'task'
        data = {'task': add.strip()}
        response = requests.post(API_BASE_URL, json=data)
        print(f"Enviando dados: {data}")  # Log dos dados enviados
        response.raise_for_status()
        flash("Tarefa adicionada com sucesso!", "success")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao adicionar a tarefa: {e}")
        flash("Erro ao adicionar a tarefa.", "error")

    return display()  # Atualiza a lista de tarefas

def display():
    """
    Obtém a lista de tarefas da API.
    """
    try:
        # Faz uma requisição GET para obter todas as tarefas
        response = requests.get(API_BASE_URL)
        response.raise_for_status()
        tarefas = response.json()  # Retorna a lista de tarefas
    except requests.exceptions.RequestException as e:
        print(f"Erro ao carregar as tarefas: {e}")
        flash("Erro ao carregar as tarefas.", "error")
        tarefas = []

    return tarefas
