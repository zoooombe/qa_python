import pytest
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
    @pytest.fixture
    def collector(self):
        return BooksCollector()

    @pytest.mark.parametrize('book_name', [
        'Книга с нормальным названием',
        'x' * 40,
        'x'
    ])
    def test_add_new_book_valid_name(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize('invalid_name', [
        '',
        'x' * 41,
        '   '
    ])
    def test_add_new_book_invalid_name(self, collector, invalid_name):
        collector.add_new_book(invalid_name)
        assert invalid_name not in collector.get_books_genre()

    def test_add_new_book_duplicate(self, collector):
        book_name = "Тестовая книга"
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert list(collector.get_books_genre().keys()).count(book_name) == 1

    def test_set_book_genre_valid(self, collector):
        book_name = "Тестовая книга"
        genre = "Фантастика"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_set_book_genre_nonexistent_book(self, collector):
        genre = "Фантастика"
        collector.set_book_genre("Несуществующая книга", genre)
        assert "Несуществующая книга" not in collector.get_books_genre()

    def test_set_book_genre_invalid_genre(self, collector):
        book_name = "Тестовая книга"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, "Несуществующий жанр")
        assert collector.get_book_genre(book_name) == ''  # Жанр не должен измениться

    def test_get_book_genre_with_genre(self, collector):
        book_name = "Тестовая книга"
        genre = "Комедии"
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_book_genre_without_genre(self, collector):
        book_name = "Тестовая книга"
        collector.add_new_book(book_name)
        assert collector.get_book_genre(book_name) == ''

    def test_get_books_with_specific_genre(self, collector):
        books = ["Книга 1", "Книга 2", "Книга 3"]
        genre = "Фантастика"

        for book in books:
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        result = collector.get_books_with_specific_genre(genre)
        assert set(result) == set(books)

    def test_get_books_with_specific_genre_nonexistent(self, collector):
        result = collector.get_books_with_specific_genre("Несуществующий жанр")
        assert result == []

    def test_get_books_genre(self, collector):
        books = {"Книга 1": "Фантастика", "Книга 2": "Комедии"}

        for book, genre in books.items():
            collector.add_new_book(book)
            collector.set_book_genre(book, genre)

        assert collector.get_books_genre() == books

    def test_get_books_for_children(self, collector):
        children_books = ["Детская книга 1", "Детская книга 2"]
        adult_books = ["Взрослая книга 1", "Взрослая книга 2"]

        for book in children_books:
            collector.add_new_book(book)
            collector.set_book_genre(book, "Мультфильмы")

        for book in adult_books:
            collector.add_new_book(book)
            collector.set_book_genre(book, "Ужасы")

        result = collector.get_books_for_children()
        assert set(result) == set(children_books)
        for book in adult_books:
            assert book not in result


    def test_add_book_in_favorites(self, collector):
        book_name = "Тестовая книга"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        assert book_name in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_nonexistent(self, collector):
        collector.add_book_in_favorites("Несуществующая книга")
        assert "Несуществующая книга" not in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_duplicate(self, collector):
        book_name = "Тестовая книга"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.add_book_in_favorites(book_name)
        assert collector.get_list_of_favorites_books().count(book_name) == 1

    def test_delete_book_from_favorites(self, collector):
        book_name = "Тестовая книга"
        collector.add_new_book(book_name)
        collector.add_book_in_favorites(book_name)
        collector.delete_book_from_favorites(book_name)
        assert book_name not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_nonexistent(self, collector):
        collector.delete_book_from_favorites("Несуществующая книга")

    def test_get_list_of_favorites_books(self, collector):
        books = ["Книга 1", "Книга 2", "Книга 3"]

        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        result = collector.get_list_of_favorites_books()
        assert set(result) == set(books)