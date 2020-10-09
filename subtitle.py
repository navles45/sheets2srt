import httplib2
import os
from apiclient import discovery
from google.oauth2 import service_account

try:
    scope = ['https://googleapis.com/auth/drive','https://googleapis.com/auth/drive.file','https://googleapis/auth/spreadsheets']

    secret_file = os.path.join(os.getcwd(), "client_secret.json")
    credentials = service_account.Credentials.from_service_account_file(secret_file)
    service = discovery.build('sheets', 'v4', credentials=credentials)

    spreadsheet_id = SPREADSHEET_ID
    spreadsheet_range = SPREADSHEET_RANGE

    request = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=spreadsheet_range, valueRenderOption='UNFORMATTED_VALUE', dateTimeRenderOption = 'FORMATTED_STRING')
    response = request.execute()

    for responses in ['values']:
        raw = response[responses]
        print(raw)

        for text in raw:
            seperator = '\n'
            print(seperator.join(map(str,text)) + seperator)


except OSError as e:
    print(e)
