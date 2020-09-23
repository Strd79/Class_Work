import pdb
from models.owner import Owner 
from models.animal import Animal 
import repositories.owner_repository as owner_repository
import repositories.animal_repository as animal_repository

owner_1 = Owner("Craig", "Alexander")
owner_2 = Owner ("David", "Strain")
animal_1 = Animal("Kass", 15, "Dog", owner_2)
animal_2 = Animal("Tila", 16, "Cat", owner_1)
owner_repository.save(owner_1)
owner_repository.save(owner_2)
animal_repository.save(animal_1)
animal_repository.save(animal_2)