from nummber_in_times_table import nummber_in_times_table
import os


x = 0
time_tabel_size = 11

table_list =[]
while x+1 < time_tabel_size:
    x+=1
    y=0
    while y+1 < time_tabel_size:
        y+=1
        table_list.append(nummber_in_times_table(x, y))


print_outpt = ""
for nummner in table_list:
    print_outpt = print_outpt + nummner.printeble_nummber()
print(print_outpt)