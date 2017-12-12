---
UID: NA:
---

# Kbdmou.h header

## -description

This header is used by Human Interface Devices (HID). For more information, see
- [Human Interface Devices (HID)](../_hid/index.md)

Kbdmou.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [PSERVICE_CALLBACK_ROUTINE callback](nc-kbdmou-pservice_callback_routine.md) | A function driver calls the class service callback in its ISR dispatch completion routine. The class service callback transfers input data from the input data buffer of a device to the class data queue. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_CONNECT_DATA structure](ns-kbdmou-_connect_data.md) | CONNECT_DATA specifies information that Kbdclass and Mouclass use to connect to a keyboard or mouse port. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_INTERNAL_KEYBOARD_CONNECT IOCTL](ni-kbdmou-ioctl_internal_keyboard_connect.md) | The IOCTL_INTERNAL_KEYBOARD_CONNECT request connects the Kbdclass service to the keyboard device. |
| [IOCTL_INTERNAL_KEYBOARD_DISCONNECT IOCTL](ni-kbdmou-ioctl_internal_keyboard_disconnect.md) | The IOCTL_INTERNAL_KEYBOARD_DISCONNECT request is completed with a status of STATUS_NOT_IMPLEMENTED. Note that a Plug and Play keyboard can be added or removed by the Plug and Play manager. |
| [IOCTL_INTERNAL_MOUSE_CONNECT IOCTL](ni-kbdmou-ioctl_internal_mouse_connect.md) | The IOCTL_INTERNAL_MOUSE_CONNECT request connects Mouclass service to a mouse device. |
| [IOCTL_INTERNAL_MOUSE_DISCONNECT IOCTL](ni-kbdmou-ioctl_internal_mouse_disconnect.md) | The IOCTL_INTERNAL_MOUSE_DISCONNECT request is completed by Moufiltr with an error status of STATUS_NOT_IMPLEMENTED. |
