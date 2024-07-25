class Book:

    def __init__(self, title: str, author: str, year: int, id: int | None = None, status: str = "в наличии"):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def model_dump(self) -> dict:
        book_dict = {}
        attributes = {'id', 'title', 'author', 'year', 'status'}
        for attr in dir(self):
            if attr in attributes:
                book_dict[attr] = getattr(self, attr)
        return book_dict

    def __str__(self):
        return (f"id: {self.id}, title: {self.title}, author: {self.author}, "
                f"year: {self.year}, status: {self.status}")
