"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""


def main():
    list1 = [{'school_class': '4a', 'scores': [2, 2, 3, 2, 2]}
        , {'school_class': '3a', 'scores': [5, 4, 5, 5, 5]},
             {'school_class': '5a', 'scores': [3, 3, 3, 4, 3]}]

    midlist = []
    for dicts in list1:
        midscore = (sum(dicts['scores']) / len(dicts['scores']))
        midlist.append(midscore)
        print(f"Для класса {dicts['school_class']} средний бал:{midscore}")
    print(f"Средний балл по школе:{sum(midlist) / len(midlist)}")


if __name__ == "__main__":
    main()
