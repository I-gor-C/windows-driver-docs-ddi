---
UID: NA:usbfnbase
---

# Usbfnbase.h header

## -description

This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Usbfnbase.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [_ALTERNATE_INTERFACE structure](ns-usbfnbase-_alternate_interface.md) | The ALTERNATE_INTERFACE structure provides information about alternate settings for a Universal Serial Bus (USB) interface. |
| [_USBFN_BUS_CONFIGURATION_INFO structure](ns-usbfnbase-_usbfn_bus_configuration_info.md) | Configuration packet that stores information about an available USB configuration. |
| [_USBFN_CLASS_INFORMATION_PACKET structure](ns-usbfnbase-_usbfn_class_information_packet.md) | Describes device interface class information associated with a USB interface. This structure can only hold information about a single function interface. |
| [_USBFN_CLASS_INFORMATION_PACKET_EX structure](ns-usbfnbase-_usbfn_class_information_packet_ex.md) | Describes device interface class information associated with a USB interface. This structure can be used to describe single and multi-interface functions. |
| [_USBFN_CLASS_INTERFACE structure](ns-usbfnbase-_usbfn_class_interface.md) | Describes an interface and its endpoints. |
| [_USBFN_CLASS_INTERFACE_EX structure](ns-usbfnbase-_usbfn_class_interface_ex.md) | Describes an interface and its endpoints. |
| [_USBFN_INTERFACE_INFO structure](ns-usbfnbase-_usbfn_interface_info.md) | Describes an interface and its endpoints. |
| [_USBFN_NOTIFICATION structure](ns-usbfnbase-_usbfn_notification.md) | Describes information about a Universal Serial Bus (USB) event notification that was received by using IOCTL_INTERNAL_USBFN_BUS_EVENT_NOTIFICATION. |
| [_USBFN_PIPE_INFORMATION structure](ns-usbfnbase-_usbfn_pipe_information.md) | Describes attributes of a pipe associated with an endpoint on a specific interface. |
| [_USBFN_USB_STRING structure](ns-usbfnbase-_usbfn_usb_string.md) | Describes a USB string descriptor and the associated string index. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_USBFN_BUS_SPEED enumeration](ne-usbfnbase-_usbfn_bus_speed.md) | The USBFN_BUS_SPEED enumeration defines possible bus speeds. |
| [_USBFN_DEVICE_STATE enumeration](ne-usbfnbase-_usbfn_device_state.md) | Defines the Universal Serial Bus (USB) device states for the device/controller. These states correspond to the USB device states as defined in section 9.1 of the USB 2.0 Specification. |
| [_USBFN_DIRECTION enumeration](ne-usbfnbase-_usbfn_direction.md) | Defines the USB data transfer direction types. |
| [_USBFN_EVENT enumeration](ne-usbfnbase-_usbfn_event.md) | Defines notifications sent to class drivers. |
| [_USBFN_PORT_TYPE enumeration](ne-usbfnbase-_usbfn_port_type.md) | Defines the possible port types that can be returned by the client driver during port detection. |
