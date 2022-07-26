'''[Onsite Day 2] เกมวิ่งเก็บ'''
def main():
    '''ระยะทางที่พี่วิ่งไปทั้งหมด เป็นทศนิยมสองตำแหน่ง'''
    start = 0
    total = 0
    var_list = [float(iso) for iso in input().spilit()]
    for iso in var_list:
        total += abs(iso - start)
        start = iso
    print("%.2f" %total)
main()
