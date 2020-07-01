# RFID Mifare NFC tag NXP-PN512 Python

* Installation of the NFC-Reader-Library and the nxppy Python wrapper for interfacing with the PN512-based NXP EXPLORE-NFC shield for the Raspberry Pi. 

* Activation / Enabling the SPI bus of the Raspberry-Pi to communicate with the RFID shield.

* Test the Python wrapper to read a UID Card.


## Usage

```bash
sudo python3 nxp_test.py 

Card UID : 04263B6A643481
Card UID : 04263B6A643481
Card UID : 04263B6A643481
Card UID : 04263B6A643481
Card UID : 04263B6A643481
Card UID : 04263B6A643481
Card UID : 04263B6A643481
```

## Installation

```bash
sudo apt-get update
sudo apt-get install build-essential cmake python3-dev python2.7-dev

sudo dpkg -i NFC-Reader-Library-4.010-2.deb

pip install nxppy
pip3 install nxppy
sudo pip install nxppy
sudo pip3 install nxppy

Activate/Enable the SPI bus
sudo raspi-config    
Reboot

cat /boot/config.txt | grep spi
dtparam=spi=on
```


## License

[DRINKOTEC](https://drinkotec.ch/)



