---
UID: NA:usb
ms.assetid: ab8aa396-e172-3b47-a11f-f0bf7862c545
ms.author: windowsdriverdev
ms.date: 01/18/18
ms.keywords: 
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: portal
---

# usb.h header



usb.h contains the following programming interfaces:







## Structures
| Title | Description |
| ---- |:---- |
| [_URB](ns-usb-_urb.md) | The URB structure is used by USB client drivers to describe USB request blocks (URBs) that send requests to the USB driver stack. The URB structure defines a format for all possible commands that can be sent to a USB device. |
| [_URB_BULK_OR_INTERRUPT_TRANSFER](ns-usb-_urb_bulk_or_interrupt_transfer.md) | The _URB_BULK_OR_INTERRUPT_TRANSFER structure is used by USB client drivers to send or receive data on a bulk pipe or on an interrupt pipe. |
| [_URB_CONTROL_DESCRIPTOR_REQUEST](ns-usb-_urb_control_descriptor_request.md) | The _URB_CONTROL_DESCRIPTOR_REQUEST structure is used by USB client drivers to get or set descriptors on a USB device. |
| [_URB_CONTROL_FEATURE_REQUEST](ns-usb-_urb_control_feature_request.md) | The _URB_CONTROL_FEATURE_REQUEST structure is used by USB client drivers to set or clear features on a device, interface, or endpoint. |
| [_URB_CONTROL_GET_CONFIGURATION_REQUEST](ns-usb-_urb_control_get_configuration_request.md) | The _URB_CONTROL_GET_CONFIGURATION_REQUEST structure is used by USB client drivers to retrieve the current configuration for a device. |
| [_URB_CONTROL_GET_INTERFACE_REQUEST](ns-usb-_urb_control_get_interface_request.md) | The _URB_CONTROL_GET_INTERFACE_REQUEST structure is used by USB client drivers to retrieve the current alternate interface setting for an interface in the current configuration. |
| [_URB_CONTROL_GET_STATUS_REQUEST](ns-usb-_urb_control_get_status_request.md) | The _URB_CONTROL_GET_STATUS_REQUEST structure is used by USB client drivers to retrieve status from a device, interface, endpoint, or other device-defined target. |
| [_URB_CONTROL_TRANSFER](ns-usb-_urb_control_transfer.md) | The _URB_CONTROL_TRANSFER structure is used by USB client drivers to transfer data to or from a control pipe. |
| [_URB_CONTROL_TRANSFER_EX](ns-usb-_urb_control_transfer_ex.md) | The _URB_CONTROL_TRANSFER_EX structure is used by USB client drivers to transfer data to or from a control pipe, with a timeout that limits the acceptable transfer time. |
| [_URB_CONTROL_VENDOR_OR_CLASS_REQUEST](ns-usb-_urb_control_vendor_or_class_request.md) | The _URB_CONTROL_VENDOR_OR_CLASS_REQUEST structure is used by USB client drivers to issue a vendor or class-specific command to a device, interface, endpoint, or other device-defined target. |
| [_URB_GET_CURRENT_FRAME_NUMBER](ns-usb-_urb_get_current_frame_number.md) | The _URB_GET_CURRENT_FRAME_NUMBER structure is used by USB client drivers to retrieve the current frame number. |
| [_URB_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS](ns-usb-_urb_get_isoch_pipe_transfer_path_delays.md) | The _URB_GET_ISOCH_PIPE_TRANSFER_PATH_DELAYS structure is used by USB client drivers to retrieve delays associated with isochronous transfer programming in the host controller and transfer completion so that the client driver can ensure that the device gets the isochronous packets in time. |
| [_URB_HEADER](ns-usb-_urb_header.md) | The _URB_HEADER structure is used by USB client drivers to provide basic information about the request being sent to the host controller driver. |
| [_URB_ISOCH_TRANSFER](ns-usb-_urb_isoch_transfer.md) | The _URB_ISOCH_TRANSFER structure is used by USB client drivers to send data to or retrieve data from an isochronous transfer pipe. |
| [_URB_OPEN_STATIC_STREAMS](ns-usb-_urb_open_static_streams.md) | The _URB_OPEN_STATIC_STREAMS structure is used by a USB client driver to open streams in the specified bulk endpoint. |
| [_URB_OS_FEATURE_DESCRIPTOR_REQUEST](ns-usb-_urb_os_feature_descriptor_request.md) | The _URB_OS_FEATURE_DESCRIPTOR_REQUEST structure is used by the USB hub driver to retrieve Microsoft OS Feature Descriptors from a USB device or an interface on a USB device. |
| [_URB_PIPE_REQUEST](ns-usb-_urb_pipe_request.md) | The _URB_PIPE_REQUEST structure is used by USB client drivers to clear a stall condition on an endpoint. |
| [_URB_SELECT_CONFIGURATION](ns-usb-_urb_select_configuration.md) | The _URB_SELECT_CONFIGURATION structure is used by client drivers to select a configuration for a USB device. |
| [_URB_SELECT_INTERFACE](ns-usb-_urb_select_interface.md) | The _URB_SELECT_INTERFACE structure is used by USB client drivers to select an alternate setting for an interface or to change the maximum packet size of a pipe in the current configuration on a USB device. |
| [_USBD_ENDPOINT_OFFLOAD_INFORMATION](ns-usb-_usbd_endpoint_offload_information.md) | Stores xHCI-specific information that is used by client drivers to transfer data to and from the offloaded endpoints. |
| [_USBD_INTERFACE_INFORMATION](ns-usb-_usbd_interface_information.md) | The USBD_INTERFACE_INFORMATION structure holds information about an interface for a configuration on a USB device. |
| [_USBD_ISO_PACKET_DESCRIPTOR](ns-usb-_usbd_iso_packet_descriptor.md) | The USBD_ISO_PACKET_DESCRIPTOR structure is used by USB client drivers to describe an isochronous transfer packet. |
| [_USBD_PIPE_INFORMATION](ns-usb-_usbd_pipe_information.md) | The USBD_PIPE_INFORMATION structure is used by USB client drivers to hold information about a pipe from a specific interface. |
| [_USBD_STREAM_INFORMATION](ns-usb-_usbd_stream_information.md) | The USBD_STREAM_INFORMATION structure stores information about a stream associated with a bulk endpoint. |
| [_USBD_VERSION_INFORMATION](ns-usb-_usbd_version_information.md) | The USBD_VERSION_INFORMATION structure is used by the GetUSBDIVersion function to report its output data. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_USB_CONTROLLER_FLAVOR](ne-usb-_usb_controller_flavor.md) | The USB_CONTROLLER_FLAVOR enumeration specifies the type of USB host controller. |
| [_USBD_ENDPOINT_OFFLOAD_MODE](ne-usb-_usbd_endpoint_offload_mode.md) | Defines values for endpoint offloading options in the USB device or host controller. |
| [_USBD_PIPE_TYPE](ne-usb-_usbd_pipe_type.md) | The USBD_PIPE_TYPE enumerator indicates the type of pipe. |