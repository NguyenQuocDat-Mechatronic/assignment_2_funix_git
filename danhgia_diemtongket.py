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
def xeploai_thidaihoc_hocsinh(link):
    handle = open(link)
    dict_xeploai = dict()
    # duyệt từng dòng của file
    for sub_line in handle:
        if not sub_line.startswith("Ma HS"):
            list_point = list()
            # tách ma_hs và point từng dòng vào list_point
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
            avg_D = f_lp[0]+f_lp[4]+f_lp[5]*2
            list_xeploai = list()
            list_diem_xep = [avg_A,avg_A1,avg_B]
            def sosanh(k,x,y,z):
                if k >= x:
                    xl = 1
                elif k<x and k >=y:
                    xl = 2
                elif k < y and k >= z:
                    xl =3
                else:
                    xl = 4
                return xl
            for i in list_diem_xep:
                list_xeploai.append(sosanh(i,24,18,12))
            list_xeploai.append(sosanh(avg_C,21,15,12))
            list_xeploai.append(sosanh(avg_D,32,24,20))
            dict_xeploai[list_point[0]]=list_xeploai
    return dict_xeploai
def main():
    link_in_file = input("đường dẫn input cho file “diem_ trungbinh.txt:")
    dict_xeploai_TBchuan = xeploai_hocsinh(link_in_file)
    dict_xeploai = xeploai_thidaihoc_hocsinh(link_in_file)
    link_out_file = input("đường dẫn output cho file “danhgia_hocsinh.txt:")
    f = open(link_out_file, mode="w")
    f.write( 'Ma HS,xeploai_TB chuan,xeploai_A,xeploai_A1,xeploai_B,xeploai_C,xeploai_D'+"\n")
    list_result = list()
    # ghep string hoc sinh + xeploai_tbchuan.
    for x,y in dict_xeploai_TBchuan.items():
        result = str(x)+";"+str(y)
        list_result.append(result)
    i = 0
    # duyệt từng học sinh
    for z in dict_xeploai.values():
        result_point = str()
        # duyệt từng loại xếp hạng rồi add string
        for u in z:
            result_point = result_point + ";" + str(u)
        final_result = list_result[i] +result_point +"\n"
        i +=1
        f.write(final_result)
main()
"""Test thử đường link"""
# D:\1.Education\1.IT\1_git\1_assignment1\2_assignment_2_funix\diem_trungbinh.txt
# D:\1.Education\1.IT\1_git\1_assignment1\2_assignment_2_funix\danhgia_hocsinh.txt