#!/usr/bin/python3

import nxppy
import time

mifare = nxppy.Mifare()

# Print card UIDs as they are detected
while True:
    try:
        uid = mifare.select()
        print("Card UID : {}".format(uid))
    except nxppy.SelectError:
        # SelectError is raised if no card is in the field.
        pass

    time.sleep(0.5)
