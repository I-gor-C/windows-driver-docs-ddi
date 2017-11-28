# Usb.h header


This header is used by unknown technology.

Usb.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [URB structure](ns-usb--urb.md) | The URB structure is used by USB client drivers to describe USB request blocks (URBs) that send requests to the USB driver stack. The URB structure defines a format for all possible commands that can be sent to a USB device. |
| [URB_BULK_OR_INTERRUPT_TRANSFER structure](ns-usb--urb-bulk-or-interrupt-transfer.md) | The _URB_BULK_OR_INTERRUPT_TRANSFER structure is used by USB client drivers to send or receive data on a bulk pipe or on an interrupt pipe. |
| [URB_CONTROL_DESCRIPTOR_REQUEST structure](ns-usb--urb-control-descriptor-request.md) | The _URB_CONTROL_DESCRIPTOR_REQUEST structure is used by USB client drivers to get or set descriptors on a USB device. |
| [URB_CONTROL_FEATURE_REQUEST structure](ns-usb--urb-control-feature-request.md) | The _URB_CONTROL_FEATURE_REQUEST structure is used by USB client drivers to set or clear features on a device, interface, or endpoint. |
| [URB_CONTROL_GET_CONFIGURATION_REQUEST structure](ns-usb--urb-control-get-configuration-request.md) | The _URB_CONTROL_GET_CONFIGURATION_REQUEST structure is used by USB client drivers to retrieve the current configuration for a device. |
| [URB_CONTROL_GET_INTERFACE_REQUEST structure](ns-usb--urb-control-get-interface-request.md) | The _URB_CONTROL_GET_INTERFACE_REQUEST structure is used by USB client drivers to retrieve the current alternate interface setting for an interface in the current configuration. |
| [URB_CONTROL_GET_STATUS_REQUEST structure](ns-usb--urb-control-get-status-request.md) | The _URB_CONTROL_GET_STATUS_REQUEST structure is used by USB client drivers to retrieve status from a device, interface, endpoint, or other device-defined target. |
| [URB_CONTROL_TRANSFER structure](ns-usb--urb-control-transfer.md) | The _URB_CONTROL_TRANSFER structure is used by USB client drivers to transfer data to or from a control pipe. |
| [URB_CONTROL_TRANSFER_EX structure](ns-usb--urb-control-transfer-ex.md) | The _URB_CONTROL_TRANSFER_EX structure is used by USB client drivers to transfer data to or from a control pipe, with a timeout that limits the acceptable transfer time. |
| [URB_CONTROL_VENDOR_OR_CLASS_REQUEST structure](ns-usb--urb-control-vendor-or-class-request.md) | The _URB_CONTROL_VENDOR_OR_CLASS_REQUEST structure is used by USB client drivers to issue a vendor or class-specific command to a device, interface, endpoint, or other device-defined target. |
| [URB_GET_CURRENT_FRAME_NUMBER structure](ns-usb--urb-get-current-frame-number.md) | The _URB_GET_CURRENT_FRAME_NUMBER structure is used by USB client drivers to retrieve the current frame number. |
| [URB_HEADER structure](ns-usb--urb-header.md) | The _URB_HEADER structure is used by USB client drivers to provide basic information about the request being sent to the host controller driver. |
| [URB_ISOCH_TRANSFER structure](ns-usb--urb-isoch-transfer.md) | The _URB_ISOCH_TRANSFER structure is used by USB client drivers to send data to or retrieve data from an isochronous transfer pipe. |
| [URB_OPEN_STATIC_STREAMS structure](ns-usb--urb-open-static-streams.md) | The _URB_OPEN_STATIC_STREAMS structure is used by a USB client driver to open streams in the specified bulk endpoint. |
| [URB_OS_FEATURE_DESCRIPTOR_REQUEST structure](ns-usb--urb-os-feature-descriptor-request.md) | The _URB_OS_FEATURE_DESCRIPTOR_REQUEST structure is used by the USB hub driver to retrieve Microsoft OS Feature Descriptors from a USB device or an interface on a USB device. |
| [URB_PIPE_REQUEST structure](ns-usb--urb-pipe-request.md) | The _URB_PIPE_REQUEST structure is used by USB client drivers to clear a stall condition on an endpoint. |
| [URB_SELECT_CONFIGURATION structure](ns-usb--urb-select-configuration.md) | The _URB_SELECT_CONFIGURATION structure is used by client drivers to select a configuration for a USB device. |
| [URB_SELECT_INTERFACE structure](ns-usb--urb-select-interface.md) | The _URB_SELECT_INTERFACE structure is used by USB client drivers to select an alternate setting for an interface or to change the maximum packet size of a pipe in the current configuration on a USB device. |
| [USBD_ENDPOINT_OFFLOAD_INFORMATION structure](ns-usb--usbd-endpoint-offload-information.md) | Stores xHCI-specific information that is used by client drivers to transfer data to and from the offloaded endpoints. |
| [USBD_INTERFACE_INFORMATION structure](ns-usb--usbd-interface-information.md) | The USBD_INTERFACE_INFORMATION structure holds information about an interface for a configuration on a USB device. |
| [USBD_ISO_PACKET_DESCRIPTOR structure](ns-usb--usbd-iso-packet-descriptor.md) | The USBD_ISO_PACKET_DESCRIPTOR structure is used by USB client drivers to describe an isochronous transfer packet. |
| [USBD_PIPE_INFORMATION structure](ns-usb--usbd-pipe-information.md) | The USBD_PIPE_INFORMATION structure is used by USB client drivers to hold information about a pipe from a specific interface. |
| [USBD_STREAM_INFORMATION structure](ns-usb--usbd-stream-information.md) | The USBD_STREAM_INFORMATION structure stores information about a stream associated with a bulk endpoint. |
| [USBD_VERSION_INFORMATION structure](ns-usb--usbd-version-information.md) | The USBD_VERSION_INFORMATION structure is used by the GetUSBDIVersion function to report its output data. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [USBD_ENDPOINT_OFFLOAD_MODE enumeration](ne-usb--usbd-endpoint-offload-mode.md) | Defines values for endpoint offloading options in the USB device or host controller. |
| [USBD_PIPE_TYPE enumeration](ne-usb--usbd-pipe-type.md) | The USBD_PIPE_TYPE enumerator indicates the type of pipe. |
| [USB_CONTROLLER_FLAVOR enumeration](ne-usb--usb-controller-flavor.md) | The USB_CONTROLLER_FLAVOR enumeration specifies the type of USB host controller. |
