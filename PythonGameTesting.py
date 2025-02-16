number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

import random

play = 0
winner = False

def print_grid(grid):
    for row in grid:
        print(row)

def check_winner(grid, user):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if all(cell == user for cell in grid[i]):  # Check rows
            return True
        if all(grid[j][i] == user for j in range(3)):  # Check columns
            return True
    if all(grid[i][i] == user for i in range(3)):  # Check main diagonal
        return True
    if all(grid[i][2 - i] == user for i in range(3)):  # Check anti-diagonal
        return True
    return False

def is_cell_empty(grid, x, y):
    return isinstance(grid[y][x], int)

while True:
    try:
        ChooseTeam = input("Which team would you like to choose (X or O)? : ").upper()
        if ChooseTeam != "X" and ChooseTeam != "O":
            raise ValueError
        else:
            break
    except ValueError:
        print("Invalid input. Please try again.")

user = ChooseTeam
computer = "X" if user == "O" else "O"

while play < 9 and not winner:
    print_grid(number_grid)

    # Bot's move
    while True:
        botXCoordinate = random.randint(0, 2)
        botYCoordinate = random.randint(0, 2)
        if is_cell_empty(number_grid, botXCoordinate, botYCoordinate):
            number_grid[botYCoordinate][botXCoordinate] = computer
            break

    print("Bot's move:")
    print_grid(number_grid)

    if check_winner(number_grid, computer):
        print("Computer wins!")
        winner = True
        break

    play += 1

    if play >= 9:
        break

    # Player's move
    while True:
        try:
            userXCoordinate = int(input("Enter the x coordinate where you want to go (0-2): "))
            userYCoordinate = int(input("Enter the y coordinate where you want to go (0-2): "))
            if userXCoordinate < 0 or userXCoordinate > 2 or userYCoordinate < 0 or userYCoordinate > 2:
                print("Coordinates out of range. Please enter values between 0 and 2.")
            elif not is_cell_empty(number_grid, userXCoordinate, userYCoordinate):
                print("This space has already been played. Enter another coordinate.")
            else:
                number_grid[userYCoordinate][userXCoordinate] = user
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if check_winner(number_grid, user):
        print("You win!")
        winner = True
        break

    play += 1

if not winner:
    print("It's a tie!")




#2D Lists (Grid with columns and rows) - Tic-Tac-Toe Game
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

import random

play = 0
winner = False

while True:
    try:
        ChooseTeam = input("Which team would you like to choose (X or O)? : ").upper()
        if ChooseTeam != "X" and ChooseTeam != "O":
            raise ValueError
        else:
            break

    except ValueError:
        print("Invalid input. Please try again.")


def check_winner(number_grid, user):
        for i in range(3):
            if all(cell == user for cell in number_grid[i]):  # check if the row is complete
                return True
            if all(number_grid[j][i] == user for j in range(3)):  # check if the column is complete
                return True
            if all(number_grid[i][2 - i] == user for i in range(3)):
                return True
            return False

while(play < 9 and not winner):

    if ChooseTeam == "X":
        user = "X"
        computer = "O"

    else:
        user = "O"
        computer = "X"


    botXCoordinate = [0, 1, 2]
    botYCoordinate = [0, 1, 2]
    if number_grid[botXCoordinate][botYCoordinate] == int:
        number_grid[random.choice(botXCoordinate)][random.choice(botYCoordinate)] = computer

    for col in number_grid:
        print(col)

    while True:
        try:
            userXCoordinate = int(input("Enter the x coordinate where you want go: "))
            if userXCoordinate < 0 or userXCoordinate > 2:
                raise ValueError

            #elif user == computer:
             #   print("This space has already been played.\n Enter another coordinate.")

            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        try:
            userYCoordinate = int(input("Enter the y coordinate where you want go: "))
            if userYCoordinate < 0 or userYCoordinate > 2:
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


    number_grid[userYCoordinate][userXCoordinate] = user

    if check_winner(number_grid, user):
        print("You win!")
        winner = True

    play += 1



#List all prime numbers
for i in range (2, 100):
    for j in range (2, i):
        if i % j == 0:
            print(f"{i} is not a prime number")
            break

        else:
            if j == i-1:
                print(f"{i} is a prime number")


words = "whatsoever"
print("Welcome to Hangman!")
play = "y"
guessed_letters = []
other_letters = []
while play == "y":
    for i in words:
        if i in guessed_letters:
            print(i, end=' ')

        else:
            print('_', end=' ')

    print("\n")
    while True:
        try:
            guess = input("Guess a letter: ")
            if guess.isalpha() and len(guess) == 1:
                break
            else:
                raise ValueError

        except ValueError:
            print("Invalid input. Please enter a letter from a-z")

    if guess in words:
        guessed_letters.append(guess)  # Add the correctly guessed letter to the correct list

    if guess in other_letters:
        other_letters.append(guess)


    for w in words:
        if w in guessed_letters:
            print(w, end=' ')

        else:
            print('_', end=' ')

    print('\n')
    print(guess, end='')
    print('\n')

    print("\nIncorrect guesses:", ', '.join(other_letters))

    play = input("Continue playing? (y, n): ")


