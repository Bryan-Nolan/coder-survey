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
    return questions_data


def calculate_question_total(data):
    """
    From the data received from teh worksheet calcuate question total
    """
    total_questions = len(data)-1
    return total_questions


def get_results_sheet_data():
    """
    Get the totals from result sheet
    """
    results_data = SHEET.worksheet("results").get_all_values()
    return results_data


def questions_output(data):
    """
    Outputting data got from sheets to screen
    """
    choice_str = []
    choice_num = []
    for value in range(len(data)-1):
        question_row = data[value+1]
        print(f"\n\nQuestion {question_row[0]}")
        print(f"{question_row[1]}\n")
        print("Please enter the number of your choice from 1-4.\n")
        print(f"1: {question_row[2]} 2: {question_row[3]} 3: {question_row[4]} 4: {question_row[5]}\n")
        data_str = input("Enter your choice here: ")
        validate_data(data_str)
        choice_str.append(question_row[int(data_str)+1])
        choice_num.append(int(data_str))
    return choice_num, choice_str


def validate_data(value):
    """
    Using try except to validate data.  That only
    numbers between 1 and 4 entered for choices
    """
    try:
        if 1 > int(value) or int(value) > 4:
            raise ValueError(
                f"Please only enter values 1 - 4 not {value} "
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return


def output_choices(choice_str):
    """
    Outputs to screen choices made by user
    """
    print("\nYou made the following choices:")
    for i in range(len(choice_str)):
        print(f"Question {i+1}: {choice_str[i]}")


def calcuate_results(results_data, choice_num):
    """
    Update results from sheet and out put to screen
    """
    print(results_data)
    print(choice_num)


def main():
    """
    This is the main function which runs all functions
    """
    data = get_questions_data()
    total_questions = calculate_question_total(data)
    results_data = get_results_sheet_data()
    print("Welcome to my Coder Survey\n")
    print(f"Please answer the following {total_questions} questions\n")
    print("Results of Survey will be posted to screen after final question\n")
    choice_num, choice_str = questions_output(data)
    output_choices(choice_str)
    calcuate_results(results_data, choice_num)


main()
