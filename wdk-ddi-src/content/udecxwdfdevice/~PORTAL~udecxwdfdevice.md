# Udecxwdfdevice.h header


This header is used by unknown technology.

Udecxwdfdevice.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [UDECX_WDF_DEVICE_CONFIG_INIT function](nf-udecxwdfdevice-udecx-wdf-device-config-init.md) | Initializes a UDECX_WDF_DEVICE_CONFIG structure. |
| [UdecxInitializeWdfDeviceInit function](nf-udecxwdfdevice-udecxinitializewdfdeviceinit.md) | Initializes device initialization operations when the Plug and Play (PnP) manager reports the existence of a device. |
| [UdecxWdfDeviceAddUsbDeviceEmulation function](nf-udecxwdfdevice-udecxwdfdeviceaddusbdeviceemulation.md) | Initializes a framework device object to support operations related to a host controller and a virtual USB device attached to the controller. |
| [UdecxWdfDeviceResetComplete function](nf-udecxwdfdevice-udecxwdfdeviceresetcomplete.md) | Informs the USB device emulation class extension (UdeCx) that the reset operation on the specified controller has competed. |
| [UdecxWdfDeviceTryHandleUserIoctl function](nf-udecxwdfdevice-udecxwdfdevicetryhandleuserioctl.md) | Attempts to handle an IOCTL request sent by a user-mode software. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [EVT_UDECX_WDF_DEVICE_QUERY_USB_CAPABILITY callback](nc-udecxwdfdevice-evt-udecx-wdf-device-query-usb-capability.md) | The UDE client driver's implementation to determine the capabilities that are supported by the emulated USB host controller. |
| [EVT_UDECX_WDF_DEVICE_RESET callback](nc-udecxwdfdevice-evt-udecx-wdf-device-reset.md) | The UDE client driver's implementation to reset the emulated host controller or the devices attached to it. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [UDECX_WDF_DEVICE_CONFIG structure](ns-udecxwdfdevice--udecx-wdf-device-config.md) | Contains pointers to event callback functions implemented by the UDE client driver for a USB host controller. Initialize this structure by calling UDECX_WDF_DEVICE_CONFIG_INIT. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [UDECX_WDF_DEVICE_RESET_ACTION enumeration](ne-udecxwdfdevice--udecx-wdf-device-reset-action.md) | Defines values that indicate the types of reset operation supported by an emulated USB host controller. |
