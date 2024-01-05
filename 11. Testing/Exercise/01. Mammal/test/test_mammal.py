from unittest import TestCase, main
from project.mammal import Mammal


class TestMammals(TestCase):

    def test_is_mammal_initialized_correctly(self):
        mammal = Mammal('Test', 'hydrochoerus', "sound")
        self.assertEqual('Test', mammal.name)
        self.assertEqual('hydrochoerus', mammal.type)
        self.assertEqual("sound", mammal.sound)
        self.assertEqual('animals', mammal._Mammal__kingdom)

    def test_make_sound(self):
        mammal = Mammal('Test', 'hydrochoerus', "sound")

        self.assertEqual(f"Test makes sound", mammal.make_sound())

    def test_get_kingdom(self):
        mammal = Mammal('Test', 'hydrochoerus', "sound")
        self.assertEqual("animals", mammal.get_kingdom())

    def test_get_info(self):
        mammal = Mammal('Test', 'hydrochoerus', "sound")
        self.assertEqual("Test is of type hydrochoerus", mammal.info())


if __name__ == '__main__':
    main()
