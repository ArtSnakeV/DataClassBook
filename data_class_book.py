from dataclasses import dataclass, field


@dataclass
class Book:
    # # назва книги
    # __title: str
    # # автор книги
    # __author: str
    # # рік видання
    # __year: int
    # # чи доступна книга для видачі (за замовчуванням: True)
    # __available: bool
    # # середній рейтинг
    # # не ініціалізується через конструктор,
    # # значення за замовчуванням: 0.0, не відображається у repr
    # __rating: float
    # # список тегів, які описують книгу (наприклад, "sci-fi", "classic")
    # # має використовуватись default_factory
    # # list[str] — це типова анотація, яка означає список рядків
    # __tags: list[str]
    # # не задається напряму при створенні
    __title: str
    __author: str
    __year: int

    __rating: float = field(init = False, default = 0.0, repr = False)
    __internal_code: str
    __available: bool = True
    __tags: list[str] = field(default_factory=list)

    # title
    def get_title(self):
        return self.__title
    def set_title(self, title):
        self.__title = title
    title = property(get_title, set_title)
    # author
    def get_author(self):
        return self.__author
    def set_author(self, author):
        self.__author = author
    author = property(get_author, set_author)
    #year
    def get_year(self):
        return self.__year
    def set_year(self, year):
        self.__year = year
    year = property(get_year, set_year)
    #availability
    def get_availability(self):
        return self.__available
    def set_availability(self, available):
        self.__available = available
    available = property(get_availability, set_availability)
    #rating
    def get_rating(self):
        return self.__rating
    def set_rating(self, rating):
        self.__rating = rating
    rating = property(get_rating, set_rating)
    #tags
    def get_tags(self):
        return self.__tags
    def set_tags(self, tags):
        self.__tags = tags
    tags = property(get_tags, set_tags)
    #internal_code
    def get_internal_code(self):
        return self.__internal_code
    def set_internal_code(self, internal_code):
        self.__internal_code = internal_code
    internal_code = property(get_internal_code, set_internal_code)






book1 = Book(
 "The Hobbit",
 "J.R.R. Tolkien",
 1937,
 True,
 ["fantasy", "adventure", "classic"]
)
print(book1.title)
print(book1.author)
print(book1.year)
print(book1.available)
print(book1.rating)
print(book1.tags)
print(book1.internal_code)