# Ucxusbdevice.h header


This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Ucxusbdevice.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [UCX_USBDEVICE_EVENT_CALLBACKS_INIT function](nf-ucxusbdevice-ucx-usbdevice-event-callbacks-init.md) | Initializes a UCX_USBDEVICE_EVENT_CALLBACKS structure with the function pointers to client driver's callback functions. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [EVT_UCX_USBDEVICE_ADDRESS callback](nc-ucxusbdevice-evt-ucx-usbdevice-address.md) | The client driver's implementation that UCX calls to address the USB device. |
| [EVT_UCX_USBDEVICE_DEFAULT_ENDPOINT_ADD callback](nc-ucxusbdevice-evt-ucx-usbdevice-default-endpoint-add.md) | The client driver's implementation that UCX calls to add a new default endpoint for a USB device. |
| [EVT_UCX_USBDEVICE_DISABLE callback](nc-ucxusbdevice-evt-ucx-usbdevice-disable.md) | The client driver's implementation that UCX calls to release controller resources associated with the device and its default endpoint. |
| [EVT_UCX_USBDEVICE_ENABLE callback](nc-ucxusbdevice-evt-ucx-usbdevice-enable.md) | The client driver's implementation that UCX calls to program information about the device and its default control endpoint into the controller. |
| [EVT_UCX_USBDEVICE_ENDPOINTS_CONFIGURE callback](nc-ucxusbdevice-evt-ucx-usbdevice-endpoints-configure.md) | The client driver's implementation that UCX calls to configure endpoints in the controller. |
| [EVT_UCX_USBDEVICE_ENDPOINT_ADD callback](nc-ucxusbdevice-evt-ucx-usbdevice-endpoint-add.md) | The client driver's implementation that UCX calls to add a new endpoint for a USB device. |
| [EVT_UCX_USBDEVICE_GET_CHARACTERISTIC callback](nc-ucxusbdevice-evt-ucx-usbdevice-get-characteristic.md) | UCX invokes this callback to retrieve the device characteristics. |
| [EVT_UCX_USBDEVICE_HUB_INFO callback](nc-ucxusbdevice-evt-ucx-usbdevice-hub-info.md) | The client driver's implementation that UCX calls to retrieve hub properties. |
| [EVT_UCX_USBDEVICE_RESET callback](nc-ucxusbdevice-evt-ucx-usbdevice-reset.md) | The client driver's implementation that UCX calls when the port to which the device is attached is reset. |
| [EVT_UCX_USBDEVICE_RESUME callback](nc-ucxusbdevice-evt-ucx-usbdevice-resume.md) | UCX invokes this callback function to resume a device from suspend state. |
| [EVT_UCX_USBDEVICE_SUSPEND callback](nc-ucxusbdevice-evt-ucx-usbdevice-suspend.md) | UCX invokes this callback function to send a device suspend state. |
| [EVT_UCX_USBDEVICE_UPDATE callback](nc-ucxusbdevice-evt-ucx-usbdevice-update.md) | The client driver's implementation that UCX calls to update device properties. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [ADDRESS0_OWNERSHIP_ACQUIRE structure](ns-ucxusbdevice--address0-ownership-acquire.md) | Contains parameters for configuring the device. |
| [UCX_USBDEVICE_CHARACTERISTIC structure](ns-ucxusbdevice--ucx-usbdevice-characteristic.md) | Stores the characteristics of an device. |
| [UCX_USBDEVICE_CHARACTERISTIC_PATH_DELAY structure](ns-ucxusbdevice--ucx-usbdevice-characteristic-path-delay.md) | Stores the isochronous transfer path delay values. |
| [UCX_USBDEVICE_EVENT_CALLBACKS structure](ns-ucxusbdevice--ucx-usbdevice-event-callbacks.md) | This structure provides a list of UCX USB device event callback functions. |
| [USBDEVICE_ABORTIO structure](ns-ucxusbdevice--usbdevice-abortio.md) | Contains a handle for the Universal Serial Bus (USB) hub or device for which to abort data transfers. |
| [USBDEVICE_ADDRESS structure](ns-ucxusbdevice--usbdevice-address.md) | Contains parameters for a request to transition the specified device to the Addressed state. This structure is passed by UCX in request parameters (Parameters.Others.Arg1) of a framework request object of the EVT_UCX_USBDEVICE_ADDRESS callback function. |
| [USBDEVICE_DISABLE structure](ns-ucxusbdevice--usbdevice-disable.md) | Contains parameters for a request to disable the specified device. This structure is passed by UCX in request parameters (Parameters.Others.Arg1) of a framework request object of the EVT_UCX_USBDEVICE_DISABLE callback function. |
| [USBDEVICE_ENABLE structure](ns-ucxusbdevice--usbdevice-enable.md) | Contains parameters for a request to enable the specified device. This structure is passed by UCX in request parameters (Parameters.Others.Arg1) of a framework request object of the EVT_UCX_USBDEVICE_ENABLE callback function. |
| [USBDEVICE_ENABLE_FAILURE_FLAGS structure](ns-ucxusbdevice--usbdevice-enable-failure-flags.md) | The flags that are set by the client driver in the EVT_UCX_USBDEVICE_ENABLE callback function. Indicate errors, if any, that might have occurred while enabling the device. |
| [USBDEVICE_HUB_INFO structure](ns-ucxusbdevice--usbdevice-hub-info.md) | Contains parameters for a request to get information about the specified hub. This structure is passed by UCX in request parameters (Parameters.Others.Arg1) of a framework request object of the EVT_UCX_USBDEVICE_HUB_INFO callback function. |
| [USBDEVICE_MGMT_HEADER structure](ns-ucxusbdevice--usbdevice-mgmt-header.md) | This structure provides a handle for the Universal Serial Bus (USB) hub or device physically connected to the bus. |
| [USBDEVICE_PURGEIO structure](ns-ucxusbdevice--usbdevice-purgeio.md) | The USBDEVICE_PURGEIO structure contains the handle for the Universal Serial Bus (USB) hub or device to purge I/O for. |
| [USBDEVICE_RESET structure](ns-ucxusbdevice--usbdevice-reset.md) | Contains parameters for a request to reset the specified device. This structure is passed by UCX in request parameters (Parameters.Others.Arg1) of a framework request object of the EVT_UCX_USBDEVICE_RESET callback function. |
| [USBDEVICE_STARTIO structure](ns-ucxusbdevice--usbdevice-startio.md) | Contains a handle for the Universal Serial Bus (USB) hub or device on which to start data transfer. |
| [USBDEVICE_TREE_PURGEIO structure](ns-ucxusbdevice--usbdevice-tree-purgeio.md) | This structure provides the handle for the Universal Serial Bus (USB) device tree to purge I/O for. |
| [USBDEVICE_UPDATE structure](ns-ucxusbdevice--usbdevice-update.md) | Passed by UCX to update the specified device. This structure is in the request parameters (Parameters.Others.Arg1) of a framework request object passed in the EVT_UCX_USBDEVICE_UPDATE callback function. |
| [USBDEVICE_UPDATE_20_HARDWARE_LPM_PARAMETERS structure](ns-ucxusbdevice--usbdevice-update-20-hardware-lpm-parameters.md) | Contains parameters for a request to update USB 2.0 link power management (LPM). UCX passes this structure in the EVT_UCX_USBDEVICE_UPDATE callback function. |
| [USBDEVICE_UPDATE_FAILURE_FLAGS structure](ns-ucxusbdevice--usbdevice-update-failure-flags.md) | The flags that are set by the client driver in the EVT_UCX_USBDEVICE_UPDATE callback function. Indicate errors, if any, that might have occurred while updating the device. |
| [USBDEVICE_UPDATE_FLAGS structure](ns-ucxusbdevice--usbdevice-update-flags.md) | Contains request flags set by UCX that is passed in the USBDEVICE_UPDATE structure when UCX invokes the client driver's EVT_UCX_USBDEVICE_UPDATE callback function. |
| [USB_DEVICE_PORT_PATH structure](ns-ucxusbdevice--usb-device-port-path.md) | Contains the port path of a USB device. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [UCX_USBDEVICE_CHARACTERISTIC_TYPE enumeration](ne-ucxusbdevice--ucx-usbdevice-characteristic-type.md) | Defines values that indicates the type of device characteristic. |
