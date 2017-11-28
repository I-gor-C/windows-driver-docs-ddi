# Usbspec.h header


This header is used by unknown technology.

Usbspec.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [USB_30_HUB_DESCRIPTOR structure](ns-usbspec--usb-30-hub-descriptor.md) | The USB_30_HUB_DESCRIPTOR structure contains a SuperSpeed hub descriptor. For information about the structure members, see Universal Serial Bus Revision 3.0 Specification, 10.13.2.1 Hub Descriptor, Table 10-3. SuperSpeed Hub Descriptor. |
| [USB_COMMON_DESCRIPTOR structure](ns-usbspec--usb-common-descriptor.md) | The USB_COMMON_DESCRIPTOR structure contains the head of the first descriptor that matches the search criteria in a call to USBD_ParseDescriptors. |
| [USB_CONFIGURATION_DESCRIPTOR structure](ns-usbspec--usb-configuration-descriptor.md) | The USB_CONFIGURATION_DESCRIPTOR structure is used by USB client drivers to hold a USB-defined configuration descriptor. |
| [USB_DEVICE_DESCRIPTOR structure](ns-usbspec--usb-device-descriptor.md) | The USB_DEVICE_DESCRIPTOR structure is used by USB client drivers to retrieve a USB-defined device descriptor. |
| [USB_DEVICE_QUALIFIER_DESCRIPTOR structure](ns-usbspec--usb-device-qualifier-descriptor.md) | The USB_DEVICE_QUALIFIER_DESCRIPTOR structure is used by USB client drivers to retrieve a USB-defined device qualifier descriptor. |
| [USB_ENDPOINT_DESCRIPTOR structure](ns-usbspec--usb-endpoint-descriptor.md) | The USB_ENDPOINT_DESCRIPTOR structure is used by USB client drivers to retrieve a USB-defined endpoint descriptor. |
| [USB_HUB_DESCRIPTOR structure](ns-usbspec--usb-hub-descriptor.md) | The USB_HUB_DESCRIPTOR structure contains a hub descriptor. |
| [USB_INTERFACE_DESCRIPTOR structure](ns-usbspec--usb-interface-descriptor.md) | The USB_INTERFACE_DESCRIPTOR structure is used by USB client drivers to retrieve a USB-defined interface descriptor. |
| [USB_STRING_DESCRIPTOR structure](ns-usbspec--usb-string-descriptor.md) | The USB_STRING_DESCRIPTOR structure is used by USB client drivers to hold a USB-defined string descriptor. |
| [USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR structure](ns-usbspec--usb-superspeed-endpoint-companion-descriptor.md) | The USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR structure is used by USB client drivers to retrieve a USB-defined SuperSpeed Endpoint Companion descriptor. For more information, see section 9.6.7 and Table 9-20 in the official USB 3.0 specification. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [USB_DEVICE_SPEED enumeration](ne-usbspec--usb-device-speed.md) | The USB_DEVICE_SPEED enumeration defines constants for USB device speeds. |
