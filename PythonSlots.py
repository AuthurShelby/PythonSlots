import random

def spinning():
    tokens = ["🍌" ,"🍒" ,"🍇", "🍎" ,"🍋"]
    return [random.choice(tokens) for _ in range(3)]

def Betting(bet,spin):   
    if spin[0] == spin[1] == spin[2]:
        if spin[0] == "🍌":
            return bet*2
        elif spin[0] == "🍒":
            return bet*3
        
        elif spin[0] == "🍇":
            return bet*4
        
        elif spin[0] == "🍎":
            return bet*10
        
        elif spin[0] == "🍋":
            return bet*10
    else:
        return 0
    
def SlotHandle():
    print("--------------")
    print("|Python Slots|")
    print("--------------")
    balance = 100
   
    
    while balance > 0:
        print("------------------------------")
        print(f"Your current balance is: ${balance}\n")
        print("Tokens - 🍌 🍒 🍇 🍎 🍋")
        print("------------------------------")
        bet = input("Enter a bet amount: ")
        if not  bet.isdigit():
            print("Invalid bet amount. Please enter a number.")
            continue
        
        bet = int(bet)

        if bet < 0:
            print("Sorry you enter a bet below 0 ")
            continue       
        
        if bet > balance:
            print("Sorry insufficient balance!")
            continue
        spins = spinning()
        Bets = Betting(bet,spins)
        print("\n*************")
        print("Spinning....\n")
        print(f"| {' | '.join(spins)} |\n")
        print("*************\n")
        balance += Bets - bet

        if Bets!=0:
            print(f"You won ${Bets}!")
            YesOrNo = input("Do you want to continue? (yes/no): ").lower()
            if YesOrNo != "yes":
                print(f"\nYour final balance is: ${balance}\n")
                print("----------------------")
                print("Thankyou For Playing!")
                print("----------------------")
                break

    if balance == 0:
        print("Sorry you ran out of balance!")

if __name__ == "__main__":
    SlotHandle()
