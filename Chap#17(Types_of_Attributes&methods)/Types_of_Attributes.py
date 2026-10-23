class Animal:
    # Class attribute
    species = "Animal"

    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age

    # Instance method
    def make_sound(self):
        return "Some generic animal sound"

    # Class method
    @classmethod
    def get_species(cls):
        return cls.species

    # Static method
    @staticmethod
    def is_animal():
        return True
