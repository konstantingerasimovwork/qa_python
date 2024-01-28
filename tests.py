import pytest
class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.get_books_genre()) == 2


    def test_add_new_book_add_existing_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.get_books_genre()) == 1


    @pytest.mark.parametrize('name, expected_result',
                             [('Н', {'Н': ''}),
                              ('Название книги длинной в сорок символов!', {'Название книги длинной в сорок символов!': ''}),
                              ('', {}),
                              ('Название книги длинной в 41 символ!!!!!!!', {})],
                              ids=['positive test - 1 character',
                                   'positive test - 40 characters',
                                   'negative test - 0 characters',
                                   'negative test - 41 characters'])
    def test_add_new_book_add_book_name_with_different_length(self, collector, name, expected_result):
        collector.add_new_book(name)
        assert collector.get_books_genre() == expected_result


    def test_set_book_genre_set_existing_genre_for_existing_book(self, collector):
        collector.add_new_book('Двенадцать стульев')
        collector.set_book_genre('Двенадцать стульев', 'Комедии')
        get_genre = collector.get_books_genre()
        assert get_genre['Двенадцать стульев'] == 'Комедии'


    def test_set_book_genre_set_existing_genre_for_non_existent_book(self, collector):
        collector.add_new_book('Двенадцать стульев')
        collector.set_book_genre('Гордость и предубеждение и зомби', 'Ужасы')
        get_genre = collector.get_books_genre()
        assert get_genre == {'Двенадцать стульев': ''}


    def test_set_book_genre_set_non_existent_genre_for_existing_book(self, collector):
        collector.add_new_book('Щегол')
        collector.set_book_genre('Щегол', 'Драма')
        get_genre = collector.get_books_genre()
        assert get_genre['Щегол'] == ''

    
    def test_get_book_genre_book_name_is_existing(self, collector):
        collector.add_new_book('Двенадцать стульев')
        collector.set_book_genre('Двенадцать стульев', 'Комедии')
        book_genre = collector.get_book_genre('Двенадцать стульев')
        assert book_genre == 'Комедии'

    
    def test_get_book_genre_book_name_is_non_existent(self, collector):
        collector.add_new_book('Двенадцать стульев')
        collector.set_book_genre('Двенадцать стульев', 'Комедии')
        book_genre = collector.get_book_genre('Щегол')
        assert book_genre is None

    
    def test_get_books_with_specific_genre_fantastic_books(self, collector):
        collector.add_new_book('Двенадцать стульев')
        collector.add_new_book('Война миров')
        collector.add_new_book('Автостопом по галактике')
        collector.set_book_genre('Двенадцать стульев', 'Комедии')
        collector.set_book_genre('Война миров', 'Фантастика')
        collector.set_book_genre('Автостопом по галактике', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['Война миров', 'Автостопом по галактике']


    def test_get_books_with_specific_genre_empty_list_of_books(self, collector):
        assert collector.get_books_with_specific_genre('Фантастика') == []

    
    def test_get_books_genre_get_dir_with_2_books(self, collector):
        collector.add_new_book('Двенадцать стульев')
        collector.add_new_book('Автостопом по галактике')
        collector.set_book_genre('Двенадцать стульев', 'Комедии')
        collector.set_book_genre('Автостопом по галактике', 'Фантастика')
        assert collector.get_books_genre() == {'Двенадцать стульев': 'Комедии', 'Автостопом по галактике': 'Фантастика'}


    def test_get_books_genre_get_empty_dir(self, collector):
        assert collector.get_books_genre() == {}

    
    def test_get_books_for_children_get_two_books_out_of_three(self, collector):
        collector.add_new_book('Сияние')
        collector.add_new_book('Винни-Пух и все-все-все')
        collector.add_new_book('Автостопом по галактике')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.set_book_genre('Винни-Пух и все-все-все', 'Мультфильмы')
        collector.set_book_genre('Автостопом по галактике', 'Фантастика')
        assert collector.get_books_for_children() == ['Винни-Пух и все-все-все', 'Автостопом по галактике']


    def test_add_book_in_favorites_add_existing_book_to_favorite(self, collector):
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')
        assert collector.get_list_of_favorites_books() == ['Сияние']

    
    def test_add_book_in_favorites_add_existing_book_twice_to_favorite(self, collector):
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')
        collector.add_book_in_favorites('Сияние')
        assert collector.get_list_of_favorites_books() == ['Сияние']

    
    def test_add_book_in_favorites_add_non_existence_book_to_favorite(self, collector):
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Автостопом по галактике')
        assert collector.get_list_of_favorites_books() == []

    
    def test_delete_book_from_favorites_delete_existing_book(self,collector):
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')
        collector.delete_book_from_favorites('Сияние')
        assert collector.get_list_of_favorites_books() == []

    
    def test_delete_book_from_favorites_delete_non_existence_book(self,collector):
        collector.add_new_book('Сияние')
        collector.add_book_in_favorites('Сияние')
        collector.delete_book_from_favorites('Автостопом по галактике')
        assert collector.get_list_of_favorites_books() == ['Сияние']

    
    def test_get_list_of_favorites_books_get_3_books(self, collector):
        collector.add_new_book('Сияние')
        collector.add_new_book('Винни-Пух и все-все-все')
        collector.add_new_book('Автостопом по галактике')
        collector.add_book_in_favorites('Сияние')
        collector.add_book_in_favorites('Винни-Пух и все-все-все')
        collector.add_book_in_favorites('Автостопом по галактике')
        assert collector.get_list_of_favorites_books() == ['Сияние', 'Винни-Пух и все-все-все', 'Автостопом по галактике']
