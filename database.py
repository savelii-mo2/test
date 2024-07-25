import json

from config import file_data_books, file_id_books


class DataBase:

    def __init__(self, file_data, file_id):
        self.file_data = file_data
        self.file_id = file_id

    def get_all_data(self) -> list[dict]:
        with open(self.file_data, encoding="UTF-8") as file_in:
            records = json.load(file_in)
        return records

    def commit(self, records: list):
        with open(self.file_data, 'w', encoding="UTF-8") as file_out:
            json.dump(records, file_out, ensure_ascii=False, indent=2, sort_keys=True)

    def get_id(self) -> int:
        with open(self.file_id, 'r', encoding="UTF-8") as file_in:
            cur_id = int(file_in.read())
        cur_id += 1
        with open(self.file_id, 'w', encoding="UTF-8") as file_out:
            file_out.write(str(cur_id))
        return cur_id


db = DataBase(file_data_books, file_id_books)
