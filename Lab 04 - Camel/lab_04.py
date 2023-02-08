import random

# main loop
def main():
    """Game instructions"""
    print("Welcome to the Escape Game. \nYour mission, if you choose to accept it, is to climb up the 200m Kalifa tower. \nYou are being persued by Dr.Gonna Get'cha and his men. Use the following actions to escape.")

    """variables and their default values"""
    done = False
    miles_travelled = 0
    hand_tiredness = 0
    Bad_guy_distance = -30
    No_of_energy_pills = 3
    while not done:
        print("\nA. Take an energy pill \nB. Climb fast. \nC. Climb slow \nD. Take a breather \nE. Look down (check status) \nQ. Abort mission ")
        player_input= input("\nWhat would you like to do? ")
        
        if player_input =='a' or 'A' or 'climb fast':
            hand_tiredness -= 20
            No_of_energy_pills -=1
            Bad_guy_distance +=10
        elif player_input == 'b':
            random_numbera = random.randint(20, 40)
            miles_travelled += random_numbera
            hand_tiredness += 15
            Bad_guy_distance -= random_numbera
        elif player_input == 'c':
            random_numberb = random.randint(5, 15)
            miles_travelled += random_numberb
            hand_tiredness += 10
            Bad_guy_distance += random_numberb
        elif player_input == 'd':
            hand_tiredness -=20
            Bad_guy_distance -=15
        elif player_input == 'e':
            print(f'You have travelled {miles_travelled} miles, \nDr. Gunna E\'tcha is {Bad_guy_distance} behind you, \nYou have {No_of_energy_pills} number of pills, \nYour tiredness level is {hand_tiredness}%')
            Bad_guy_distance += 5
        elif player_input == 'Q':
            done = True
        if No_of_energy_pills == 0:
                print("GAME OVER!! You are out of energy pills")
                done=True

        if hand_tiredness >= 100:
            print(f"Your hand fatigue is {hand_tiredness}%. \nYou're hands gave out. \nNext time monitor your hand tiredness and REMEMBER to take energy pills")
            done = True
        if Bad_guy_distance >= 0:
            print("GAME OVER!! Dr.Gunna E'tcha has captured you.")
            done = True
        if miles_travelled >=200:
            print ("CONGRATULATIONS!! You have escpaed from the hands of Evil.")
            done = True

# call the main function 
main()