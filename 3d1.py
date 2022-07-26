'''Suvarnabhumi Airport'''
def syd():
    '''Sydney'''
    return 12
def sgn():
    '''Ho Chi Minh '''
    return 1.50
def atl():
    '''Atlanta Georgia'''
    return 9.55
def yvr():
    '''Vancouver Canada'''
    return 2.20
def ktm():
    '''Kathmandu'''
    return 14.15
def main():
    '''Timezone'''
    home = input()
    goal = input()
    timeho = input()
    if "SYD" in goal:
        print("BKK - SYD")
        timego = syd()
        print()
    elif "SGN" in goal:
        print("BKK - SGN")
        timego = sgn()
        print()
    elif "ATL" in goal:
        print("BKK - ATL")
        timego = atl()
        print("")
    elif "YVR" in goal:
        print("BKK - YVR")
        timego = yvr()
        print("")
    elif "KTM" in goal:
        print("BKK - KTM")
        timego = ktm()
        print("")
main()
