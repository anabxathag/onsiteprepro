'''เบื่อแล้วขนมตู้ อยากเป็นชู้กับเธอ'''
def sn_1(rest):
    '''snack 1'''
    if rest % 3 == 0:
        return 10
    elif rest % 3 == 1:
        return 15
    elif rest % 3 == 2:
        return 20
def sn_2(rest):
    '''snack 2'''
    if rest % 3 == 0:
        return 12
    elif rest % 3 == 1:
        return 15
    elif rest % 3 == 2:
        return 18
def sn_3(rest):
    '''snack 3'''
    if rest % 3 == 0:
        return 5
    elif rest % 3 == 1:
        return 7
    elif rest % 3 == 2:
        return 9
def main():
    '''store'''
    budget = int(input())
    water = int(input())
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    rest = budget - water
    cost_1 = num_1 * sn_1(rest)
    rest -= cost_1
    cost_2 = num_2 * sn_2(rest)
    rest -= cost_2
    cost_3 = num_3 * sn_3(rest)
    rest -= cost_3
    if rest < 0:
        print("Now you have %d left." %budget)
        print("You don't have enough money!")
    elif rest >= 0:
        print("Now you have %d left." %rest)
        print("Here's your order!")
        print("Water: %d baht" %water)
        print("Snack number 1: %d baht" %cost_1)
        print("Snack number 2: %d baht" %cost_2)
        print("Snack number 3: %d baht" %cost_3)
main()
