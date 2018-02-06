---
UID: NA:ntddpcm
ms.assetid: 4c1a57f9-d840-38ed-bb42-d0f3a4965439
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# ntddpcm.h header



ntddpcm.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_GET_TUPLE_DATA](ni-ntddpcm-ioctl_get_tuple_data.md) | This request retrieves tuple data that is stored in a PC Card's or CardBus card's attribute memory. |
| [IOCTL_SOCKET_INFORMATION](ni-ntddpcm-ioctl_socket_information.md) | This request retrieves socket information for the socket that is indicated by the caller. |


## Functions
| Title | Description |
| ---- |:---- |
| [PCMCIA_IS_WRITE_PROTECTED](nc-ntddpcm-pcmcia_is_write_protected.md) | The PCMCIA_IS_WRITE_PROTECTED interface routine returns the write-protect condition of a PCMCIA memory card. |
| [PCMCIA_MODIFY_MEMORY_WINDOW](nc-ntddpcm-pcmcia_modify_memory_window.md) | The PCMCIA_MODIFY_MEMORY_WINDOW interface routine sets the attributes of a memory window for a PCMCIA memory card. The memory window is mapped by the PCMCIA bus driver. |
| [PCMCIA_SET_VPP](nc-ntddpcm-pcmcia_set_vpp.md) | The PCMCIA_SET_VPP interface routine sets the power level of the Vpp PCMCIA pin (secondary power source). |



## Structures
| Title | Description |
| ---- |:---- |
| [_PCMCIA_INTERFACE_STANDARD](ns-ntddpcm-_pcmcia_interface_standard.md) | The PCMCIA bus driver makes the PCMCIA_INTERFACE_STANDARD interface available to PCMCIA memory card drivers in order to allow them to make direct calls to the bus driver without allocating IRPs. |
| [_PCMCIA_SOCKET_INFORMATION](ns-ntddpcm-_pcmcia_socket_information.md) | The PCMCIA_SOCKET_INFORMATION structure is used in conjunction with the IOCTL_SOCKET_INFORMATION request to retrieve socket configuration and state data. |
| [_TUPLE_REQUEST](ns-ntddpcm-_tuple_request.md) | The TUPLE_REQUEST structure is used in conjunction with the IOCTL_GET_TUPLE_DATA request to retrieve tuple data from a PC Card's or CardBus card's attribute memory. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_PCMCIA_CONTROLLER_CLASS](ne-ntddpcm-_pcmcia_controller_class.md) | The PCMCIA_CONTROLLER_CLASS enumeration lists the different sorts of PC Card and CardBus controllers. |