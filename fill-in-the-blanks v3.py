# IPND Stage 2 Final Project
# jacobscottanthony@gmail.com

""" Define the paragraphs and answers as strings and lists respectively """

level_easy = "Stephen Curry wears number: __1__. Kevin Durant wears number: __2__. Draymond Green wears number: __3__. Klay Thompson wears number: __4__."
answers_easy = ["30", "35", "23", "11"]

level_medium = "Shaun Livingstone wears number: __1__. Zaza Pachulia wears number: __2__. Andre Iguodala wears number: __3__. David West wears number: __4__."
answers_medium = ["34", "27", "9", "3"]

level_hard = "JaVale McGee wears number: __1__. Nick Young wears number: __2__. Patrick McCaw wears number: __3__. Quin Cook wears number: __4__."
answers_hard = ["1", "6", "0", "4"]

questions = ["__1__", "__2__", "__3__", "__4__"]

""" choose_level, selects the level the user will play using nested ifs"""

def choose_level():
    print "Let's see how much you know about the Golden State Warriors. Please choose a level: Easy, Medium, Hard"
    level_name = raw_input("\n Type in: Easy, Medium or Hard \n").lower()

    if level_name == "easy":
        play(level_easy, questions, answers_easy)

    elif level_name == "medium":
        play(level_medium, questions, answers_medium)

    elif level_name == "hard":
        play(level_hard, questions, answers_hard)

    else:
        print "I don't understand. Please start again.\n"
        return choose_level()

""" restart is used to cut down lines in the play function as it was repeated twice in play. it takes the input from user to
decide if we restart the game or exit """

def restart():
    if raw_input() == "Y":
        choose_level()
    else:
        print "Close the program. Bye"
        exit()

""" play uses three variables to run through the game. max_attempts in not user assignable and is set at 5 per item. for and while
loops used to loop through all possible positions in questions parameter. paragraph is printed each time a correct answer is entered.
number of attempts remaining displayed each time an incorrect answer is entered
game ends if max_attempts reached or all answers are correct. User is then prompted to play again """

def play(quiz, blanks, answers):
    max_attempts = 5
    
    print "You have " + str(max_attempts) + " attempts. Here we go!\n"

    for answer_number in range(0, len(blanks)):
        current_guess = 0
        answer = answers[answer_number]
        key = '__{}__'.format(answer_number + 1)
        
        while current_guess < max_attempts:
            print quiz
            guess = raw_input("What number is: " + key + "  ")
            if guess == answer:
                print '\nCorrect!\n'
                quiz = quiz.replace(key, answer)
                break
            current_guess += 1
            print "\nYou have " + str(max_attempts - current_guess) + " attemps remaining.\n"

        if current_guess == max_attempts:
            print "Hit the showers, you don't know the Warriors. Want to play again? Y/N?\n\n"
            restart()
            
    print quiz + '\n' + "\nYou win! Want to play again? Y/N\n\n"
    restart()

choose_level()
