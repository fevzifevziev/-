#Импорт библиотеки time для контроля скорости выполнения алгоритма
import time

def mergeSort(array, left, right, demoArray, sleeptime):
    """Функция сортировки массива слиянием"""
    if left < right:
        middle = (left + right) // 2
        mergeSort(array, left, middle, demoArray, sleeptime)
        mergeSort(array, middle + 1, right, demoArray, sleeptime)
        merge(array, left, middle, right, demoArray, sleeptime)


def merge(array, left, middle, right, demoArray, sleeptime):
    """Слияние подмассивов"""
    demoArray(array, painting(len(array), left, middle, right))
    time.sleep(sleeptime)
    leftPart = array[left : middle + 1]
    rightPart = array[middle + 1 : right + 1]
    l = 0
    r = 0
    for dataIdx in range(left, right + 1):
        if l < len(leftPart) and r < len(rightPart):
            if leftPart[l] <= rightPart[r]:
                array[dataIdx] = leftPart[l]
                l += 1
            else:
                array[dataIdx] = rightPart[r]
                r += 1
        elif l < len(leftPart):
            array[dataIdx] = leftPart[l]
            l += 1
        else:
            array[dataIdx] = rightPart[r]
            r += 1
    demoArray(array, ["#77E596" if x >= left and x <=                           #зеленый
                      right else "#FB5560" for x in range(len(array))])         #красный
    time.sleep(sleeptime)


def painting(length, left, middle, right):
    """Функция цветовой разметки элементов массива на холсте"""
    colors = []
    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colors.append("#5E5CE6")                                        #синий
            else:
                colors.append("#77E596")                                        #зеленый
        else:
            colors.append("#FE8045")                                            #оранжевый

    return colors
