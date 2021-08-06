# Imports required modules
import pyautogui
import time

# List of payloads
the_bee_movie = open("Payloads/beemovie.txt", 'r')
shrek = open("Payloads/shrek.txt", 'r')
shrek2= open("Payloads/shrek2.txt", 'r')
shrek3 = open("Payloads/shrek3.txt", 'r')

# Input
payload = input("""Select a number for your payload to spam with:
1: The Bee Movie script
2: The Shrek script
3: The Shrek 2 script
4: The Shrek 3 script
""")


# Name pretty self explainatory. Used this function so I won't have to keep writing the same code over and over again
def launch_payload(set_payload):
    time.sleep(5)
    for word in set_payload:
        pyautogui.typewrite(word)
        pyautogui.press('enter')

# Configuring payloads, then launching them
if payload == "1":
    launch_payload(the_bee_movie)
elif payload == '2':
    launch_payload(shrek)
elif payload == '3':
    launch_payload(shrek2)
elif payload == '4':
    launch_payload(shrek3)
else:
    print("Invalid payload")