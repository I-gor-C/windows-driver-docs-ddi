# Ntddpcm.h header


This header is used by PCMCIA. For more information, see
- [PCMCIA](../_PCMCIA/index.md)

Ntddpcm.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PCMCIA_IS_WRITE_PROTECTED callback](nc-ntddpcm-pcmcia-is-write-protected.md) | The PCMCIA_IS_WRITE_PROTECTED interface routine returns the write-protect condition of a PCMCIA memory card. |
| [PCMCIA_MODIFY_MEMORY_WINDOW callback](nc-ntddpcm-pcmcia-modify-memory-window.md) | The PCMCIA_MODIFY_MEMORY_WINDOW interface routine sets the attributes of a memory window for a PCMCIA memory card. The memory window is mapped by the PCMCIA bus driver. |
| [PCMCIA_SET_VPP callback](nc-ntddpcm-pcmcia-set-vpp.md) | The PCMCIA_SET_VPP interface routine sets the power level of the Vpp PCMCIA pin (secondary power source). |

## Structures

| Title   | Description   |
| ---- |:---- |
| [PCMCIA_INTERFACE_STANDARD structure](ns-ntddpcm--pcmcia-interface-standard.md) | The PCMCIA bus driver makes the PCMCIA_INTERFACE_STANDARD interface available to PCMCIA memory card drivers in order to allow them to make direct calls to the bus driver without allocating IRPs. |
| [PCMCIA_SOCKET_INFORMATION structure](ns-ntddpcm--pcmcia-socket-information.md) | The PCMCIA_SOCKET_INFORMATION structure is used in conjunction with the IOCTL_SOCKET_INFORMATION request to retrieve socket configuration and state data. |
| [TUPLE_REQUEST structure](ns-ntddpcm--tuple-request.md) | The TUPLE_REQUEST structure is used in conjunction with the IOCTL_GET_TUPLE_DATA request to retrieve tuple data from a PC Card's or CardBus card's attribute memory. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_GET_TUPLE_DATA IOCTL](ni-ntddpcm-ioctl-get-tuple-data.md) | This request retrieves tuple data that is stored in a PC Card's or CardBus card's attribute memory. |
| [IOCTL_SOCKET_INFORMATION IOCTL](ni-ntddpcm-ioctl-socket-information.md) | This request retrieves socket information for the socket that is indicated by the caller. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [PCMCIA_CONTROLLER_CLASS enumeration](ne-ntddpcm--pcmcia-controller-class.md) | The PCMCIA_CONTROLLER_CLASS enumeration lists the different sorts of PC Card and CardBus controllers. |
