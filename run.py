import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Love_sandwiches')

def get_sales_data():
    '''
    This function will get the sales data from the user.
    '''
    print("Please enter sales data from last markets")
    print("The sales figure should consist of six numbers separated by commas")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Input your data here:")
    print(f"The data provided are {data_str}")

get_sales_data()