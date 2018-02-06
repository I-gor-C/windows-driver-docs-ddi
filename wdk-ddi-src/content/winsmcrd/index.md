---
UID: NA:winsmcrd
ms.assetid: 54c6f73d-38ec-3d87-b18f-4f7647666e1a
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# winsmcrd.h header



winsmcrd.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_SMARTCARD_EJECT](ni-winsmcrd-ioctl_smartcard_eject.md) | The IOCTL_SMARTCARD_EJECT request ejects the currently inserted smart card from the smart card reader. |
| [IOCTL_SMARTCARD_GET_ATTRIBUTE](ni-winsmcrd-ioctl_smartcard_get_attribute.md) | The IOCTL_SMARTCARD_GET_ATTRIBUTE control code queries for smart card attribues. |
| [IOCTL_SMARTCARD_GET_LAST_ERROR](ni-winsmcrd-ioctl_smartcard_get_last_error.md) | The IOCTL_SMARTCARD_GET_LAST_ERROR request retrieves the error code of the most previous operation because there is no option to return an error code immediately after an overlapped operation is complete. |
| [IOCTL_SMARTCARD_GET_STATE](ni-winsmcrd-ioctl_smartcard_get_state.md) | The IOCTL_SMARTCARD_GET_STATE control code gets the current status of the smart card. |
| [IOCTL_SMARTCARD_IS_ABSENT](ni-winsmcrd-ioctl_smartcard_is_absent.md) | The IOCTL_SMARTCARD_IS_ABSENT control code returns immediately with STATUS_SUCCESS if no smart card is currently detected. |
| [IOCTL_SMARTCARD_IS_PRESENT](ni-winsmcrd-ioctl_smartcard_is_present.md) | The IOCTL_SMARTCARD_IS_PRESENT control code detects whether a smart card is currently detected. |
| [IOCTL_SMARTCARD_POWER](ni-winsmcrd-ioctl_smartcard_power.md) | Windows may require a driver to have this IOCTL to be NOP and return success. |
| [IOCTL_SMARTCARD_SET_ATTRIBUTE](ni-winsmcrd-ioctl_smartcard_set_attribute.md) | The IOCTL_SMARTCARD_SET_ATTRIBUTE control code sets an attribute and returns STATUS_SUCCESS on SCARD_ATTR_DEVICE_IN_USE; otherwise, it returns STATUS_NOT_SUPPORTED. |
| [IOCTL_SMARTCARD_SET_PROTOCOL](ni-winsmcrd-ioctl_smartcard_set_protocol.md) | Sets the procotol the driver communicates to the smart card with after the card is detected. |
| [IOCTL_SMARTCARD_SWALLOW](ni-winsmcrd-ioctl_smartcard_swallow.md) | The IOCTL_SMARTCARD_SWALLOW request causes the smart card reader to swallow the card. |
| [IOCTL_SMARTCARD_TRANSMIT](ni-winsmcrd-ioctl_smartcard_transmit.md) | Transmits data from the client to the detected smart card in ISO7816-4 compliant APDU. |




## Structures
| Title | Description |
| ---- |:---- |
| [_SCARD_IO_REQUEST](ns-winsmcrd-_scard_io_request.md) | This structure is used to identify a smart card I/O request. |