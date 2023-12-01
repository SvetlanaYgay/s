
import datetime

print("* * * Приложение ЗАМЕТКИ * * *")
# print("***Инструкция***" + "\n" + "Команды для работы:" + "\n" +
#       "add - ввод новых данных" + "\n" +
#       "ed - редактирование данных" + "\n" +
#       "sch - поиск данных" + "\n" +
#       "all - печать всего списка заметок" + "\n" +
#       "ex - выход из программы")

# Имя файла
nameFile = 'pythonNotes.json'
fileID = 'idNotes.txt'

#текущее время

dt_now = datetime.datetime.now()
print(dt_now)

###Цикл программы
def processing():
    exit = True
    while exit == True:
        print("Команды: add - ввод; " +
              "ed - редакт.; " +
              "sch - поиск; " +
              "all - весь cписок заметок.; " +
              "ex - выход. ")
        comand = input("Введите команду: ")

        if comand == "add":

            print(newNote(inputZag(),inputbodyNote()))
            continue

        if comand == "ed":
            ed = input("Поиск заметки: ").lower()
            # функция печати списка с найденной заметкой
            notesPrint(searchNote(ed))
            # печать данных от функции проверки и ф-ии редактирования
            jkl = searchNote(ed)
            print(examination(jkl))
            continue

        if comand == "all":
            # функция печати всего списка заметок
            printAllNotes()
            continue

        if comand == "sch":
            sch = input("Поиск заметок: ").lower()
            # функция печати списка с найденной заметкой
            notesPrint(searchNote(sch))
            continue

        if comand == "ex":
            print("До скорой встречи!")
            break

        else:
            print("Ошибка ввода!")

def inputZag():
    zagolovok = str(input("Введите заголовок заметки: "))

    return zagolovok

def inputbodyNote():
    bodyNote = str(input("Введите заметку: "))
    return  bodyNote




##Ввод новой заметки
def newNote(zag,k):
    with open(nameFile, "a") as somefile:
        id = idVerification() + 1
        somefile.write("id = " + str(id) + "; " +"TimeCreate: " + str(dt_now)+
                       " ***" + zag.lower() + "***: " +  k.lower() + '\n')
        # перезаписываем новый id
        overwritingID(id)

        return "Заметка добавлена"


# получение последнего введеного id
def idVerification():
    with open(fileID, "r") as file:
        temp = ''.join(file.readlines())
        id = int(temp)

        return id


# перезапись id в файле nameFileID
def overwritingID(id):
    with open(fileID, "w") as file:
        file.write(str(id))


# проверка найдена ли заметка
def examination(dict):
    if dict.get("er") == None:
        # передаем найденную заметку в функцию "redactAbon"
        # для редактирования

        redactNote(dict)
        # Печать результата выполнения
        return redactNote(dict)


##Поиск заметки
def searchNote(ed):
    with open(nameFile, "r") as file:
        dictionary = {}
        contents = file.readlines()
        for num in range(len(contents)):
            if ed in contents[num]:
                ind = str(num)
                dictionary[ind] = contents[num]

        if len(dictionary) < 1:
            dict2 = {}
            dict2['er'] = 'Данные не найдены.'
            return dict2

        else:
            return dictionary


# Замена заметки
def redactNote(dict2):
    ex = True
    while ex == True:
        rowSelection = input("Укажите номер строки или введите *** 2 раза: ")

        if rowSelection == '***' and len(rowSelection) == 3:
            return 'Редактирование выполнено.'

        if rowSelection in dict2:

            print("Выполните редактирование(при вводе пустой строки," +
                                "заметка будет удалена): ")
            newData = " ***" +   inputZag() + "***: "  + inputbodyNote()

            with open(nameFile, 'r') as f:
                old_data = f.read()
                data = dict2[rowSelection]
                if len(newData) ==0:
                    new_data = old_data.replace(data, newData + '\n')
                    new_data = new_data.lower()
                else:
                    id = idVerification() + 1
                    new_data = old_data.replace(data, "id = " + str(id) + "; " +" TimeCreate: " +
                                                str(dt_now) + "; " + newData + '\n')
                    new_data = new_data.lower()
                    overwritingID(id)

            with open(nameFile, 'w') as f:
                f.writelines(new_data )
                print('Готово!')
            continue


        elif rowSelection not in dict2 and rowSelection != '***':
            print("Повторите ввод!")
        continue


##Печать заметок
def notesPrint(dict1):
    for key, value in dict1.items():
        print(f"Строка: {key}  Заметка: {value} ")


# Печать всего списка
def printAllNotes():
    with open(nameFile, "r") as file:
        for message in file:
            list1 = []
            list1.append(message)
            list1 = [line.strip() for line in file.readlines() if len(line.strip()) != 0]
            # print(message, end="\n")
        print("* * * Список заметок * * *")
        for i in list1:
            print(i)
        return 1


##Продолжение выполнения программы
processing()
