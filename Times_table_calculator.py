# Modify the welcome message to greet the users to the times table quiz
print('Welcome to the times table quiz')
# Modify the print statements for the two inputs in reference to the quiz
print('Which times table do you want to test')
try: # checks integer has been entered
    times_table = int(input())
except ValueError:
    print("You must enter a number")
    times_table = int(input())
print('Enter a max number for the times table to go up to')
try: # checks integer has been entered
    max_value = int(input())
except ValueError:
    print("You must enter a number")
    max_value = int(input())
max_value_plus = max_value + 1 # Adds 1 to value so the range will include the number inputted
answer = 0
print(f'You will be tested on the {times_table} times table up to {max_value}') # Rephrase the code to say that they will be tested on their chosen times table 
score = 0 # Score variable initiated so total score can be added to below in loop

for x in range(1,max_value_plus):
    answer = x * times_table
    print(f'Please type your answer to {x} times {times_table}')
        # Loop to ensure user enters a valid number
    while True:
        try:
            user_answer = int(input())
            break  # Exit loop if a valid number is entered
        except ValueError:
            print("You must enter a valid number. Please try again:")

    # Checking the user's answer
    if user_answer == answer:
        score += 1  # Increments score by 1 if answer is correct
        print('You are correct!')
    else:
        print(f'You are incorrect, the correct answer for {x} times {times_table} is {answer}.')

print(f'End of quiz, your final score is {score} out of a possible {max_value}')