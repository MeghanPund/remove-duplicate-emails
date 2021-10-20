from os import remove
import re

# open files for reading
email_file = open('jazzhangsemails.txt', 'r')
email_file2 = open('campmerlotemails.txt', 'r')

# compile lists
email_list = email_file.read() + email_file2.read()

# close the O.G. email list files
email_file.close()
email_file2.close()

# all characters lowercase, split at commas (,)
email_list = email_list.lower().split(',')

# this will be the compiled list
new_list = []

# remove duplicate emails and strip list items of whitespace
for email in email_list:
    if email not in new_list:
        new_list.append(email.strip())

# program variables
adding_emails = True
user_input = input("Add a new email or enter q to quit: ").lower().strip()

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
updated_email_list = open('updatedjazzhangsemails.txt', 'w')

# sort(alphabetize) list and format for use in gmail, then write new list to file
updated_email_list.write(str(new_list).replace(",", ";").replace("'", ""))