from lib.most_often import *

def test_object_initialization():
    most_often = MostOften([1, 2, 3, 1, 2, 1])
    assert most_often.starting_list == [1, 2, 3, 1, 2, 1]

def test_adding_new_element_to_empty_list():
    most_often = MostOften([])
    most_often.add_new(2)
    assert most_often.starting_list == [2]

def test_adding_new_element_to_existing_list():
    most_often = MostOften([1, 2, 3, 1, 2, 1])
    most_often.add_new(2)
    assert most_often.starting_list == [1, 2, 3, 1, 2, 1, 2]

def test_adding_string_element_to_existing_list():
    most_often = MostOften([1, 2, 3, 1, 2, 1])
    most_often.add_new("hello")
    assert most_often.starting_list == [1, 2, 3, 1, 2, 1, "hello"]

def test_get_most_often_winner():
    most_often = MostOften([1, 2, 3, 1, 2, 1])
    assert most_often.get_most_often() == 1

def test_get_most_often_no_winner():
    most_often = MostOften([1, 2, 3, 1, 2])
    assert most_often.get_most_often() == "no clear winner"

def test_get_most_often_count_updated_correctly():
    most_often = MostOften([1, 3, 1, 1, 2, 1, 1, 3, 3, 3, 3, 3])
    assert most_often.get_most_often() == 3

def test_get_most_often_float():
    most_often = MostOften([3, 3, 3, 3.2, 3.2, 3.2])
    assert most_often.get_most_often() == "no clear winner"

def test_get_most_often_integers_and_floats():
    most_often = MostOften([3, 2, 2, 3.0, 3.0])
    assert most_often.get_most_often() == 3

def test_get_most_often_integers_and_floats_no_winner():
    most_often = MostOften([3, 2, 2.0, 3.0])
    assert most_often.get_most_often() == "no clear winner"

def test_get_most_often_integers_and_floats_no_winner():
    most_often = MostOften([3, 2, 2.0, -3])
    assert most_often.get_most_often() == 2