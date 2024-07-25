import os
import json

from config import file_data_books, file_id_books
from model import Book
from dao_book import BookDAO


def create_data_file(file_name: str):
    records = []
    with open(file_name, 'w', encoding="UTF-8") as file_out:
        json.dump(records, file_out, ensure_ascii=False, indent=2)


def create_id_file(file_name: str):
    identifier = 0
    with open(file_name, 'w', encoding="UTF-8") as file_out:
        file_out.write(str(identifier))


def start_app():
    print("Управление библиотекой")

    while True:

        print("\n1) Добавить книгу\n2) Удалить книгу\n3) Поиск книги\n"
              "4) Вывод всех книг\n5) Изменить статус книги\n6) Выйти")

        action = input("Выберите действие: ")

        if action == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = input("Введите год издания: ")
            while not year.isdigit():
                print("Год должен быть числом")
                year = input("Введите год издания: ")
            BookDAO.add_book(Book(title, author, int(year)))
            print("Книга добавлена")

        elif action == "2":
            try:
                identify = input("Введите id книги для удаления: ")
                while not identify.isdigit():
                    print("ID должно быть числом")
                    identify = input("Введите id книги для удаления: ")
                BookDAO.remove_book(int(identify))
                print("Книга удалена")
            except KeyError as e:
                print(e)

        elif action == "3":
            params = {}
            print("Поиск книги осуществляется по нескольким параметрам"
                  "\nчтобы пропустить параметр нажмите enter")
            title = input("Введите название: ")
            if title:
                params['title'] = title
            author = input("Введите автора: ")
            if author:
                params['author'] = author
            year = input("Введите год издания: ")
            while not year.isdigit() and year != "":
                print("Год должен быть числом")
                year = input("Введите год издания: ")

            if year:
                params['year'] = int(year)
            results = BookDAO.get_books(**params)

            if not results:
                print("Книги с заданными параметрами отсутствуют")

            for result in results:
                book = Book(**result)
                print(book)

        elif action == "4":
            books = BookDAO.get_all_books()
            if len(books) == 0:
                print("В данный момент нет книг")
                continue

            for book in books:
                book = Book(**book)
                print(book)

        elif action == "5":
            try:
                identify = input("Введите id книги для изменения: ")
                while not identify.isdigit():
                    print("ID должно быть числом")
                    identify = input("Введите id книги для изменения: ")
                print("Выберите статус книги\n1) В наличии\n2) Выдана")
                status = input("Введите стаутус: ")
                while status != '1' and status != '2':
                    status = "Введите статус: "
                status_book = 'в наличии' if status == '1' else 'выдана'
                BookDAO.change_status(int(identify), status_book)
                print("Статус книги изменен")
            except KeyError as e:
                print(e)

        elif action == "6":
            break

        else:
            print("Нет такой команды")


if __name__ == "__main__":
    if not os.path.isfile(file_data_books):
        create_data_file(file_data_books)

    if not os.path.isfile(file_id_books):
        create_id_file(file_id_books)

    start_app()
