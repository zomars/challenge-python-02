# Resolve the problem!!
import string
import random

SYMBOLS = list('!"#$%&\'()*+,-./:;?@[]^_`{|}~')


def get_random_lowercase():
    return random.choice(string.ascii_lowercase)


def get_random_uppercase():
    return random.choice(string.ascii_uppercase)


def get_random_symbol():
    return random.choice(SYMBOLS)


def get_random_number():
    return random.randint(0, 9)


character_getter_dictionary = {
    'lowercase': get_random_lowercase,
    'uppercase': get_random_uppercase,
    'symbol': get_random_symbol,
    'number': get_random_number,
}


def generate_password():
    """
        La contraseña debe entre 8 y 16 caracteres
        1.  Necesito una función que me regrese de manera aleatoria un carácter
            de los permitidos.
        2.  Necesito una función que me regrese de manera aleatoría una longitud
            entre 8 y 16 caracteres.
        3.  Necesito decidir cuantos caracteres de cada tipo va  tener la
            contraseña (minúsculas, mayúsculas, números y símbolos).
    """
    number_of_characters = random.randint(8, 16)  # [2]
    new_password = ''
    available_getters = list(character_getter_dictionary.keys())

    while len(new_password) < number_of_characters:
        if len(available_getters) > 0:
            # Elige al azar el tipo de carácter a utilizar
            character_getter_key = random.choice(available_getters)
            print('Tipo de carácter', character_getter_key)
            # Ya usamos ese tipo de carácter, lo quitamos
            available_getters.remove(character_getter_key)
            # Obtenemos la funcion generadora de caraceter
            character_getter = character_getter_dictionary[
                character_getter_key
            ]
            # Introduce el carácter nuevo a la contraseña
            new_password = new_password + str(character_getter())
        else:
            # Reiniciamos los tipos de caracteres disponibles
            available_getters = list(character_getter_dictionary.keys())

    print('new_password', new_password)
    return new_password


def validate(password):

    if len(password) >= 8 and len(password) <= 16:
        has_lowercase_letters = False
        has_numbers = False
        has_uppercase_letters = False
        has_symbols = False

        for char in password:
            if char in string.ascii_lowercase:
                has_lowercase_letters = True
                break

        for char in password:
            if char in string.ascii_uppercase:
                has_uppercase_letters = True
                break

        for char in password:
            if char in string.digits:
                has_numbers = True
                break

        for char in password:
            if char in SYMBOLS:
                has_symbols = True
                break

        if has_symbols and has_numbers and has_lowercase_letters and has_uppercase_letters:
            return True
    return False


def run():
    password = generate_password()
    if validate(password):
        print('Secure Password')
    else:
        print('Insecure Password')


if __name__ == '__main__':
    run()
