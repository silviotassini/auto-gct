from datetime import datetime, timedelta, timezone

from servicos import obter_servico_calendar

def formatar_data_google(data):

    if not data:
        return None

    return datetime.fromisoformat(
        data.replace("Z", "+00:00")
    ).strftime("%d-%m-%Y")

def ajustar_periodo(
    data_inicial=None,
    data_final=None,
    dias=None
):

    agora = datetime.now(timezone.utc)

    if dias is not None:
        inicio = agora
        fim = agora + timedelta(days=dias)

        return inicio, fim

    if data_inicial:
        inicio = data_inicial.replace(
            tzinfo=timezone.utc
        )

    else:
        inicio = agora

    if data_final:
        fim = data_final.replace(
            hour=23,
            minute=59,
            second=59,
            tzinfo=timezone.utc
        )

    else:
        fim = None

    if fim and inicio > fim:
        raise ValueError(
            "Data inicial maior que data final."
        )

    return inicio, fim


def listar_eventos(
    data_inicial=None,
    data_final=None,
    numero_eventos=None,
    dias=None
):
    try:
        service = obter_servico_calendar()

        inicio, fim = ajustar_periodo(
            data_inicial,
            data_final,
            dias
        )

        parametros = {
            'calendarId': 'primary',
            'timeMin': inicio.isoformat(),
            'singleEvents': True,
            'orderBy': 'startTime'
        }

        if fim:
            parametros['timeMax'] = fim.isoformat()

        if numero_eventos:
            parametros['maxResults'] = numero_eventos

        resultado = service.events().list(
            **parametros
        ).execute()

        eventos = resultado.get('items', [])

        if not eventos:
            print("Nenhum evento encontrado.")
            return {
                "sucesso": True,
                "eventos": []
            }

        resultado_final = []
        for evento in eventos:

            inicio_evento = evento['start'].get(
                'dateTime',
                evento['start'].get('date')
            )

            resultado_final.append({
                "id": evento['id'],
                "titulo": evento.get('summary'),
                "inicio": formatar_data_google(inicio_evento),
            })
        
        return {
            "sucesso": True,
            "eventos": resultado_final
        }

    except Exception as e:
        return {
            "sucesso": False,
            "mensagem": str(e)
        }


def criar_evento(
    titulo,
    data,
    hora_inicio,
    hora_fim,
    descricao=None
):
    try:

        service = obter_servico_calendar()

        inicio = datetime.strptime(
            f"{data} {hora_inicio}",
            "%d-%m-%Y %H:%M"
        ).replace(tzinfo=timezone.utc)

        fim = datetime.strptime(
            f"{data} {hora_fim}",
            "%d-%m-%Y %H:%M"
        ).replace(tzinfo=timezone.utc)

        evento = {
            'summary': titulo,
            'description': descricao,
            'start': {
                'dateTime': inicio.isoformat()
            },
            'end': {
                'dateTime': fim.isoformat()
            }
        }

        resultado = service.events().insert(
            calendarId='primary',
            body=evento
        ).execute()

        return {
            "sucesso": True,
            "mensagem": "Evento criado.",
            "id": resultado['id']
        }

    except Exception as e:
        return {
            "sucesso": False,
            "mensagem": str(e)
        }


def remover_evento(event_id):
    try:
        service = obter_servico_calendar()

        service.events().delete(
            calendarId='primary',
            eventId=event_id
        ).execute()

        return {
            "sucesso": True,
            "mensagem": "Evento removido."
        }

    except Exception as e:
        return {
            "sucesso": False,
            "mensagem": str(e)
        }