# Ufxbase.h header


This header is used by unknown technology.

Ufxbase.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [UFX_DEVICE_CAPABILITIES structure](ns-ufxbase--ufx-device-capabilities.md) | The UFX_DEVICE_CAPABILITIES structure is used USB to define properties of the Universal Serial Bus (USB) device created by the controller. |
| [UFX_HARDWARE_FAILURE_CONTEXT structure](ns-ufxbase--ufx-hardware-failure-context.md) | The UFX_HARDWARE_FAILURE_CONTEXT structure is used to define controller-specific hardware failure properties. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_INTERNAL_USBFN_DESCRIPTOR_UPDATE IOCTL](ni-ufxbase-ioctl-internal-usbfn-descriptor-update.md) | The USB function class extension sends this request to the client driver to update to the endpoint descriptor for the specified endpoint. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [USBFN_ACTION enumeration](ne-ufxbase--usbfn-action.md) | Defines special actions UFX should take when the client driver calls the UfxDevicePortDetectCompleteEx function. |
