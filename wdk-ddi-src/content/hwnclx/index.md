---
UID: NA:hwnclx
---

# Hwnclx.h header

## -description

This header is used by Hardware notifications. For more information, see
- [Hardware notifications](../_gpiobtn/index.md)

Hwnclx.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [HwNProcessAddDevicePostDeviceCreate function](nf-hwnclx-hwnprocessadddevicepostdevicecreate.md) | Creates I/O queues. It should be called after the client driver’s EVT_WDF_DRIVER_DEVICE_ADD callback function is invoked and the device object has been created. |
| [HwNProcessAddDevicePreDeviceCreate function](nf-hwnclx-hwnprocessadddevicepredevicecreate.md) | Supplies the device prepare/release and entry/exit callbacks to the Windows Driver Foundation (WDF) for transitioning the device into different states. |
| [HwNRegisterClient function](nf-hwnclx-hwnregisterclient.md) | Registers the hardware notification client driver and its callback functions with the class extension. |
| [HwNUnregisterClient function](nf-hwnclx-hwnunregisterclient.md) | Unregisters the hardware notification client driver and its callback functions with the class extension. This function should be invoked when the client driver is unloaded. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_CLIENT_DEVICE_INFORMATION structure](ns-hwnclx-_client_device_information.md) | The CLIENT_DEVICE_INFORMATION structure is used by the hardware notification callback HWN_CLIENT_QUERY_DEVICE_INFORMATION to return the total number of hardware notifications that the client device driver provides. |
| [_HWN_CLIENT_REGISTRATION_PACKET structure](ns-hwnclx-_hwn_client_registration_packet.md) | Hardware Notification client driver registration packet that is passed to the class extension when a client driver is registered. Contains version information and client driver callback functions. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_HWN_CLX_EXPORT_INDEX enumeration](ne-hwnclx-_hwn_clx_export_index.md) | Defines the position for each of the Hardware Notification exports in the export table. |
