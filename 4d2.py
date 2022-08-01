'''[Onsite Day 2] Math Symbol'''
def main():
    '''ผลลัพธ์ ทศนิยม 2 ตำเเหน่ง'''
    var_list = []
    while True:
        num = input()
        if num == "+":
            print("%.2f" %(sum(var_list)))
            break
        elif num == "-":
            print("%.2f" %(diff(var_list)))
            break
        elif num == "*":
            print("%.2f" %(mul(var_list)))
            break
        elif num == "/":
            print("%.2f" %(sub(var_list)))
            break
        else:
            var_list += [float(num)]
def diff(varlist):
    '''-'''
    first = varlist.pop(0)
    for iso in varlist:
        first -= iso
    return first
def mul(varlist):
    '''*'''
    first = varlist.pop(0)
    for iso in varlist:
        first *= iso
    return first
def sub(varlist):
    '''/'''
    first = varlist.pop(0)
    for iso in varlist:
        first /= iso
    return first
main()
