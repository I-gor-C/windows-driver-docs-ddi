---
UID: TP:gpiobtn
---

# Hardware notifications

## -description
Overview of the Hardware notifications technology.

To develop Hardware notifications, you need these headers:

 * [hwnclx.h](..\hwnclx\index.md)

For the programming guide, see [Hardware notifications](https://docs.microsoft.com/en-us/windows-hardware/drivers/gpiobtn).

## Functions

| Title   | Description   |
| ---- |:---- |
| [HwNProcessAddDevicePostDeviceCreate function](..\hwnclx\nf-hwnclx-hwnprocessadddevicepostdevicecreate.md) | Creates I/O queues. It should be called after the client driver’s EVT_WDF_DRIVER_DEVICE_ADD callback function is invoked and the device object has been created. |
| [HwNProcessAddDevicePreDeviceCreate function](..\hwnclx\nf-hwnclx-hwnprocessadddevicepredevicecreate.md) | Supplies the device prepare/release and entry/exit callbacks to the Windows Driver Foundation (WDF) for transitioning the device into different states. |
| [HwNRegisterClient function](..\hwnclx\nf-hwnclx-hwnregisterclient.md) | Registers the hardware notification client driver and its callback functions with the class extension. |
| [HwNUnregisterClient function](..\hwnclx\nf-hwnclx-hwnunregisterclient.md) | Unregisters the hardware notification client driver and its callback functions with the class extension. This function should be invoked when the client driver is unloaded. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_CLIENT_DEVICE_INFORMATION structure](..\hwnclx\ns-hwnclx-_client_device_information.md) | The CLIENT_DEVICE_INFORMATION structure is used by the hardware notification callback HWN_CLIENT_QUERY_DEVICE_INFORMATION to return the total number of hardware notifications that the client device driver provides. |
| [_HWN_CLIENT_REGISTRATION_PACKET structure](..\hwnclx\ns-hwnclx-_hwn_client_registration_packet.md) | Hardware Notification client driver registration packet that is passed to the class extension when a client driver is registered. Contains version information and client driver callback functions. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_HWN_CLX_EXPORT_INDEX enumeration](..\hwnclx\ne-hwnclx-_hwn_clx_export_index.md) | Defines the position for each of the Hardware Notification exports in the export table. |
