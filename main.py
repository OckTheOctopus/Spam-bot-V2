# Imports required modules
import pyautogui
import time
import sys

def main():
    # List of payloads
    the_bee_movie = open("Payloads/beemovie.txt", 'r')
    shrek = open("Payloads/shrek.txt", 'r')
    shrek2= open("Payloads/shrek2.txt", 'r')
    shrek3 = open("Payloads/shrek3.txt", 'r')

    # Names pretty self explanatory.
    def launch_movie(set_payload, delay):
        time.sleep(delay)
        for word in set_payload:
            pyautogui.typewrite(word)
            pyautogui.press('enter')

    def launch_custom_movie(filepath, delay):
        file = open(filepath, 'r')
        for word in file:
            pyautogui.typewrite(word)
            pyautogui.press('enter')

    def launch_movie_config(movie_name, movie):
        time_delay = input(f"You have selected {movie_name}. There will be a delay before the script launches so you will have time to find a place to input text. If at any point you would like to exit the script, return here to the terminal and run CONTROL + 'C'. How long would you like the delay to be (in seconds - make sure it is an integer):\n")
        try:
            time_delay = int(time_delay)
            if time_delay < 0:
                print("Uh-oh, looks like something broke on our end. Make sure you typed in a positive integer")
                sys.exit()
        except:
            print("Uh-oh, looks like something broke on our end. Make sure you typed in a positive integer")
            sys.exit()
        print("Running script. Have fun!")
        if movie_name == "CUSTOM FILE":
            launch_custom_movie(movie, time_delay)
        else:
            launch_movie(movie, time_delay)
        print("File ended.")

    # Using copypasta mode or movie script mode
    print("Welcome to Ock's spamming script! Designed to make your friends' lives hell! Use wisely; you only get banned once!")
    while True:
        selection = input("""Type in the corresponding number to select which spamming mode you would like to enter:
1: Movie script
2: Copypasta
3: 100 bottles of beer
4: Help
5: Exit
    """)
        if selection == '1':
            print("Good choice. Type in the number that corresponds to the movie you would like to select.")
            while True:
                movie_payload = input("""Please select one of the options from below:
1: The bee movie script
2: The Shrek script
3: The Shrek 2 script
4: The Shrek 3 script
5: Help
6: Exit
    """)
                if movie_payload == '1':
                    launch_movie_config("THE BEE MOVIE SCRIPT", the_bee_movie)
                elif movie_payload == '2':
                    launch_movie_config("THE SHREK SCRIPT", shrek)
                elif movie_payload == '3':
                    launch_movie_config("THE SHREK 2 SCRIPT", shrek2)
                elif movie_payload == '4':
                    launch_movie_config("THE SHREK 3 SCRIPT", shrek3)
                elif movie_payload == '5':
                    print("""1: Sends the entire bee movie script. It sends it line by line.
        2: Sends the entire Shrek script. It sends it line by line.
        3: Sends the entire Shrek 2 script. It sends it line by line.
        4: Sends the entire Shrek 3 script. It sends it line by line.
        5: Displays this message.
        6: Exits the script.
        """)
                elif movie_payload == '6':
                    print("Thanks for using!")
                    sys.exit()
                break
        elif selection == '2':
            print("Excellent choice. Unfortunately at this time there are no built in choices for you to use. You will have to supply your own.")
            copypasta_text = input("Please enter your copypasta text.\n")
            loop_num = input("Please enter the number of times you would like this to be sent (make sure it is an integer greater than 0).\n")

            try:
                loop_num = int(loop_num)
                if loop_num < 1:
                    print("Uh-oh! Please make sure you enter an integer larger than 1! Run the script and try again.")
                    sys.exit()
            except:
                print("Uh-oh! Something broke on our end. Please make sure you typed in an integer greater than 1! Run the script and try again.")
                sys.exit()

            interval_delay = int(input("How long would you like the delay to be (in seconds) in between messages? (Hit enter)\n"))

            time.sleep(interval_delay)
            for i in range(loop_num + 1):
                pyautogui.typewrite(copypasta_text)
                pyautogui.press("enter")

        elif selection == '3':
            beverage = input("Select your beverage:\n")

            try:
                time_delay = int(input("How long would you like to wait (in seconds) before the spamming starts?\n"))
                if time_delay < 0:
                    print("Uh-oh, looks like something broke on our end. Make sure you typed in a positive integer")
                    sys.exit()
            except:
                print("Uh-oh, looks like something broke on our end. Make sure you typed in a positive integer")
                sys.exit()

            time.sleep(time_delay)
            for i in range(3, -1, -1):
                if i > 1:
                    pyautogui.typewrite(f"{i} bottles of {beverage} on the wall,")
                    pyautogui.press('enter')
                    pyautogui.typewrite(f"{i} bottles of {beverage} on the wall,")
                    pyautogui.press('enter')
                    pyautogui.typewrite("You take one down and pass it around,")
                    pyautogui.press('enter')
                    pyautogui.typewrite(f"{i-1} bottles of {beverage} on the wall.")
                    pyautogui.press('enter')
                elif i == 1:
                    pyautogui.typewrite(f"{i} bottle of {beverage} on the wall,")
                    pyautogui.press('enter')
                    pyautogui.typewrite(f"{i} bottle of {beverage} on the wall,")
                    pyautogui.press('enter')
                    pyautogui.typewrite("You take one down and pass it around,")
                    pyautogui.press('enter')
                    pyautogui.typewrite(f"No bottles of {beverage} on the wall.")
                    pyautogui.press('enter')
                else:
                    pyautogui.typewrite(f"No bottles of {beverage} on the wall,")
                    pyautogui.press('enter')
                    pyautogui.typewrite(f"No bottles of {beverage} on the wall,")
                    pyautogui.press('enter')
                    pyautogui.typewrite("You go to the store and buy some more,")
                    pyautogui.press('enter')
                    pyautogui.typewrite(f"100 bottles of {beverage} on the wall.")
                    pyautogui.press('enter')
        elif selection == '4':
            # Help message
            print("""1: Launches an entire movie-sized chunk of text once - it reads every line then hits enter until the end of the file to avoid character limits.
2: Sends a copypasta-sized chunk of text (normally <1500 characters) repeatedly in the same message to wreak havoc.
3: Displays this message.
4: Exits the script
    """)
        elif selection == '5':
            print("Thanks for using!")
            sys.exit()
        else:
            print("Invalid input. Try typing in '1' (without the quotation marks)")

if __name__ == "__main__":
    main()