import string
from random import randint, choice


def strong_password_generator() -> str:
    """
    Generates and prints strong random password with:
        - lowercase and uppercase characters;
        - digits;
        - punctuation characters;
        - length from 14 to 64 symbols.
    :return: <String> password for testing.
    """
    allowed_chars = string.ascii_letters + string.digits + string.punctuation
    password_length = randint(14, 64)
    password = "".join(choice(allowed_chars) for _ in range(password_length))

    return password


if __name__ == "__main__":
    print(strong_password_generator())
