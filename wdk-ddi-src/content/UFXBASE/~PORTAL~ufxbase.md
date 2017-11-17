# Declarations in the ufxbase header
This header Ufxbase contains these programming interfaces:

Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_INTERNAL_USBFN_DESCRIPTOR_UPDATE IOCTL](ni-ufxbase-ioctl-internal-usbfn-descriptor-update.md) | The USB function class extension sends this request to the client driver to update to the endpoint descriptor for the specified endpoint. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [UFX_CLASS_FUNCTIONS enumeration](ne-ufxbase--ufx-class-functions.md) | TBD |
| [USBFN_ACTION enumeration](ne-ufxbase--usbfn-action.md) | Defines special actions UFX should take when the client driver calls the UfxDevicePortDetectCompleteEx function. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_UFX_CLASS callback function](nc-ufxbase-pfn-ufx-class.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UFXENDPOINT_INIT structure](ns-ufxbase--ufxendpoint-init.md) | TBD |
| [UFX_DEVICE_CAPABILITIES structure](ns-ufxbase--ufx-device-capabilities.md) | The UFX_DEVICE_CAPABILITIES structure is used USB to define properties of the Universal Serial Bus (USB) device created by the controller. |
| [UFX_GLOBALS structure](ns-ufxbase--ufx-globals.md) | TBD |
| [UFX_HARDWARE_FAILURE_CONTEXT structure](ns-ufxbase--ufx-hardware-failure-context.md) | The UFX_HARDWARE_FAILURE_CONTEXT structure is used to define controller-specific hardware failure properties. |

This header is used in these topics:

- [usbref](..content/_usbref)
