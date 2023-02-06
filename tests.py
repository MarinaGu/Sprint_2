from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # 1
    def test_set_book_rating_set_rating_four(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 4)

        assert collector.books_rating['Гордость и предубеждение и зомби'] == 4

    # 2
    def test_set_book_rating_not_set_rating_zero(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 0)

        assert collector.books_rating['Гордость и предубеждение и зомби'] == 1

    # 3
    def test_set_book_rating_not_set_rating_more_ten(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 12)

        assert collector.books_rating['Гордость и предубеждение и зомби'] == 1

    # 4
    def test_get_book_rating_on_name_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 4)

        collector.get_books_rating()

        assert collector.books_rating['Гордость и предубеждение и зомби'] == 4

    # 5
    def test_get_books_with_specific_rating_seven(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Гарри Поттер и филосовский камень')

        collector.set_book_rating('Гордость и предубеждение и зомби', 4)
        collector.set_book_rating('Что делать, если ваш кот хочет вас убить', 3)
        collector.set_book_rating('Гарри Поттер и филосовский камень', 7)

        assert len(collector.get_books_with_specific_rating(7)) == 1

    # 6
    def test_get_books_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        collector.add_new_book('Гарри Поттер и филосовский камень')

        assert len(collector.books_rating) == 3

    # 7
    def test_add_book_in_favorites_add_one_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.favorites) == 1

    # 8
    def test_add_book_in_favorites_not_have_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Гарри Поттер и филосовский камень')

        assert len(collector.favorites) == 0

    # 9
    def test_add_book_in_favorites_add_book_that_already_exists(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.favorites) == 1

    # 10
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')
        collector.delete_book_from_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.favorites) == 0

    # 11
    def test_get_list_of_favorites_books_not_null(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        collector.add_book_in_favorites('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_list_of_favorites_books()) != 0

    # 12 
    def test_get_list_of_favorites_books_is_null(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_list_of_favorites_books()) == 0