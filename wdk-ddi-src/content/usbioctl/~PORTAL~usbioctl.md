# Declarations in the usbioctl header
This header Usbioctl contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [USB_TRANSPORT_CHARACTERISTICS structure](ns-usbioctl--usb-transport-characteristics.md) | Stores the transport characteristics at relevant points in time. This structure is used in the IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS request. |
| [USB_BUS_NOTIFICATION structure](ns-usbioctl--usb-bus-notification.md) | TBD |
| [USB_START_FAILDATA structure](ns-usbioctl--usb-start-faildata.md) | TBD |
| [USB_PORT_CONNECTOR_PROPERTIES structure](ns-usbioctl--usb-port-connector-properties.md) | The USB_PORT_CONNECTOR_PROPERTIES structure is used with the IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES I/O control request to retrieve information about a port on a particular SuperSpeed hub. |
| [USB_NODE_CONNECTION_INFORMATION_EX structure](ns-usbioctl--usb-node-connection-information-ex.md) | The USB_NODE_CONNECTION_INFORMATION_EX structure is used in conjunction with the IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX request to obtain information about the connection associated with the indicated USB port. |
| [USB_TRANSPORT_CHARACTERISTICS_CHANGE_REGISTRATION structure](ns-usbioctl--usb-transport-characteristics-change-registration.md) | Contains registration information for the IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE request. |
| [USB_NOTIFICATION structure](ns-usbioctl--usb-notification.md) | TBD |
| [USB_COMPOSITE_FUNCTION_INFO structure](ns-usbioctl--usb-composite-function-info.md) | TBD |
| [USB_START_TRACKING_FOR_TIME_SYNC_INFORMATION structure](ns-usbioctl--usb-start-tracking-for-time-sync-information.md) | The input and output buffer for the IOCTL_USB_START_TRACKING_FOR_TIME_SYNC request. |
| [USB_NODE_CONNECTION_INFORMATION structure](ns-usbioctl--usb-node-connection-information.md) | The USB_NODE_CONNECTION_INFORMATION structure is used with the IOCTL_USB_GET_NODE_CONNECTION_INFORMATION request to retrieve information about a USB port and connected device. |
| [HCD_STAT_COUNTERS structure](ns-usbioctl--hcd-stat-counters.md) | TBD |
| [USB_HUB_INFORMATION_EX structure](ns-usbioctl--usb-hub-information-ex.md) | The USB_HUB_INFORMATION_EX structure is used with the IOCTL_USB_GET_HUB_INFORMATION_EX I/O control request to retrieve information about a Universal Serial Bus (USB) hub. |
| [USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS structure](ns-usbioctl--usb-node-connection-information-ex-v2-flags.md) | The USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS union is used to indicate the speed at which a USB 3.0 device is currently operating and whether it can operate at higher speed, when attached to a particular port. |
| [USB_HUB_NAME structure](ns-usbioctl--usb-hub-name.md) | The USB_HUB_NAME structure stores the hub's symbolic device name. |
| [USB_HUB_CAP_FLAGS structure](ns-usbioctl--usb-hub-cap-flags.md) | The USB_HUB_CAP_FLAGS structure is used to report the capabilities of a hub. |
| [USB_PORT_PROPERTIES structure](ns-usbioctl--usb-port-properties.md) | The USB_PORT_PROPERTIES union is used to report the capabilities of a Universal Serial Bus (USB) port.The port capabilities are retrieved in the USB_PORT_CONNECTOR_PROPERTIES structure by the IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES I/O control request. |
| [USB_NODE_INFORMATION structure](ns-usbioctl--usb-node-information.md) | The USB_NODE_INFORMATION structure is used with the IOCTL_USB_GET_NODE_INFORMATION I/O control request to retrieve information about a parent device. |
| [USB_DEVICE_PERFORMANCE_INFO structure](ns-usbioctl--usb-device-performance-info.md) | TBD |
| [USB_STOP_TRACKING_FOR_TIME_SYNC_INFORMATION structure](ns-usbioctl--usb-stop-tracking-for-time-sync-information.md) | TBD |
| [HCD_ISO_STAT_COUNTERS structure](ns-usbioctl--hcd-iso-stat-counters.md) | TBD |
| [USB_TRANSPORT_CHARACTERISTICS_CHANGE_NOTIFICATION structure](ns-usbioctl--usb-transport-characteristics-change-notification.md) | Contains registration information filled when the IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE request completes. |
| [USB_NODE_CONNECTION_INFORMATION_EX_V2 structure](ns-usbioctl--usb-node-connection-information-ex-v2.md) | The USB_NODE_CONNECTION_INFORMATION_EX_V2 structure is used with the IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX_V2 I/O control request to retrieve speed information about a Universal Serial Bus (USB) device that is attached to a particular port. |
| [USB_TRANSPORT_CHARACTERISTICS_CHANGE_UNREGISTRATION structure](ns-usbioctl--usb-transport-characteristics-change-unregistration.md) | Contains unregistration information for the IOCTL_USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE request. |
| [USB_NODE_CONNECTION_NAME structure](ns-usbioctl--usb-node-connection-name.md) | The USB_NODE_CONNECTION_NAME structure is used with the IOCTL_USB_GET_NODE_CONNECTION_NAME I/O control request to retrieve the symbolic link of the downstream hub that is attached to the port. |
| [USB_PROTOCOLS structure](ns-usbioctl--usb-protocols.md) | The USB_PROTOCOLS union is used to report the Universal Serial Bus (USB) signaling protocols that are supported by the port. |
| [HCD_STAT_INFORMATION_1 structure](ns-usbioctl--hcd-stat-information-1.md) | TBD |
| [USB_NODE_CONNECTION_DRIVERKEY_NAME structure](ns-usbioctl--usb-node-connection-driverkey-name.md) | The USB_NODE_CONNECTION_DRIVERKEY_NAME structure is used with the IOCTL_USB_GET_NODE_CONNECTION_DRIVERKEY_NAME I/O control request to retrieve the driver key name for the device that is connected to the indicated port. |
| [USB_ACQUIRE_INFO structure](ns-usbioctl--usb-acquire-info.md) | TBD |
| [USB_DESCRIPTOR_REQUEST structure](ns-usbioctl--usb-descriptor-request.md) | The USB_DESCRIPTOR_REQUEST structure is used with the IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION I/O control request to retrieve one or more descriptors for the device that is associated with the indicated connection index. |
| [USB_TOPOLOGY_ADDRESS structure](ns-usbioctl--usb-topology-address.md) | The USB_TOPOLOGY_ADDRESS structure is used with the IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS I/O request to retrieve information about a USB device?s location in the USB device tree. |
| [USB_HUB_INFORMATION structure](ns-usbioctl--usb-hub-information.md) | The USB_HUB_INFORMATION structure contains information about a hub. |
| [HUB_DEVICE_CONFIG_INFO_V1 structure](ns-usbioctl--hub-device-config-info-v1.md) | The HUB_DEVICE_CONFIG_INFO structure is used in conjunction with the kernel-mode IOCTL, IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO to request to report information about a USB device and the hub to which the device is attached. |
| [USB_NODE_CONNECTION_ATTRIBUTES structure](ns-usbioctl--usb-node-connection-attributes.md) | The USB_NODE_CONNECTION_ATTRIBUTES structure is used with the IOCTL_USB_GET_NODE_CONNECTION_ATTRIBUTES I/O control request to retrieve the attributes of a connection. |
| [USB_HUB_DEVICE_UXD_SETTINGS structure](ns-usbioctl--usb-hub-device-uxd-settings.md) | TBD |
| [USB_DEVICE_NODE_INFO structure](ns-usbioctl--usb-device-node-info.md) | TBD |
| [USB_HUB_CAPABILITIES_EX structure](ns-usbioctl--usb-hub-capabilities-ex.md) | The USB_HUB_CAPABILITIES_EX structure is used with the IOCTL_USB_GET_HUB_CAPABILITIES I/O control request to retrieve the capabilities of a particular USB hub. |
| [USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION structure](ns-usbioctl--usb-frame-number-and-qpc-for-time-sync-information.md) | Stores the frame and microframe numbers and the calculated system QPC values. This structure is used in the IOCTL_USB_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC request. |
| [USB_HUB_DEVICE_INFO structure](ns-usbioctl--usb-hub-device-info.md) | TBD |
| [USB_PIPE_INFO structure](ns-usbioctl--usb-pipe-info.md) | The USB_PIPE_INFO structure is used in conjunction with the USB_NODE_CONNECTION_INFORMATION_EX structure and the IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX request to obtain information about a connection and its associated pipes. |
| [USB_CONTROLLER_DEVICE_INFO structure](ns-usbioctl--usb-controller-device-info.md) | TBD |
| [USB_HCD_DRIVERKEY_NAME structure](ns-usbioctl--usb-hcd-driverkey-name.md) | The USB_HCD_DRIVERKEY_NAME structure is used with the IOCTL_GET_HCD_DRIVERKEY_NAME I/O control request to retrieve the driver key in the registry for the USB host controller driver. |
| [USB_MI_PARENT_INFORMATION structure](ns-usbioctl--usb-mi-parent-information.md) | The USB_MI_PARENT_INFORMATION structure contains information about a composite device. |
| [USB_ROOT_HUB_NAME structure](ns-usbioctl--usb-root-hub-name.md) | The USB_ROOT_HUB_NAME structure stores the root hub's symbolic device name. |
| [HCD_STAT_INFORMATION_2 structure](ns-usbioctl--hcd-stat-information-2.md) | TBD |
| [USB_ID_STRING structure](ns-usbioctl--usb-id-string.md) | The USB_ID_STRING structure is used to store a string or multi-string. |
| [USB_HUB_PORT_INFORMATION structure](ns-usbioctl--usb-hub-port-information.md) | TBD |
| [USB_CONNECTION_NOTIFICATION structure](ns-usbioctl--usb-connection-notification.md) | TBD |
| [USB_DEVICE_STATE structure](ns-usbioctl--usb-device-state.md) | TBD |
| [USB_DEVICE_CHARACTERISTICS structure](ns-usbioctl--usb-device-characteristics.md) | Contains information about the USB device’s characteristics, such as the maximum send and receive delays for any request. This structure is used in the IOCTL_USB_GET_DEVICE_CHARACTERISTICS request. |
| [USB_HUB_CAPABILITIES structure](ns-usbioctl--usb-hub-capabilities.md) | The USB_HUB_CAPABILITIES structure has been deprecated. Use USB_HUB_CAPABILITIES_EX instead. |
| [USB_COMPOSITE_DEVICE_INFO structure](ns-usbioctl--usb-composite-device-info.md) | TBD |
| [USB_CYCLE_PORT_PARAMS structure](ns-usbioctl--usb-cycle-port-params.md) | TBD |
| [USB_DEVICE_INFO structure](ns-usbioctl--usb-device-info.md) | TBD |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS IOCTL](ni-usbioctl-ioctl-usb-get-transport-characteristics.md) | The client driver sends this request to retrieve the transport characteristics. |
| [IOCTL_USB_HCD_GET_STATS_1 IOCTL](ni-usbioctl-ioctl-usb-hcd-get-stats-1.md) | TBD |
| [IOCTL_USB_HCD_GET_STATS_2 IOCTL](ni-usbioctl-ioctl-usb-hcd-get-stats-2.md) | TBD |
| [IOCTL_INTERNAL_USB_GET_DEVICE_HANDLE_EX IOCTL](ni-usbioctl-ioctl-internal-usb-get-device-handle-ex.md) | TBD |
| [IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO IOCTL](ni-usbioctl-ioctl-internal-usb-get-device-config-info.md) | TBD |
| [IOCTL_USB_GET_NODE_INFORMATION IOCTL](ni-usbioctl-ioctl-usb-get-node-information.md) | TBD |
| [IOCTL_INTERNAL_USB_RECORD_FAILURE IOCTL](ni-usbioctl-ioctl-internal-usb-record-failure.md) | TBD |
| [IOCTL_INTERNAL_USB_GET_DEVICE_HANDLE IOCTL](ni-usbioctl-ioctl-internal-usb-get-device-handle.md) | TBD |
| [IOCTL_USB_HCD_ENABLE_PORT IOCTL](ni-usbioctl-ioctl-usb-hcd-enable-port.md) | TBD |
| [IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES IOCTL](ni-usbioctl-ioctl-usb-get-port-connector-properties.md) | TBD |
| [IOCTL_INTERNAL_USB_CYCLE_PORT IOCTL](ni-usbioctl-ioctl-internal-usb-cycle-port.md) | TBD |
| [IOCTL_USB_RESET_HUB IOCTL](ni-usbioctl-ioctl-usb-reset-hub.md) | TBD |
| [IOCTL_INTERNAL_USB_GET_PORT_STATUS IOCTL](ni-usbioctl-ioctl-internal-usb-get-port-status.md) | TBD |
| [IOCTL_INTERNAL_USB_ENABLE_PORT IOCTL](ni-usbioctl-ioctl-internal-usb-enable-port.md) | TBD |
| [IOCTL_USB_DIAG_IGNORE_HUBS_OFF IOCTL](ni-usbioctl-ioctl-usb-diag-ignore-hubs-off.md) | TBD |
| [IOCTL_INTERNAL_USB_GET_TT_DEVICE_HANDLE IOCTL](ni-usbioctl-ioctl-internal-usb-get-tt-device-handle.md) | TBD |
| [IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION IOCTL](ni-usbioctl-ioctl-usb-get-descriptor-from-node-connection.md) | TBD |
| [IOCTL_INTERNAL_USB_REQ_GLOBAL_SUSPEND IOCTL](ni-usbioctl-ioctl-internal-usb-req-global-suspend.md) | TBD |
| [IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX_V2 IOCTL](ni-usbioctl-ioctl-usb-get-node-connection-information-ex-v2.md) | TBD |
| [IOCTL_INTERNAL_USB_GET_CONTROLLER_NAME IOCTL](ni-usbioctl-ioctl-internal-usb-get-controller-name.md) | TBD |
| [IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE IOCTL](ni-usbioctl-ioctl-usb-register-for-transport-characteristics-change.md) | This request registers for notifications about the changes in transport characteristics. |
| [IOCTL_INTERNAL_USB_RESET_PORT IOCTL](ni-usbioctl-ioctl-internal-usb-reset-port.md) | TBD |
| [IOCTL_USB_DIAGNOSTIC_MODE_ON IOCTL](ni-usbioctl-ioctl-usb-diagnostic-mode-on.md) | TBD |
| [IOCTL_USB_HUB_CYCLE_PORT IOCTL](ni-usbioctl-ioctl-usb-hub-cycle-port.md) | TBD |
| [IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX IOCTL](ni-usbioctl-ioctl-usb-get-node-connection-information-ex.md) | TBD |
| [IOCTL_INTERNAL_USB_GET_BUSGUID_INFO IOCTL](ni-usbioctl-ioctl-internal-usb-get-busguid-info.md) | TBD |
| [IOCTL_USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE IOCTL](ni-usbioctl-ioctl-usb-unregister-for-transport-characteristics-change.md) | This request unregisters the caller from getting notifications about transport characteristics changes. |
| [IOCTL_INTERNAL_USB_NOTIFY_IDLE_READY IOCTL](ni-usbioctl-ioctl-internal-usb-notify-idle-ready.md) | TBD |
| [IOCTL_USB_GET_DEVICE_CHARACTERISTICS IOCTL](ni-usbioctl-ioctl-usb-get-device-characteristics.md) | TBD |
| [IOCTL_USB_GET_ROOT_HUB_NAME IOCTL](ni-usbioctl-ioctl-usb-get-root-hub-name.md) | TBD |
| [IOCTL_INTERNAL_USB_FAIL_GET_STATUS_FROM_DEVICE IOCTL](ni-usbioctl-ioctl-internal-usb-fail-get-status-from-device.md) | TBD |
| [IOCTL_USB_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC IOCTL](ni-usbioctl-ioctl-usb-get-frame-number-and-qpc-for-time-sync.md) | TBD |
| [IOCTL_USB_DIAGNOSTIC_MODE_OFF IOCTL](ni-usbioctl-ioctl-usb-diagnostic-mode-off.md) | TBD |
| [IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS IOCTL](ni-usbioctl-ioctl-internal-usb-get-topology-address.md) | TBD |
| [IOCTL_USB_START_TRACKING_FOR_TIME_SYNC IOCTL](ni-usbioctl-ioctl-usb-start-tracking-for-time-sync.md) | This request registers the caller with USB driver stack for time sync services. |
| [IOCTL_USB_GET_HUB_CAPABILITIES_EX IOCTL](ni-usbioctl-ioctl-usb-get-hub-capabilities-ex.md) | TBD |
| [IOCTL_INTERNAL_USB_SUBMIT_IDLE_NOTIFICATION IOCTL](ni-usbioctl-ioctl-internal-usb-submit-idle-notification.md) | TBD |
| [IOCTL_USB_GET_NODE_CONNECTION_DRIVERKEY_NAME IOCTL](ni-usbioctl-ioctl-usb-get-node-connection-driverkey-name.md) | TBD |
| [IOCTL_USB_GET_NODE_CONNECTION_ATTRIBUTES IOCTL](ni-usbioctl-ioctl-usb-get-node-connection-attributes.md) | TBD |
| [IOCTL_INTERNAL_USB_REQUEST_REMOTE_WAKE_NOTIFICATION IOCTL](ni-usbioctl-ioctl-internal-usb-request-remote-wake-notification.md) | TBD |
| [IOCTL_USB_DIAG_IGNORE_HUBS_ON IOCTL](ni-usbioctl-ioctl-usb-diag-ignore-hubs-on.md) | TBD |
| [IOCTL_INTERNAL_USB_GET_ROOTHUB_PDO IOCTL](ni-usbioctl-ioctl-internal-usb-get-roothub-pdo.md) | TBD |
| [IOCTL_INTERNAL_USB_GET_HUB_COUNT IOCTL](ni-usbioctl-ioctl-internal-usb-get-hub-count.md) | TBD |
| [IOCTL_INTERNAL_USB_REQ_GLOBAL_RESUME IOCTL](ni-usbioctl-ioctl-internal-usb-req-global-resume.md) | TBD |
| [IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DEVICE IOCTL](ni-usbioctl-ioctl-internal-usb-register-composite-device.md) | TBD |
| [IOCTL_INTERNAL_USB_GET_BUS_INFO IOCTL](ni-usbioctl-ioctl-internal-usb-get-bus-info.md) | TBD |
| [IOCTL_USB_STOP_TRACKING_FOR_TIME_SYNC IOCTL](ni-usbioctl-ioctl-usb-stop-tracking-for-time-sync.md) | TBD |
| [IOCTL_GET_HCD_DRIVERKEY_NAME IOCTL](ni-usbioctl-ioctl-get-hcd-driverkey-name.md) | TBD |
| [IOCTL_USB_GET_NODE_CONNECTION_NAME IOCTL](ni-usbioctl-ioctl-usb-get-node-connection-name.md) | TBD |
| [IOCTL_USB_HCD_DISABLE_PORT IOCTL](ni-usbioctl-ioctl-usb-hcd-disable-port.md) | TBD |
| [IOCTL_USB_GET_HUB_INFORMATION_EX IOCTL](ni-usbioctl-ioctl-usb-get-hub-information-ex.md) | TBD |
| [IOCTL_USB_NOTIFY_ON_TRANSPORT_CHARACTERISTICS_CHANGE IOCTL](ni-usbioctl-ioctl-usb-notify-on-transport-characteristics-change.md) | This request notifies the caller of change in transport characteristics. |
| [IOCTL_USB_GET_NODE_CONNECTION_INFORMATION IOCTL](ni-usbioctl-ioctl-usb-get-node-connection-information.md) | TBD |
| [IOCTL_USB_GET_HUB_CAPABILITIES IOCTL](ni-usbioctl-ioctl-usb-get-hub-capabilities.md) | TBD |
| [IOCTL_INTERNAL_USB_SUBMIT_URB IOCTL](ni-usbioctl-ioctl-internal-usb-submit-urb.md) | TBD |
| [IOCTL_INTERNAL_USB_GET_HUB_NAME IOCTL](ni-usbioctl-ioctl-internal-usb-get-hub-name.md) | TBD |
| [IOCTL_INTERNAL_USB_GET_PARENT_HUB_INFO IOCTL](ni-usbioctl-ioctl-internal-usb-get-parent-hub-info.md) | TBD |
| [IOCTL_INTERNAL_USB_UNREGISTER_COMPOSITE_DEVICE IOCTL](ni-usbioctl-ioctl-internal-usb-unregister-composite-device.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [USB_NOTIFICATION_TYPE enumeration](ne-usbioctl--usb-notification-type.md) | TBD |
| [USB_HUB_NODE enumeration](ne-usbioctl--usb-hub-node.md) | The USB_HUB_NODE enumerator indicates whether a device is a hub or a composite device. |
| [USB_WMI_DEVICE_NODE_TYPE enumeration](ne-usbioctl--usb-wmi-device-node-type.md) | TBD |
| [USB_CONNECTION_STATUS enumeration](ne-usbioctl--usb-connection-status.md) | The USB_CONNECTION_STATUS enumerator indicates the status of the connection to a device on a USB hub port. |
| [USB_CONNECTION_STATUS enumeration](ne-usbioctl--usb-connection-status~r2.md) | The USB_CONNECTION_STATUS enumerator indicates the status of the connection to a device on a USB hub port. |
| [USB_CONNECTION_STATUS enumeration](ne-usbioctl--usb-connection-status~r1.md) | The USB_CONNECTION_STATUS enumerator indicates the status of the connection to a device on a USB hub port. |
| [USB_NOTIFICATION_TYPE enumeration](ne-usbioctl--usb-notification-type~r1.md) | TBD |
| [USB_HUB_TYPE enumeration](ne-usbioctl--usb-hub-type.md) | The USB_HUB_TYPE enumeration defines constants that indicate the type of USB hub. The hub type is retrieved by the IOCTL_USB_GET_HUB_INFORMATION_EX I/O control request. |

This header is used in these topics:

- [usbref](..content/_usbref)
