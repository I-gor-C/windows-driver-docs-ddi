# Usbfnbase.h header


This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Usbfnbase.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [ALTERNATE_INTERFACE structure](ns-usbfnbase--alternate-interface.md) | The ALTERNATE_INTERFACE structure provides information about alternate settings for a Universal Serial Bus (USB) interface. |
| [USBFN_BUS_CONFIGURATION_INFO structure](ns-usbfnbase--usbfn-bus-configuration-info.md) | Configuration packet that stores information about an available USB configuration. |
| [USBFN_CLASS_INFORMATION_PACKET structure](ns-usbfnbase--usbfn-class-information-packet.md) | Describes device interface class information associated with a USB interface. This structure can only hold information about a single function interface. |
| [USBFN_CLASS_INFORMATION_PACKET_EX structure](ns-usbfnbase--usbfn-class-information-packet-ex.md) | Describes device interface class information associated with a USB interface. This structure can be used to describe single and multi-interface functions. |
| [USBFN_CLASS_INTERFACE structure](ns-usbfnbase--usbfn-class-interface.md) | Describes an interface and its endpoints. |
| [USBFN_CLASS_INTERFACE_EX structure](ns-usbfnbase--usbfn-class-interface-ex.md) | Describes an interface and its endpoints. |
| [USBFN_INTERFACE_INFO structure](ns-usbfnbase--usbfn-interface-info.md) | Describes an interface and its endpoints. |
| [USBFN_NOTIFICATION structure](ns-usbfnbase--usbfn-notification.md) | Describes information about a Universal Serial Bus (USB) event notification that was received by using IOCTL_INTERNAL_USBFN_BUS_EVENT_NOTIFICATION. |
| [USBFN_PIPE_INFORMATION structure](ns-usbfnbase--usbfn-pipe-information.md) | Describes attributes of a pipe associated with an endpoint on a specific interface. |
| [USBFN_USB_STRING structure](ns-usbfnbase--usbfn-usb-string.md) | Describes a USB string descriptor and the associated string index. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [USBFN_BUS_SPEED enumeration](ne-usbfnbase--usbfn-bus-speed.md) | The USBFN_BUS_SPEED enumeration defines possible bus speeds. |
| [USBFN_DEVICE_STATE enumeration](ne-usbfnbase--usbfn-device-state.md) | Defines the Universal Serial Bus (USB) device states for the device/controller. These states correspond to the USB device states as defined in section 9.1 of the USB 2.0 Specification. |
| [USBFN_DIRECTION enumeration](ne-usbfnbase--usbfn-direction.md) | Defines the USB data transfer direction types. |
| [USBFN_EVENT enumeration](ne-usbfnbase--usbfn-event.md) | Defines notifications sent to class drivers. |
| [USBFN_PORT_TYPE enumeration](ne-usbfnbase--usbfn-port-type.md) | Defines the possible port types that can be returned by the client driver during port detection. |
