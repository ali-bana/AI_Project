from Opening import *
from Utils import *
from Utils2 import *
import csv


def save_data_with_features(number):
    data = get_arrays('data.csv')
    data = data[0:number]
    writer = csv.writer(open("data_f.csv", 'w'))
    file = open("data_f.txt", "w+")
    for i in range(len(data)):
        #show_picture(data[i][1])
        a = has_closed(data[i][1])
        b = len_wid(data[i][1])
        #temp = np.append(data[i][1], a)
        #temp2 = np.append(temp, b)
        #bana = temp2.tolist()
        #bana = (data[i][0], bana)
        #bana = str(bana)
        file.write(str(a) + " " + str(b))
        file.write("\n")
        #writer.writerow(bana)
        #x = get_arrays("data_f.csv")
        #print(x)
        print(i)
    pass


if __name__ == "__main__":
    save_data_with_features()
    akbar = get_from_txt("data_f.txt")
    print(akbar)
