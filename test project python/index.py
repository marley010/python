MAX_LINES = 3 # dit is een nummer dat nooit zal gaan veranderen
MAX_BET = 100
MIN_BET = 1


def deposit(): #function
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit(): #dit zorgt ervoor dat het een nummer is
            amount = int(amount)# dit ook
            if amount > 0: #als het hoger is dan 0 dan is het goed
                break
            else:
                print("amount must be greater than 0.")
        else:
            print("please enter a number")
            
    return amount

def get_number_of_lines():
    while True:
        lines = input("enter the number of lines to bet on (1-" + str(MAX_LINES) +")? ")
        if lines.isdigit(): #dit zorgt ervoor dat het een nummer is
            lines = int(lines)# dit ook
            if 1 <= lines <= MAX_LINES : #als het 1,2,3 is dan is het goed
                break
            else:
                print("enter a valid number of lines.")
        else:
            print("please enter a number")
            
    return lines

def get_bet():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit(): #dit zorgt ervoor dat het een nummer is
            amount = int(amount)# dit ook
            if MIN_BET <= amount <= MAX_BET: #als het hoger is dan 0 dan is het goed
                break
            else:
                print(f"amount must be between${MIN_BET} - ${MAX_BET}.")
        else:
            print("please enter a number")
            
    return amount


    


def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines} total bet is equal to: ${total_bet}")
    
main()