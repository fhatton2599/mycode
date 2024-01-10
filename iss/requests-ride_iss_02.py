#!/usr/bin/python3
"""tracking the iss using
   api.open-notify.org/astros.json | Alta3 Research"""

import requests

MAJORTOM = 'http://api.open-notify.org/astros.json'

def main():
    """runtime code"""

    groundctrl = requests.get(MAJORTOM)
    helmetson = groundctrl.json()

    print("\n\nPeople in Space:", helmetson['number'])

    people = helmetson['people']
    for person in people:
        print(f"{person['name']} on the {person['craft']}")

if __name__ == "__main__":
    main()
