# Smclib.h header


This header is used by Smart Card Reader Devices. For more information, see
- [Smart Card Reader Devices](../_smartcrd/index.md)

Smclib.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [CLOCK_RATE_CONVERSION structure](ns-smclib--clock-rate-conversion.md) | The CLOCK_RATE_CONVERSION structure holds a value that determines the duration of a bit of data and the corresponding maximum operating frequency that accompanies the indicated bit length. |
| [PTS_DATA structure](ns-smclib--pts-data.md) | The PTS_DATA structure is used for protocol type selection (PTS). |
| [SCARD_CARD_CAPABILITIES structure](ns-smclib--scard-card-capabilities.md) | The SCARD_CARD_CAPABILITIES structure declaration defines the data that is stored in the CardCapabilites member of the SMARTCARD_EXTENSION structure and holds all information that is specific to the particular smart card that is currently used. |
| [SCARD_READER_CAPABILITIES structure](ns-smclib--scard-reader-capabilities.md) | The SCARD_READER_CAPABILITIES structure holds state information about the smart card reader. |
| [SMARTCARD_EXTENSION structure](ns-smclib--smartcard-extension.md) | The SMARTCARD_EXTENSION structure is used by both the smart card reader driver and the smart card driver library to access all other smart card data structures. |
| [SMARTCARD_EXTENSION structure](ns-smclib--smartcard-extension~r1.md) | The SMARTCARD_EXTENSION structure is used by both the smart card reader driver and the smart card driver library to access all other smart card data structures. |
| [SMARTCARD_REPLY structure](ns-smclib--smartcard-reply.md) | Describes the reply buffer received from the smart card. |
| [SMARTCARD_REQUEST structure](ns-smclib--smartcard-request.md) | Describes the request buffer that contains data to send to the card. |
| [T0_DATA structure](ns-smclib--t0-data.md) | The T0_DATA structure is used by the smart card driver library to process T0 I/O. |
| [T1_DATA structure](ns-smclib--t1-data.md) | The T1_DATA structure is used by the smart card driver library to process T1 I/O. |
| [VENDOR_ATTR structure](ns-smclib--vendor-attr.md) | The VENDOR_ATTR structure defines the data that is stored in the VendorAttr member of the SMARTCARD_EXTENSION structure. VENDOR_ATTR also holds information that identifies the smart card reader, such as the vendor name, unit number, and serial number. |
