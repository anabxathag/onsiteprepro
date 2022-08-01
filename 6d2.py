'''[Onsite Day 2] ความรักคือการหมุนรอบกัน ไม่ใช่ให้เธอหมุนรอบฉัน หรือให้ฉันหมุนรอบใคร'''
def main():
    '''string ที่โดนหมุนมาแล้ว CR:P'หมูกรอบ'''
    func = input()
    line = int(input())
    mylist = []
    invalid = False
    for i in range(line):
        mylist.append(input())
    checklen = len(mylist[0])
    for i in range(1, len(mylist)):
        if len(mylist[i]) != checklen:
            invalid = True
            break
    if invalid:
        print("Invalid size")
    else:
        if func == "90":
            string = ""
            for i in mylist[::-1]:
                string += i
            for i in range(checklen):
                print(string[i::checklen])
        elif func == "180":
            for i in mylist[::-1]:
                print(i[::-1])
        elif func == "flip":
            for i in mylist:
                print(i[::-1])
main()
