# Ufxclient.h header


This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Ufxclient.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [UFX_DEVICE_CALLBACKS_INIT function](nf-ufxclient-ufx-device-callbacks-init.md) | The UFX_DEVICE_CALLBACKS_INIT macro initializes the UFX_DEVICE_CALLBACKS structure. |
| [UFX_DEVICE_CAPABILITIES_INIT function](nf-ufxclient-ufx-device-capabilities-init.md) | The UFX_DEVICE_CAPABILITIES_INIT macro the initializes the UFX_DEVICE_CAPABILITIES structure. |
| [UFX_ENDPOINT_CALLBACKS_INIT function](nf-ufxclient-ufx-endpoint-callbacks-init.md) | The UFX_ENDPOINT_CALLBACKS_INIT macro initializes the UFX_ENDPOINT_CALLBACKS structure. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [EVT_UFX_DEVICE_ADDRESSED callback](nc-ufxclient-evt-ufx-device-addressed.md) | The client driver's implementation to assign an address on the function controller. |
| [EVT_UFX_DEVICE_CONTROLLER_RESET callback](nc-ufxclient-evt-ufx-device-controller-reset.md) | The client driver's implementation to reset the function controller to its initial state. |
| [EVT_UFX_DEVICE_DEFAULT_ENDPOINT_ADD callback](nc-ufxclient-evt-ufx-device-default-endpoint-add.md) | The client driver's implementation to create a default control endpoint. |
| [EVT_UFX_DEVICE_ENDPOINT_ADD callback](nc-ufxclient-evt-ufx-device-endpoint-add.md) | The client driver's implementation to create a default endpoint object. |
| [EVT_UFX_DEVICE_HOST_CONNECT callback](nc-ufxclient-evt-ufx-device-host-connect.md) | The client driver's implementation to initiate connection with the host. |
| [EVT_UFX_DEVICE_HOST_DISCONNECT callback](nc-ufxclient-evt-ufx-device-host-disconnect.md) | The client driver's implementation to disable the function controller's communication with the host. |
| [EVT_UFX_DEVICE_PORT_CHANGE callback](nc-ufxclient-evt-ufx-device-port-change.md) | The client driver's implementation to update the type of the new port to which the USB device is connected. |
| [EVT_UFX_DEVICE_PORT_DETECT callback](nc-ufxclient-evt-ufx-device-port-detect.md) | The client driver's implementation to initiate port detection. |
| [EVT_UFX_DEVICE_PROPRIETARY_CHARGER_RESET callback](nc-ufxclient-evt-ufx-device-proprietary-charger-reset.md) | The client driver's implementation to resets proprietary charger. |
| [EVT_UFX_DEVICE_PROPRIETARY_CHARGER_SET_PROPERTY callback](nc-ufxclient-evt-ufx-device-proprietary-charger-set-property.md) | The client driver's implementation to set charger information that it uses to enable charging over USB. |
| [EVT_UFX_DEVICE_REMOTE_WAKEUP_SIGNAL callback](nc-ufxclient-evt-ufx-device-remote-wakeup-signal.md) | The client driver's implementation to initiate remote wake-up on the function controller. |
| [EVT_UFX_DEVICE_SUPER_SPEED_POWER_FEATURE callback](nc-ufxclient-evt-ufx-device-super-speed-power-feature.md) | The client driver's implementation to set or clear the specified power feature on the function controller. |
| [EVT_UFX_DEVICE_TEST_MODE_SET callback](nc-ufxclient-evt-ufx-device-test-mode-set.md) | The client driver's implementation to set the test mode of the function controller. |
| [EVT_UFX_DEVICE_USB_STATE_CHANGE callback](nc-ufxclient-evt-ufx-device-usb-state-change.md) | The client driver's implementation to update the state of the USB device. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [UFX_DEVICE_CALLBACKS structure](ns-ufxclient--ufx-device-callbacks.md) | The UFX_DEVICE_CALLBACKS structure is used to define then event callback functions supported by the client driver. |
| [UFX_ENDPOINT_CALLBACKS structure](ns-ufxclient--ufx-endpoint-callbacks.md) | The UFX_ENDPOINT_CALLBACKS structure is used to define then event callback functions supported by the client driver. |
