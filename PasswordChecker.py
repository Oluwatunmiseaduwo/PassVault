import math
import string

def CheckStrength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak Strength"

    elif score <= 4:
        return "Medium Strength"

    else:
        return "Strong Strength"

def CalculateEntropy(password):
    pool = 0

    if any(char.islower() for char in password):
        pool += 26

    if any(char.isupper() for char in password):
        pool += 26

    if any(char.isdigit() for char in password):
        pool += 10

    if any (char in string.punctuation for char in password):
        pool += len(string.punctuation)

    entropy = len(password) * math.log2(pool)

    return round(entropy, 3)

def CrackTime(entropy):

    guesses = 2 ** entropy

    guesses_per_second = 1_000_000_000

    seconds = guesses / guesses_per_second

    if seconds < 60:
        return f"{round(seconds, 2)} seconds"

    minutes = seconds / 60

    if minutes < 60:
        return f"{round(minutes, 2)} minutes"

    hours = minutes / 60

    if hours < 24:
        return f"{round(hours, 2)} hours"

    days = hours / 24

    if days < 365:
        return f"{round(days, 2)} days"

    years = days / 365

    if years < 1000:
        return f"{round(years/1000, 2)} years"

    elif years < 1_000_000:
        return f"{round(years/1_000_000, 2)} thousand years"

    elif years < 1_000_000_000:
        return f"{round(years/1_000_000_000, 2)} million years"

    else:
        return f"{round(years,1)} billion years"

def CheckCommonPassword(password):

    try:
        with open("CommonPasswords.txt", "r") as file:
            common = file.read().splitlines()

            if password.lower() in common:
                return True
    except FileNotFoundError:
        return False

    return False
"""
def CheckHistory(password):

    try:
        with open("PasswordHistory.txt", "r") as file:
            history = file.read().splitlines()

            if password in history:
                return True

    except FileNotFoundError:
        return False

    return False

def SavePasswordHistory(password):

    with open("PasswordHistory.txt", "a") as file:
        file.write(password + "\n")
"""