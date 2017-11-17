# Declarations in the udecxusbdevice header
This header Udecxusbdevice contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS structure](ns-udecxusbdevice--udecx-usb-device-state-change-callbacks.md) | Initializes a UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS structure with pointers to callback functions that are implemented by a UDE client for a virtual USB device. |
| [UDECX_ENDPOINTS_CONFIGURE_PARAMS structure](ns-udecxusbdevice--udecx-endpoints-configure-params.md) | Contains the configuration options specified by USB device emulation class extension (UdeCx) to the client driver when the class extension invokes EVT_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE. |
| [UDECX_USB_ENDPOINT_INIT_AND_METADATA structure](ns-udecxusbdevice--udecx-usb-endpoint-init-and-metadata.md) | Contains the descriptors supported by an endpoint of a virtual USB device. |
| [UDECX_USB_DEVICE_PLUG_IN_OPTIONS structure](ns-udecxusbdevice--udecx-usb-device-plug-in-options.md) | Contains the port numbers to which a virtual USB device is connected. Initialize this structure by calling the UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT method. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_UDECX_USB_DEVICE_D0_ENTRY callback function](nc-udecxusbdevice-evt-udecx-usb-device-d0-entry.md) | TBD |
| [*PFN_UDECXUSBDEVICESIGNALWAKE callback function](nc-udecxusbdevice-pfn-udecxusbdevicesignalwake.md) | TBD |
| [EVT_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE callback](nc-udecxusbdevice-evt-udecx-usb-device-endpoints-configure.md) | The USB device emulation class extension (UdeCx) invokes this callback function to change the configuration by selecting an alternate setting, disabling current endpoints, or adding dynamic endpoints. |
| [*PFN_UDECXUSBDEVICELINKPOWERENTRYCOMPLETE callback function](nc-udecxusbdevice-pfn-udecxusbdevicelinkpowerentrycomplete.md) | TBD |
| [*PFN_UDECXUSBDEVICELINKPOWEREXITCOMPLETE callback function](nc-udecxusbdevice-pfn-udecxusbdevicelinkpowerexitcomplete.md) | TBD |
| [*PFN_UDECXUSBDEVICEINITSETSTATECHANGECALLBACKS callback function](nc-udecxusbdevice-pfn-udecxusbdeviceinitsetstatechangecallbacks.md) | TBD |
| [*PFN_UDECXUSBDEVICEPLUGOUTANDDELETE callback function](nc-udecxusbdevice-pfn-udecxusbdeviceplugoutanddelete.md) | TBD |
| [*PFN_UDECXUSBDEVICEINITADDSTRINGDESCRIPTORRAW callback function](nc-udecxusbdevice-pfn-udecxusbdeviceinitaddstringdescriptorraw.md) | TBD |
| [EVT_UDECX_USB_DEVICE_D0_EXIT callback function](nc-udecxusbdevice-evt-udecx-usb-device-d0-exit.md) | TBD |
| [EVT_UDECX_USB_DEVICE_SET_FUNCTION_SUSPEND_AND_WAKE callback function](nc-udecxusbdevice-evt-udecx-usb-device-set-function-suspend-and-wake.md) | TBD |
| [EVT_UDECX_USB_DEVICE_ENDPOINT_ADD callback](nc-udecxusbdevice-evt-udecx-usb-device-endpoint-add.md) | The USB device emulation class extension (UdeCx) invokes this callback function to request the client driver to create a dynamic endpoint on the virtual USB device. |
| [*PFN_UDECXUSBDEVICEINITADDSTRINGDESCRIPTOR callback function](nc-udecxusbdevice-pfn-udecxusbdeviceinitaddstringdescriptor.md) | TBD |
| [*PFN_UDECXUSBDEVICECREATE callback function](nc-udecxusbdevice-pfn-udecxusbdevicecreate.md) | TBD |
| [*PFN_UDECXUSBDEVICEINITADDDESCRIPTOR callback function](nc-udecxusbdevice-pfn-udecxusbdeviceinitadddescriptor.md) | TBD |
| [*PFN_UDECXUSBDEVICEINITALLOCATE callback function](nc-udecxusbdevice-pfn-udecxusbdeviceinitallocate.md) | TBD |
| [*PFN_UDECXUSBDEVICEINITADDDESCRIPTORWITHINDEX callback function](nc-udecxusbdevice-pfn-udecxusbdeviceinitadddescriptorwithindex.md) | TBD |
| [*PFN_UDECXUSBDEVICESETFUNCTIONSUSPENDANDWAKECOMPLETE callback function](nc-udecxusbdevice-pfn-udecxusbdevicesetfunctionsuspendandwakecomplete.md) | TBD |
| [*PFN_UDECXUSBDEVICEINITFREE callback function](nc-udecxusbdevice-pfn-udecxusbdeviceinitfree.md) | TBD |
| [*PFN_UDECXUSBDEVICEINITSETENDPOINTSTYPE callback function](nc-udecxusbdevice-pfn-udecxusbdeviceinitsetendpointstype.md) | TBD |
| [EVT_UDECX_USB_DEVICE_POST_ENUMERATION_RESET callback function](nc-udecxusbdevice-evt-udecx-usb-device-post-enumeration-reset.md) | TBD |
| [*PFN_UDECXUSBDEVICESIGNALFUNCTIONWAKE callback function](nc-udecxusbdevice-pfn-udecxusbdevicesignalfunctionwake.md) | TBD |
| [*PFN_UDECXUSBDEVICEPLUGIN callback function](nc-udecxusbdevice-pfn-udecxusbdeviceplugin.md) | TBD |
| [EVT_UDECX_USB_DEVICE_DEFAULT_ENDPOINT_ADD callback](nc-udecxusbdevice-evt-udecx-usb-device-default-endpoint-add.md) | The USB device emulation class extension (UdeCx) invokes this callback function to request the client driver to create the default control endpoint on the virtual USB device. |
| [*PFN_UDECXUSBDEVICEINITSETSPEED callback function](nc-udecxusbdevice-pfn-udecxusbdeviceinitsetspeed.md) | TBD |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [UdecxUsbDeviceSetFunctionSuspendAndWakeComplete function](nf-udecxusbdevice-udecxusbdevicesetfunctionsuspendandwakecomplete.md) | Completes an asynchronous request for changing the power state of a particular function of a virtual USB 3.0 device. |
| [UdecxUsbDeviceCreate function](nf-udecxusbdevice-udecxusbdevicecreate.md) | Creates a USB Device Emulation (UDE) device object. |
| [UdecxUsbDeviceInitAddDescriptorWithIndex function](nf-udecxusbdevice-udecxusbdeviceinitadddescriptorwithindex.md) | Adds a USB descriptor to the initialization parameters used to create a virtual USB device. |
| [UdecxUsbDeviceInitAddDescriptor function](nf-udecxusbdevice-udecxusbdeviceinitadddescriptor.md) | Adds a USB descriptor to the initialization parameters used to create a virtual USB device. |
| [UdecxUsbDevicePlugIn function](nf-udecxusbdevice-udecxusbdeviceplugin.md) | Notifies the USB device emulation class extension (UdeCx) that the USB device has been plugged in the specified port. |
| [UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT function](nf-udecxusbdevice-udecx-usb-device-plug-in-options-init.md) | Initializes a UDECX_USB_DEVICE_PLUG_IN_OPTIONS structure. |
| [UdecxUsbDeviceSignalWake function](nf-udecxusbdevice-udecxusbdevicesignalwake.md) | Initiates wake up from a low link power state for a virtual USB 2.0 device. |
| [UdecxUsbDeviceInitAllocate function](nf-udecxusbdevice-udecxusbdeviceinitallocate.md) | Allocates memory for a UDECXUSBDEVICE_INIT structure that is used to initialize a virtual USB device. |
| [UdecxUsbDeviceInitAddStringDescriptor function](nf-udecxusbdevice-udecxusbdeviceinitaddstringdescriptor.md) | Adds a USB string descriptor to the initialization parameters used to create a virtual USB device. |
| [UDECX_USB_DEVICE_CALLBACKS_INIT function](nf-udecxusbdevice-udecx-usb-device-callbacks-init.md) | Initializes a UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS structure before a UdecxUsbDeviceCreate call. |
| [UdecxUsbDeviceLinkPowerEntryComplete function](nf-udecxusbdevice-udecxusbdevicelinkpowerentrycomplete.md) | Completes an asynchronous request for bringing the device out of a low power state. |
| [UdecxUsbDeviceInitSetStateChangeCallbacks function](nf-udecxusbdevice-udecxusbdeviceinitsetstatechangecallbacks.md) | Initializes a WDF-allocated structure with pointers to callback functions. |
| [UdecxUsbDeviceSignalFunctionWake function](nf-udecxusbdevice-udecxusbdevicesignalfunctionwake.md) | Initiates wake up of the specified function from a low power state. This applies to virtual USB 3.0 devices. |
| [UdecxUsbDeviceLinkPowerExitComplete function](nf-udecxusbdevice-udecxusbdevicelinkpowerexitcomplete.md) | Completes an asynchronous request for sending the device to a low power state. |
| [UdecxUsbDeviceInitFree function](nf-udecxusbdevice-udecxusbdeviceinitfree.md) | Releases the resources that were allocated by the UdecxUsbDeviceInitAllocate call. |
| [UdecxUsbDeviceInitSetEndpointsType function](nf-udecxusbdevice-udecxusbdeviceinitsetendpointstype.md) | Indicates the type of endpoint (simple or dynamic) in the initialization parameters that the client driver uses to create the virtual USB device. |
| [UdecxUsbDeviceInitSetSpeed function](nf-udecxusbdevice-udecxusbdeviceinitsetspeed.md) | Sets the USB speed of the virtual USB device to create. |
| [UdecxUsbDevicePlugOutAndDelete function](nf-udecxusbdevice-udecxusbdeviceplugoutanddelete.md) | Disconnects the virtual USB device. |
| [UdecxUsbDeviceInitAddStringDescriptorRaw function](nf-udecxusbdevice-udecxusbdeviceinitaddstringdescriptorraw.md) | Adds a USB string descriptor to the initialization parameters used to create a virtual USB device. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [UDECX_USB_DEVICE_SPEED enumeration](ne-udecxusbdevice--udecx-usb-device-speed.md) | Defines values for USB device speeds. |
| [UDECX_ENDPOINTS_CONFIGURE_TYPE enumeration](ne-udecxusbdevice--udecx-endpoints-configure-type.md) | TBD |
| [UDECX_USB_DEVICE_WAKE_SETTING enumeration](ne-udecxusbdevice--udecx-usb-device-wake-setting.md) | Defines values for remote wake capability of a virtual USB device. |
| [UDECX_USB_DEVICE_FUNCTION_POWER enumeration](ne-udecxusbdevice--udecx-usb-device-function-power.md) | Defines values for function wake capability of a virtual USB 3.0 device. |
| [UDECX_ENDPOINT_TYPE enumeration](ne-udecxusbdevice--udecx-endpoint-type.md) | Defines values for endpoint types supported by a virtual USB device. |

This header is used in these topics:

- [usbref](..content/_usbref)
