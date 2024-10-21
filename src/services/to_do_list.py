# import os
# from flask import flash

# # Define o caminho para o diretório onde o arquivo será salvo
# BASE_DIR = os.path.expanduser("~")  # Diretório home do usuário
# DIRECTORY = os.path.join(BASE_DIR, "my_tasks")  # Cria um diretório chamado "my_tasks"
# FILENAME = os.path.join(DIRECTORY, 'my_task.txt')  # Caminho completo do arquivo
# def my_list(add):
#     try:
#         # Verifica se o diretório existe, se não, cria
#         if not os.path.exists(DIRECTORY):
#             os.makedirs(DIRECTORY)

#         # Se a tarefa for vazia ou composta apenas por espaços, não a adiciona
#         if not add.strip():
#             flash("A tarefa não pode ser vazia.", "error")
#             return display()

#         # Adiciona a nova tarefa ao arquivo
#         with open(FILENAME, 'a') as file:
#             file.write(add.strip() + '\n')  # Use strip() para evitar espaços em branco

#         return display()  # Chame a função display para retornar a lista completa

#     except Exception as e:
#         print(f"Erro: {e}")
#         flash("Erro ao adicionar a tarefa.", "error")
#         return []  # Retorna uma lista vazia em caso de erro


# def display():
#     tarefas = []  # Lista para armazenar as tarefas
#     try:
#         with open(FILENAME, "r") as arquivo:
#             linhas = arquivo.readlines()
#             for linha in linhas:
#                 tarefas.append(linha.strip())  # Adiciona cada linha à lista de tarefas

#     except FileNotFoundError:
#         print(f"Arquivo não encontrado: {FILENAME}. Um novo arquivo será criado na próxima execução.")
#         return []  # Retorna uma lista vazia se o arquivo não existir
#     except Exception as e:
#         print(f"Erro: {e}")
#         return []  # Retorna uma lista vazia em caso de erro
    
#     return tarefas  # Retorna a lista completa de tarefas

# def delete_task(task_id):
#     try:
#         tarefas = display()  # Chama a função display para obter a lista de tarefas

#         # Verifica se o ID da tarefa está dentro do intervalo válido
#         if 0 <= task_id < len(tarefas):
#             # Remove a tarefa selecionada
#             tarefas.pop(task_id)

#             # Escreve as tarefas atualizadas de volta ao arquivo
#             with open(FILENAME, 'w') as file:
#                 for tarefa in tarefas:
#                     file.write(tarefa + '\n')

#             flash('Tarefa removida com sucesso!', 'success')  # Mensagem de sucesso
#         else:
#             flash('ID da tarefa inválido.', 'error')  # Mensagem de erro se o ID for inválido

#     except Exception as e:
#         print(f"Erro ao deletar tarefa: {e}")
#         flash('Erro ao remover a tarefa.', 'error')  # Mensagem de erro em caso de exceção

#     return display()  # Retorna a lista atualizada de tarefas
