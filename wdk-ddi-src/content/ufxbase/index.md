---
UID: NA:ufxbase
ms.assetid: 852c4c2e-5b6d-36ca-9232-1ebba63ec849
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# ufxbase.h header



ufxbase.h contains the following programming interfaces:




## IOCTLs
| Title | Description |
| ---- |:---- |
| [IOCTL_INTERNAL_USBFN_DESCRIPTOR_UPDATE](ni-ufxbase-ioctl_internal_usbfn_descriptor_update.md) | The USB function class extension sends this request to the client driver to update to the endpoint descriptor for the specified endpoint. |




## Structures
| Title | Description |
| ---- |:---- |
| [_UFX_DEVICE_CAPABILITIES](ns-ufxbase-_ufx_device_capabilities.md) | The UFX_DEVICE_CAPABILITIES structure is used USB to define properties of the Universal Serial Bus (USB) device created by the controller. |
| [_UFX_HARDWARE_FAILURE_CONTEXT](ns-ufxbase-_ufx_hardware_failure_context.md) | The UFX_HARDWARE_FAILURE_CONTEXT structure is used to define controller-specific hardware failure properties. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_USBFN_ACTION](ne-ufxbase-_usbfn_action.md) | Defines special actions UFX should take when the client driver calls the UfxDevicePortDetectCompleteEx function. |