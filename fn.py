import random


def roll_dice(n: int) -> int:
    return random.randint(1, n)


def cuenta_chiste() -> str:
    chistes = [
        '¿Qué le dice un jardinero a otro? Seamos felices mientras podamos',
        '¿Qué dice una cereza mirándose al espejo? "¿Ceré eza?"',
        '¿Por qué las focas del circo miran siempre hacia arriba? Porque es dónde están los focos',
        'Iba a contar un chiste sobre sodio... pero Na',
        '¿Por qué la gallina cuida tanto a sus pollitos? Porque le costó un huevo tenerlos',
        '¿Quién es el padre de ET? Donette'
    ]
    return random.choice(chistes)


def roll_d6() -> int:
    return random.randint(1, 6)


def get_d6_img(n: int) -> str:
    return f'https://bormolina.github.io/assets/d6_{n}_sd.webm'


def get_url_flag(country: str) -> str:
    base_url = "https://countryflagsapi.com/png/"
    return base_url + country

