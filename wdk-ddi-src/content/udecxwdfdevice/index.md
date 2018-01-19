---
UID : NA:udecxwdfdevice
ms.assetid : d0a5a6e1-0a40-3c57-8704-6ba20faac4d9
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# udecxwdfdevice.h header



udecxwdfdevice.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [EVT_UDECX_WDF_DEVICE_QUERY_USB_CAPABILITY](nc-udecxwdfdevice-evt_udecx_wdf_device_query_usb_capability.md) | The UDE client driver's implementation to determine the capabilities that are supported by the emulated USB host controller. |
| [EVT_UDECX_WDF_DEVICE_RESET](nc-udecxwdfdevice-evt_udecx_wdf_device_reset.md) | The UDE client driver's implementation to reset the emulated host controller or the devices attached to it. |
| [UDECX_WDF_DEVICE_CONFIG_INIT](nf-udecxwdfdevice-udecx_wdf_device_config_init.md) | Initializes a UDECX_WDF_DEVICE_CONFIG structure. |
| [UdecxInitializeWdfDeviceInit](nf-udecxwdfdevice-udecxinitializewdfdeviceinit.md) | Initializes device initialization operations when the Plug and Play (PnP) manager reports the existence of a device. |
| [UdecxWdfDeviceAddUsbDeviceEmulation](nf-udecxwdfdevice-udecxwdfdeviceaddusbdeviceemulation.md) | Initializes a framework device object to support operations related to a host controller and a virtual USB device attached to the controller. |
| [UdecxWdfDeviceResetComplete](nf-udecxwdfdevice-udecxwdfdeviceresetcomplete.md) | Informs the USB device emulation class extension (UdeCx) that the reset operation on the specified controller has competed. |
| [UdecxWdfDeviceTryHandleUserIoctl](nf-udecxwdfdevice-udecxwdfdevicetryhandleuserioctl.md) | Attempts to handle an IOCTL request sent by a user-mode software. |



## Structures
| Title | Description |
| ---- |:---- |
| [_UDECX_WDF_DEVICE_CONFIG](ns-udecxwdfdevice-_udecx_wdf_device_config.md) | Contains pointers to event callback functions implemented by the UDE client driver for a USB host controller. Initialize this structure by calling UDECX_WDF_DEVICE_CONFIG_INIT. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_UDECX_WDF_DEVICE_RESET_ACTION](ne-udecxwdfdevice-_udecx_wdf_device_reset_action.md) | Defines values that indicate the types of reset operation supported by an emulated USB host controller. |