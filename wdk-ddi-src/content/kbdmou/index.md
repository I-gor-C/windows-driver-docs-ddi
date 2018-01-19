---
UID : NA:kbdmou
ms.assetid : 7916a78e-8897-372f-8e32-22081a9589d3
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# kbdmou.h header



kbdmou.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_INTERNAL_KEYBOARD_CONNECT](ni-kbdmou-ioctl_internal_keyboard_connect.md) | The IOCTL_INTERNAL_KEYBOARD_CONNECT request connects the Kbdclass service to the keyboard device. |
| [IOCTL_INTERNAL_KEYBOARD_DISCONNECT](ni-kbdmou-ioctl_internal_keyboard_disconnect.md) | The IOCTL_INTERNAL_KEYBOARD_DISCONNECT request is completed with a status of STATUS_NOT_IMPLEMENTED. Note that a Plug and Play keyboard can be added or removed by the Plug and Play manager. |
| [IOCTL_INTERNAL_MOUSE_CONNECT](ni-kbdmou-ioctl_internal_mouse_connect.md) | The IOCTL_INTERNAL_MOUSE_CONNECT request connects Mouclass service to a mouse device. |
| [IOCTL_INTERNAL_MOUSE_DISCONNECT](ni-kbdmou-ioctl_internal_mouse_disconnect.md) | The IOCTL_INTERNAL_MOUSE_DISCONNECT request is completed by Moufiltr with an error status of STATUS_NOT_IMPLEMENTED. |


## Functions
| Title | Description |
| ---- |:---- |
| [PSERVICE_CALLBACK_ROUTINE](nc-kbdmou-pservice_callback_routine.md) | A function driver calls the class service callback in its ISR dispatch completion routine. The class service callback transfers input data from the input data buffer of a device to the class data queue. |



## Structures
| Title | Description |
| ---- |:---- |
| [_CONNECT_DATA](ns-kbdmou-_connect_data.md) | CONNECT_DATA specifies information that Kbdclass and Mouclass use to connect to a keyboard or mouse port. |