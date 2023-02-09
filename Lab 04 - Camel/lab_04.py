import random
# at step no. 13. 
# main loop
def main():
    """Game instructions"""
    print("Welcome to Camel! \nYou have stolen a camel to make your way across the great Mobi desert. \nThe natives want their camel back and are chasing you down! Survive your desert trek and outrun the natives.")

    """variables and their default values"""
    done = False
    miles_travelled = 0
    thirst = 0
    camel_tiredness = 0
    distance_from_natives = -30
    drinks_in_canteen = 3
    while not done:
        print("\nA. Drink from your canteen. \nB. Ahead moderate speed. \nC. Ahead full speed. \nD. Stop for the night. \nE. Status check \nQ. Quit.")
        # ask for user choice
        user_choice = input("\nWhat would you like to do? ")
        if user_choice.upper() == "A":
            thirst -= 20
            drinks_in_canteen -=1
            distance_from_natives +=10
        elif user_choice.upper() == 'B':
            random_numbera = random.randint(20, 40)
            # 10 is the constant pace of the natives
            miles_travelled += random_numbera + 10
            thirst += 15
            camel_tiredness += 20
            # 10 is the constant pace of the natives
            distance_from_natives -= random_numbera + 10
        elif user_choice.upper() == 'C':
            random_numberb = random.randint(5, 15)
            miles_travelled += random_numberb
            thirst += 10
            camel_tiredness += 30
            distance_from_natives = random_numberb
        elif user_choice.upper() == 'D':
            thirst -=20
            camel_tiredness -= 30
            distance_from_natives -=15
        elif user_choice.upper() == 'E':
            print(f'You have travelled {miles_travelled} miles. \nDr. Gunna E\'tcha is {distance_from_natives} behind you. \nYou have {drinks_in_canteen} number of pills. \nCamel_tiredness is {camel_tiredness}%. \nYour tiredness level is {thirst}%.')
            distance_from_natives += 5
        elif user_choice.upper() == 'Q':
            print(f"You quit. \nMiles travelled: {miles_travelled} \nDrinks in canteen: {drinks_in_canteen} \nThe natives are {-distance_from_natives} miles behind you.")
            done = True
        if drinks_in_canteen == 0:
            print("GAME OVER!! You are out of energy pills")
            done=True
        if distance_from_natives >= -15:
            print("The natives are getting close.")

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