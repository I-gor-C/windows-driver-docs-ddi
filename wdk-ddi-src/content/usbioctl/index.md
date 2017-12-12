---
UID: NA:
---

# Usbioctl.h header

## -description

This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Usbioctl.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [_HUB_DEVICE_CONFIG_INFO_V1 structure](ns-usbioctl-_hub_device_config_info_v1.md) | The HUB_DEVICE_CONFIG_INFO structure is used in conjunction with the kernel-mode IOCTL, IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO to request to report information about a USB device and the hub to which the device is attached. |
| [_USB_CYCLE_PORT_PARAMS structure](ns-usbioctl-_usb_cycle_port_params.md) | The USB_CYCLE_PORT_PARAMS structure is used with the IOCTL_USB_HUB_CYCLE_PORT I/O control request to power cycle the port that is associated with the PDO that receives the request. |
| [_USB_DESCRIPTOR_REQUEST structure](ns-usbioctl-_usb_descriptor_request.md) | The USB_DESCRIPTOR_REQUEST structure is used with the IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION I/O control request to retrieve one or more descriptors for the device that is associated with the indicated connection index. |
| [_USB_DEVICE_CHARACTERISTICS structure](ns-usbioctl-_usb_device_characteristics.md) | Contains information about the USB device’s characteristics, such as the maximum send and receive delays for any request. This structure is used in the IOCTL_USB_GET_DEVICE_CHARACTERISTICS request. |
| [_USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION structure](ns-usbioctl-_usb_frame_number_and_qpc_for_time_sync_information.md) | Stores the frame and microframe numbers and the calculated system QPC values. This structure is used in the IOCTL_USB_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC request. |
| [_USB_HCD_DRIVERKEY_NAME structure](ns-usbioctl-_usb_hcd_driverkey_name.md) | The USB_HCD_DRIVERKEY_NAME structure is used with the IOCTL_GET_HCD_DRIVERKEY_NAME I/O control request to retrieve the driver key in the registry for the USB host controller driver. |
| [_USB_HUB_CAPABILITIES structure](ns-usbioctl-_usb_hub_capabilities.md) | The USB_HUB_CAPABILITIES structure has been deprecated. Use USB_HUB_CAPABILITIES_EX instead. |
| [_USB_HUB_CAPABILITIES_EX structure](ns-usbioctl-_usb_hub_capabilities_ex.md) | The USB_HUB_CAPABILITIES_EX structure is used with the IOCTL_USB_GET_HUB_CAPABILITIES I/O control request to retrieve the capabilities of a particular USB hub. |
| [_USB_HUB_CAP_FLAGS structure](ns-usbioctl-_usb_hub_cap_flags.md) | The USB_HUB_CAP_FLAGS structure is used to report the capabilities of a hub. |
| [_USB_HUB_INFORMATION structure](ns-usbioctl-_usb_hub_information.md) | The USB_HUB_INFORMATION structure contains information about a hub. |
| [_USB_HUB_INFORMATION_EX structure](ns-usbioctl-_usb_hub_information_ex.md) | The USB_HUB_INFORMATION_EX structure is used with the IOCTL_USB_GET_HUB_INFORMATION_EX I/O control request to retrieve information about a Universal Serial Bus (USB) hub. |
| [_USB_HUB_NAME structure](ns-usbioctl-_usb_hub_name.md) | The USB_HUB_NAME structure stores the hub's symbolic device name. |
| [_USB_ID_STRING structure](ns-usbioctl-_usb_id_string.md) | The USB_ID_STRING structure is used to store a string or multi-string. |
| [_USB_MI_PARENT_INFORMATION structure](ns-usbioctl-_usb_mi_parent_information.md) | The USB_MI_PARENT_INFORMATION structure contains information about a composite device. |
| [_USB_NODE_CONNECTION_ATTRIBUTES structure](ns-usbioctl-_usb_node_connection_attributes.md) | The USB_NODE_CONNECTION_ATTRIBUTES structure is used with the IOCTL_USB_GET_NODE_CONNECTION_ATTRIBUTES I/O control request to retrieve the attributes of a connection. |
| [_USB_NODE_CONNECTION_DRIVERKEY_NAME structure](ns-usbioctl-_usb_node_connection_driverkey_name.md) | The USB_NODE_CONNECTION_DRIVERKEY_NAME structure is used with the IOCTL_USB_GET_NODE_CONNECTION_DRIVERKEY_NAME I/O control request to retrieve the driver key name for the device that is connected to the indicated port. |
| [_USB_NODE_CONNECTION_INFORMATION structure](ns-usbioctl-_usb_node_connection_information.md) | The USB_NODE_CONNECTION_INFORMATION structure is used with the IOCTL_USB_GET_NODE_CONNECTION_INFORMATION request to retrieve information about a USB port and connected device. |
| [_USB_NODE_CONNECTION_INFORMATION_EX structure](ns-usbioctl-_usb_node_connection_information_ex.md) | The USB_NODE_CONNECTION_INFORMATION_EX structure is used in conjunction with the IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX request to obtain information about the connection associated with the indicated USB port. |
| [_USB_NODE_CONNECTION_INFORMATION_EX_V2 structure](ns-usbioctl-_usb_node_connection_information_ex_v2.md) | The USB_NODE_CONNECTION_INFORMATION_EX_V2 structure is used with the IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX_V2 I/O control request to retrieve speed information about a Universal Serial Bus (USB) device that is attached to a particular port. |
| [_USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS structure](ns-usbioctl-_usb_node_connection_information_ex_v2_flags.md) | The USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS union is used to indicate the speed at which a USB 3.0 device is currently operating and whether it can operate at higher speed, when attached to a particular port. |
| [_USB_NODE_CONNECTION_NAME structure](ns-usbioctl-_usb_node_connection_name.md) | The USB_NODE_CONNECTION_NAME structure is used with the IOCTL_USB_GET_NODE_CONNECTION_NAME I/O control request to retrieve the symbolic link of the downstream hub that is attached to the port. |
| [_USB_NODE_INFORMATION structure](ns-usbioctl-_usb_node_information.md) | The USB_NODE_INFORMATION structure is used with the IOCTL_USB_GET_NODE_INFORMATION I/O control request to retrieve information about a parent device. |
| [_USB_PIPE_INFO structure](ns-usbioctl-_usb_pipe_info.md) | The USB_PIPE_INFO structure is used in conjunction with the USB_NODE_CONNECTION_INFORMATION_EX structure and the IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX request to obtain information about a connection and its associated pipes. |
| [_USB_PORT_CONNECTOR_PROPERTIES structure](ns-usbioctl-_usb_port_connector_properties.md) | The USB_PORT_CONNECTOR_PROPERTIES structure is used with the IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES I/O control request to retrieve information about a port on a particular SuperSpeed hub. |
| [_USB_PORT_PROPERTIES structure](ns-usbioctl-_usb_port_properties.md) | The USB_PORT_PROPERTIES union is used to report the capabilities of a Universal Serial Bus (USB) port.The port capabilities are retrieved in the USB_PORT_CONNECTOR_PROPERTIES structure by the IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES I/O control request. |
| [_USB_PROTOCOLS structure](ns-usbioctl-_usb_protocols.md) | The USB_PROTOCOLS union is used to report the Universal Serial Bus (USB) signaling protocols that are supported by the port. |
| [_USB_ROOT_HUB_NAME structure](ns-usbioctl-_usb_root_hub_name.md) | The USB_ROOT_HUB_NAME structure stores the root hub's symbolic device name. |
| [_USB_START_TRACKING_FOR_TIME_SYNC_INFORMATION structure](ns-usbioctl-_usb_start_tracking_for_time_sync_information.md) | The input and output buffer for the IOCTL_USB_START_TRACKING_FOR_TIME_SYNC request. |
| [_USB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION structure](ns-usbioctl-_usb_stop_tracking_for_time_sync_information.md) | The input buffer for the IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC request. |
| [_USB_TOPOLOGY_ADDRESS structure](ns-usbioctl-_usb_topology_address.md) | The USB_TOPOLOGY_ADDRESS structure is used with the IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS I/O request to retrieve information about a USB device?s location in the USB device tree. |
| [_USB_TRANSPORT_CHARACTERISTICS structure](ns-usbioctl-_usb_transport_characteristics.md) | Stores the transport characteristics at relevant points in time. This structure is used in the IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS request. |
| [_USB_TRANSPORT_CHARACTERISTICS_CHANGE_NOTIFICATION structure](ns-usbioctl-_usb_transport_characteristics_change_notification.md) | Contains registration information filled when the IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE request completes. |
| [_USB_TRANSPORT_CHARACTERISTICS_CHANGE_REGISTRATION structure](ns-usbioctl-_usb_transport_characteristics_change_registration.md) | Contains registration information for the IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE request. |
| [_USB_TRANSPORT_CHARACTERISTICS_CHANGE_UNREGISTRATION structure](ns-usbioctl-_usb_transport_characteristics_change_unregistration.md) | Contains unregistration information for the IOCTL_USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE request. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_USB_GET_DEVICE_CHARACTERISTICS IOCTL](ni-usbioctl-ioctl_usb_get_device_characteristics.md) | The client driver sends this request to determine general characteristics about a USB device, such as maximum send and receive delays for any request. |
| [IOCTL_USB_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC IOCTL](ni-usbioctl-ioctl_usb_get_frame_number_and_qpc_for_time_sync.md) | . |
| [IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS IOCTL](ni-usbioctl-ioctl_usb_get_transport_characteristics.md) | The client driver sends this request to retrieve the transport characteristics. |
| [IOCTL_USB_NOTIFY_ON_TRANSPORT_CHARACTERISTICS_CHANGE IOCTL](ni-usbioctl-ioctl_usb_notify_on_transport_characteristics_change.md) | This request notifies the caller of change in transport characteristics. |
| [IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE IOCTL](ni-usbioctl-ioctl_usb_register_for_transport_characteristics_change.md) | This request registers for notifications about the changes in transport characteristics. |
| [IOCTL_USB_START_TRACKING_FOR_TIME_SYNC IOCTL](ni-usbioctl-ioctl_usb_start_tracking_for_time_sync.md) | This request registers the caller with USB driver stack for time sync services. |
| [IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC IOCTL](ni-usbioctl-ioctl_usb_stop_tracking_for_time_sync.md) | This request unegisters the caller with USB driver stack for time sync services. |
| [IOCTL_USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE IOCTL](ni-usbioctl-ioctl_usb_unregister_for_transport_characteristics_change.md) | This request unregisters the caller from getting notifications about transport characteristics changes. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_USB_CONNECTION_STATUS enumeration](ne-usbioctl-_usb_connection_status.md) | The USB_CONNECTION_STATUS enumerator indicates the status of the connection to a device on a USB hub port. |
| [_USB_CONNECTION_STATUS enumeration](ne-usbioctl-_usb_connection_status~r1.md) | The USB_CONNECTION_STATUS enumerator indicates the status of the connection to a device on a USB hub port. |
| [_USB_CONNECTION_STATUS enumeration](ne-usbioctl-_usb_connection_status~r2.md) | The USB_CONNECTION_STATUS enumerator indicates the status of the connection to a device on a USB hub port. |
| [_USB_HUB_NODE enumeration](ne-usbioctl-_usb_hub_node.md) | The USB_HUB_NODE enumerator indicates whether a device is a hub or a composite device. |
| [_USB_HUB_TYPE enumeration](ne-usbioctl-_usb_hub_type.md) | The USB_HUB_TYPE enumeration defines constants that indicate the type of USB hub. The hub type is retrieved by the IOCTL_USB_GET_HUB_INFORMATION_EX I/O control request. |
