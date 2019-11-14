# test_SWAPI.py
from swapi import People
from assertpy import assert_that


def test_get_people():
    # Tests that SWAPI either turns an OK status or returns a 500 status
    people = People.get_people()
    if people.ok:
        assert_that(people.status_code).is_equal_to(200)
    else:
        assert_that(people.status_code).is_equal_to(500)
