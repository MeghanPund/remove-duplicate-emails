import re
from datetime import datetime


# open files for reading (r) and appending (a)
email_file = open('dummyemaillist.txt', 'r')
email_file2 = open('dummyemaillist2.txt', 'r')
error_log = open('error_log.txt', 'a')

# log error to .txt file with date+time stamp
def write_error_to_log(error=str):
    
    error_log = open('error_log.txt', 'a')
    error_date = str(datetime.now())
    error_log.write(error_date + ' ' + error + '\n')
    error_log.close()

    return error_date, error

# option for user to import email list
def get_user_email_list():
    
    global email_list
    # all characters lowercase, split at commas (,)
    email_list = (email_file.read() + email_file2.read()).lower().split(',')
    does_user_have_list = input("Do you have an email list formatted as a .txt file that you would like to import? Enter Y for yes or N for no: ").upper()
        
    if does_user_have_list == "Y":
        while does_user_have_list:
            user_email_list = str(input("Enter the filepath to your email list: "))
            try:
                user_email_file = open(user_email_list, 'r')
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

    # close the O.G. email list files
    email_file.close()
    email_file2.close()
    if 'user_email_file' in globals(): user_email_file.close()

    return email_list

# called it
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

# accept new emails as input
def get_new_email():
    global user_input
    # regex string checks for a string of digits, characters, and/or numbers 
    # followed by the @ symbol, followed by another string (the email domain), 
    # followed by ., followed by the last string
    valid_email = re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', user_input)

    if valid_email != None:
        if user_input not in new_list:        
            new_list.append(user_input)
            print(f'{user_input} added')               
        elif user_input in new_list:
            print("Sorry. This email already exists.")
    elif valid_email == None:
            print("Invalid email entry. Try again.")
    user_input = input("Add another new email or enter q to quit: ").lower().strip()       
    return new_list

# master loop to add new emails to email list
while adding_emails:
    if user_input == "q" or user_input == "quit":
        adding_emails == False
        break
    elif user_input != "q" or "quit":
        get_new_email()
        continue
    else:
        print("Invalid input.")
        continue

new_list = sorted(list(set(new_list)))

# for testing
print(new_list)

# print how many emails are present in the list
print(f"There are {str(len(new_list))} unique emails in your list." )

# open file for writing new email list
new_file_name = input("What would you like your new email list to be called?: ")
updated_email_list = open(str(new_file_name) + '.txt', 'x')

# sort(alphabetize) list and format for use in gmail, then write new list to file
updated_email_list.write(str(new_list).replace(",", ";").replace("'", ""))
print(f"You just created a new file called {new_file_name}.txt! Your new email list is saved there.")