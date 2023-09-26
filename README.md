# Telegram-Json-To-Whatsapp-txt

This program converts a chat exported from Telegram to Whatsapp format, so that Telegram can import it later.

For the program to work, follow the steps below:

1 - Export the chat from Telegram Desktop;
2 - Go to the export location and follow: Telegram Desktop/ChatExport_'date'/
3 - Make a copy of the result.json file
4 - Make sure both converter.py and result.json file are at the same folder
5 - Run converter.py
6 - The program will ask for the name of the contact from the first message. It can be found opening the result.json file and searching for the 11th line, as something like ' "from": "contact_name", '
7 - The program will ask for the contact id from the first message. It can be found found opening the result.json file and searching for the 12th line, as something like ' "from_id": "contact_id", '
8 - Do the same for the second contact (you) as the program asks
9 - Wait until the program finish and generate a whatsapp.txt file
