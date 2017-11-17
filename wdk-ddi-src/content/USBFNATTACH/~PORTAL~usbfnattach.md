# Declarations in the usbfnattach header
This header Usbfnattach contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [USBFN_GET_ATTACH_ACTION_ABORT callback](nc-usbfnattach-usbfn-get-attach-action-abort.md) | The filter driver's implementation to abort an attach-detect operation. |
| [USBFN_GET_ATTACH_ACTION callback](nc-usbfnattach-usbfn-get-attach-action.md) | The filter driver's implementation that gets invoked when charger is attached to the port. |
| [USBFN_SET_DEVICE_STATE callback](nc-usbfnattach-usbfn-set-device-state.md) | The filter driver's implementation to set the device state and operating bus speed. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [USBFN_ATTACH_ACTION enumeration](ne-usbfnattach--usbfn-attach-action.md) | Defines the actions that the Universal Serial Bus (USB) function stack takes when a device is attached to a USB port. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [USBFN_INTERFACE_ATTACH structure](ns-usbfnattach--usbfn-interface-attach.md) | Stores pointers to driver-implemented callback functions for handling attach and detach operations. |
| [USBFN_ON_ATTACH structure](ns-usbfnattach--usbfn-on-attach.md) | Describes the detected port type and attach action. |

This header is used in these topics:

- [usbref](..content/_usbref)
