# remove-duplicate-emails
## Program Description
A short Python program to compile email lists and remove duplicate emails. Also accepts new emails through user input.

## How to Run It
1. Open a terminal or your favorite code editor (like VS Code) that has a built in terminal.
2. Clone the GitHub repository to your computer by typing `git clone https://github.com/MeghanPund/remove-duplicate-emails` 
into the command line/terminal.
3. Change (cd) to the root directory of the cloned repository and enter `python removeduplicateemails.py`

## Code Louisville Requirements met:
 **1) Implement a “master loop” console application where the user can repeatedly enter
 commands/perform actions, including choosing to exit the program.**
- User may enter new email addresses, which are appended to the email list. User enters q to quit.

 **2) Create a dictionary or list, populate it with several values, retrieve at least one value, and
 use it in your program.**
- Created a list "new_list" which is populated with user input of new emails plus the retrieval of emails 
from multiple .txt files, which are split into list items at commas. 
Values are retrieved from new_list when they are printed at the end of the program and when they are written to a new file.

 **3) Read data from an external file, such as text, JSON, CSV, etc and use that data in your application.**
- Read data from .txt files (Including user input .txt files). Used data to create new_list. Wrote new_list, 
formatted with semi-colons instead of commas, to a new .txt file.

 **4) Analyze text and display information about it (ex: how many words in a paragraph).**
- Analyzed the length of new_list and display how many emails it holds.

 **5) Implement a log that records errors, invalid inputs, or other important events and writes
them to a text file.**
- When the user makes errors inputting their email list filepath, the errors are written to error_log.txt

 **6) Implement a regular expression (regex) to ensure a field either a phone number or an
email address is always stored and displayed in the same format.**
- Check if emails input by user are valid with re.fullmatch(). If they are not, prompt user to re-enter email address correctly.

## Future Additions
