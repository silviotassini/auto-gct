from datetime import datetime

from servicos import obter_servico_tasks

def formatar_data_google(data):

    if not data:
        return None

    return datetime.fromisoformat(
        data.replace("Z", "+00:00")
    ).strftime("%d-%m-%Y")
    
def listar_tarefas():

    service = obter_servico_tasks()
    resultado_listas = service.tasklists().list().execute()
    listas = resultado_listas.get('items', [])

    if not listas:
        print("Nenhuma lista encontrada.")
        return None

    resultado_final = []
    for lista in listas:

        nome_lista = lista['title']
        lista_id = lista['id']

        print(f"LISTA: {nome_lista}")

        resultado_tarefas = service.tasks().list(
            tasklist=lista_id
        ).execute()

        tarefas = resultado_tarefas.get('items', [])

        if not tarefas:
            print("Nenhuma tarefa.")
            continue

        for tarefa in tarefas:
            print("ID:", tarefa.get('id'))
            print("Título:", tarefa.get('title'))
            print("Status:", tarefa.get('status'))

            if 'due' in tarefa:
                print("Prazo:", formatar_data_google(tarefa['due']))
            tarefa_formatada = {
                "title": tarefa.get("title"),
                "status": tarefa.get("status"),
                "updated": tarefa.get("updated"),
                "due": formatar_data_google(tarefa.get("due")),
                "webViewLink": tarefa.get("webViewLink")
            }

            resultado_final.append(
                tarefa_formatada
            )

    return resultado_final


def criar_tarefa(
    titulo,
    descricao=None,
    data_limite=None
):

    service = obter_servico_tasks()

    tarefa = {
        'title': titulo
    }

    if descricao:
        tarefa['notes'] = descricao

    if data_limite:
        data = datetime.strptime(
            data_limite,
            "%d-%m-%Y"
        )

        tarefa['due'] = data.isoformat() + 'Z'

    resultado = service.tasks().insert(
        tasklist='@default',
        body=tarefa
    ).execute()

    print("Tarefa criada.")
    print("ID:", resultado['id'])


def remover_tarefa(task_id):

    service = obter_servico_tasks()

    service.tasks().delete(
        tasklist='@default',
        task=task_id
    ).execute()

    print("Tarefa removida.")


def concluir_tarefa(task_id):

    service = obter_servico_tasks()

    tarefa = service.tasks().get(
        tasklist='@default',
        task=task_id
    ).execute()

    tarefa['status'] = 'completed'

    service.tasks().update(
        tasklist='@default',
        task=task_id,
        body=tarefa
    ).execute()

    print("Tarefa concluída.")