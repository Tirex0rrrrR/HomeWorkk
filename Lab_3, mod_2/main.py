class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self) ->str:
        return self._name

    @property
    def author(self) -> str:
        return self._author

    @name.setter
    def name(self, value):
        pass

    @author.setter
    def author(self, value):
        pass

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Количество страниц {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self.pages!r})"

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, new_pages: int):
        if isinstance(new_pages, (int)) and new_pages > 0:
            self._pages = new_pages
        else:
            self._pages=0

class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration
    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}. Размер книги {self.duration}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self.duration!r})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, new_duration: float):
        if isinstance(new_duration, (float)) and new_duration > 0:
            self._duration = new_duration
        else:
            self._duration=0