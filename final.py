
note = [
    "Имя пользователя:",
    "Содержание заметки:",
    "Статус:",
    "Дата создания:",
    "Дата изменения:",
    ["Заголовок 1:","Заголовок 2:"]
]
username = input("Ваше имя: ")
content = input("Содержание заметки: ")
status = input("Статус: ")
created_date = input("Дата создания (пример 26-02-2025): ")
issue_date = input("Дата изменения (пример 26-02-2025): ")
titles1 = input("Название первого заголовка: ")
titles2 = input("Название второго заголовка: ")

print(note[0], username)
print(note[1], content)
print(note[2], status)
print(note[3], created_date)
print(note[4], issue_date)
print(note[5][0], titles1)
print(note[5][1], titles2)