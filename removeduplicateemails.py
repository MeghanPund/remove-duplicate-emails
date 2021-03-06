import re
from datetime import datetime


def write_error_to_log(error):
    '''Log error to .txt file with datetime stamp'''
    with open('error_log.txt', 'a') as error_log:
        error_date = str(datetime.now())
        error_log.write(f'{error_date} {error}\n')

    return error_date, error


def get_user_email_list():
    '''
    Option for user to import email list.
    Prompts user to input whether or not they've got an email list,
    then takes filepath to list (if present) and reads it into
    the program. After importing list or if no list, prompts next phase of program,
    which is to enter individual emails.
    '''
    global email_list
    # all characters lowercase, split at commas (,)
    does_user_have_list = input("Do you have an email list formatted as a .txt file that you would like to import? Enter Y for yes or N for no: ").upper()

    if does_user_have_list == "Y":
        while does_user_have_list:
            user_email_list = str(input("Enter the filepath to your email list: "))
            try:
                with open(user_email_list, 'r') as user_email_file:
                    email_list = email_list + user_email_file.read().lower().split(',')
                print(f"Your list at {user_email_list} was added!")
            except FileNotFoundError:
                print("Oops - try entering your filepath again.")
                write_error_to_log('FileNotFoundError')
            except UnicodeDecodeError:
                print("Sorry. We can currently only accept text files with utf8 formatting.")
                write_error_to_log('UnicodeDecodeError')
            except ValueError:
                print("I/O operation on closed file.")
                write_error_to_log('ValueError')
            break
    elif does_user_have_list == "N":
        print("No email list imported. Proceed to enter individual emails.")
    else:
        print("Invalid input.")
        get_user_email_list()

    return email_list


with open('dummyemaillist.txt', 'r') as email_file:
    with open('dummyemaillist2.txt', 'r') as email_file2:
        email_list = (email_file.read() + email_file2.read()).lower().split(',')
        get_user_email_list()

# this will be the compiled email list
new_list = []

# remove duplicate emails and strip list items of whitespace
for email in email_list:
    if email not in new_list:
        new_list.append(email.strip())
    elif email in new_list:
        print(f"{email} appeared in multiple email lists. The duplicate has been removed.")
        continue

# program variables
adding_emails = True
user_input = input("Welcome to the email list deduplicator! Add a new email or enter q to quit: ").lower().strip()


def get_new_email():
    '''
    Accepts new emails as user input.
    Prompts user for input of new emails, one by one,
    to be added to list. When user has entered input,
    a regex statement checks the formatting of the input
    and returns an error if incorrect, along with a prompt
    to retype the input.
    '''
    global user_input
    # regex string checks for a string of digits, characters, and/or numbers
    # followed by the @ symbol, followed by another string (the email domain),
    # followed by ., followed by the last string
    valid_email = re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', user_input)

    if valid_email is not None:
        if user_input not in new_list:
            new_list.append(user_input)
            print(f'{user_input} added')
        elif user_input in new_list:
            print("Sorry. This email already exists.")
    elif valid_email is None:
        print("Invalid email entry. Try again.")
    user_input = input("Add another new email or enter q to quit: ").lower().strip()
    return new_list


# master loop to add new emails to email list
while adding_emails:
    if user_input == "q" or user_input == "quit":
        adding_emails is False
        break
    elif user_input != "q" or "quit":
        get_new_email()
        continue
    else:
        print("Invalid input.")
        continue

new_list = sorted(list(set(new_list)))

# for testing
print(f'The emails currently in your list are: {new_list}')

# print how many emails are present in the list
print(f"There are {str(len(new_list))} unique emails in your list.")

# open file for writing new email list
new_file_name = input("What would you like your new email list to be called?: ")
updated_email_list = open(str(new_file_name) + '.txt', 'x')

# sort(alphabetize) list and format for use in gmail, then write new list to file
updated_email_list.write(str(new_list).replace(",", ";").replace("'", ""))
print(f"You just created a new file called {new_file_name}.txt! Your new email list is saved there.")
