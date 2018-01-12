---
UID: NA:usbspec
---

# Usbspec.h header

## -description

This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Usbspec.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [_USB_30_HUB_DESCRIPTOR structure](ns-usbspec-_usb_30_hub_descriptor.md) | The USB_30_HUB_DESCRIPTOR structure contains a SuperSpeed hub descriptor. For information about the structure members, see Universal Serial Bus Revision 3.0 Specification, 10.13.2.1 Hub Descriptor, Table 10-3. SuperSpeed Hub Descriptor. |
| [_USB_COMMON_DESCRIPTOR structure](ns-usbspec-_usb_common_descriptor.md) | The USB_COMMON_DESCRIPTOR structure contains the head of the first descriptor that matches the search criteria in a call to USBD_ParseDescriptors. |
| [_USB_CONFIGURATION_DESCRIPTOR structure](ns-usbspec-_usb_configuration_descriptor.md) | The USB_CONFIGURATION_DESCRIPTOR structure is used by USB client drivers to hold a USB-defined configuration descriptor. |
| [_USB_DEVICE_DESCRIPTOR structure](ns-usbspec-_usb_device_descriptor.md) | The USB_DEVICE_DESCRIPTOR structure is used by USB client drivers to retrieve a USB-defined device descriptor. |
| [_USB_DEVICE_QUALIFIER_DESCRIPTOR structure](ns-usbspec-_usb_device_qualifier_descriptor.md) | The USB_DEVICE_QUALIFIER_DESCRIPTOR structure is used by USB client drivers to retrieve a USB-defined device qualifier descriptor. |
| [_USB_ENDPOINT_DESCRIPTOR structure](ns-usbspec-_usb_endpoint_descriptor.md) | The USB_ENDPOINT_DESCRIPTOR structure is used by USB client drivers to retrieve a USB-defined endpoint descriptor. |
| [_USB_HUB_DESCRIPTOR structure](ns-usbspec-_usb_hub_descriptor.md) | The USB_HUB_DESCRIPTOR structure contains a hub descriptor. |
| [_USB_INTERFACE_DESCRIPTOR structure](ns-usbspec-_usb_interface_descriptor.md) | The USB_INTERFACE_DESCRIPTOR structure is used by USB client drivers to retrieve a USB-defined interface descriptor. |
| [_USB_STRING_DESCRIPTOR structure](ns-usbspec-_usb_string_descriptor.md) | The USB_STRING_DESCRIPTOR structure is used by USB client drivers to hold a USB-defined string descriptor. |
| [_USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR structure](ns-usbspec-_usb_superspeed_endpoint_companion_descriptor.md) | The USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR structure is used by USB client drivers to retrieve a USB-defined SuperSpeed Endpoint Companion descriptor. For more information, see section 9.6.7 and Table 9-20 in the official USB 3.0 specification. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_USB_DEVICE_SPEED enumeration](ne-usbspec-_usb_device_speed.md) | The USB_DEVICE_SPEED enumeration defines constants for USB device speeds. |
