from solution import RunModel, Molecule
from random import randint


def randcolor(a: int, b: int):
    return randint(a, b), randint(a, b), randint(a, b)


model = RunModel(30, 'Molecules simulation', window_size=(900, 600))

Molecule.power = 0.02
Molecule.contact_distance = 70

molecule_big1 = Molecule(400, 400, speed=randint(1, 3), size=randint(100, 120), color=(255, 50, 50))
molecule_big2 = Molecule(400, 500, speed=randint(1, 3), size=randint(100, 120), color=(0, 128, 255))

model.objects.add(molecule_big1)
model.objects.add(molecule_big2)

molecule1 = Molecule(100, 100, speed=randint(3, 5), size=randint(30, 40), color=randcolor(128, 255))
molecule2 = Molecule(100, 200, speed=randint(3, 5), size=randint(30, 40), color=randcolor(128, 255))
molecule3 = Molecule(100, 300, speed=randint(3, 5), size=randint(30, 40), color=randcolor(128, 255))
molecule4 = Molecule(200, 100, speed=randint(3, 5), size=randint(30, 40), color=randcolor(128, 255))

model.objects.add(molecule1)
model.objects.add(molecule2)
model.objects.add(molecule3)
model.objects.add(molecule4)

molecule1 = Molecule(100, 100, speed=randint(3, 5), size=randint(30, 40), color=randcolor(200, 255))
molecule2 = Molecule(100, 200, speed=randint(3, 5), size=randint(30, 40), color=randcolor(200, 255))
molecule3 = Molecule(100, 300, speed=randint(3, 5), size=randint(30, 40), color=randcolor(200, 255))
molecule4 = Molecule(200, 100, speed=randint(3, 5), size=randint(30, 40), color=randcolor(200, 255))

model.objects.add(molecule1)
model.objects.add(molecule2)
model.objects.add(molecule3)
model.objects.add(molecule4)

model.run()
