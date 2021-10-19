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

# for testing
print(sorted(new_list))

# print how many emails are present in the list
print("There are " + str(len(new_list)) + " unique emails in your list." )

# open file for writing new email list
updated_email_list = open('updatedjazzhangsemails.txt', 'w')

# sort(alphabetize) list and format for use in gmail, then write new list to file
updated_email_list.write(str(sorted(new_list)).replace(",", ";").replace("'", ""))