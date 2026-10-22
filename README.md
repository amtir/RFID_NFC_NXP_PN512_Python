# RFID / NFC Reader — NXP PN512 with Python on Raspberry Pi

Reads **MIFARE / NFC tag UIDs** with the **NXP EXPLORE-NFC** shield (PN512 chip) on a Raspberry Pi, through the **NXP NFC Reader Library** and the **nxppy** Python wrapper over **SPI**.

## Features

- Installs the NXP NFC Reader Library (Debian package) on Raspberry Pi OS
- Enables the SPI bus to talk to the PN512 shield
- Python script that detects cards and prints their UID continuously

## Hardware

| Component | Details |
|-----------|---------|
| Board | Raspberry Pi |
| Reader | NXP EXPLORE-NFC (PN512), plugged on the GPIO header |
| Interface | SPI |
| Tags | MIFARE Classic / Ultralight, NTAG and other ISO 14443A cards |

## Installation

```bash
sudo apt-get update
sudo apt-get install build-essential cmake python3-dev

# NXP NFC Reader Library (included in lib/)
sudo dpkg -i lib/NFC-Reader-Library-4.010-2.deb

# Python wrapper
sudo pip3 install -r requirements.txt

# Enable SPI: raspi-config → Interface Options → SPI, then reboot
sudo raspi-config
grep spi /boot/config.txt      # → dtparam=spi=on
```

The full installation session is in [`docs/installation_log.txt`](docs/installation_log.txt). Screenshots of downloading the library from NXP are in [`photos/`](photos/).

## Usage

```bash
sudo python3 src/nxp_test.py
```

```
Card UID : 04XXXXXXXXXXXX
Card UID : 04XXXXXXXXXXXX
```

The UID is masked here; `04` is the manufacturer code for NXP.

## Repository Structure

```
.
├── src/nxp_test.py      # Card UID reader
├── lib/                 # NXP NFC Reader Library (.deb)
├── docs/                # Installation session log
├── photos/              # Library download screenshots
└── requirements.txt
```

## Tech Stack

Python 3 · nxppy · NXP NFC Reader Library · PN512 · SPI · Raspberry Pi · RFID / NFC (ISO 14443A)

## Author

**Akram M'Tir**, [@amtir](https://github.com/amtir)
