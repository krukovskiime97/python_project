class English:

    def greeting(self):
        print('Hello!')


class Franch:

    def greeting(self):
        print('Bounjur')


eng = English()
fr = Franch()

language = [eng, fr]


for lang in language:
    lang.greeting()
