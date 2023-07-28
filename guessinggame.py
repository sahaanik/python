import random
number = random.randint(1, 6)
number_of_guesses = 0

player_name = input("Hello, What's your name?")
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 100:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('warmer')
    if guess > number:
        print('colder')
    if guess == number:
        break
if guess == number:
    print('you guess the number in' + str(number_of_guesses) + 'tries')
else:
    print('the number is ' +str(number)+  ' done')
