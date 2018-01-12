---
UID: NA:usbioctl
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
| [IOCTL_GET_HCD_DRIVERKEY_NAME IOCTL](ni-usbioctl-ioctl_get_hcd_driverkey_name.md) | The IOCTL_GET_HCD_DRIVERKEY_NAME I/O control request retrieves the driver key name in the registry for a USB host controller driver. |
| [IOCTL_INTERNAL_USB_CYCLE_PORT IOCTL](ni-usbioctl-ioctl_internal_usb_cycle_port.md) | The IOCTL_INTERNAL_USB_CYCLE_PORT I/O request simulates a device unplug and replug on the port associated with the PDO. |
| [IOCTL_INTERNAL_USB_ENABLE_PORT IOCTL](ni-usbioctl-ioctl_internal_usb_enable_port.md) | The IOCTL_INTERNAL_USB_ENABLE_PORT IOCTL has been deprecated. Do not use. |
| [IOCTL_INTERNAL_USB_GET_BUSGUID_INFO IOCTL](ni-usbioctl-ioctl_internal_usb_get_busguid_info.md) | The IOCTL_INTERNAL_USB_GET_BUSGUID_INFO IOCTL has been deprecated. Do not use. |
| [IOCTL_INTERNAL_USB_GET_BUS_INFO IOCTL](ni-usbioctl-ioctl_internal_usb_get_bus_info.md) | The IOCTL_INTERNAL_USB_GET_BUS_INFO I/O request queries the bus driver for certain bus information. |
| [IOCTL_INTERNAL_USB_GET_CONTROLLER_NAME IOCTL](ni-usbioctl-ioctl_internal_usb_get_controller_name.md) | The IOCTL_INTERNAL_USB_GET_CONTROLLER_NAME I/O request queries the bus driver for the device name of the USB host controller. |
| [IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO IOCTL](ni-usbioctl-ioctl_internal_usb_get_device_config_info.md) | The IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO I/O request returns information about a USB device and the hub it is attached to. |
| [IOCTL_INTERNAL_USB_GET_DEVICE_HANDLE IOCTL](ni-usbioctl-ioctl_internal_usb_get_device_handle.md) | The IOCTL_INTERNAL_USB_GET_DEVICE_HANDLE IOCTL is used by the USB hub driver. Do not use. |
| [IOCTL_INTERNAL_USB_GET_DEVICE_HANDLE_EX IOCTL](ni-usbioctl-ioctl_internal_usb_get_device_handle_ex.md) | The IOCTL_INTERNAL_USB_GET_DEVICE_HANDLE_EX IOCTL is used by the USB hub driver. Do not use. |
| [IOCTL_INTERNAL_USB_GET_HUB_COUNT IOCTL](ni-usbioctl-ioctl_internal_usb_get_hub_count.md) | The IOCTL_INTERNAL_USB_GET_HUB_COUNT IOCTL is used by the USB hub driver. Do not use. |
| [IOCTL_INTERNAL_USB_GET_HUB_NAME IOCTL](ni-usbioctl-ioctl_internal_usb_get_hub_name.md) | The IOCTL_INTERNAL_USB_GET_HUB_NAME I/O request is used by drivers to retrieve the UNICODE symbolic name for the target PDO if the PDO is for a hub. |
| [IOCTL_INTERNAL_USB_GET_PARENT_HUB_INFO IOCTL](ni-usbioctl-ioctl_internal_usb_get_parent_hub_info.md) | The IOCTL_INTERNAL_USB_GET_PARENT_HUB_INFO is used by the USB hub driver. Do not use. |
| [IOCTL_INTERNAL_USB_GET_PORT_STATUS IOCTL](ni-usbioctl-ioctl_internal_usb_get_port_status.md) | The IOCTL_INTERNAL_USB_GET_PORT_STATUS I/O request queries the status of the PDO. IOCTL_INTERNAL_USB_GET_PORT_STATUS is a kernel-mode I/O control request. This request targets the USB hub PDO. This IOCTL must be sent at IRQL = PASSIVE_LEVEL. |
| [IOCTL_INTERNAL_USB_GET_ROOTHUB_PDO IOCTL](ni-usbioctl-ioctl_internal_usb_get_roothub_pdo.md) | The IOCTL_INTERNAL_USB_GET_ROOTHUB_PDO IOCTL is used by the USB hub driver. Do not use. |
| [IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS IOCTL](ni-usbioctl-ioctl_internal_usb_get_topology_address.md) | The IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS I/O request returns information about the host controller the USB device is attached to, and the device's location in the USB device tree. |
| [IOCTL_INTERNAL_USB_GET_TT_DEVICE_HANDLE IOCTL](ni-usbioctl-ioctl_internal_usb_get_tt_device_handle.md) | The IOCTL_INTERNAL_USB_GET_TT_DEVICE_HANDLE is used by the USB hub driver. Do not use. |
| [IOCTL_INTERNAL_USB_NOTIFY_IDLE_READY IOCTL](ni-usbioctl-ioctl_internal_usb_notify_idle_ready.md) | The IOCTL_INTERNAL_USB_NOTIFY_IDLE_READY IOCTL is used by the USB hub driver. Do not use. |
| [IOCTL_INTERNAL_USB_RECORD_FAILURE IOCTL](ni-usbioctl-ioctl_internal_usb_record_failure.md) | The IOCTL_INTERNAL_USB_RECORD_FAILURE IOCTL is used by the USB hub driver. Do not use. |
| [IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DEVICE IOCTL](ni-usbioctl-ioctl_internal_usb_register_composite_device.md) | The IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DEVICE I/O request registers the driver of a USB multi-function device (composite driver) with the underlying USB driver stack. |
| [IOCTL_INTERNAL_USB_REQUEST_REMOTE_WAKE_NOTIFICATION IOCTL](ni-usbioctl-ioctl_internal_usb_request_remote_wake_notification.md) | The IOCTL_INTERNAL_USB_REQUEST_REMOTE_WAKE_NOTIFICATION I/O request is sent by the driver of a Universal Serial Bus (USB) multi-function device (composite driver) to request remote wake-up notifications from a specific function in the device. |
| [IOCTL_INTERNAL_USB_REQ_GLOBAL_RESUME IOCTL](ni-usbioctl-ioctl_internal_usb_req_global_resume.md) | The IOCTL_INTERNAL_USB_REQ_GLOBAL_RESUME IOCTL is used by the USB hub driver. Do not use. |
| [IOCTL_INTERNAL_USB_REQ_GLOBAL_SUSPEND IOCTL](ni-usbioctl-ioctl_internal_usb_req_global_suspend.md) | The IOCTL_INTERNAL_USB_REQ_GLOBAL_SUSPEND IOCTL is used by the USB hub driver. Do not use. |
| [IOCTL_INTERNAL_USB_RESET_PORT IOCTL](ni-usbioctl-ioctl_internal_usb_reset_port.md) | The IOCTL_INTERNAL_USB_RESET_PORT I/O control request is used by a driver to reset the upstream port of the device it manages. |
| [IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION IOCTL](ni-usbioctl-ioctl_internal_usb_submit_idle_notification.md) | The IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION I/O request is used by drivers to inform the USB bus driver that a device is idle and can be suspended. |
| [IOCTL_INTERNAL_USB_SUBMIT_URB IOCTL](ni-usbioctl-ioctl_internal_usb_submit_urb.md) | The IOCTL_INTERNAL_USB_SUBMIT_URB I/O control request is used by drivers to submit an URB to the bus driver. IOCTL_INTERNAL_USB_SUBMIT_URB is a kernel-mode I/O control request. This request targets the USB hub PDO. |
| [IOCTL_INTERNAL_USB_UNREGISTER_COMPOSITE_DEVICE IOCTL](ni-usbioctl-ioctl_internal_usb_unregister_composite_device.md) | The IOCTL_INTERNAL_USB_UNREGISTER_COMPOSITE_DEVICE I/O request unregisters the driver of a USB multi-function device (composite driver) and releases all resources that are associated with registration. |
| [IOCTL_USB_DIAGNOSTIC_MODE_OFF IOCTL](ni-usbioctl-ioctl_usb_diagnostic_mode_off.md) | The IOCTL_USB_DIAGNOSTIC_MODE_OFF I/O control has been deprecated. Do not use. |
| [IOCTL_USB_DIAGNOSTIC_MODE_ON IOCTL](ni-usbioctl-ioctl_usb_diagnostic_mode_on.md) | The IOCTL_USB_DIAGNOSTIC_MODE_ON I/O control has been deprecated. Do not use. |
| [IOCTL_USB_DIAG_IGNORE_HUBS_OFF IOCTL](ni-usbioctl-ioctl_usb_diag_ignore_hubs_off.md) | The IOCTL_USB_DIAG_IGNORE_HUBS_OFF I/O control has been deprecated. Do not use. |
| [IOCTL_USB_DIAG_IGNORE_HUBS_ON IOCTL](ni-usbioctl-ioctl_usb_diag_ignore_hubs_on.md) | The IOCTL_USB_DIAG_IGNORE_HUBS_ON I/O control has been deprecated. Do not use. |
| [IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION IOCTL](ni-usbioctl-ioctl_usb_get_descriptor_from_node_connection.md) | The IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION I/O control request retrieves one or more descriptors for the device that is associated with the indicated port index.IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION is a user-mode I/O control request. |
| [IOCTL_USB_GET_DEVICE_CHARACTERISTICS IOCTL](ni-usbioctl-ioctl_usb_get_device_characteristics.md) | The client driver sends this request to determine general characteristics about a USB device, such as maximum send and receive delays for any request. |
| [IOCTL_USB_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC IOCTL](ni-usbioctl-ioctl_usb_get_frame_number_and_qpc_for_time_sync.md) | . |
| [IOCTL_USB_GET_HUB_CAPABILITIES IOCTL](ni-usbioctl-ioctl_usb_get_hub_capabilities.md) | The IOCTL_USB_GET_HUB_CAPABILITIES I/O control request retrieves the capabilities of a USB hub. |
| [IOCTL_USB_GET_HUB_CAPABILITIES_EX IOCTL](ni-usbioctl-ioctl_usb_get_hub_capabilities_ex.md) | The IOCTL_USB_GET_HUB_CAPABILITIES_EX I/O control request retrieves the capabilities of a USB hub.IOCTL_USB_GET_HUB_CAPABILITIES_EX is a user-mode I/O control request. This request targets the USB hub device (GUID_DEVINTERFACE_USB_HUB). |
| [IOCTL_USB_GET_HUB_INFORMATION_EX IOCTL](ni-usbioctl-ioctl_usb_get_hub_information_ex.md) | The IOCTL_USB_GET_HUB_INFORMATION_EX I/O control request is sent by an application to retrieve information about a USB hub in a USB_HUB_INFORMATION_EX structure.The request retrieves the highest port number on the hub. |
| [IOCTL_USB_GET_NODE_CONNECTION_ATTRIBUTES IOCTL](ni-usbioctl-ioctl_usb_get_node_connection_attributes.md) | The IOCTL_USB_GET_NODE_CONNECTION_ATTRIBUTES I/O control request retrieves the Microsoft-extended port attributes for a specific port. |
| [IOCTL_USB_GET_NODE_CONNECTION_DRIVERKEY_NAME IOCTL](ni-usbioctl-ioctl_usb_get_node_connection_driverkey_name.md) | The IOCTL_USB_GET_NODE_CONNECTION_DRIVERKEY_NAME I/O control request retrieves the driver registry key name that is associated with the device that is connected to the indicated port. |
| [IOCTL_USB_GET_NODE_CONNECTION_INFORMATION IOCTL](ni-usbioctl-ioctl_usb_get_node_connection_information.md) | The IOCTL_USB_GET_NODE_CONNECTION_INFORMATION request retrieves information about the indicated USB port and the device that is attached to the port, if there is one.Client drivers must send this IOCTL at an IRQL of PASSIVE_LEVEL.IOCTL_USB_GET_NODE_CONNECTION_INFORMATION is a user-mode I/O control request. This request targets the USB hub device (GUID_DEVINTERFACE_USB_HUB). Do not send this request to the root hub. |
| [IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX IOCTL](ni-usbioctl-ioctl_usb_get_node_connection_information_ex.md) | The IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX request retrieves information about a USB port and the device that is attached to the port, if there is one.Client drivers must send this IOCTL at an IRQL of PASSIVE_LEVEL.IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX is a user-mode I/O control request. This request targets the USB hub device (GUID_DEVINTERFACE_USB_HUB). Do not send this request to the root hub. |
| [IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX_V2 IOCTL](ni-usbioctl-ioctl_usb_get_node_connection_information_ex_v2.md) | The IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX_V2 I/O control is sent by an application to retrieve information about the protocols that are supported by a particular USB port on a hub. The request also retrieves the speed capability of the port. |
| [IOCTL_USB_GET_NODE_CONNECTION_NAME IOCTL](ni-usbioctl-ioctl_usb_get_node_connection_name.md) | The IOCTL_USB_GET_NODE_CONNECTION_NAME I/O control request is used with the USB_NODE_CONNECTION_NAME structure to retrieve the symbolic link name of the hub that is attached to the downstream port.IOCTL_USB_GET_NODE_CONNECTION_NAME is a user-mode I/O control request. This request targets the USB hub device (GUID_DEVINTERFACE_USB_HUB). |
| [IOCTL_USB_GET_NODE_INFORMATION IOCTL](ni-usbioctl-ioctl_usb_get_node_information.md) | The IOCTL_USB_GET_NODE_INFORMATION I/O control request is used with the USB_NODE_INFORMATION structure to retrieve information about a parent device.IOCTL_USB_GET_NODE_INFORMATION is a user-mode I/O control request. |
| [IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES IOCTL](ni-usbioctl-ioctl_usb_get_port_connector_properties.md) | The IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES I/O control request is sent by an application to retrieve information about a specific port on a USB hub. |
| [IOCTL_USB_GET_ROOT_HUB_NAME IOCTL](ni-usbioctl-ioctl_usb_get_root_hub_name.md) | The IOCTL_USB_GET_ROOT_HUB_NAME I/O control request is used with the USB_ROOT_HUB_NAME structure to retrieve the symbolic link name of the root hub.IOCTL_USB_GET_ROOT_HUB_NAME is a user-mode I/O control request. |
| [IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS IOCTL](ni-usbioctl-ioctl_usb_get_transport_characteristics.md) | The client driver sends this request to retrieve the transport characteristics. |
| [IOCTL_USB_HCD_DISABLE_PORT IOCTL](ni-usbioctl-ioctl_usb_hcd_disable_port.md) | The IOCTL_USB_HCD_DISABLE_PORT IOCTL has been deprecated. Do not use. |
| [IOCTL_USB_HCD_ENABLE_PORT IOCTL](ni-usbioctl-ioctl_usb_hcd_enable_port.md) | The IOCTL_USB_HCD_ENABLE_PORT IOCTL has been deprecated. Do not use. |
| [IOCTL_USB_HCD_GET_STATS_1 IOCTL](ni-usbioctl-ioctl_usb_hcd_get_stats_1.md) | The IOCTL_USB_HCD_GET_STATS_1 IOCTL has been deprecated. Do not use. |
| [IOCTL_USB_HCD_GET_STATS_2 IOCTL](ni-usbioctl-ioctl_usb_hcd_get_stats_2.md) | The IOCTL_USB_HCD_GET_STATS_2 IOCTL has been deprecated. Do not use. |
| [IOCTL_USB_HUB_CYCLE_PORT IOCTL](ni-usbioctl-ioctl_usb_hub_cycle_port.md) | The IOCTL_USB_HUB_CYCLE_PORT I/O control request power-cycles the port that is associated with the PDO that receives the request. |
| [IOCTL_USB_NOTIFY_ON_TRANSPORT_CHARACTERISTICS_CHANGE IOCTL](ni-usbioctl-ioctl_usb_notify_on_transport_characteristics_change.md) | This request notifies the caller of change in transport characteristics. |
| [IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE IOCTL](ni-usbioctl-ioctl_usb_register_for_transport_characteristics_change.md) | This request registers for notifications about the changes in transport characteristics. |
| [IOCTL_USB_RESET_HUB IOCTL](ni-usbioctl-ioctl_usb_reset_hub.md) | The IOCTL_USB_RESET_HUB IOCTL is used by the USB driver stack. Do not use. |
| [IOCTL_USB_START_TRACKING_FOR_TIME_SYNC IOCTL](ni-usbioctl-ioctl_usb_start_tracking_for_time_sync.md) | This request registers the caller with USB driver stack for time sync services. |
| [IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC IOCTL](ni-usbioctl-ioctl_usb_stop_tracking_for_time_sync.md) | This request unegisters the caller with USB driver stack for time sync services. |
| [IOCTL_USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE IOCTL](ni-usbioctl-ioctl_usb_unregister_for_transport_characteristics_change.md) | This request unregisters the caller from getting notifications about transport characteristics changes. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_USB_CONNECTION_STATUS enumeration](ne-usbioctl-_usb_connection_status.md) | The USB_CONNECTION_STATUS enumerator indicates the status of the connection to a device on a USB hub port. |
| [_USB_HUB_NODE enumeration](ne-usbioctl-_usb_hub_node.md) | The USB_HUB_NODE enumerator indicates whether a device is a hub or a composite device. |
| [_USB_HUB_TYPE enumeration](ne-usbioctl-_usb_hub_type.md) | The USB_HUB_TYPE enumeration defines constants that indicate the type of USB hub. The hub type is retrieved by the IOCTL_USB_GET_HUB_INFORMATION_EX I/O control request. |
