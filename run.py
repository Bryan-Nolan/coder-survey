import gspread
from google.oauth2.service_account import Credentials
import os

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

    return questions_data

def calculate_question_total (data):
    """
    From the data received from teh worksheet calcuate question total
    """
    total_questions = len(data)-1

    return total_questions

def questions_output(data):

    for value in range(len(data)-1):
        question_row = data[value+1]
        print(f"{question_row[0]}: {question_row[1]}\n")
        print("Please enter the number of her choice.")
        print(f"1: {question_row[2]} 2: {question_row[3]} 3: {question_row[4]} 4: {question_row[5]}\n")

def main():
    """
    This is the main function which runs all functions
    """
    clear = lambda:os.system('cls')
    clear()
    data = get_questions_data()
    total_questions = calculate_question_total(data)
    print("Welcome to my Coder Survey\n")
    print(f"Please anwser the following {total_questions} questions\n")
    print("Results of Survey will be posted to screen after final question\n")
    questions_output(data)
    

main()