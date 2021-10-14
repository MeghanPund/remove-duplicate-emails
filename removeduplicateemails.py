email_file = open('/Users/Brazuka/Desktop/RemoveDuplicateEmails/jazzhangsemails.txt', 'r')
email_file2 = open('/Users/Brazuka/Desktop/RemoveDuplicateEmails/campmerlotemails.txt', 'r')

# compile lists
content = email_file.read() + email_file2.read()

# all characters lowercase, split at commas (,)
email_list = content.lower().split(',')

# this will be the compiled list
new_list = []

# remove duplicate emails
for email in email_list:
    if email not in new_list:
        new_list.append(email.strip())

# for testing
print(sorted(new_list))

# write new list to file
update_email_list = open('/Users/Brazuka/Desktop/RemoveDuplicateEmails/updatedjazzhangsemails.txt', 'w')

# sort(alphabetize) list and format for use in gmail
update_email_list.write(str(sorted(new_list)).replace(",", ";").replace("'", ""))

email_file.close()