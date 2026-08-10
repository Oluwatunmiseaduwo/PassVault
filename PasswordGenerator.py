import secrets
import string

def generate_password(length, use_upper=True, use_digits=True,
                      use_symbols=True, use_periods_only=False):

    if length < 6:
        raise ValueError("Password length must be at least 6")

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits

    if use_periods_only:
        symbols = ".,"

    else:
        symbols = string.punctuation

    CharacterPool = lowercase
    password = [secrets.choice(lowercase)]

    if use_upper:
        password.append(secrets.choice(uppercase))
        CharacterPool += uppercase

    if use_digits:
        password.append(secrets.choice(digits))
        CharacterPool += digits

    if use_symbols:
        password.append(secrets.choice(symbols))
        CharacterPool += symbols

    while len(password) < length:
        password.append(secrets.choice(CharacterPool))

    secrets.SystemRandom().shuffle(password)

    return "".join(password)

"""    
    characters = string.ascii_lowercase

    if use_upper:
        characters += string.ascii_uppercase

    if use_digits:
            characters += string.digits

    if use_symbols:
        if use_periods_only:
            characters += ".,"

        else:
            characters += string.punctuation

    password = ""

    for _ in range(length):
        password += secrets.choice(characters)

    return password
"""