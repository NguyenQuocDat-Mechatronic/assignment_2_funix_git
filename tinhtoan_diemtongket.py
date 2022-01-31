"""Assignment 2"""
def tinhdiem_trungbinh(x):
    handle = open(x)
    string_subject = str()
    dict_subject = list()
    for line in handle:
        if line.startswith("Ma HS"):
            string_subject = line
            for i in line.split(","):
                dict_subject.append(i.strip())
        break
    total_dict = dict()
    list_MaHS = list()
    for sub_line in handle:
        if not sub_line.startswith("Ma HS"):
            list_point = list()
            for point in sub_line.split(";"):
                list_point.append(point.strip())
            avg = 0
            sub_dict =dict()
            i = 0
            for point_cal in list_point:
                point = list(map(int,point_cal.split(",")))
                if len(point) ==4:
                    avg = round(point[0]*5/100+point[1]*10/100+point[2]*15/100+point[3]*70/100,2)
                    sub_dict[dict_subject[1+i]] = avg
                    i +=1
                if len(point) ==5:
                    avg = round(point[0]*5/100+point[1]*10/100+point[2]*10/100+point[3]*15/100+point[4]*60/100,2)
                    sub_dict[dict_subject[1+i]] = avg
                    i +=1
        total_dict[list_point[0]] = sub_dict
    print(total_dict)

def main():
    link = input()
    tinhdiem_trungbinh(link)
main()
# tinhdiem_trungbinh(".\.\diem_chitiet.txt")
# tinhdiem_trungbinh("D:\1.Education\1.IT\1_git\1_assignment1\2_assignment_2_funix\diem_chitiet.txt")
