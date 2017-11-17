# Declarations in the ufxclient header
This header Ufxclient contains these programming interfaces:

Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_UFX_DEVICE_TEST_MODE_SET callback](nc-ufxclient-evt-ufx-device-test-mode-set.md) | The client driver's implementation to set the test mode of the function controller. |
| [EVT_UFX_DEVICE_TESTHOOK callback function](nc-ufxclient-evt-ufx-device-testhook.md) | TBD |
| [UFX_DEVICE_NOTIFY_RESET callback function](nc-ufxclient-ufx-device-notify-reset.md) | TBD |
| [EVT_UFX_DEVICE_PROPRIETARY_CHARGER_DETECT callback function](nc-ufxclient-evt-ufx-device-proprietary-charger-detect.md) | TBD |
| [UFX_ENDPOINT_GET_TRANSFER_QUEUE callback function](nc-ufxclient-ufx-endpoint-get-transfer-queue.md) | TBD |
| [UFX_ENDPOINT_GET_COMMAND_QUEUE callback function](nc-ufxclient-ufx-endpoint-get-command-queue.md) | TBD |
| [EVT_UFX_DEVICE_PORT_CHANGE callback](nc-ufxclient-evt-ufx-device-port-change.md) | The client driver's implementation to update the type of the new port to which the USB device is connected. |
| [UFX_ENDPOINT_CREATE callback function](nc-ufxclient-ufx-endpoint-create.md) | TBD |
| [UFX_DEVICE_NOTIFY_ATTACH callback function](nc-ufxclient-ufx-device-notify-attach.md) | TBD |
| [UFX_DEVICE_PORT_DETECT_COMPLETE callback function](nc-ufxclient-ufx-device-port-detect-complete.md) | TBD |
| [EVT_UFX_DEVICE_ADDRESSED callback](nc-ufxclient-evt-ufx-device-addressed.md) | The client driver's implementation to assign an address on the function controller. |
| [UFX_DEVICE_CREATE callback function](nc-ufxclient-ufx-device-create.md) | TBD |
| [UFX_DEVICE_IO_CONTROL callback function](nc-ufxclient-ufx-device-io-control.md) | TBD |
| [UFX_DEVICE_NOTIFY_HARDWARE_READY callback function](nc-ufxclient-ufx-device-notify-hardware-ready.md) | TBD |
| [EVT_UFX_DEVICE_PROPRIETARY_CHARGER_RESET callback](nc-ufxclient-evt-ufx-device-proprietary-charger-reset.md) | The client driver's implementation to resets proprietary charger. |
| [EVT_UFX_DEVICE_DEFAULT_ENDPOINT_ADD callback](nc-ufxclient-evt-ufx-device-default-endpoint-add.md) | The client driver's implementation to create a default control endpoint. |
| [EVT_UFX_DEVICE_PORT_DETECT callback](nc-ufxclient-evt-ufx-device-port-detect.md) | The client driver's implementation to initiate port detection. |
| [EVT_UFX_DEVICE_HOST_CONNECT callback](nc-ufxclient-evt-ufx-device-host-connect.md) | The client driver's implementation to initiate connection with the host. |
| [EVT_UFX_DEVICE_REMOTE_WAKEUP_SIGNAL callback](nc-ufxclient-evt-ufx-device-remote-wakeup-signal.md) | The client driver's implementation to initiate remote wake-up on the function controller. |
| [UFX_DEVICE_EVENT_COMPLETE callback function](nc-ufxclient-ufx-device-event-complete.md) | TBD |
| [UFX_DEVICE_NOTIFY_DETACH callback function](nc-ufxclient-ufx-device-notify-detach.md) | TBD |
| [EVT_UFX_DEVICE_ENDPOINT_ADD callback](nc-ufxclient-evt-ufx-device-endpoint-add.md) | The client driver's implementation to create a default endpoint object. |
| [UFX_DEVICE_NOTIFY_SUSPEND callback function](nc-ufxclient-ufx-device-notify-suspend.md) | TBD |
| [EVT_UFX_DEVICE_CONTROLLER_RESET callback](nc-ufxclient-evt-ufx-device-controller-reset.md) | The client driver's implementation to reset the function controller to its initial state. |
| [EVT_UFX_DEVICE_HOST_DISCONNECT callback](nc-ufxclient-evt-ufx-device-host-disconnect.md) | The client driver's implementation to disable the function controller's communication with the host. |
| [EVT_UFX_DEVICE_PROPRIETARY_CHARGER_SET_PROPERTY callback](nc-ufxclient-evt-ufx-device-proprietary-charger-set-property.md) | The client driver's implementation to set charger information that it uses to enable charging over USB. |
| [EVT_UFX_DEVICE_SUPER_SPEED_POWER_FEATURE callback](nc-ufxclient-evt-ufx-device-super-speed-power-feature.md) | The client driver's implementation to set or clear the specified power feature on the function controller. |
| [UFX_DEVICE_IO_INTERNAL_CONTROL callback function](nc-ufxclient-ufx-device-io-internal-control.md) | TBD |
| [UFX_DEVICE_PROPRIETARY_CHARGER_DETECT_COMPLETE callback function](nc-ufxclient-ufx-device-proprietary-charger-detect-complete.md) | TBD |
| [UFX_DEVICE_NOTIFY_HARDWARE_FAILURE callback function](nc-ufxclient-ufx-device-notify-hardware-failure.md) | TBD |
| [UFX_DEVICE_PORT_DETECT_COMPLETE_EX callback function](nc-ufxclient-ufx-device-port-detect-complete-ex.md) | TBD |
| [UFX_ENDPOINT_INIT_SET_EVENT_CALLBACKS callback function](nc-ufxclient-ufx-endpoint-init-set-event-callbacks.md) | TBD |
| [UFX_ENDPOINT_NOTIFY_SETUP callback function](nc-ufxclient-ufx-endpoint-notify-setup.md) | TBD |
| [EVT_UFX_DEVICE_USB_STATE_CHANGE callback](nc-ufxclient-evt-ufx-device-usb-state-change.md) | The client driver's implementation to update the state of the USB device. |
| [UFX_DEVICE_NOTIFY_RESUME callback function](nc-ufxclient-ufx-device-notify-resume.md) | TBD |
| [UFX_FDO_INIT callback function](nc-ufxclient-ufx-fdo-init.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [UfxDeviceCreate function](nf-ufxclient-ufxdevicecreate.md) | TBD |
| [UfxDeviceNotifyHardwareFailure function](nf-ufxclient-ufxdevicenotifyhardwarefailure.md) | TBD |
| [UfxDeviceNotifyReset function](nf-ufxclient-ufxdevicenotifyreset.md) | TBD |
| [UfxDevicePortDetectCompleteEx function](nf-ufxclient-ufxdeviceportdetectcompleteex.md) | TBD |
| [UfxDeviceNotifySuspend function](nf-ufxclient-ufxdevicenotifysuspend.md) | TBD |
| [UFX_DEVICE_CAPABILITIES_INIT function](nf-ufxclient-ufx-device-capabilities-init.md) | The UFX_DEVICE_CAPABILITIES_INIT macro the initializes the UFX_DEVICE_CAPABILITIES structure. |
| [UfxDeviceNotifyHardwareReady function](nf-ufxclient-ufxdevicenotifyhardwareready.md) | TBD |
| [UfxEndpointGetTransferQueue function](nf-ufxclient-ufxendpointgettransferqueue.md) | TBD |
| [UfxDeviceNotifyResume function](nf-ufxclient-ufxdevicenotifyresume.md) | TBD |
| [UfxFdoInit function](nf-ufxclient-ufxfdoinit.md) | TBD |
| [UfxDeviceEventComplete function](nf-ufxclient-ufxdeviceeventcomplete.md) | TBD |
| [UfxDeviceNotifyDetach function](nf-ufxclient-ufxdevicenotifydetach.md) | TBD |
| [UfxDeviceNotifyAttach function](nf-ufxclient-ufxdevicenotifyattach.md) | TBD |
| [UfxDeviceIoInternalControl function](nf-ufxclient-ufxdeviceiointernalcontrol.md) | TBD |
| [UfxDeviceProprietaryChargerDetectComplete function](nf-ufxclient-ufxdeviceproprietarychargerdetectcomplete.md) | TBD |
| [UfxDevicePortDetectComplete function](nf-ufxclient-ufxdeviceportdetectcomplete.md) | TBD |
| [UfxEndpointGetCommandQueue function](nf-ufxclient-ufxendpointgetcommandqueue.md) | TBD |
| [UfxEndpointNotifySetup function](nf-ufxclient-ufxendpointnotifysetup.md) | TBD |
| [UfxDeviceIoControl function](nf-ufxclient-ufxdeviceiocontrol.md) | TBD |
| [UfxEndpointInitSetEventCallbacks function](nf-ufxclient-ufxendpointinitseteventcallbacks.md) | TBD |
| [UFX_DEVICE_CALLBACKS_INIT function](nf-ufxclient-ufx-device-callbacks-init.md) | The UFX_DEVICE_CALLBACKS_INIT macro initializes the UFX_DEVICE_CALLBACKS structure. |
| [UFX_ENDPOINT_CALLBACKS_INIT function](nf-ufxclient-ufx-endpoint-callbacks-init.md) | The UFX_ENDPOINT_CALLBACKS_INIT macro initializes the UFX_ENDPOINT_CALLBACKS structure. |
| [UfxEndpointCreate function](nf-ufxclient-ufxendpointcreate.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UFX_ENDPOINT_CALLBACKS structure](ns-ufxclient--ufx-endpoint-callbacks.md) | The UFX_ENDPOINT_CALLBACKS structure is used to define then event callback functions supported by the client driver. |
| [UFX_DEVICE_CALLBACKS structure](ns-ufxclient--ufx-device-callbacks.md) | The UFX_DEVICE_CALLBACKS structure is used to define then event callback functions supported by the client driver. |

This header is used in these topics:

- [usbref](..content/_usbref)
