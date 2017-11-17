# Declarations in the usbbusif header
This header Usbbusif contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [USB_BUS_INTERFACE_USBDI_V0 structure](ns-usbbusif--usb-bus-interface-usbdi-v0.md) | The USB_BUS_INTERFACE_USBDI_V0 structure is provided by the USB hub driver to allow USB clients to make direct calls to the hub driver without allocating IRPs. |
| [USB_BUS_INTERFACE_USBDI_V2 structure](ns-usbbusif--usb-bus-interface-usbdi-v2.md) | The USB_BUS_INTERFACE_USBDI_V2 structure is provided by the USB hub driver to allow USB clients to make direct calls to the hub driver without allocating IRPs. |
| [USB_BUS_INFORMATION_LEVEL_1 structure](ns-usbbusif--usb-bus-information-level-1.md) | The USB_BUS_INFORMATION_LEVEL_1 structure is used in conjunction with the QueryBusInformation interface routine to report information about the bus. |
| [USBC_FUNCTION_DESCRIPTOR structure](ns-usbbusif--usbc-function-descriptor.md) | The USBC_FUNCTION_DESCRIPTOR structure describes a USB function and its associated interface collection. |
| [USB_BUS_INTERFACE_USBDI_V3 structure](ns-usbbusif--usb-bus-interface-usbdi-v3.md) | The USB_BUS_INTERFACE_USBDI_V3 structure is provided by the USB hub driver to allow USB clients to make direct calls to the hub driver without allocating IRPs. |
| [USB_BUS_INTERFACE_USBDI_V1 structure](ns-usbbusif--usb-bus-interface-usbdi-v1.md) | The USB_BUS_INTERFACE_USBDI_V1 structure is provided by the USB hub driver to allow USB clients to make direct calls to the hub driver without allocating IRPs. |
| [USB_BUS_INFORMATION_LEVEL_0 structure](ns-usbbusif--usb-bus-information-level-0.md) | The USB_BUS_INFORMATION_LEVEL_0 structure is used in conjunction with the QueryBusInformation interface routine to report information about the bus. |
| [USBC_DEVICE_CONFIGURATION_INTERFACE_V1 structure](ns-usbbusif--usbc-device-configuration-interface-v1.md) | The USBC_DEVICE_CONFIGURATION_INTERFACE_V1 structure is exposed by the vendor-supplied filter drivers to assist the USB generic parent driver in defining interface collections. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [PUSB_BUSIFFN_QUERY_BUS_INFORMATION callback function](nc-usbbusif-pusb-busiffn-query-bus-information.md) | TBD |
| [PUSB_BUSIFFN_GETUSBDI_VERSION callback function](nc-usbbusif-pusb-busiffn-getusbdi-version.md) | TBD |
| [PUSB_BUSIFFN_IS_DEVICE_HIGH_SPEED callback function](nc-usbbusif-pusb-busiffn-is-device-high-speed.md) | TBD |
| [PUSB_BUSIFFN_QUERY_BUS_TIME callback function](nc-usbbusif-pusb-busiffn-query-bus-time.md) | TBD |
| [PUSB_BUSIFFN_ENUM_LOG_ENTRY callback function](nc-usbbusif-pusb-busiffn-enum-log-entry.md) | TBD |
| [PUSB_BUSIFFN_QUERY_BUS_TIME_EX callback function](nc-usbbusif-pusb-busiffn-query-bus-time-ex.md) | TBD |
| [USBC_START_DEVICE_CALLBACK callback](nc-usbbusif-usbc-start-device-callback.md) | The USBC_START_DEVICE_CALLBACK routine allows a USB client driver to provide a custom definition of the interface collections on a device. |
| [USBC_PDO_ENABLE_CALLBACK callback function](nc-usbbusif-usbc-pdo-enable-callback.md) | TBD |
| [PUSB_BUSIFFN_QUERY_CONTROLLER_TYPE callback function](nc-usbbusif-pusb-busiffn-query-controller-type.md) | TBD |
| [PUSB_BUSIFFN_SUBMIT_ISO_OUT_URB callback function](nc-usbbusif-pusb-busiffn-submit-iso-out-urb.md) | TBD |

This header is used in these topics:

- [usbref](..content/_usbref)
