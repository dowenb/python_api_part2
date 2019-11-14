# swapi.py
"""makes requests to the Starwars API and returns responce objects"""
import requests

class People:
    """Get one or many people from the Starwars API"""
    def __init__(self):
        self.base_url = 'https://swapi.co/api/'

    @classmethod
    def get_people(cls):
        """Returns a response object for all the star wars people"""
        # TODO: handle paging
        people_url = 'https://swapi.co/api/people/'
        return requests.get(people_url)

    @classmethod
    def get_person(cls):
        """Returns a single star wars person"""
        person_url = 'https://swapi.co/api/people/1'
        return requests.get(person_url)
