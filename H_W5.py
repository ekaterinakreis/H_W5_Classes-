from datetime import date

class Musician:
    def __init__(self, instrument, sex, year_of_birth, city):
        self.instrument = instrument
        self.sex = sex
        self.year_of_birth = year_of_birth
        self.age = self.get_age()
        self.city = city


    def get_age(self):
        today = date.today()
        return today.year - self.year_of_birth

    def play_music(self):
        print(f' I play my {self.instrument}')

    def concert(self):
        print(f'I give a concert in the city {self.city}')

class Pianist(Musician):
    def __init__(self, instrument, sex, year_of_birth, city):
        super().__init__(instrument, sex, year_of_birth, city)
        # self.instrument = instrument

    def play_music(self):
        print(f'I play my {self.instrument}')

    def play_modern(self):
        print(f'I change my {self.instrument} to synthesizer')

    def concerts(self):
        self.city = "Roma"
        print(f'I give a new concert in the city {self.city}')

class Singer(Musician):
    def __init__(self, instrument, sex, year_of_birth, city, song):
        super().__init__(instrument, sex, year_of_birth, city)
        self.song = song

    def play_music(self):
        print(f"I`m singing {self.song}!")

    def performance(self):
        print('I`m singing and dancing!')


Richter = Pianist('Piano', 'male', 1966, 'London')
print(Richter.instrument)
print(Richter.__dict__)
Richter.play_music()
Richter.play_modern()
Richter.concert()
# Richter.concerts()

Bessonov = Pianist("Grand_piano", "male", 2002, "Moscow")
print(Bessonov.__dict__)
Bessonov.play_modern()
Bessonov.concerts()

Adele = Singer('Voice','female', 1988, "London", "Skyfall")
print(Adele.__dict__)
Adele.concert()
Adele.play_music()
Adele.performance()
