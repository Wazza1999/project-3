import gspread
from google.oauth2.service_account import Credentials

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

# Input Username (Wazza123) and Password (1234) 
print("Welcome to Le Bouchon Hotel and Brasseries' sales data.")
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

# If yes is selected the program will show the sales data
user_input = input('Would you like to see the Sales data that is available? y/n:')
if user_input == 'y':
    print(data)

else:
    print("Thank you have a nice day :)")

