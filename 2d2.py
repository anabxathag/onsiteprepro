'''[Onsite Day 2] ตัวเลขที่มีอยู่'''
def main():
    '''ผลรวมของตัวเลข'''
    long = float(input())
    total = 0
    if long == 0:
        print("No Tape Measure")
    if long != 0:
        num = input()
        while num != "No more!":
            if float(num) <= long:
                total += float(num)
            num = input()
        if total != 0:
            print("Sum of Found Number = %d" %total)
        else:
            print("Not Found Number")
main()
