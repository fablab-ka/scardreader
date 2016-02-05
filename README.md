# ID Reader

Python script to read the id of a mifare card (e.g. with REINERSCT basic reader).

## Installaion on Raspberry PI

http://enerds.eu/blog/reiner-cyberjack-rfid-basis.html

## Usage

python read_id.py

returns the ID in hex of the available card.

## Error Codes

* FAILED - failed to establish context
* NO_READER - no Reader connected
* NO_CARD - no card found