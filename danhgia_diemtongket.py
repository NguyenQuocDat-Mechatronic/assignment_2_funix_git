def xeploai_hocsinh(x):
    handle = open(x)
    dict_hang = dict()
    for sub_line in handle:
        if not sub_line.startswith("Ma HS"):
            list_point = list()
            # tách từng dòng vào list_point
            for point in sub_line.split(";"):
                list_point.append(point.strip())
            sub_lpoint = list()
            for sub_point in list_point[1].split(","):
                sub_lpoint.append(sub_point)
                f_lp = list(map(float,sub_lpoint))
            dtb_chuan = ((f_lp[0]+f_lp[4]+f_lp[5])*2.0 + (f_lp[1]+f_lp[2]+f_lp[3]+f_lp[6]+f_lp[7])*1.0)/11.0
            #dùng filter để tìm ra giá trí trong f_lp phù hơp tiêu chí a<8.0,6.5,5.0,4.5
            if dtb_chuan>9.0 and (len(list(filter(lambda a: a<8.0, f_lp))) ==0):
                hang = "Xuat sac"
            elif dtb_chuan>8.0 and (len(list(filter(lambda a: a<6.5, f_lp))) ==0):
                hang = "Gioi"
            elif dtb_chuan>6.5 and (len(list(filter(lambda a: a<5.0, f_lp))) ==0):
                hang = "Kha"
            elif dtb_chuan>6.0 and (len(list(filter(lambda a: a<4.5, f_lp))) ==0):
                hang = "TB kha"
            else:
                hang = "TB"
            dict_hang[list_point[0]]= hang
    return dict_hang
print(xeploai_hocsinh('D:\\1.Education\\1.IT\\1_git\\1_assignment1\\2_assignment_2_funix\\diem_trungbinh.txt'))
def xeploai_thidaihoc_hocsinh(link):
    handle = open(link)
    dict_xeploai = dict()
    for sub_line in handle:
        if not sub_line.startswith("Ma HS"):
            list_point = list()
            # tách từng dòng vào list_point
            for point in sub_line.split(";"):
                list_point.append(point.strip())
            sub_lpoint = list()
            for sub_point in list_point[1].split(","):
                sub_lpoint.append(sub_point)
                f_lp = list(map(float,sub_lpoint))
            avg_A = f_lp[0]+f_lp[1]+f_lp[2]
            avg_A1= f_lp[0]+f_lp[1]+f_lp[5]
            avg_B = f_lp[0]+f_lp[2]+f_lp[3]
            avg_C = f_lp[4]+f_lp[6]+f_lp[7]
            avg_D = f_lp[0]+f_lp[4]+f_lp[5]
            list_xeploai = list()
            list_diem_xep = [avg_A,avg_A1,avg_B]
            print(list_diem_xep)
            for i in list_diem_xep:
                if i >= 24:
                    xl = 1
                elif i<24 and i >=18:
                    xl = 2
                elif i < 18 and i >= 12:
                    xl =3
                else:
                    xl = 4
                list_xeploai.append(xl)
            return list_xeploai
print(xeploai_thidaihoc_hocsinh('D:\\1.Education\\1.IT\\1_git\\1_assignment1\\2_assignment_2_funix\\diem_trungbinh.txt'))