from PasswordGenerator import generate_password
from PasswordChecker import (CheckStrength, CalculateEntropy, CrackTime,
                             CheckCommonPassword)
""", CheckHistory, SavePasswordHistory"""


print("========================\n"
      " Password Generator Tool\n"
      "========================")

length = int(input("Choose Password Length: "))
uppercase = input("Use Uppercase yes/no? ").lower() == "yes"
numbers = input("Use Numbers? yes/no? ").lower() == "yes"
symbols = input("Use Symbols yes/no? ").lower() == "yes"
periods = input("Only use . and , yes/no? ").lower() == "yes"

while True:

    password = generate_password(length, uppercase, numbers, symbols, periods)

    strength = CheckStrength(password)

    if strength == "Strong Strength":
        break
    print("Generated password was not strong enough; Trying again...")

print("\nGenerated Password: ")
print(password)

entropy = CalculateEntropy(password)
time = CrackTime(entropy)

print("\nSecurity Analysis: "
      "---------------------")
print("Strength: \n",strength)
print("Entropy: \n", entropy, "bits")
print("Estimated Crack Time: \n", time)

if CheckCommonPassword(password):
    print("Warning: This password is in the common password list.")

else:
    print("Not found in common password list.")
"""
if CheckHistory(password):
    print("Warning: You have generated this password before!")

else:
    SavePasswordHistory(password)
    print("This Password will be saved to history.")"""