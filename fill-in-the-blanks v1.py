# IPND Stage 2 Final Project

# I found this project might frustrating and had to borrow liberally from the forums in order to get this to function.
# In the end, I have something that works :-)

# Define the quiz levels and their content

level_easy = "Stephen Curry wears number: __1__. Kevin Durant wears number: __2__. Draymond Green wears number: __3__. Klay Thompson wears number: __4__."
answers_easy = ["30", "35", "23", "11"]

level_medium = "Shaun Livingstone wears number: __1__. Zaza Pachulia wears number: __2__. Andre Iguodala wears number: __3__. David West wears number: __4__."
answers_medium = ["34", "27", "9", "3"]

level_hard = "JaVale McGee wears number: __1__. Nick Young wears number: __2__. Patrick McCaw wears number: __3__. Quin Cook wears number: __4__."
answers_hard = ["1", "6", "0", "4"]

questions = ["__1__", "__2__", "__3__", "__4__"]

# Level selection

def choose_level():
    print "Let's see how much you know about the Golden State Warriors. Please choose a level: Easy, Medium, Hard"
    level_name = raw_input("Type in: Easy, Medium or Hard\n").lower()

    if level_name == "easy":
        paragraph(level_easy, questions, answers_easy)

    elif level_name == "medium":
        paragraph(level_medium, questions, answers_medium)

    elif level_name == "hard":
        paragraph(level_hard, questions, answers_hard)

    else:
        print "I don't understand. Please start again.\n"
        return choose_level()

# Starts the quiz

# change the while loop to a FOR loop

def paragraph(quiz, blanks, answers):
    max_attempts = 5
    attempts = 0

    print "You have " + str(max_attempts) + " attempts. Here we go!\n"

    print quiz

    for count_blanks in range(0, len(blanks)):
        answer_input = raw_input("\nWhat number is " + blanks[count_blanks] +"?  ")

        while answer_input != answers[count_blanks]:
            attempts += 1
            answer_input = raw_input("Nope. " + str(max_attempts - attempts) + " attempts remaining. What number is" + blanks[count_blanks] + "?  ")

            if answer_input == answers[count_blanks]:
                quiz = quiz.replace(blanks[count_blanks], answers[count_blanks])
                print("Correct!  " + quiz)

            else:
                if attempts == max_attempts:
                    print ("Looks like you don't know the Warriors that well :-( Want to play again Y/N?\n")
                    if raw_input().lower == "y":
                        choose_level()
                    else:
                        print "Close the program. Bye"
            
    if len(blanks) == len(answers):
        print ("\nYou know the Warriors. Good for you. Want to play again? Y/N?\n")
        if raw_input().lower == "y":
            choose_level()
        else:
            print "Close the program. Bye"

choose_level()
