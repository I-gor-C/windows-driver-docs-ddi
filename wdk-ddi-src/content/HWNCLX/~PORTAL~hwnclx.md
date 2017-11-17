# Declarations in the hwnclx header
This header Hwnclx contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [HWN_CLX_PROCESS_ADD_DEVICE_PRE_DEVICE_CREATE callback function](nc-hwnclx-hwn-clx-process-add-device-pre-device-create.md) | TBD |
| [HWN_CLIENT_INITIALIZE_DEVICE callback](nc-hwnclx-hwn-client-initialize-device.md) | Implemented by the client driver and is invoked as a result of a call to EVT_WDF_DEVICE_PREPARE_HARDWARE. |
| [HWN_CLIENT_UNINITIALIZE_DEVICE callback](nc-hwnclx-hwn-client-uninitialize-device.md) | Implemented by the client driver and invoked as invoked as a result of a call to EVT_WDF_DEVICE_RELEASE_HARDWARE. This callback function uninitializes the hardware notification component. |
| [HWN_CLIENT_START_DEVICE callback](nc-hwnclx-hwn-client-start-device.md) | Implemented by the client driver to start the hardware notification component. It is invoked as a result of a call to EVT_WDF_DEVICE_D0_ENTRY. |
| [HWN_CLX_UNREGISTER_CLIENT callback function](nc-hwnclx-hwn-clx-unregister-client.md) | TBD |
| [PHWN_CLX_EXPORTED_INTERFACES callback function](nc-hwnclx-phwn-clx-exported-interfaces.md) | TBD |
| [HWN_CLIENT_GET_STATE callback](nc-hwnclx-hwn-client-get-state.md) | Implemented by the client driver to get hardware notification component state. It is invoked when a user requests status information. |
| [HWN_CLIENT_STOP_DEVICE callback](nc-hwnclx-hwn-client-stop-device.md) | Implemented by the client driver TO start the hardware notification component. It is invoked as a result of a call to EVT_WDF_DEVICE_D0_EXIT. |
| [HWN_CLIENT_SET_STATE callback](nc-hwnclx-hwn-client-set-state.md) | Implemented by the client driver to set hardware notification component state. It is invoked when a user wants to change the state of a driver. |
| [HWN_CLIENT_QUERY_DEVICE_INFORMATION callback](nc-hwnclx-hwn-client-query-device-information.md) | Implemented by the client driver to retrieve hardware notification component attributes. |
| [HWN_CLX_PROCESS_ADD_DEVICE_POST_DEVICE_CREATE callback function](nc-hwnclx-hwn-clx-process-add-device-post-device-create.md) | TBD |
| [HWN_CLX_REGISTER_CLIENT callback function](nc-hwnclx-hwn-clx-register-client.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [HwNProcessAddDevicePreDeviceCreate function](nf-hwnclx-hwnprocessadddevicepredevicecreate.md) | Supplies the device prepare/release and entry/exit callbacks to the Windows Driver Foundation (WDF) for transitioning the device into different states. |
| [HwNRegisterClient function](nf-hwnclx-hwnregisterclient.md) | Registers the hardware notification client driver and its callback functions with the class extension. |
| [HwNProcessAddDevicePostDeviceCreate function](nf-hwnclx-hwnprocessadddevicepostdevicecreate.md) | Creates I/O queues. It should be called after the client driver’s EVT_WDF_DRIVER_DEVICE_ADD callback function is invoked and the device object has been created. |
| [HwNUnregisterClient function](nf-hwnclx-hwnunregisterclient.md) | Unregisters the hardware notification client driver and its callback functions with the class extension. This function should be invoked when the client driver is unloaded. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [HWN_CLX_EXPORT_INDEX enumeration](ne-hwnclx--hwn-clx-export-index.md) | Defines the position for each of the Hardware Notification exports in the export table. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [HWN_CLIENT_REGISTRATION_PACKET structure](ns-hwnclx--hwn-client-registration-packet.md) | Hardware Notification client driver registration packet that is passed to the class extension when a client driver is registered. Contains version information and client driver callback functions. |
| [CLIENT_DEVICE_INFORMATION structure](ns-hwnclx--client-device-information.md) | The CLIENT_DEVICE_INFORMATION structure is used by the hardware notification callback HWN_CLIENT_QUERY_DEVICE_INFORMATION to return the total number of hardware notifications that the client device driver provides. |

This header is used in these topics:

- [gpiobtn](..content/_gpiobtn)
