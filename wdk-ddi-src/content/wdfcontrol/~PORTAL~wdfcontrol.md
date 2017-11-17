# Declarations in the wdfcontrol header
This header Wdfcontrol contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [WdfControlFinishInitializing function](nf-wdfcontrol-wdfcontrolfinishinitializing.md) | The WdfControlFinishInitializing method informs the framework that a driver has finished initializing a specified control device object. |
| [WdfControlDeviceInitSetShutdownNotification function](nf-wdfcontrol-wdfcontroldeviceinitsetshutdownnotification.md) | The WdfControlDeviceInitSetShutdownNotification method sets shutdown notification information for a control device object. |
| [WdfControlDeviceInitAllocate function](nf-wdfcontrol-wdfcontroldeviceinitallocate.md) | The WdfControlDeviceInitAllocate method allocates a WDFDEVICE_INIT structure that a driver uses when creating a new control device object. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [WDF_DEVICE_SHUTDOWN_FLAGS enumeration](ne-wdfcontrol--wdf-device-shutdown-flags.md) | The WDF_DEVICE_SHUTDOWN_FLAGS enumeration defines flags that identify types of shutdown notifications that a driver can receive. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PFN_WDFCONTROLDEVICEINITALLOCATE callback function](nc-wdfcontrol-pfn-wdfcontroldeviceinitallocate.md) | TBD |
| [PFN_WDFCONTROLFINISHINITIALIZING callback function](nc-wdfcontrol-pfn-wdfcontrolfinishinitializing.md) | TBD |
| [PFN_WDFCONTROLDEVICEINITSETSHUTDOWNNOTIFICATION callback function](nc-wdfcontrol-pfn-wdfcontroldeviceinitsetshutdownnotification.md) | TBD |

This header is used in these topics:

- [wdf](..content/_wdf)
