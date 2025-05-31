class Dog:
    approved_breeds = [
        "Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle",
        "French Bulldog", "Pug", "Pointer"
    ]

    def __init__(self, name="Unknown", breed="Unknown"):
        self.name = name
        self.breed = breed  # Use the setter to ensure validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0 or len(value) > 25:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unknown"
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value != "Unknown" and value not in Dog.approved_breeds:
            print("Breed must be in list of approved breeds.")
            self._breed = "Unknown"
        else:
            self._breed = value
