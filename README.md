# Google Automation (Calendar & Tasks)

Python scripts to manage Google Calendar events and Google Tasks directly from the terminal.
With these scripts and an appropriate Skill for the Hermes agent, it is possible to use Telegram, for example,
to handle Google events and tasks.

## 📋 Prerequisites

1. **API Credentials**: Keep the `credentials.json` file in the project root.
2. **Virtual Environment**:
   ```bash
   uv venv
   uv sync google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```

## 🚀 How to use

The main script is `main.py`. It uses subcommands to separate functionalities.

### 📅 Events (Google Calendar)

**List events:**
```bash
# Next 10 events
uv run main.py eventos listar

# Events in a date range (DD-MM-AAAA)
uv run main.py eventos listar -di 20-05-2026 -df 25-05-2026

# Define number of days ahead
uv run main.py eventos listar -n 5
uv run main.py eventos listar --dias 7
```

**Create event:**
```bash
uv run main.py eventos criar --titulo "Reunião de Perícia" --data 20-05-2026 --hora_inicio 14:00 --hora_fim 15:00 --descricao "Análise de logs de rede"
```

**Remove event:**
```bash
uv run main.py eventos remover --id "ID_DO_EVENTO"
```

---

### ✅ Tasks (Google Tasks)

**List tasks:**
```bash
uv run main.py tarefas listar
```

**Create task:**
```bash
uv run main.py tarefas criar --titulo "Relatório Final" --descricao "Enviar para o tribunal" --data_limite 2026-05-22T23:59:00Z
```

**Complete task:**
```bash
uv run main.py tarefas concluir --id "ID_DA_TAREFA"
```

**Remove task:**
```bash
uv run main.py tarefas remover --id "ID_DA_TAREFA"
```

## 🛠️ Main Features

- `events module`: Manages integration with the Calendar API.
- `tasks module`: Manages integration with the Tasks API.

---
*Note: On the first run, the browser will open so you can authorize access to your Google account. The token will be saved in `token.json`.*
