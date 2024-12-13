"""
CP1404 Prac 06
Estimate Time: 20 mins
Actual Time: 25 mins
"""
from prac_06.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    programming_languages = [python, ruby, visual_basic]
    print_dynamic_languages(programming_languages)


def print_dynamic_languages(languages):
    """print list of dynamically typed languages in languages"""
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
