from flask import flash
FILENAME = 'src/services/my_task.txt'

def my_list(add):
    try:
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

      

    except Exception as e:
        print(f"Erro: {e}")
        return []  # Retorna uma lista vazia em caso de erro
    
    return tarefas  # Retorna a lista completa de tarefas


