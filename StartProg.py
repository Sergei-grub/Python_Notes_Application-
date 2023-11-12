# Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания
import datetime
from MakeNote import New_record


def add_note(new_id, note):
    name = input("Введите заголовок: ")
    text = input("Введите заметку: ")
    time = datetime.datetime.today()
    note_time = time.strftime("%d-%m-%Y.%H:%M:%S")
    note.append([new_id, name, text, note_time])
    return note


def custom_key(people):
    return people[3]


def print_notes(note):
    note.sort(key=custom_key)
    print(note)
    print("Обратная сортировка по дате")
    note.sort(reverse=True)
    print(note)


def switch_case(note, comand):
    id_note = 0
    new_id = id_note + 1

    print("___")

    match comand:
        case "1":
            add_note(new_id, note)
        case "2":
            print_notes(note)
        case "3":
            print("I'm a teapot")


note = []
user_comand = "1"
while (user_comand != "0"):
    print("\n1 - добавить запись"
          "\n2 - посмотреть список записей"
          "\n3 - выход")
    user_comand = input("Введите команду: ")
    switch_case(note, user_comand)

print("Программа завершена")

# notes.insert([id_note, name, text])
# today = datetime.datetime.today()
# print(today.strftime("%m/%d/%Y"))  # '04/05/2017'
