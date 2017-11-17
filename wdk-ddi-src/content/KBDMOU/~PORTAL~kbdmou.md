# Declarations in the kbdmou header
This header Kbdmou contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PSERVICE_CALLBACK_ROUTINE callback](nc-kbdmou-pservice-callback-routine.md) | A function driver calls the class service callback in its ISR dispatch completion routine. The class service callback transfers input data from the input data buffer of a device to the class data queue. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_INTERNAL_KEYBOARD_DISABLE IOCTL](ni-kbdmou-ioctl-internal-keyboard-disable.md) | TBD |
| [IOCTL_INTERNAL_MOUSE_CONNECT IOCTL](ni-kbdmou-ioctl-internal-mouse-connect.md) | The IOCTL_INTERNAL_MOUSE_CONNECT request connects Mouclass service to a mouse device. |
| [IOCTL_INTERNAL_MOUSE_DISABLE IOCTL](ni-kbdmou-ioctl-internal-mouse-disable.md) | TBD |
| [IOCTL_INTERNAL_MOUSE_ENABLE IOCTL](ni-kbdmou-ioctl-internal-mouse-enable.md) | TBD |
| [IOCTL_INTERNAL_KEYBOARD_ENABLE IOCTL](ni-kbdmou-ioctl-internal-keyboard-enable.md) | TBD |
| [IOCTL_INTERNAL_KEYBOARD_DISCONNECT IOCTL](ni-kbdmou-ioctl-internal-keyboard-disconnect.md) | The IOCTL_INTERNAL_KEYBOARD_DISCONNECT request is completed with a status of STATUS_NOT_IMPLEMENTED. Note that a Plug and Play keyboard can be added or removed by the Plug and Play manager. |
| [IOCTL_INTERNAL_KEYBOARD_CONNECT IOCTL](ni-kbdmou-ioctl-internal-keyboard-connect.md) | The IOCTL_INTERNAL_KEYBOARD_CONNECT request connects the Kbdclass service to the keyboard device. |
| [IOCTL_INTERNAL_MOUSE_DISCONNECT IOCTL](ni-kbdmou-ioctl-internal-mouse-disconnect.md) | The IOCTL_INTERNAL_MOUSE_DISCONNECT request is completed by Moufiltr with an error status of STATUS_NOT_IMPLEMENTED. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [CONNECT_DATA structure](ns-kbdmou--connect-data.md) | CONNECT_DATA specifies information that Kbdclass and Mouclass use to connect to a keyboard or mouse port. |

This header is used in these topics:

- [hid](..content/_hid)
