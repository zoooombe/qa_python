import pytest

class TestBooksCollector:

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
        assert collector.get_book_genre(book_name) == ''

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

    def test_get_list_of_favorites_books(self, collector):
        books = ["Книга 1", "Книга 2", "Книга 3"]

        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        result = collector.get_list_of_favorites_books()
        assert set(result) == set(books)