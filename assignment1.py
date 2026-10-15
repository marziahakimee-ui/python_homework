# Task 1: Hello
def hello():
    return "Hello!"


# Task 2: Greet
def greet(name):
    return f"Hello, {name}!"


# Task 3: Calculator
def calc(first, second, operation="multiply"):
    try:
        if operation == "add":
            return first + second
        elif operation == "subtract":
            return first - second
        elif operation == "multiply":
            return first * second
        elif operation == "divide":
            return first / second
        elif operation == "modulo":
            return first % second
        elif operation == "int_divide":
            return first // second
        elif operation == "power":
            return first ** second
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return f"You can't {operation} those values!"


# Task 4: Data Type Conversion
def data_type_conversion(value, type):
    try:
        if type == "float":
            return float(value)
        elif type == "str":
            return str(value)
        elif type == "int":
            return int(value)
    except ValueError:
        return f"You can't convert {value} into a {type}."


# Task 5: Grading System
def grade(*args):
    try:
        average = sum(args) / len(args)

        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ZeroDivisionError):
        return "Invalid data was provided."


# Task 6: Repeat
def repeat(string, count):
    result = ""

    for _ in range(count):
        result += string

    return result


# Task 7: Student Scores
def student_scores(operation, **kwargs):
    if operation == "best":
        return max(kwargs, key=kwargs.get)
    elif operation == "mean":
        return sum(kwargs.values()) / len(kwargs)


# Task 8: Titleize
def titleize(string):
    little_words = ["a", "on", "an", "the", "of", "and", "is", "in"]
    words = string.split()

    result = []

    for i, word in enumerate(words):
        if i == 0 or i == len(words) - 1 or word not in little_words:
            result.append(word.capitalize())
        else:
            result.append(word)

    return " ".join(result)


# Task 9: Hangman
def hangman(secret, guess):
    result = ""

    for letter in secret:
        if letter in guess:
            result += letter
        else:
            result += "_"

    return result


# Task 10: Pig Latin
def pig_latin(string):
    vowels = "aeiou"
    words = string.split()
    result = []

    for word in words:
        if word[0] in vowels:
            result.append(word + "ay")
        elif word.startswith("qu"):
            result.append(word[2:] + "quay")
        else:
            first_vowel = 0

            while first_vowel < len(word) and word[first_vowel] not in vowels:
                first_vowel += 1

            result.append(word[first_vowel:] + word[:first_vowel] + "ay")

    return " ".join(result)
