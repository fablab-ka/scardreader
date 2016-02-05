#! /usr/bin/env python

from smartcard.scard import *
import smartcard.util

hresult, hcontext = SCardEstablishContext(SCARD_SCOPE_USER)

if hresult == SCARD_S_SUCCESS:

  hresult, readers = SCardListReaders(hcontext, [])

  if len(readers) > 0:

    reader = readers[0]

    hresult, hcard, dwActiveProtocol = SCardConnect(
        hcontext,
        reader,
        SCARD_SHARE_SHARED,
        SCARD_PROTOCOL_T0 | SCARD_PROTOCOL_T1)

    if hresult == 0:
      hresult, response = SCardTransmit(hcard,dwActiveProtocol,[0xFF,0xCA,0x00,0x00,0x00])

      print(smartcard.util.toHexString(response))
    else:
      print("NO_CARD")
  else:
    print("NO_READER")
else:
  print("FAILED")