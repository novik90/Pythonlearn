from people import Person, anyone_like_dogs
import pytest


@pytest.fixture()
def person(**kwargs):
    def _person(**kwargs):
        return Person(name="Bob", **kwargs)

    return _person


def test_anyone_like_dogs_true(person):
    people = [
        person(favorite_animal="Bob"),
        person(favorite_animal="cat"),
        person(favorite_animal="dog")
    ]
    assert anyone_like_dogs(people) is True
