#!/usr/bin/env python3
"""Alta3 Research | Exploring interfaces library"""

import netifaces

def main():
    print(netifaces.interfaces())

    for i in netifaces.interfaces():
        print('\n********Details of Interface - ' + i + ' ************')
        try:    # This is a new line, you also need to indent the code below this line by 4 whitespaces
            print('MAC: ', end = '')
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
            print('IP: ', end = '')
            print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
        except:
            print('Could not collect adapter info')

if __name__ == "__main__":
    main()
