from barcodes import Ean13
import pygame
import math
import random
import numpy as np
import pandas as pd


class AirConditioning:
    __status = False
    __temperature = None

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, new):
        pass

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, new):
        pass

    def __repr__(self):
        if self.__status:
            return f'Кондиционер включен. Температурный режим: {self.__temperature} градусов'
        return 'Кондиционер выключен.'

    def switch_on(self):
        self.__status = True
        self.__temperature = 18

    def switch_off(self):
        self.__status = False
        self.__temperature = None

    def reset(self):
        if self.__status:
            self.__temperature = 18

    def get_temperature(self):
        return self.__temperature

    def raise_temperature(self):
        if self.__temperature is not None:
            if self.__temperature < 43:
                self.__temperature += 1

    def lower_temperature(self):
        if self.__temperature is not None:
            if self.__temperature > 0:
                self.__temperature -= 1


class Product:
    __code = None

    def __init__(self, code: int, cost=0, name=None):
        self.__code = code
        self.__cost = cost
        self.name = name

    def __eq__(self, other):
        if self.__code == other.__code:
            return True
        return False

    def __hash__(self):
        return hash(self.__code)

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, new):
        self.__code = new

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, new):
        pass

    @property
    def country(self):
        if not self.__code:
            return None

        country_code = self.__code // 10 ** 10
        if country_code in Ean13.country_by_code:
            return Ean13.country_by_code[country_code]
        else:
            return 'Любая страна'

    @country.setter
    def country(self, new):
        pass

    def __repr__(self):
        return f'Наименование: {self.name} \n' \
               f'Код товара: {self.code} \n' \
               f'Производитель: {self.country} \n' \
               f'Цена: {self.cost}'


class ShoppingCart:
    __cart = {}
    __total_cost = 0

    def __init__(self, file_name):
        self.__file = file_name

        self.__cart = {}
        with open(self.__file, 'a', encoding='utf8') as _:
            pass
        with open(self.__file, encoding='utf8') as f:
            name = ''
            cost = -1
            code = None
            number = 0
            for line in f:
                if 'Наименование' in line:
                    name = line.split()[1]
                elif 'Код' in line:
                    code = int(line.split()[2])
                elif 'Цена' in line:
                    cost = int(line.split()[1])
                elif 'Количество' in line:
                    number = int(line.split()[1])

                if name and code and (cost != -1) and number:
                    self.__cart[Product(code, cost, name)] = number
                    name = ''
                    cost = -1
                    code = None
                    number = 0

    @property
    def cart(self):
        return self.__cart

    @cart.setter
    def cart(self, new):
        pass

    @property
    def total_cost(self):
        return sum([prod.cost * num for prod, num in self.__cart.items()])

    @total_cost.setter
    def total_cost(self, new):
        pass

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, new):
        pass

    def add_product(self, product: Product, number=1):
        self.__cart[product] = self.__cart.get(product, 0) + number
        with open(self.file, 'w', encoding='utf8') as f:
            f.writelines([f'{prod} \nКоличество: {num}\n\n' for prod, num in self.__cart.items()])

    def del_product(self, product: Product):
        self.__cart[product] = self.__cart.get(product, 1) - 1
        if self.__cart[product] == 0:
            del self.__cart[product]
        with open(self.file, 'w', encoding='utf8') as f:
            f.writelines([f'{prod} \nКоличество: {num}\n\n' for prod, num in self.__cart.items()])


class Track:
    def __init__(self, name: str, musician: str, duration: str, year: int, file: str):
        self.name = name
        self.musician = musician
        self.duration = duration
        self.year = year
        self.file = file
        self.playing = 0

    def play(self):
        if not self.playing:
            self.playing = 2
            pygame.mixer.init()
            pygame.mixer.music.load(self.file)
            pygame.mixer.music.play()
        else:
            self.playing = 2
            pygame.mixer.music.unpause()

    def pause(self):
        if self.playing:
            self.playing = 1
            pygame.mixer.music.pause()

    def stop(self):
        if self.playing:
            self.playing = 0
            pygame.mixer.music.stop()
            pygame.mixer.quit()

    def __repr__(self):
        if self.playing == 2:
            return f'ИГРАЕТ| {self.name} - {self.musician} ({self.year}) [{self.duration}]'
        elif self.playing == 1:
            return f'ПАУЗА | {self.name} - {self.musician} ({self.year}) [{self.duration}]'
        else:
            return f'------| {self.name} - {self.musician} ({self.year}) [{self.duration}]'


class Album:
    def __init__(self, name: str, year: int, tracks=[]):
        self.name = name
        self.year = year
        self.tracks = tracks
        self.chosen_track = 0

    def add_track(self, track):
        self.tracks.append(track)

    def print_info(self):
        print('\t\t', self)
        print(*self.tracks, sep='\n')

    def __repr__(self):
        return f'Альбом: {self.name} - {self.year}'

    def next_track(self):
        self.stop()
        self.chosen_track += 1
        if self.chosen_track >= len(self.tracks):
            self.chosen_track = 0

        self.play()

    def play(self):
        self.tracks[self.chosen_track].play()

    def pause(self):
        self.tracks[self.chosen_track].pause()

    def stop(self):
        self.tracks[self.chosen_track].stop()


