import argparse
from datetime import datetime

from eventos import (
    listar_eventos,
    criar_evento,
    remover_evento
)

from tarefas import (
    listar_tarefas,
    criar_tarefa,
    remover_tarefa,
    concluir_tarefa
)


def validar_data(valor):

    try:

        return datetime.strptime(
            valor,
            "%d-%m-%Y"
        )

    except ValueError:

        raise argparse.ArgumentTypeError(
            "Formato deve ser DD-MM-AAAA"
        )


parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(
    dest="modulo",
    required=True
)

# =========================================================
# EVENTOS
# =========================================================

parser_eventos = subparsers.add_parser("eventos")

sub_eventos = parser_eventos.add_subparsers(
    dest="acao",
    required=True
)

# LISTAR EVENTOS

listar_ev = sub_eventos.add_parser("listar")

listar_ev.add_argument("-di", "--data_inicial", type=validar_data)
listar_ev.add_argument("-df", "--data_final", type=validar_data)
listar_ev.add_argument("-n", "--numero_eventos", type=int)
listar_ev.add_argument("--dias", type=int)

# CRIAR EVENTO

criar_ev = sub_eventos.add_parser("criar")

criar_ev.add_argument("--titulo", required=True)
criar_ev.add_argument("--data", required=True)
criar_ev.add_argument("--hora_inicio", required=True)
criar_ev.add_argument("--hora_fim", required=True)
criar_ev.add_argument("--descricao")

# REMOVER EVENTO

remover_ev = sub_eventos.add_parser("remover")

remover_ev.add_argument("--id", required=True)

# =========================================================
# TAREFAS
# =========================================================

parser_tarefas = subparsers.add_parser("tarefas")

sub_tarefas = parser_tarefas.add_subparsers(
    dest="acao",
    required=True
)

# LISTAR

listar_tf = sub_tarefas.add_parser("listar")

# CRIAR

criar_tf = sub_tarefas.add_parser("criar")

criar_tf.add_argument("--titulo", required=True)
criar_tf.add_argument("--descricao")
criar_tf.add_argument("--data_limite")

# REMOVER

remover_tf = sub_tarefas.add_parser("remover")

remover_tf.add_argument("--id", required=True)

# CONCLUIR

concluir_tf = sub_tarefas.add_parser("concluir")

concluir_tf.add_argument("--id", required=True)

# =========================================================
# EXECUÇÃO
# =========================================================

args = parser.parse_args()

# EVENTOS

if args.modulo == "eventos":

    if args.acao == "listar":

        listar_eventos(
            data_inicial=args.data_inicial,
            data_final=args.data_final,
            numero_eventos=args.numero_eventos,
            dias=args.dias
        )

    elif args.acao == "criar":

        criar_evento(
            titulo=args.titulo,
            data=args.data,
            hora_inicio=args.hora_inicio,
            hora_fim=args.hora_fim,
            descricao=args.descricao
        )

    elif args.acao == "remover":

        remover_evento(args.id)

# TAREFAS

elif args.modulo == "tarefas":

    if args.acao == "listar":

        listar_tarefas()

    elif args.acao == "criar":

        criar_tarefa(
            titulo=args.titulo,
            descricao=args.descricao,
            data_limite=args.data_limite
        )

    elif args.acao == "remover":

        remover_tarefa(args.id)

    elif args.acao == "concluir":

        concluir_tarefa(args.id)