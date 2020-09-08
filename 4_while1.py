"""

Домашнее задание №1

Цикл while: ask_user

* Напишите функцию ask_user(), которая с помощью input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""


def ask_user():
    while True:
        print('Как дела?')
        answer=input('Ответ:')
        if answer=='Хорошо':
            print('У меня тоже')
            break
        else:
            print('Непрвильный ответ)')

if __name__ == "__main__":
    ask_user()