class Subject:
    def __init__(self, name: str, group: int, number: int, teacher: str):
        self.group = group
        self.name = name
        self.number = number
        self.teacher = teacher


class GroupSchedule:
    time = ['9:00-10:35', '10:50-12:25', '12:40-14:15', '14:30-16:05', '16:20-17:55', '18:10-19:45']

    def __init__(self, group: int):
        self.schedule = pd.DataFrame()
        self.schedule['time'] = GroupSchedule.time
        for day in ('monday', 'tuesday', 'wednesday', 'thisday', 'friday', 'saturday', 'sunday'):
            self.schedule[day] = 0
        self.group = group

    def __eq__(self, other):
        return self.group == other.group

    def add_subject(self, subject: Subject):
        if subject.group == self.group:
            for _ in range(subject.number):
                flag = False
                for day in ('monday', 'tuesday', 'wednesday', 'thisday', 'friday', 'saturday'):
                    for index, row in self.schedule.iterrows():
                        if row[day] == 0:
                            self.schedule.at[index, day] = subject.name
                            flag = True
                            break
                    if flag:
                        break


class FacultySchedule:
    groups_schedules = {}

    def add_subject(self, subject: Subject):
        if subject.group in self.groups_schedules.keys():
            self.groups_schedules[subject.group].add_subject(subject)
        else:
            self.groups_schedules[subject.group] = GroupSchedule(subject.group)
            self.groups_schedules[subject.group].add_subject(subject)

    def print_group_schedule(self, group):
        if group in self.groups_schedules:
            print(self.groups_schedules[group].schedule)


class RunModel:

    def __init__(self, fps, caption, window_size=(400, 400)):
        self.fps = fps
        pygame.init()
        self.window_size = window_size
        self.objects = pygame.sprite.Group()
        self.display = pygame.display.set_mode(self.window_size)
        self.width, self.height = pygame.display.get_window_size()
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.escape = False

    def update(self):
        self.objects.update()

    def catch(self):
        for obj in self.objects:
            obj.catch(*self.window_size)

    def draw(self):
        self.display.fill((0, 0, 0))
        self.objects.draw(self.display)

    def handle(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.escape = True
                pygame.quit()

    def run(self):
        while not self.escape:
            self.handle()
            self.catch()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.fps)


class Molecule(pygame.sprite.Sprite):
    molecules = []
    power = 0.002
    contact_distance = 50

    def __init__(self, x, y, size, speed=1, color=(128, 128, 128)):
        pygame.sprite.Sprite.__init__(self)
        self.size = size
        self.color = color
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.size/2, self.size/2), self.size/2)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed = speed
        self.direction = random.uniform(0, 2 * math.pi)
        self.speed_x = math.cos(self.direction) * self.speed
        self.speed_y = math.sin(self.direction) * self.speed

        Molecule.molecules.append(self)

    def __sub__(self, other):
        return math.sqrt((self.rect.x - other.rect.x) ** 2 + (self.rect.y - other.rect.y) ** 2) \
            - self.size / 2 - other.size / 2

    @property
    def mass(self):
        return 0.01 * self.size

    @mass.setter
    def mass(self, new):
        pass

    def catch(self, width=400, height=400):
        for mol in Molecule.molecules:
            if 0 < self - mol < self.contact_distance:
                self.speed_x += Molecule.power * \
                                (abs(self.speed_x) + 0.5 / Molecule.power) * np.sign(self.rect.x - mol.rect.x) * (
                                        mol.mass / self.mass)

                self.speed_y += Molecule.power * \
                                (abs(self.speed_y) + 0.5 / Molecule.power) * np.sign(self.rect.y - mol.rect.y) * (
                                        mol.mass / self.mass)

        if self.rect.x + self.speed_x < self.contact_distance:
            self.speed_x -= Molecule.power * (self.rect.x - self.contact_distance) * 2
        elif self.rect.x + self.speed_x > width - self.contact_distance:
            self.speed_x -= Molecule.power * (self.contact_distance - (self.rect.x - width)) * 2

        if self.rect.y + self.speed_y < self.contact_distance:
            self.speed_y -= Molecule.power * (self.rect.y - self.contact_distance) * 2
        elif self.rect.y + self.speed_y > height - self.contact_distance:
            self.speed_y -= Molecule.power * (self.contact_distance - (self.rect.y - height)) * 2

        while not (40 < self.rect.x + self.speed_x < width - 40) \
                or not (40 < self.rect.y + self.speed_y < height - 40):
            self.direction = random.uniform(0, 2 * math.pi)
            self.speed_x = math.cos(self.direction) * self.speed
            self.speed_y = math.sin(self.direction) * self.speed

    def update(self):

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
