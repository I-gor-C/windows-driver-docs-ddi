---
UID: NA:wdfcontrol
---

# Wdfcontrol.h header

## -description

This header is used by Windows Driver Framework. For more information, see
- [Windows Driver Framework](../_wdf/index.md)

Wdfcontrol.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [PFN_WDFCONTROLDEVICEINITALLOCATE function](nc-wdfcontrol-pfn_wdfcontroldeviceinitallocate.md) | The WdfControlDeviceInitAllocate method allocates a WDFDEVICE_INIT structure that a driver uses when creating a new control device object. |
| [PFN_WDFCONTROLDEVICEINITSETSHUTDOWNNOTIFICATION function](nc-wdfcontrol-pfn_wdfcontroldeviceinitsetshutdownnotification.md) | The WdfControlDeviceInitSetShutdownNotification method sets shutdown notification information for a control device object. |
| [PFN_WDFCONTROLFINISHINITIALIZING function](nc-wdfcontrol-pfn_wdfcontrolfinishinitializing.md) | The WdfControlFinishInitializing method informs the framework that a driver has finished initializing a specified control device object. |
| [WdfControlDeviceInitAllocate function](nf-wdfcontrol-wdfcontroldeviceinitallocate.md) | The WdfControlDeviceInitAllocate method allocates a WDFDEVICE_INIT structure that a driver uses when creating a new control device object. |
| [WdfControlDeviceInitSetShutdownNotification function](nf-wdfcontrol-wdfcontroldeviceinitsetshutdownnotification.md) | The WdfControlDeviceInitSetShutdownNotification method sets shutdown notification information for a control device object. |
| [WdfControlFinishInitializing function](nf-wdfcontrol-wdfcontrolfinishinitializing.md) | The WdfControlFinishInitializing method informs the framework that a driver has finished initializing a specified control device object. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_WDF_DEVICE_SHUTDOWN_FLAGS enumeration](ne-wdfcontrol-_wdf_device_shutdown_flags.md) | The WDF_DEVICE_SHUTDOWN_FLAGS enumeration defines flags that identify types of shutdown notifications that a driver can receive. |
