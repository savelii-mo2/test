from database import db
from model import Book


class BookDAO:

    @staticmethod
    def get_all_books():
        records = db.get_all_data()
        return records

    @staticmethod
    def add_book(book: Book):
        records = db.get_all_data()
        book.id = db.get_id()
        records.append(book.model_dump())
        db.commit(records)

    @staticmethod
    def get_book_by_id(id: int) -> int:
        records = db.get_all_data()
        for i, record in enumerate(records):
            if record['id'] == id:
                return i
        return -1

    @staticmethod
    def remove_book(id: int):
        records = db.get_all_data()
        index_del = BookDAO.get_book_by_id(id)
        if index_del == -1:
            raise KeyError("Книга с данным id отсутствует")
        records.pop(index_del)
        db.commit(records)

    @staticmethod
    def change_status(id: int, new_status: str):
        records = db.get_all_data()
        index_change = BookDAO.get_book_by_id(id)
        if index_change == -1:
            raise KeyError("Книга с данным id отсутствует")
        records[index_change]['status'] = new_status
        db.commit(records)


    @staticmethod
    def get_books(**kwargs) -> list:
        records = db.get_all_data()
        results = []
        for record in records:
            flag = True
            for key, value in kwargs.items():
                if record[key] != value:
                    flag = False
            if flag:
                results.append(record)

        return results
