---
UID: NA:ufxclient
---

# Ufxclient.h header

## -description

This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Ufxclient.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [UFX_DEVICE_CALLBACKS_INIT function](nf-ufxclient-ufx_device_callbacks_init.md) | The UFX_DEVICE_CALLBACKS_INIT macro initializes the UFX_DEVICE_CALLBACKS structure. |
| [UFX_DEVICE_CAPABILITIES_INIT function](nf-ufxclient-ufx_device_capabilities_init.md) | The UFX_DEVICE_CAPABILITIES_INIT macro the initializes the UFX_DEVICE_CAPABILITIES structure. |
| [UFX_ENDPOINT_CALLBACKS_INIT function](nf-ufxclient-ufx_endpoint_callbacks_init.md) | The UFX_ENDPOINT_CALLBACKS_INIT macro initializes the UFX_ENDPOINT_CALLBACKS structure. |
| [UfxDeviceCreate function](nf-ufxclient-ufxdevicecreate.md) | Creates a UFX device object, registers event callback routines, and specifies capabilities specific to the controller. |
| [UfxDeviceEventComplete function](nf-ufxclient-ufxdeviceeventcomplete.md) | Informs UFX that the client driver has completed processing a UFX callback function. |
| [UfxDeviceIoControl function](nf-ufxclient-ufxdeviceiocontrol.md) | Passes non-internal IOCTLs from user-mode to UFX. |
| [UfxDeviceIoInternalControl function](nf-ufxclient-ufxdeviceiointernalcontrol.md) | Passes kernel mode IOCTLs to UFX. |
| [UfxDeviceNotifyAttach function](nf-ufxclient-ufxdevicenotifyattach.md) | Notifies UFX that the device's USB cable has been attached. |
| [UfxDeviceNotifyDetach function](nf-ufxclient-ufxdevicenotifydetach.md) | Notifies UFX that the device's USB cable has been detached. |
| [UfxDeviceNotifyHardwareFailure function](nf-ufxclient-ufxdevicenotifyhardwarefailure.md) | Notifies UFX about a non-recoverable hardware failure in the controller. |
| [UfxDeviceNotifyHardwareReady function](nf-ufxclient-ufxdevicenotifyhardwareready.md) | Notifies UFX that the hardware is ready. |
| [UfxDeviceNotifyReset function](nf-ufxclient-ufxdevicenotifyreset.md) | Notifies UFX about a USB bus reset event. |
| [UfxDeviceNotifyResume function](nf-ufxclient-ufxdevicenotifyresume.md) | Notifies UFX about a USB bus resume event. |
| [UfxDeviceNotifySuspend function](nf-ufxclient-ufxdevicenotifysuspend.md) | Notifies UFX about a USB bus suspend event. |
| [UfxDevicePortDetectComplete function](nf-ufxclient-ufxdeviceportdetectcomplete.md) | Notifies UFX about the port type that was detected. |
| [UfxDevicePortDetectCompleteEx function](nf-ufxclient-ufxdeviceportdetectcompleteex.md) | Notifies UFX about the port type that was detected, and optionally requests an action. |
| [UfxDeviceProprietaryChargerDetectComplete function](nf-ufxclient-ufxdeviceproprietarychargerdetectcomplete.md) | Notifies UFX about a detected proprietary port/charger type. |
| [UfxEndpointCreate function](nf-ufxclient-ufxendpointcreate.md) | Creates an endpoint object. |
| [UfxEndpointGetCommandQueue function](nf-ufxclient-ufxendpointgetcommandqueue.md) | Returns the command queue previously created by UfxEndpointCreate. |
| [UfxEndpointGetTransferQueue function](nf-ufxclient-ufxendpointgettransferqueue.md) | Returns the transfer queue previously created by UfxEndpointCreate. |
| [UfxEndpointInitSetEventCallbacks function](nf-ufxclient-ufxendpointinitseteventcallbacks.md) | Initialize a UFXENDPOINT_INIT structure. |
| [UfxEndpointNotifySetup function](nf-ufxclient-ufxendpointnotifysetup.md) | Notifies UFX when the client driver receives a setup packet from the host. |
| [UfxFdoInit function](nf-ufxclient-ufxfdoinit.md) | Initializes the WDFDEVICE_INIT structure that the client driver subsequently provides when it calls WdfDeviceCreate. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_UFX_DEVICE_CALLBACKS structure](ns-ufxclient-_ufx_device_callbacks.md) | The UFX_DEVICE_CALLBACKS structure is used to define then event callback functions supported by the client driver. |
| [_UFX_ENDPOINT_CALLBACKS structure](ns-ufxclient-_ufx_endpoint_callbacks.md) | The UFX_ENDPOINT_CALLBACKS structure is used to define then event callback functions supported by the client driver. |
