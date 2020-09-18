# Импорт необходимых библиотек
from tkinter import *
import random

#Функция сортировки вставками
def sorting(list):
    for i in range(1, len(list)):
        current = list[i]
        f = i-1
        while f>=0:
            if current < list[f]:
                list[f+1] = list[f]
                list[f] = current
                f = f-1
            else:
                break
a[]
#Генерация рандомного списка
a = []
for i in range (11):
    x = random.randrange(10, 100)
    a.append(x)
#Размещение списка в файле input.txt
address = open('input.txt', 'w')
for item in a:
    address.write("%s\n" % item)
address.close()

#Открытие списка из файла на чтение
with open('input.txt') as f:
    content = f.readlines()
b = [x.strip() for x in content]
address.close()

#Функция вывода списка после сортировки
def printafter():
    sorting(b)
    afterlabel = Label(root, text="список после сортировки вставками", fg="black")
    afterlabel.grid(row=0, column=3, padx=10)
    after = Label (root, text=b, fg="black", bg='#DCDCDC')
    after.grid(row=1, column=3, padx=10, pady=10)

    #Размещение сортированного списка в файле output.txt
    addressout = open('output.txt', 'w')
    for item in b:
        addressout.write("%s\n" % item)
    addressout.close()

#Создание главного окна приложения
root = Tk()
root.title("insertion sort")

#Вывод рандомного списка и заголовка к нему
beforelabel = Label (root, text="рандомно сгенерированный список", fg="black")
beforelabel.grid(row=0, column=1, padx=10)
before = Label (root, text=a, fg="black", bg='#DCDCDC')
before.grid(row=1, column=1, padx=10, pady=10)

#Кнопка, при нажатии которой выполняется сортировка, и выводится отсортированный список
arrow = Button(root, text="->", command=printafter, bg = '#C0C0C0', font="Helvetica 10", relief = 'groove', activebackground='#A9A9A9')
arrow.grid(row=1, column=2, padx=10, pady=10)

#Ячейки, которые заполняются при нажатии на кнопку
afterlabel1 = Label(root, text="список после сортировки вставками", fg="black")
afterlabel1.grid(row=0, column=3, padx=10)
after1 = Label(root, text=b,  fg="#DCDCDC", bg='#DCDCDC')
after1.grid(row=1, column=3, padx=10, pady=10)

root.mainloop()