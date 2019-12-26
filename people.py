class Person(object):
    def __init__(self, name, favorite_animal=None):
        self.name = name
        self.favorite_animal = favorite_animal


def anyone_like_dogs(people):
    return any(
        [p.favorite_animal == "dog" for p in people]
    )
