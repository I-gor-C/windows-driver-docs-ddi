# Declarations in the usb header
This header Usb contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [USBD_TRANSFER_DIRECTION_FLAG function](nf-usb-usbd-transfer-direction-flag.md) | TBD |
| [USBD_PENDING function](nf-usb-usbd-pending.md) | TBD |
| [URB_FROM_IRP function](nf-usb-urb-from-irp.md) | TBD |
| [USBD_ERROR function](nf-usb-usbd-error.md) | TBD |
| [USBD_PIPE_DIRECTION_IN function](nf-usb-usbd-pipe-direction-in.md) | TBD |
| [USBD_SUCCESS function](nf-usb-usbd-success.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [URB_HCD_AREA structure](ns-usb--urb-hcd-area.md) | TBD |
| [URB_GET_FRAME_LENGTH structure](ns-usb--urb-get-frame-length.md) | TBD |
| [URB structure](ns-usb--urb.md) | The URB structure is used by USB client drivers to describe USB request blocks (URBs) that send requests to the USB driver stack. The URB structure defines a format for all possible commands that can be sent to a USB device. |
| [URB_CONTROL_GET_CONFIGURATION_REQUEST structure](ns-usb--urb-control-get-configuration-request.md) | TBD |
| [URB_ISOCH_TRANSFER structure](ns-usb--urb-isoch-transfer.md) | TBD |
| [URB_GET_CURRENT_FRAME_NUMBER structure](ns-usb--urb-get-current-frame-number.md) | TBD |
| [URB_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS structure](ns-usb--urb-get-isoch-pipe-transfer-path-delays.md) | TBD |
| [USBD_DEVICE_INFORMATION structure](ns-usb--usbd-device-information.md) | TBD |
| [URB_CONTROL_GET_STATUS_REQUEST structure](ns-usb--urb-control-get-status-request.md) | TBD |
| [URB_CONTROL_DESCRIPTOR_REQUEST structure](ns-usb--urb-control-descriptor-request.md) | TBD |
| [URB_CONTROL_VENDOR_OR_CLASS_REQUEST structure](ns-usb--urb-control-vendor-or-class-request.md) | TBD |
| [USBD_INTERFACE_INFORMATION structure](ns-usb--usbd-interface-information.md) | The USBD_INTERFACE_INFORMATION structure holds information about an interface for a configuration on a USB device. |
| [URB_OPEN_STATIC_STREAMS structure](ns-usb--urb-open-static-streams.md) | TBD |
| [URB_PIPE_REQUEST structure](ns-usb--urb-pipe-request.md) | TBD |
| [USBD_ENDPOINT_OFFLOAD_INFORMATION structure](ns-usb--usbd-endpoint-offload-information.md) | Stores xHCI-specific information that is used by client drivers to transfer data to and from the offloaded endpoints. |
| [URB_OS_FEATURE_DESCRIPTOR_REQUEST structure](ns-usb--urb-os-feature-descriptor-request.md) | TBD |
| [USBD_VERSION_INFORMATION structure](ns-usb--usbd-version-information.md) | The USBD_VERSION_INFORMATION structure is used by the GetUSBDIVersion function to report its output data. |
| [URB_SELECT_INTERFACE structure](ns-usb--urb-select-interface.md) | TBD |
| [URB_CONTROL_TRANSFER structure](ns-usb--urb-control-transfer.md) | TBD |
| [URB_SELECT_CONFIGURATION structure](ns-usb--urb-select-configuration.md) | TBD |
| [URB_FRAME_LENGTH_CONTROL structure](ns-usb--urb-frame-length-control.md) | TBD |
| [USBD_PIPE_INFORMATION structure](ns-usb--usbd-pipe-information.md) | The USBD_PIPE_INFORMATION structure is used by USB client drivers to hold information about a pipe from a specific interface. |
| [URB_CONTROL_TRANSFER_EX structure](ns-usb--urb-control-transfer-ex.md) | TBD |
| [OS_STRING structure](ns-usb--os-string.md) | TBD |
| [USBD_ISO_PACKET_DESCRIPTOR structure](ns-usb--usbd-iso-packet-descriptor.md) | The USBD_ISO_PACKET_DESCRIPTOR structure is used by USB client drivers to describe an isochronous transfer packet. |
| [URB_CONTROL_FEATURE_REQUEST structure](ns-usb--urb-control-feature-request.md) | TBD |
| [URB_BULK_OR_INTERRUPT_TRANSFER structure](ns-usb--urb-bulk-or-interrupt-transfer.md) | TBD |
| [URB_CONTROL_GET_INTERFACE_REQUEST structure](ns-usb--urb-control-get-interface-request.md) | TBD |
| [URB_HEADER structure](ns-usb--urb-header.md) | TBD |
| [USBD_STREAM_INFORMATION structure](ns-usb--usbd-stream-information.md) | The USBD_STREAM_INFORMATION structure stores information about a stream associated with a bulk endpoint. |
| [URB_SET_FRAME_LENGTH structure](ns-usb--urb-set-frame-length.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [USBD_PIPE_TYPE enumeration](ne-usb--usbd-pipe-type.md) | The USBD_PIPE_TYPE enumerator indicates the type of pipe. |
| [USB_CONTROLLER_FLAVOR enumeration](ne-usb--usb-controller-flavor.md) | The USB_CONTROLLER_FLAVOR enumeration specifies the type of USB host controller. |
| [USBD_ENDPOINT_OFFLOAD_MODE enumeration](ne-usb--usbd-endpoint-offload-mode.md) | Defines values for endpoint offloading options in the USB device or host controller. |

This header is used in these topics:

- [usbref](..content/_usbref)
