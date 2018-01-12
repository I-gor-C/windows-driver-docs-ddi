---
UID: NA:ntddpcm
---

# Ntddpcm.h header

## -description

This header is used by PCMCIA. For more information, see
- [PCMCIA](../_PCMCIA/index.md)

Ntddpcm.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [_PCMCIA_INTERFACE_STANDARD structure](ns-ntddpcm-_pcmcia_interface_standard.md) | The PCMCIA bus driver makes the PCMCIA_INTERFACE_STANDARD interface available to PCMCIA memory card drivers in order to allow them to make direct calls to the bus driver without allocating IRPs. |
| [_PCMCIA_SOCKET_INFORMATION structure](ns-ntddpcm-_pcmcia_socket_information.md) | The PCMCIA_SOCKET_INFORMATION structure is used in conjunction with the IOCTL_SOCKET_INFORMATION request to retrieve socket configuration and state data. |
| [_TUPLE_REQUEST structure](ns-ntddpcm-_tuple_request.md) | The TUPLE_REQUEST structure is used in conjunction with the IOCTL_GET_TUPLE_DATA request to retrieve tuple data from a PC Card's or CardBus card's attribute memory. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_GET_TUPLE_DATA IOCTL](ni-ntddpcm-ioctl_get_tuple_data.md) | This request retrieves tuple data that is stored in a PC Card's or CardBus card's attribute memory. |
| [IOCTL_SOCKET_INFORMATION IOCTL](ni-ntddpcm-ioctl_socket_information.md) | This request retrieves socket information for the socket that is indicated by the caller. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_PCMCIA_CONTROLLER_CLASS enumeration](ne-ntddpcm-_pcmcia_controller_class.md) | The PCMCIA_CONTROLLER_CLASS enumeration lists the different sorts of PC Card and CardBus controllers. |
