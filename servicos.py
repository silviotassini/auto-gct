import os.path

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build


SCOPES = [
    'https://www.googleapis.com/auth/calendar',
    'https://www.googleapis.com/auth/tasks'
]


def autenticar():

    creds = None

    if os.path.exists('token.json'):

        creds = Credentials.from_authorized_user_file(
            'token.json',
            SCOPES
        )

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:

            creds.refresh(Request())

        else:

            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json',
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:

            token.write(creds.to_json())

    return creds


def obter_servico_calendar():

    creds = autenticar()

    return build(
        'calendar',
        'v3',
        credentials=creds
    )


def obter_servico_tasks():

    creds = autenticar()

    return build(
        'tasks',
        'v1',
        credentials=creds
    )