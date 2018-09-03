import matplotlib.pyplot as plt
import numpy as np
import math as mt

def func(x):
    res = 0
    for monom in equation:
        res += monom[0] * (x ** monom[1])
    return res

equationList = []
i = 0

fin = open('input.txt', 'r')

text =''
for vv in fin:
    text += vv

strs = text.split("\n")

for str1 in strs:
    equation = []
    monom = ''
    i = 0
    for a in str1:
        i = i + 1
        if (a == '-') or (a == '+') or (len(str1) == i):
            if len(str1) == i:
                monom = monom + a
            zn = True  # true is '+', false is '-'
            coefOrIndex = True  # true is to coef
            coef = 0
            index = 0
            for b in monom:
                if b == '-':
                    zn = False
                if b.isalpha():
                    coefOrIndex = False
                    index = 1
                    if coef == 0:
                        coef = 1
                if b.isdigit() and coefOrIndex:
                    coef = coef * 10 + int(b, 10)
                if b.isdigit() and not coefOrIndex:
                    if index == 1:
                        index = int(b, 10)
                    else:
                        index = index * 10 + int(b, 10)
            if zn == False:
                coef = coef * -1
            equation.append([coef, index])
            monom = a
        else:
            monom += a
    equationList.append(equation)

print(equationList)

fin.close()
fout = open('output.txt', 'w')

x = np.arange(-10, 10, 0.1)

leng = mt.ceil(len(equationList) / 3)
i = 0

for equation in equationList:
    i = i + 1

    eq = ''
    for monom in equation:
        if (monom[0] > 0) and (eq != ''):
            eq = eq + '+' + str(monom[0]) + '*x^' + str(monom[1])
        else:
            eq = eq + str(monom[0]) + '*x^' + str(monom[1])

    last = 0
    for a in x:
        y = func(a)
        if (last > y):
            fout.write(eq + ' = ' + str(a) + '\n')
        last = y

    y = func(x)

    plt.subplot(3, leng, i)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(eq, size = 'x-small', weight = 'light')
    plt.plot(x, y, 'c')
    plt.grid(True, linestyle='-', color='0.75')

fout.close()
plt.show()