def Location(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y) if x > y:       #guard: if x > y execute the case, if not then move to next case
            print(f"X={x}, Y={y}")
        case (x, y) if x < y:  # guard: if x < y execute the case, if not then move to next case
            print(f"X={x}, Y={y}--")
        case _:
            ValueError("Not a point")

print(Location((5, 6)))

def Calculator (n1, op, n2):
    answer = 0
    match op:
        case '+':
            answer = n1 + n2
        case '-':
            answer = n1 - n2
        case '*':
            answer = n1 * n2
        case '/':
            if n2 == 0:
                print("You can't divide by zero")
            else:
                answer = n1 / n2
    return answer

num1 = (float(input("Enter first number: ")))
operator = (input("Enter operand: "))
num2 = (float(input("Enter second number: ")))
result = (Calculator(num1, operator, num2))
print("the answer is: ", result)

character_name = "matthew"
print((character_name.index("h")))
print(len(character_name))
print(character_name.replace("ew", "hat"))
#len = function for length (ex: len(variable_name))
#[] for isolating value at specified index (ex: variable_name[2])
#index = function for counting (ex: variable_name.index)

from math import *
my_num = -100
print(pow(my_num, 3))
print(ceil(4.5))
print(floor(4.5))


#lists - a structure that can store information
#mutable - can change
numbers = [23, 2, 1, 43, 7]
friends = ["Mark", "Matthew", "Luke", "John"]
print(friends[1:3])
#[#:#] - include number between left and right number (not including number)
friends.reverse()
print(friends)
numbers.sort()
print(numbers)

#tuples - a structure that can store information
#syntax - ex:coordinates = (4,5)
#immutable - can't be changed (think c++ constants)
coordinates = (66, 34)
print(coordinates[0])


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3
print(max_num(2, 9, 3))

friends = ["Halpert", "Mark", "Matthew"]
for index in range(7):
    print(friends)

for index in range(1):
    print(index)
    if index == 0:
        print("first iteration\n")


#exponent function
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
print(raise_to_power(2, 4))


#How to build a translator
#TODO: vowels -> g
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation


#print(translate(input("Enter a phrase: ")))

try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
#do not have except by itself (too vague)
#except [specific error]
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("Invalid input")

'''
Test_file = open("Test.txt", "a")
Test_file.write("Toby - Human Resources")
print(Test_file.readable()) #test if file is readable
print("\n ")
# Open the file for reading
with open("Test.txt", "r") as file:
    # Read the entire file content
    content = file.read() #readlines()[0] for singular line
    print(content)

#print(Test_file.read)
#open("Test.py", "r+")
#open("Test.py", "w") //overwrites existing file or creates new file
#open("Test.py", "a")

import UsefulTools

print(UsefulTools.roll_dice(10))
'''

print("\n")

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b

for num in range(2, 10):
    if num % 2 == 0:
        print(f"Found an even number {num}") #add f before string to include variables
    else:
        print(f"Found an odd number {num}")

for n in range(2, 10):      #loops through all values from 2 to 10
    for x in range(2, n):       #loops through all values again
        if n % x == 0:                      #checks that each value is divisible by some other value from 2 to 10
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')       #if no values are divisible, it is a prime number


#practicing tuples
point = (1,0)
match point:
    case (0,0):
        print("Origin")
    case (0,1):
        print("Up1")
    case (1,0):
        print("Right1")
    case (1,1):
        print("Up1Right1")

"""import random

while True:
    try:
        play = input("Want to play rock-paper-scissors? y/n : ")
        if play not in ["y", "n"]:
            raise ValueError
        else:
            break

    except ValueError:
        print("invalid input. Please enter y or n")

while play == 'y':
    while True:
        try:
            user = input("Do you want to play rock (r), paper (p), or scissors (s)? : ")
            if user not in ["r", "p", "s"]:
                raise ValueError
            else:
                break

        except ValueError:
            print("invalid input. Please enter r, s, or p")

    computer = random.choice(["r", "p", "s"])

    print(f"player played {user}")
    print(f"computer played {computer}")

    if computer == user:
        print("You Tied!")

    elif computer == "r" and user == "p":
        print("You Win!")

    elif computer == "p" and user == "s":
        print("You Win!")

    elif computer == "s" and user == "r":
        print("You Win!")

    else:
        print("Computer Wins!")

    play = input("Do you want to play again? y/n : ")
"""


#Hangman Game
secret_word = "giraffe"
guess = ""
guess_counter = 0
guess_limit = 5
out_of_guesses = False
while guess != secret_word and not out_of_guesses:
    if guess_counter < guess_limit:
        guess = input("Guess the word: ")
        print(f"You have {guess_limit} guesses")
        guess_counter+= 1


    else:
        out_of_guesses = True
if out_of_guesses:
    print("YOU LOSE")
else:
    print("You Win!")




word = input("Write something: ")
for letter in word:
    if letter in word == "ABCDEFabcdef":
        print("Can I NOT or can I yes?")

    else:
        letter = letter.upper()

print(word)




