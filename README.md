# remove-duplicate-emails
A short Python program to compile email lists and remove duplicate emails. Also accepts new emails through user input.

Code Louisville Requirements met:
1) Implement a “master loop” console application where the user can repeatedly enter
commands/perform actions, including choosing to exit the program.
- User may enter new email addresses, which are appended to the email list (Lines 46-55)

2) Create a dictionary or list, populate it with several values, retrieve at least one value, and
use it in your program.
- Created a list (Line 57: "new_list") which is populated from user input of new emails plus the retrieval of emails from two .txt files, which are split into list items at the commas. Values are retrieved from new_list when they are printed at the end (Line 60) and when they are written to a new file (Line 71)

3) Read data from an external file, such as text, JSON, CSV, etc and use that data in your
application.
- Read data from two .txt files (Lines 5 and 6). Used data to create new_list (Line 57). Wrote new_list, formatted with semi-colons instead of commas, to a new .txt file(Line 71).

4) Analyze text and display information about it (ex: how many words in a paragraph).
- Analyzed the length of new_list and display how many emails it holds(Line 63).

Planning to implement a regex to check that the user-entered emails are in the correct format.
Will soon add capability for user to import their own file, for which I will can include error handling and write the invalid inputs/important events to a .txt file.
Also planning to get the current date and append it to the new file (containing the email list) when it's written so the user knows when it was created.