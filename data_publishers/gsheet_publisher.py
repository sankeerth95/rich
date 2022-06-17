import pygsheets
from pygsheets.client import Client
import pandas as pd


def authorize_client(service_account_file) -> Client:
    return pygsheets.authorize(service_account_file=service_account_file)

def update_main_sheet(client: Client, spreadsheet: str, worksheet: str, dataframe: pd.DataFrame):
    sh = client.open(spreadsheet)
    if worksheet in [ws.title for ws in sh.worksheets()]:
        wks = sh.worksheet_by_title(worksheet)
    else:
        wks = sh.add_worksheet(worksheet)
    wks.set_dataframe(dataframe, start='A1')


