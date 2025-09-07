# qa_python
1. Тесты для метода add_new_book
test_add_new_book_valid_name - Проверяет добавление книги с валидным названием (включая граничные значения: 1 и 40 символов)
test_add_new_book_invalid_name - Проверяет невозможность добавления книги с невалидным названием (пустая строка, 41 символ, строка из пробелов)
test_add_new_book_duplicate - Проверяет невозможность добавления дубликата книги
2. Тесты для метода set_book_genre
test_set_book_genre_valid - Проверяет установку валидного жанра для существующей книги
test_set_book_genre_nonexistent_book - Проверяет невозможность установки жанра для несуществующей книги
test_set_book_genre_invalid_genre - Проверяет невозможность установки невалидного жанра
3. Тесты для метода get_book_genre
test_get_book_genre_with_genre - Проверяет получение жанра для книги с установленным жанром
test_get_book_genre_without_genre - Проверяет получение жанра для книги без жанра (возвращает пустую строку)
4. Тесты для метода get_books_with_specific_genre
test_get_books_with_specific_genre - Проверяет получение списка книг с определенным жанром
test_get_books_with_specific_genre_nonexistent - Проверяет получение пустого списка для несуществующего жанра
5. Тесты для метода get_books_genre
test_get_books_genre - Проверяет получение всего словаря книг
6. Тесты для метода get_books_for_children
test_get_books_for_children - Проверяет получение книг, подходящих для детей (без возрастного рейтинга), и исключение книг с возрастным рейтингом
7. Тесты для метода add_book_in_favorites
test_add_book_in_favorites - Проверяет добавление книги в избранное
test_add_book_in_favorites_nonexistent - Проверяет невозможность добавления несуществующей книги в избранное
test_add_book_in_favorites_duplicate - Проверяет невозможность повторного добавления книги в избранное
8. Тесты для метода delete_book_from_favorites
test_delete_book_from_favorites - Проверяет удаление книги из избранного
9. Тесты для метода get_list_of_favorites_books
test_get_list_of_favorites_books - Проверяет получение списка избранных книг
Параметризация
В тестах использована параметризация для проверки граничных значений в методе add_new_book:
Проверка имен длиной 1, 40, 0 и 41 символ