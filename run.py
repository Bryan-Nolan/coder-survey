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
SHEET = GSPREAD_CLIENT.open('coder_survey_questions')

def get_questions_data():
    """
    Get the Questions ans Answers from worksheet
    """
    questions_data = SHEET.worksheet("questions").get_all_values()
    question_row = questions_data[1]
    print(question_row)
    
    return questions_data

def calculate_question_total (data):
    """
    From the data received from teh worksheet calcuate question total
    """
    total_questions = len(data)-1

    return total_questions

    
def main():
    """
    This is the main function which runs all functions
    """
    data = get_questions_data()
    total_questions = calculate_question_total(data)
    print("Welcome to my Coder Survey\n")
    print(f"Please anwser the following {total_questions} questions\n")
    print("Results of Survey will be posted to screen\n")
    

main()