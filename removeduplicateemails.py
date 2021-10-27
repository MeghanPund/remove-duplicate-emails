from os import close, read, remove
import re
from typing import Text
import logging
from datetime import date, datetime

# logging config
logging.basicConfig(filename='error_log.txt', format='%(asctime)s %(message)s', encoding='utf-8', level=logging.DEBUG)

# open for reading
email_file = open('jazzhangsemails.txt', 'r')
email_file2 = open('campmerlotemails.txt', 'r')
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
                email_list = email_list + user_email_file.read()        
                print(sorted(list(set(email_list))))
                print("Your list at " + user_email_list + " was added!")
            except FileNotFoundError:
                print("Oops - try entering your filepath again.")
                write_error_to_log('FileNotFoundError')
            except UnicodeDecodeError:
                print("Sorry. We can currently only accept text files with utf8 formatting.")
                write_error_to_log('UnicodeDecodeError')
            except ValueError:
                print("I/O operation on closed file.")
                write_error_to_log('ValueError')
            else:
                print("Something went wrong.")
                write_error_to_log('UnknownError')
                break
                 
    elif does_user_have_list == "N":
        # compile lists
        print("No email list imported. Proceed to enter individual emails.")        
    else:
        print("Invalid input.")
        get_user_email_list()

    # close the O.G. email list files
    email_file.close()
    email_file2.close()
    if 'user_email_file' in globals(): user_email_file.close()

# called it
get_user_email_list()

# this will be the compiled list
new_list = []

# remove duplicate emails and strip list items of whitespace
for email in email_list:
    if email not in new_list:
        new_list.append(email.strip())

# program variables
adding_emails = True
user_input = input("Welcome to the email list deduplicator! Add a new email or enter q to quit: ").lower().strip()

# accept new emails as input !! ADD REGEX TO CHECK EMAIL FORMAT !!
def get_new_email():
    global user_input
    if user_input not in new_list:
        new_list.append(user_input)
        print("You just added: " + user_input)
        user_input = input("Add another new email or enter q to quit: ").lower().strip()
        return        
    elif user_input in new_list:
        print("Sorry. This email already exists.")
        user_input = input("Add another new email or enter q to quit: ").lower().strip()


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
print("There are " + str(len(new_list)) + " unique emails in your list." )

# open file for writing new email list
new_file_name = input("What would you like your new email list to be called?: ")
updated_email_list = open(str(new_file_name) + '.txt', 'x')

# sort(alphabetize) list and format for use in gmail, then write new list to file
updated_email_list.write(str(new_list).replace(",", ";").replace("'", ""))
print("You just created a new file called " + str(new_file_name) + ".txt! Your new email list is saved there.")