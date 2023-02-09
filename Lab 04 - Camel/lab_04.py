import random

# main loop
def main():
    """Game instructions"""
    print("Welcome to Camel! \nYou have stolen a camel to make your way across the great Mobi desert. \nThe natives want their camel back and are chasing you down! Survive your desert trek and outrun the natives.")

    """variables and their default values"""
    done = False
    miles_travelled = 0
    thirst = 0
    distance_from_natives = -30
    water_swigs_left = 3
    while not done:
        print("\nA. Drink from your canteen. \nB. Ahead moderate speed. \nC. Ahead full speed. \nD. Stop for the night. \nE. Status check \nQ. Quit.")
        # ask for user choice
        user_choice = input("\nWhat would you like to do? ")
        if user_choice.upper() == "A":
            thirst -= 20
            water_swigs_left -=1
            distance_from_natives +=10
        elif user_choice.upper() == 'B':
            random_numbera = random.randint(20, 40)
            miles_travelled += random_numbera
            thirst += 15
            distance_from_natives -= random_numbera
        elif user_choice.upper() == 'C':
            random_numberb = random.randint(5, 15)
            miles_travelled += random_numberb
            thirst += 10
            distance_from_natives += random_numberb
        elif user_choice.upper() == 'D':
            thirst -=20
            distance_from_natives -=15
        elif user_choice.upper() == 'E':
            print(f'You have travelled {miles_travelled} miles, \nDr. Gunna E\'tcha is {distance_from_natives} behind you, \nYou have {water_swigs_left} number of pills, \nYour tiredness level is {thirst}%')
            distance_from_natives += 5
        elif user_choice.upper() == 'Q':
            print("You quit.")
            done = True
        if water_swigs_left == 0:
            print("GAME OVER!! You are out of energy pills")
            done=True

        if thirst >= 100:
            print(f"Your hand fatigue is {thirst}%. \nYou're hands gave out. \nNext time monitor your hand tiredness and REMEMBER to take energy pills")
            done = True
        if distance_from_natives >= 0:
            print("GAME OVER!! Dr.Gunna E'tcha has captured you.")
            done = True
        if miles_travelled >=200:
            print ("CONGRATULATIONS!! You have escpaed from the hands of Evil.")
            done = True

# call the main function 
main()