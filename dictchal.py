#!/bin/env python3

#Select character
char_name = input(" Which character do you want to know about? (Starlord, Mystique, Hulk)")
print(f"You chose {char_name.capitalize()}!")

#select hero statistic
char_stat = input(" What statistic do you want to know about? (real name, powers, archenemy)")
print(f"You want to learn about {char_stat.capitalize()}!")

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

#link to dictionary and print
value = marvelchars[char_name][char_stat]
print(f"{char_name.capitalize()}'s {char_stat.capitalize()} is: {value}")
