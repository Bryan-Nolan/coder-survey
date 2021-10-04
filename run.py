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
    Get the totals from result sheet and input into dictoionary
    """
    results_data = SHEET.worksheet("results").get_all_values()
    return results_data


def questions_output(data):
    """
    Outputting data got from sheets to screen
    """
    choice_str = []
    choice_num_list = []
    for value in range(len(data)-1):
        while True:
            question_row = data[value+1]
            print(f"\n\nQuestion {question_row[0]}")
            print(f"{question_row[1]}\n")
            print("Please enter the number of your choice from 1-4.\n")
            print(f"1: {question_row[2]} 2: {question_row[3]} "
                  f"3: {question_row[4]} 4: {question_row[5]}\n")
            data_str = input("Enter your choice here:\n")

            if validate_data(data_str):
                print("Thank you")
                break

        choice_str.append(question_row[int(data_str)+1])
        choice_num_list.append(int(data_str))

    return choice_num_list, choice_str


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
        return False

    return True


def output_choices(choice_str):
    """
    Outputs to screen choices made by user
    """
    print("\nYou made the following choices:")
    for i in range(len(choice_str)):
        print(f"Question {i+1}: {choice_str[i]}")


def update_results_data(choice_num_list):
    """
    Update results from sheet and out put to screen
    """
    print("\nUpdating results worksheet. Results will follow.")
    results = SHEET.worksheet("results").get_all_records()
    row_data = []
    current_results_data = []
    worksheet_to_update = SHEET.worksheet("results")
    worksheet_to_update.delete_rows(2, len(choice_num_list)+1)
    for value in range(len(choice_num_list)):
        row = results[value]
        choice_num = choice_num_list[value]
        updated_row = update_results_row(choice_num, row)
        row_data = list(updated_row.values())
        current_results_data.append(row_data)
        worksheet_to_update.append_row(row_data)
    return current_results_data


def update_results_row(choice_num, row):
    """
    Cycle throug choice numbers and increment corresponding
    value in dictionary
    """
    if (choice_num == 1):
        key = "Answer 1"
        row[key] += 1
        return row
    elif (choice_num == 2):
        key = "Answer 2"
        row[key] += 1
        return row
    elif (choice_num == 3):
        key = "Answer 3"
        row[key] += 1
        return row
    elif (choice_num == 4):
        key = "Answer 4"
        row[key] += 1
        return row
    else:
        print("Invalid Data")


def calculate_totals(current_results_data, data):
    """
    Calculate total participants and corresponding % to choices
    """
    data_row = []
    data_row = current_results_data[0]
    total = sum(data_row)-1
    print(f"\n{total} people have participated in this survey to date\n")
    for value in range(len(data)-1):
        data_row = current_results_data[value]
        question_row = data[value+1]
        print(f"Results for Question {question_row[0]}")
        print(question_row[1])
        print(f"1: {question_row[2]} {round((data_row[1]/total)*100)}% "
              f"2: {question_row[3]} {round((data_row[2]/total)*100)}% "
              f"3: {question_row[4]} {round((data_row[3]/total)*100)}% "
              f"4: {question_row[5]} {round((data_row[4]/total)*100)}%\n")


def main():
    """
    This is the main function which runs all functions
    """
    data = get_questions_data()
    total_questions = calculate_question_total(data)
    get_results_sheet_data()
    print("Welcome to my Coder Survey\n")
    print(f"Please answer the following {total_questions} questions\n")
    print("Results of Survey will be posted to screen after final question\n")
    choice_num_list, choice_str = questions_output(data)
    output_choices(choice_str)
    current_results_data = update_results_data(choice_num_list)
    calculate_totals(current_results_data, data)
    print("\nThank you for your participation.")


main()
