from cat import Cat
from dog import Dog


class Gibrid(Dog, Cat):
    def print_create(self):
        print(f'We created catdog')