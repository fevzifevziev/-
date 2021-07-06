#Импорт графической библиотеки
from tkinter import *
from tkinter import ttk
#Библиотека Python для генерации случайных чисел
import random
#Импорт модулей сортировок
from mergeSort import mergeSort


#Настройки окна приложения
root = Tk()
root.title ('Визуализация алгоритма сортировки слиянием.')
root.geometry("835x480+350+100")
root.config(bg="#F2F2F2")
root.iconbitmap('iso.ico')

#Глобальные переменные
selected_algorithm = StringVar()
array = []


def setArray():
    """Функция задает предустановленный массив"""
    global array
    array_size = int(sizeScale.get())
    array = [20, 18, 7, 6, 4, 1, 2, 31, 5, 10, 23, 10, 40, 10, 5,6, 17, 5, 10, 9]
    del array[array_size -1  : -1]
    demoArray(array,['#FB5560' for x in range(len(array))])


def generateArray():
    """Генерация случайного массива"""
    global array
    array_size = int(sizeScale.get())
    array = []
    for i in range(array_size):
        array.append(random.randrange(0,100))
    demoArray(array, ['#FB5560' for x in range (len(array))])


def createArray():
    """Генерация заданного пользователем массива"""
    global array
    array_size = int(sizeScale.get())
    unsplit_array = user_array.get().split()
    for i in unsplit_array:
        array.append(int(i))

    del array[array_size -1  : -1]
    demoArray(array,['#FB5560' for x in range(len(array))])

def delArray():
    canvas.delete('all')
    global array
    array_size = int(sizeScale.get())
    array = []
    del array[array_size -1  : -1]

def demoArray (array, colorArray):
    """Отрисовка массива чисел на холсте"""
    canvas.delete('all')
    canvas_height = 220
    canvas_width = 770
    x_width = canvas_width / (len(array) + 1)
    offset = 5
    spacing = 15
    normalized_data  = [i / max(array) for i in array]
    for i, height in enumerate(normalized_data):
        x_0 = i * x_width + offset + spacing
        y_0 = canvas_height - height * 100
        x_1 = (i + 1) * x_width + offset
        y_1= canvas_height
        canvas.create_rectangle(x_0, y_0, x_1, y_1, fill=colorArray[i])
        canvas.create_text(x_0 + 2, y_0, anchor=SW, text=str(array[i]))
        canvas.create_text(125 , 30)
        root.update_idletasks()


def sorting():
    global array
    _sorting_speed = float(sorting_speed.get())
    mergeSort(array, 0, len(array) - 1, demoArray, _sorting_speed )
    demoArray(array, ['#77E596' for element in range(len(array))])


#Отрисовка интерфея приложения и положения рабочей области
UI_frame = Frame(root, width=835, height=480, bg ='#068888')
UI_frame.grid(row=0, column=0, padx=10, pady=5)
canvas = Canvas(root, width=770, height=350,bg='#CECDD2')
canvas.place(x=420, y =350, anchor="c", height=250, width=750, bordermode=OUTSIDE)

#Отрисовка управляющих элементов
btn_set = Button(UI_frame, text='Готовый массив', command=setArray,
            bg='#ffffff', foreground='#000000')
btn_set.place(x=150, y=40, anchor="c", height=40, width=170, bordermode=OUTSIDE)

btn_generate =  Button(UI_frame, text='Сгенерировать массив', command=generateArray,
             bg='#ffffff', foreground='#000000')
btn_generate.place(x=150, y=100, anchor="c", height=40, width=170, bordermode=OUTSIDE)

btn_create =  Button(UI_frame, text='Задать массив', command=createArray,
             bg='#8A7FF5', foreground='#000000')
btn_create.place(x=520, y=100, anchor="c", height=40, width=140, bordermode=OUTSIDE)

btn_del =  Button(UI_frame, text='Очистить', command=delArray,
             bg='#EEC3D1', foreground='#000000')
btn_del.place(x=680, y=100, anchor="c", height=40, width=140, bordermode=OUTSIDE)

canvas_btn_start = Canvas(UI_frame, width=770, height=350,bg='#CECDD2')
canvas_btn_start.place(x=600, y=160, anchor="c", height=50, width=190, bordermode=OUTSIDE)
btn_start = Button(UI_frame, text='Сортировать', command=sorting,
             bg='#5CDC78', foreground='#000000',font=20)
btn_start.place(x=600, y=160, anchor="c", height=40, width=170, bordermode=OUTSIDE)

sizeScale = Scale(UI_frame, from_ = 2, to=20, length=100, digits=1, resolution=0.2, orient=HORIZONTAL, label = 'Размер массива')
sizeScale.place(x=340, y=40, anchor="c", height=60, width=150, bordermode=OUTSIDE)

label_speed = Label(text = "Скорость =")
label_speed.place(x=325, y=105, anchor="c", height=40, width=100)
sorting_speed = Entry(UI_frame,
             bg='#ffffff', foreground='#000000', justify='center')
sorting_speed.insert(0, "0.5")
sorting_speed.place(x=390, y=100, anchor="c", height=30, width=30, bordermode=OUTSIDE)

label_user_array = Label(bg='#66CDAA',text = "Свой список через пробел")
label_user_array.place(x=610, y=25, anchor="c", height=20, width=300)
user_array = Entry(UI_frame,
             bg='#ffffff', foreground='#000000', justify='center')
user_array.place(x=600, y=50, anchor="c", height=30, width=300, bordermode=OUTSIDE)



root.mainloop()
