# Automações Google (Calendar & Tasks)

Scripts em Python para gerenciar eventos do Google Agenda e tarefas do Google Tasks diretamente pelo terminal. 
Com esses scripts e uma Skill apropriada para o agente Hermes, pode se usar o Telegrma, por exemplo, 
para tratar eventos e tarefas do Google.

## 📋 Pré-requisitos

1. **Credenciais API**: Tenha o arquivo `credentials.json` na raiz do projeto.
2. **Ambiente Virtual**:
   ```bash
   uv venv
   uv sync google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```

## 🚀 Como usar

O script principal é o `main.py`. Ele utiliza subcomandos para separar as funcionalidades.

### 📅 Eventos (Google Calendar)

**Listar eventos:**
```bash
# Próximos 10 eventos
uv run main.py eventos listar

# Eventos em um intervalo de datas (DD-MM-AAAA)
uv run main.py eventos listar -di 20-05-2026 -df 25-05-2026

# Definir quantidade ou dias à frente
uv run main.py eventos listar -n 5
uv run main.py eventos listar --dias 7
```

**Criar evento:**
```bash
uv run main.py eventos criar --titulo "Reunião de Perícia" --data 20-05-2026 --hora_inicio 14:00 --hora_fim 15:00 --descricao "Análise de logs de rede"
```

**Remover evento:**
```bash
uv run main.py eventos remover --id "ID_DO_EVENTO"
```

---

### ✅ Tarefas (Google Tasks)

**Listar tarefas:**
```bash
uv run main.py tarefas listar
```

**Criar tarefa:**
```bash
uv run main.py tarefas criar --titulo "Relatório Final" --descricao "Enviar para o tribunal" --data_limite 2026-05-22T23:59:00Z
```

**Concluir tarefa:**
```bash
uv run main.py tarefas concluir --id "ID_DA_TAREFA"
```

**Remover tarefa:**
```bash
uv run main.py tarefas remover --id "ID_DA_TAREFA"
```

## 🛠️ Funções Principais

- `modulo eventos`: Gerencia integração com a API do Calendar.
- `modulo tarefas`: Gerencia integração com a API do Tasks.

---
*Nota: Na primeira execução, o navegador será aberto para autorizar o acesso à sua conta Google. O token será salvo em `token.json`.*
