"""
CP1404/CP5632 Practical
Hex colours in a dictionary
"""

COLOUR_TO_HEX = {"darkorchid": "#9932cc", "french blue": "#0072bb", "lapis lazuli": "#26619c", "limegreen": "#32cd32",
                 "magenta": "#ff00ff", "mint": "#3eb489", "orange peel": "#ff9f00", "orchid": "#da70d6",
                 "pistachio": "#93c572", "raspberry": "#e30b5d"}

colour = input("Enter colour: ").lower()
while colour != "":
    try:
        print(colour, "is", COLOUR_TO_HEX[colour])
    except KeyError:
        print("Invalid colour")
    colour = input("Enter colour: ").lower()
