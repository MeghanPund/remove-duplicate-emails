email_file = open('/Users/Brazuka/Desktop/RemoveDuplicateEmails/jazzhangsemails.txt', 'r')
email_file2 = open('/Users/Brazuka/Desktop/RemoveDuplicateEmails/campmerlotemails.txt', 'r')

content = email_file.read() + email_file2.read()

email_list = content.lower().split(',')

new_list = []

for email in email_list:
    if email not in new_list:
        new_list.append(email.strip())

# new_list = list(set(new_list))

print(sorted(new_list))

update_email_list = open('/Users/Brazuka/Desktop/RemoveDuplicateEmails/updatedjazzhangsemails.txt', 'w')

update_email_list.write(str(sorted(new_list)).replace(",", ";").replace("'", ""))

email_file.close()