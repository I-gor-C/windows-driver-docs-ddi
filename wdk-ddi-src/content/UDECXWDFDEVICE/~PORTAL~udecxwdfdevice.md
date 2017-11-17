# Declarations in the udecxwdfdevice header
This header Udecxwdfdevice contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [*PFN_UDECXWDFDEVICETRYHANDLEUSERIOCTL callback function](nc-udecxwdfdevice-pfn-udecxwdfdevicetryhandleuserioctl.md) | TBD |
| [*PFN_UDECXWDFDEVICEADDUSBDEVICEEMULATION callback function](nc-udecxwdfdevice-pfn-udecxwdfdeviceaddusbdeviceemulation.md) | TBD |
| [*PFN_UDECXWDFDEVICERESETCOMPLETE callback function](nc-udecxwdfdevice-pfn-udecxwdfdeviceresetcomplete.md) | TBD |
| [EVT_UDECX_WDF_DEVICE_QUERY_USB_CAPABILITY callback](nc-udecxwdfdevice-evt-udecx-wdf-device-query-usb-capability.md) | The UDE client driver's implementation to determine the capabilities that are supported by the emulated USB host controller. |
| [*PFN_UDECXINITIALIZEWDFDEVICEINIT callback function](nc-udecxwdfdevice-pfn-udecxinitializewdfdeviceinit.md) | TBD |
| [EVT_UDECX_WDF_DEVICE_RESET callback](nc-udecxwdfdevice-evt-udecx-wdf-device-reset.md) | The UDE client driver's implementation to reset the emulated host controller or the devices attached to it. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UDECX_WDF_DEVICE_CONFIG structure](ns-udecxwdfdevice--udecx-wdf-device-config.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [UDECX_WDF_DEVICE_CONFIG_INIT function](nf-udecxwdfdevice-udecx-wdf-device-config-init.md) | TBD |
| [UdecxWdfDeviceTryHandleUserIoctl function](nf-udecxwdfdevice-udecxwdfdevicetryhandleuserioctl.md) | Attempts to handle an IOCTL request sent by a user-mode software. |
| [UdecxWdfDeviceResetComplete function](nf-udecxwdfdevice-udecxwdfdeviceresetcomplete.md) | Informs the USB device emulation class extension (UdeCx) that the reset operation on the specified controller has competed. |
| [UdecxWdfDeviceAddUsbDeviceEmulation function](nf-udecxwdfdevice-udecxwdfdeviceaddusbdeviceemulation.md) | Initializes a framework device object to support operations related to a host controller and a virtual USB device attached to the controller. |
| [UdecxInitializeWdfDeviceInit function](nf-udecxwdfdevice-udecxinitializewdfdeviceinit.md) | Initializes device initialization operations when the Plug and Play (PnP) manager reports the existence of a device. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [UDECX_WDF_DEVICE_RESET_ACTION enumeration](ne-udecxwdfdevice--udecx-wdf-device-reset-action.md) | Defines values that indicate the types of reset operation supported by an emulated USB host controller. |

This header is used in these topics:

- [usbref](..content/_usbref)
