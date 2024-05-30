import gspread
from google.oauth2.service_account import Credentials

# Input Username (Wazza123) and Password (1234) 
attempts = 0

while attempts < 3:
    Username = input("Enter your Username:")
    Password = input("Enter your Password:")

    if Username == 'Wazza123' and Password =='1234':
        print('Welcome to LeBouchon Wazza123. ')
        break
        
    else:
        print('Incorrect Credentials. Please try again.')
        attempts += 1
        continue

### SCOPE code
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Le_Bouchon')

sales = SHEET.worksheet('Sales')

data = sales.get_all_values()

