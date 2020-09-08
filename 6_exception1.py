"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию ask_user() из задания while2, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def ask_user():
    ask_ans = {"Привет": "Привет", "Как дела": "Хорошо!", "Что делаешь?": "Программирую", "Пока": "Досвидания"}
    ask = input('Задай вопрос \n')
    while ask in ask_ans:
        try:
            print(ask_ans[f'{ask}'])
            ask = input('Задай вопрос \n')
        except(KeyboardInterrupt):
            print('Досвидания')
            break


if __name__ == "__main__":
    ask_user()
