import matplotlib.pyplot as plt
import numpy as np
import pandas
import re
'''
# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])

# plt.plot([1, 2, 3, 4], [1, 4, 2, 3])

# plt.show()

x = np.linspace(0, 2, 25)
#
# fig, ax = plt.subplots()
# ax.plot(x, x ,'bs',label='linear')
# ax.plot(x, x**2 ,'g^', label='quadratic')
# ax.plot(x, x**3 ,'r--', label='cubic')
# ax.set_xlabel("x label")
# ax.set_ylabel("y label")
# ax.legend()
# plt.show()

plt.scatter(x, x ,label='linear')
plt.plot(x, x**2 ,label='quadratic')
line, = plt.plot(x, x**3 ,'r--', label='cubic')

plt.legend()
plt.show()

# line.set_antialiased(False)


import tkinter as tk
from tkinter import ttk

# Creating tkinter window
window = tk.Tk()
window.title('Combobox')
window.geometry('500x250')

# label text for title
ttk.Label(window, text="GFG Combobox Widget",
          background='green', foreground="white",
          font=("Times New Roman", 15)).grid(row=0, column=1)

# label
ttk.Label(window, text="Select the Month :",
          font=("Times New Roman", 10)).grid(column=0,
                                             row=5, padx=10, pady=25)

# Combobox creation
n = tk.StringVar()
monthchoosen = ttk.Combobox(window, width=27, textvariable=n)

# Adding combobox drop down list
monthchoosen['values'] = (' January',
                          ' February',
                          ' March',
                          ' April',
                          ' May',
                          ' June',
                          ' July',
                          ' August',
                          ' September',
                          ' October',
                          ' November',
                          ' December')

monthchoosen.grid(column=1, row=5)
monthchoosen.current()
window.mainloop()

'''
# f = lambda x: (x<0,abs(x))
#
# print(f(-1))
#
#


str1 = '''
*  (d:  1, mar:0000124a
*  (d:  8, mar:0000124a
*  (d:  2, mar:00001249
*  (d:  6, mar:00001249
*  (d:  3, mar:00001249
*  (d:  7, mar:0000124a
*  (d:  4, mar:00012424
*  (d:  5, mar:00001292
'''
def convert_WDL_to_disklnum (raw_input):
    regex = re.compile(r'\(d: +([0-9]+), mar:([0-9a-f]+)')
    lnums = regex.findall(raw_input)
    print(lnums)

    for id, lnum in lnums:
        int_num = int(lnum,16)
        bin_num = bin(int_num)
        lnum_list = []
        for index, pos in enumerate(list(bin_num)[2::][::-1]):
            if pos == '1':
                lnum_list.append(index)
        print(id,lnum_list)
























