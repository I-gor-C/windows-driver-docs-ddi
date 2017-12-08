# Usbfnioctl.h header


This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Usbfnioctl.h contain these programming interfaces:


## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_INTERNAL_USBFN_ACTIVATE_USB_BUS IOCTL](ni-usbfnioctl-ioctl-internal-usbfn-activate-usb-bus.md) | The USB class driver sends this request to activate the bus so that the driver can prepare to process bus events and handle traffic. |
| [IOCTL_INTERNAL_USBFN_BUS_EVENT_NOTIFICATION IOCTL](ni-usbfnioctl-ioctl-internal-usbfn-bus-event-notification.md) | The USB class driver sends this request to prepare for notifications received from the USB function class extension (UFX) in response to an event on the bus, such as a change in the port type or a receipt of a non-standard setup packet. |
| [IOCTL_INTERNAL_USBFN_CONTROL_STATUS_HANDSHAKE_IN IOCTL](ni-usbfnioctl-ioctl-internal-usbfn-control-status-handshake-in.md) | The class driver sends this request to send a zero-length control status handshake on endpoint 0 in the IN direction. |
| [IOCTL_INTERNAL_USBFN_CONTROL_STATUS_HANDSHAKE_OUT IOCTL](ni-usbfnioctl-ioctl-internal-usbfn-control-status-handshake-out.md) | The class driver sends this request to send a zero-length control status handshake on endpoint 0 in the OUT direction. |
| [IOCTL_INTERNAL_USBFN_GET_CLASS_INFO IOCTL](ni-usbfnioctl-ioctl-internal-usbfn-get-class-info.md) | The class driver sends this request IO control code to retrieve information about the available pipes for a device, as configured in the registry. |
| [IOCTL_INTERNAL_USBFN_GET_INTERFACE_DESCRIPTOR_SET IOCTL](ni-usbfnioctl-ioctl-internal-usbfn-get-interface-descriptor-set.md) | The class driver sends this request to get the entire USB interface descriptor set for a function on the device. |
| [IOCTL_INTERNAL_USBFN_GET_PIPE_STATE IOCTL](ni-usbfnioctl-ioctl-internal-usbfn-get-pipe-state.md) | The class driver sends this request to get the stall state of the specified pipe. |
| [IOCTL_INTERNAL_USBFN_REGISTER_USB_STRING IOCTL](ni-usbfnioctl-ioctl-internal-usbfn-register-usb-string.md) | The class driver sends this request to register a USB string descriptor. |
| [IOCTL_INTERNAL_USBFN_SET_PIPE_STATE IOCTL](ni-usbfnioctl-ioctl-internal-usbfn-set-pipe-state.md) | The class driver sends this request to set the stall state of the specified USB pipe. |
| [IOCTL_INTERNAL_USBFN_SIGNAL_REMOTE_WAKEUP IOCTL](ni-usbfnioctl-ioctl-internal-usbfn-signal-remote-wakeup.md) | The class driver sends this request to get remote wake-up notifications from endpoints. |
| [IOCTL_INTERNAL_USBFN_TRANSFER_IN IOCTL](ni-usbfnioctl-ioctl-internal-usbfn-transfer-in.md) | The class driver sends this request to initiate a data transfer to the host on the specified pipe. |
| [IOCTL_INTERNAL_USBFN_TRANSFER_IN_APPEND_ZERO_PKT IOCTL](ni-usbfnioctl-ioctl-internal-usbfn-transfer-in-append-zero-pkt.md) | The class driver sends this request to initiate an IN transfer to the specified pipe and appends a zero-length packet to indicate the end of the transfer. |
| [IOCTL_INTERNAL_USBFN_TRANSFER_OUT IOCTL](ni-usbfnioctl-ioctl-internal-usbfn-transfer-out.md) | The class driver sends this request to initiate a data transfer from the host on the specified pipe. |
