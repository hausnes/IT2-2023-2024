# "Until version 3.10, Python never had a feature that implemented what the switch statement does in other programming languages."
# Kjelde: https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/

lang = input("What's the programming language you want to learn? ")

match lang:
    case "JavaScript":
        print("You can become a web developer.")
    case "Python":
        print("You can become a Data Scientist")
    case "PHP":
        print("You can become a backend developer")
    case "Solidity":
        print("You can become a Blockchain developer")
    case "Java":
        print("You can become a mobile app developer")
    case _:
        print("The language doesn't matter, what matters is solving problems.")