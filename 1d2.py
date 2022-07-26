'''[Onsite Day 2] Atbash Cipher'''
def main():
    '''เป็น Stringหลังการเข้ารหัสแบบ Atbash'''
    asc_1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    asc_re = asc_1[::-1]
    messa = input()
    for iso in messa:
        if iso.islower() == True:
            posi = asc_1.lower().index(iso)
            print(asc_re.lower()[posi], end="")
        elif iso.isupper() == True:
            posi = asc_1.index(iso)
            print(asc_re[posi], end="")
        else:
            print(iso, end="")
main()
