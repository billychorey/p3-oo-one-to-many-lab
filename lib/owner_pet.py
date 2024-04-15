class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise ValueError(f"Invalid pet type: {pet_type}. Must be one of {', '.join(self.PET_TYPES)}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        if owner:
            owner.add_pet(self)
        self.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self.pet_list = []

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Argument 'pet' must be an instance of Pet class")
        self.pet_list.append(pet)
        pet.owner = self

    def pets(self):
        return self.pet_list

    def sort_pets_by_name(self):
        return sorted(self.pet_list, key=lambda pet: pet.name)

    def get_sorted_pets(self):
        return sorted(self.pet_list, key=lambda pet: pet.name)
