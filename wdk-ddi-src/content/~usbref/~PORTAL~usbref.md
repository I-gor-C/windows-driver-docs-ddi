# Declarations in the usbref technology
This technology  contains these programming interfaces:

Function

| Title        | Description    |
| ------------- |:-------------:|
| [UCM_CONNECTOR_TYPEC_CONFIG_INIT function](..\ucmmanager\nf-ucmmanager-ucm-connector-typec-config-init.md) | Initializes the UCM_CONNECTOR_TYPEC_CONFIG structure. |
| [UCM_CONNECTOR_CONFIG_INIT function](..\ucmmanager\nf-ucmmanager-ucm-connector-config-init.md) | Initializes a UCM_CONNECTOR_CONFIG structure. |
| [UCM_CONNECTOR_PD_CONFIG_INIT function](..\ucmmanager\nf-ucmmanager-ucm-connector-pd-config-init.md) | Initializes a UCM_CONNECTOR_PD_CONFIG structure. |
| [UCM_MANAGER_CONFIG_INIT function](..\ucmmanager\nf-ucmmanager-ucm-manager-config-init.md) | Initializes a UCM_MANAGER_CONFIG structure. |
| [UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS_INIT function](..\ucmmanager\nf-ucmmanager-ucm-connector-pd-conn-state-changed-params-init.md) | Initializes a UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS structure. |
| [UCM_CONNECTOR_TYPEC_ATTACH_PARAMS_INIT function](..\ucmmanager\nf-ucmmanager-ucm-connector-typec-attach-params-init.md) | Initializes a UCM_CONNECTOR_TYPEC_ATTACH_PARAMS structure. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UCM_CONNECTOR_PD_CONFIG structure](..\ucmmanager\ns-ucmmanager--ucm-connector-pd-config.md) | Describes the Power Delivery 2.0 capabilities of the connector. |
| [UCM_CONNECTOR_TYPEC_ATTACH_PARAMS structure](..\ucmmanager\ns-ucmmanager--ucm-connector-typec-attach-params.md) | Describes the partner that is currently attached to the connector. |
| [UCM_MANAGER_CONFIG structure](..\ucmmanager\ns-ucmmanager--ucm-manager-config.md) | Describes the configuration options for the UCM Manager. An initialized UCM_MANAGER_CONFIG structure is an input parameter value to UcmInitializeDevice. |
| [UCM_CONNECTOR_PD_CONN_STATE_CHANGED_PARAMS structure](..\ucmmanager\ns-ucmmanager--ucm-connector-pd-conn-state-changed-params.md) | Describes the parameters for PD connection changed event. |
| [UCM_CONNECTOR_CONFIG structure](..\ucmmanager\ns-ucmmanager--ucm-connector-config.md) | Describes the configuration options for a Type-C connector object. An initialized UCM_MANAGER_CONFIG structure is an input parameter value to UcmInitializeDevice. |
| [UCM_CONNECTOR_TYPEC_CONFIG structure](..\ucmmanager\ns-ucmmanager--ucm-connector-typec-config.md) | Describes the configuration options for a Type-C connector. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_UCM_CONNECTOR_SET_DATA_ROLE callback](..\ucmmanager\nc-ucmmanager-evt-ucm-connector-set-data-role.md) | The client driver's implementation of the EVT_UCM_CONNECTOR_SET_DATA_ROLE event callback function that swaps the data role of the connector to the specified role when attached to a partner connector. |
| [EVT_UCM_CONNECTOR_SET_POWER_ROLE callback](..\ucmmanager\nc-ucmmanager-evt-ucm-connector-set-power-role.md) | The client driver's implementation of the EVT_UCM_CONNECTOR_SET_POWER_ROLE event callback function that sets the power role of the connector to the specified role when attached to a partner connector. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL IOCTL](..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-get-control.md) | Gets the values of all control registers defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_CONFIGURED IOCTL](..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-displayport-configured.md) | Notifies the client driver that the DisplayPort alternate mode on the partner device has been configured with pin assignment so that the driver can perform additional tasks. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED IOCTL](..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-displayport-display-out-status-changed.md) | Notifies the client driver that the display out status of the DisplayPort connection has changed so that the driver can perform additional tasks. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS_CHANGED IOCTL](..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-displayport-hpd-status-changed.md) | Notifies the client driver that the hot-plug detect status of the DisplayPort connection has changed so that the driver can perform additional tasks. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_COMMAND IOCTL](..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-command.md) | Sets the value of a command register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONFIG_STANDARD_OUTPUT IOCTL](..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-config-standard-output.md) | Sets the CONFIG_STANDARD_OUTPUT Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_MESSAGE_HEADER_INFO IOCTL](..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-message-header-info.md) | Sets the value of the MESSAGE_HEADER_INFO Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONTROL IOCTL](..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-control.md) | Sets the value of a control register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_STATUS IOCTL](..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-get-status.md) | Gets values of all status registers as per the Universal Serial Bus Type-C Port Controller Interface Specification. The client driver must retrieve the values of the CC_STATUS, POWER_STATUS, and FAULT_STATUS registers. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT IOCTL](..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-transmit.md) | Sets the TRANSMIT Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_BUFFER IOCTL](..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-transmit-buffer.md) | Sets the TRANSMIT_BUFER Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_EXITED IOCTL](..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-alternate-mode-exited.md) | Notifies the client driver that an alternate mode is exited so that the driver can perform additional tasks. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_ENTERED IOCTL](..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-alternate-mode-entered.md) | Notifies the client driver that an alternate mode is entered so that the driver can perform additional tasks. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_RECEIVE_DETECT IOCTL](..\ucmtcpciportcontrollerrequests\ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-receive-detect.md) | Sets the RECEIVE_DETECT Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_PIN_ASSIGNMENT enumeration](..\ucmtcpciportcontrollerrequests\ne-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-displayport-pin-assignment.md) | TBD. |
| [UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS enumeration](..\ucmtcpciportcontrollerrequests\ne-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-displayport-display-out-status.md) | Defines values to determine whether a display out status for a DisplayPort device is enabled. |
| [UCMTCPCI_PORT_CONTROLLER_IOCTL enumeration](..\ucmtcpciportcontrollerrequests\ne-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-ioctl.md) | Defines the various device I/O control requests that are sent to the client driver for the port controller. This indicates the type of IOCTL in WPP. |
| [UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS enumeration](..\ucmtcpciportcontrollerrequests\ne-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-displayport-hpd-status.md) | Defines values to determine whether a DisplayPort device is plugged in. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-transmit-in-params.md) | Stores the values of TRANSMIT Register. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT request. |
| [UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-displayport-display-out-status-changed-in-params.md) | Stores information about display out status of the DisplayPort connection. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED request. |
| [UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS_CHANGED_IN_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-displayport-hpd-status-changed-in-params.md) | Stores information about hot plug detect status of the DisplayPort connection. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS_CHANGED request. |
| [UCMTCPCI_PORT_CONTROLLER_GET_CONTROL_OUT_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-get-control-out-params.md) | Stores the values of all control registers of the port controller retrieved by the IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL request. |
| [UCMTCPCI_PORT_CONTROLLER_SET_RECEIVE_DETECT_IN_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-receive-detect-in-params.md) | Stores the value of the RECEIVE_DETECT Register. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_RECEIVE_DETECT request. |
| [UCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-control-in-params.md) | Stores the values of all control registers. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONTROL request. |
| [UCMTCPCI_PORT_CONTROLLER_SET_MESSAGE_HEADER_INFO_IN_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-message-header-info-in-params.md) | Stores the value of the VBUS_VOLTAGE_ALARM_LO_CFG Register. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_MESSAGE_HEADER_INFO request. |
| [UCMTCPCI_PORT_CONTROLLER_GET_STATUS_IN_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-get-status-in-params.md) | This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_STATUS request. |
| [UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_EXITED_IN_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-alternate-mode-exited-in-params.md) | Stores information about the alternate mode that was exited. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_EXITED request. |
| [UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_CONFIGURED_IN_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-displayport-configured-in-params.md) | Stores information about the pin assignment of the DisplayPort alternate mode that was configured. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_CONFIGURED request. |
| [UCMTCPCI_PORT_CONTROLLER_SET_CONFIG_STANDARD_OUTPUT_IN_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-config-standard-output-in-params.md) | Stores the value of the CONFIG_STANDARD_OUTPUT Register. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONFIG_STANDARD_OUTPUT request. |
| [UCMTCPCI_PORT_CONTROLLER_GET_CONTROL_IN_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-get-control-in-params.md) | This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL request. |
| [UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_BUFFER_IN_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-transmit-buffer-in-params.md) | Stores the value of the TRANSMIT_BUFFER Register. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_BUFFER request. |
| [UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_ENTERED_IN_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-alternate-mode-entered-in-params.md) | Stores information about the alternate mode that was detected. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_ENTERED request. |
| [UCMTCPCI_PORT_CONTROLLER_SET_COMMAND_IN_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-command-in-params.md) | Stores the specified command registers. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_COMMAND request. |
| [UCMTCPCI_PORT_CONTROLLER_GET_STATUS_OUT_PARAMS structure](..\ucmtcpciportcontrollerrequests\ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-get-status-out-params.md) | Stores the values of all status registers of the port controller. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_STATUS request. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [UCM_PD_POWER_DATA_OBJECT_TYPE enumeration](..\ucmtypes\ne-ucmtypes--ucm-pd-power-data-object-type.md) | Defines Power Data Object types. |
| [UCM_POWER_ROLE enumeration](..\ucmtypes\ne-ucmtypes--ucm-power-role.md) | Defines power roles of USB Type-C connected devices. |
| [UCM_TYPEC_CURRENT enumeration](..\ucmtypes\ne-ucmtypes--ucm-typec-current.md) | Defines different Type-C current levels, as defined in the Type-C specification. |
| [UCM_TYPEC_PARTNER enumeration](..\ucmtypes\ne-ucmtypes--ucm-typec-partner.md) | Defines the state of the Type-C connector. |
| [UCM_TYPEC_OPERATING_MODE enumeration](..\ucmtypes\ne-ucmtypes--ucm-typec-operating-mode.md) | Defines operating modes of a USB Type-C connector. |
| [UCM_PD_CONN_STATE enumeration](..\ucmtypes\ne-ucmtypes--ucm-pd-conn-state.md) | Defines power delivery (PD) negotiation states of a Type-C port. |
| [UCM_CHARGING_STATE enumeration](..\ucmtypes\ne-ucmtypes--ucm-charging-state.md) | Defines the charging state of a Type-C connector. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [UCM_PD_POWER_DATA_OBJECT_INIT_ULONG function](..\ucmtypes\nf-ucmtypes-ucm-pd-power-data-object-init-ulong.md) | Initializes a UCM_PD_POWER_DATA_OBJECT structure by interpreting Power Data Object values and sets each field correctly. |
| [UCM_PD_POWER_DATA_OBJECT_INIT_BATTERY function](..\ucmtypes\nf-ucmtypes-ucm-pd-power-data-object-init-battery.md) | Initializes a UCM_PD_POWER_DATA_OBJECT structure as a Battery Supply type Power Data Object. |
| [UCM_PD_POWER_DATA_OBJECT_GET_TYPE function](..\ucmtypes\nf-ucmtypes-ucm-pd-power-data-object-get-type.md) | Retrieves the type of Power Data Object from the UCM_PD_POWER_DATA_OBJECT structure. |
| [UCM_PD_REQUEST_DATA_OBJECT_INIT_ULONG function](..\ucmtypes\nf-ucmtypes-ucm-pd-request-data-object-init-ulong.md) | Initializes a UCM_PD_REQUEST_DATA_OBJECT structure by interpreting Request Data Object values and sets each field correctly. |
| [UCM_PD_POWER_DATA_OBJECT_INIT_VARIABLE_NON_BATTERY function](..\ucmtypes\nf-ucmtypes-ucm-pd-power-data-object-init-variable-non-battery.md) | Initializes a UCM_PD_POWER_DATA_OBJECT structure as a Variable Supply Non Battery type Power Data Object. |
| [UCM_PD_POWER_DATA_OBJECT_INIT_FIXED function](..\ucmtypes\nf-ucmtypes-ucm-pd-power-data-object-init-fixed.md) | Initializes a to the UCM_PD_POWER_DATA_OBJECT for a Fixed Supply type Power Data Object. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_UCX_CONTROLLER_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC callback](..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-get-frame-number-and-qpc-for-time-sync.md) | UCX invokes this callback to retrieves the system query performance counter (QPC) value synchronized with the frame and microframe. |
| [EVT_UCX_CONTROLLER_RESET callback](..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-reset.md) | The client driver's implementation that UCX calls to reset the controller. |
| [EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS callback](..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-get-transport-characteristics.md) | UCX invokes this callback to retrieve the host controller characteristics. |
| [EVT_UCX_CONTROLLER_QUERY_USB_CAPABILITY callback](..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-query-usb-capability.md) | The client driver's implementation to determine if the controller supports a specific capability. |
| [EVT_UCX_CONTROLLER_START_TRACKING_FOR_TIME_SYNC callback](..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-start-tracking-for-time-sync.md) | UCX invokes this callback function to the start time tracking functionality in the controller. |
| [EVT_UCX_CONTROLLER_SET_TRANSPORT_CHARACTERISTICS_CHANGE_NOTIFICATION callback](..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-set-transport-characteristics-change-notification.md) | UCX invokes this callback function to specify its preference in transport characteristics for which the client driver must send notifications when changes occur. |
| [EVT_UCX_CONTROLLER_GET_CURRENT_FRAMENUMBER callback](..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-get-current-framenumber.md) | The client driver's implementation that UCX calls to retrieve the current 32-bit frame number. |
| [EVT_UCX_CONTROLLER_STOP_TRACKING_FOR_TIME_SYNC callback](..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-stop-tracking-for-time-sync.md) | UCX invokes this callback function to the stop time tracking functionality in the controller. |
| [EVT_UCX_CONTROLLER_USBDEVICE_ADD callback](..\ucxcontroller\nc-ucxcontroller-evt-ucx-controller-usbdevice-add.md) | The client driver's implementation that UCX calls when a new USB device is detected. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [UCX_CONTROLLER_STATE enumeration](..\ucxcontroller\ne-ucxcontroller--ucx-controller-state.md) | This enumeration provides values to specify the UCX controller state after a reset. |
| [UCX_CONTROLLER_PARENT_BUS_TYPE enumeration](..\ucxcontroller\ne-ucxcontroller--ucx-controller-parent-bus-type.md) | The UCX_CONTROLLER_PARENT_BUS_TYPE enumeration defines the parent bus type. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [UcxControllerSetIdStrings function](..\ucxcontroller\nf-ucxcontroller-ucxcontrollersetidstrings.md) | Updates the identifier strings of a controller after the controller has been initialized. |
| [UCX_CONTROLLER_CONFIG_SET_ACPI_INFO function](..\ucxcontroller\nf-ucxcontroller-ucx-controller-config-set-acpi-info.md) | Initializes a UCX_CONTROLLER_CONFIG structure with the specified values for the controller with ACPI as the parent. |
| [UcxControllerNotifyTransportCharacteristicsChange function](..\ucxcontroller\nf-ucxcontroller-ucxcontrollernotifytransportcharacteristicschange.md) | Notifies UCX about a new port change event from host controller. |
| [UCX_CONTROLLER_CONFIG_SET_PCI_INFO function](..\ucxcontroller\nf-ucxcontroller-ucx-controller-config-set-pci-info.md) | Initializes a UCX_CONTROLLER_CONFIG structure with the specified values for the controller with PCI as the parent bus type. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS structure](..\ucxcontroller\ns-ucxcontroller--ucx-controller-transport-characteristics.md) | Stores the transport characteristics at relevant points in time. This structure is used in the EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS callback function. |
| [UCX_CONTROLLER_RESET_COMPLETE_INFO structure](..\ucxcontroller\ns-ucxcontroller--ucx-controller-reset-complete-info.md) | Contains information about the operation to reset the controller. This is used by the client driver in its EVT_UCX_CONTROLLER_RESET callback function. |
| [UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS_CHANGE_FLAGS structure](..\ucxcontroller\ns-ucxcontroller--ucx-controller-transport-characteristics-change-flags.md) | Defines flags for the transport characteristics changes. This structure is used in the EVT_UCX_CONTROLLER_SET_TRANSPORT_CHARACTERISTICS_CHANGE_NOTIFICATION callback function. |
| [UCX_CONTROLLER_ACPI_INFORMATION structure](..\ucxcontroller\ns-ucxcontroller--ucx-controller-acpi-information.md) | This structure provides information about an advanced Configuration and power interface (ACPI) USB controller. |
| [UCX_CONTROLLER_CONFIG structure](..\ucxcontroller\ns-ucxcontroller--ucx-controller-config.md) | This structure configuration data for a USB controller. |
| [UCX_CONTROLLER_PCI_INFORMATION structure](..\ucxcontroller\ns-ucxcontroller--ucx-controller-pci-information.md) | This structure provides information about a PCI USB controller. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UCX_ENDPOINT_CHARACTERISTIC structure](..\ucxendpoint\ns-ucxendpoint--ucx-endpoint-characteristic.md) | Stores the characteristics of an endpoint. |
| [UCX_ENDPOINT_ISOCH_TRANSFER_PATH_DELAYS structure](..\ucxendpoint\ns-ucxendpoint--ucx-endpoint-isoch-transfer-path-delays.md) | Stores the isochronous transfer path delay values. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [UCX_ENDPOINT_CHARACTERISTIC_TYPE enumeration](..\ucxendpoint\ne-ucxendpoint--ucx-endpoint-characteristic-type.md) | Defines values that indicates the type of endpoint characteristic. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_UCX_ENDPOINT_GET_ISOCH_TRANSFER_PATH_DELAYS callback](..\ucxendpoint\nc-ucxendpoint-evt-ucx-endpoint-get-isoch-transfer-path-delays.md) | UCX invokes this callback function to get information about transfer path delays for an isochronous endpoint. |
| [EVT_UCX_ENDPOINT_SET_CHARACTERISTIC callback](..\ucxendpoint\nc-ucxendpoint-evt-ucx-endpoint-set-characteristic.md) | UCX invokes this callback function to set the priority on an endpoint. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UCX_USBDEVICE_CHARACTERISTIC structure](..\ucxusbdevice\ns-ucxusbdevice--ucx-usbdevice-characteristic.md) | Stores the characteristics of an device. |
| [UCX_USBDEVICE_CHARACTERISTIC_PATH_DELAY structure](..\ucxusbdevice\ns-ucxusbdevice--ucx-usbdevice-characteristic-path-delay.md) | Stores the isochronous transfer path delay values. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [UdecxUrbSetBytesCompleted function](..\udecxurb\nf-udecxurb-udecxurbsetbytescompleted.md) | Sets the number of bytes transferred for the URB contained within a framework request object. |
| [UdecxUrbCompleteWithNtStatus function](..\udecxurb\nf-udecxurb-udecxurbcompletewithntstatus.md) | Completes the URB request with an NTSTATUS code. |
| [UdecxUrbRetrieveControlSetupPacket function](..\udecxurb\nf-udecxurb-udecxurbretrievecontrolsetuppacket.md) | Retrieves a USB control setup packet from a specified framework request object. |
| [UdecxUrbComplete function](..\udecxurb\nf-udecxurb-udecxurbcomplete.md) | Completes the URB request with a USB-specific completion status code. |
| [UdecxUrbRetrieveBuffer function](..\udecxurb\nf-udecxurb-udecxurbretrievebuffer.md) | Retrieves the transfer buffer of an URB from the specified framework request object sent to the endpoint queue. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS structure](..\udecxusbdevice\ns-udecxusbdevice--udecx-usb-device-state-change-callbacks.md) | Initializes a UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS structure with pointers to callback functions that are implemented by a UDE client for a virtual USB device. |
| [UDECX_ENDPOINTS_CONFIGURE_PARAMS structure](..\udecxusbdevice\ns-udecxusbdevice--udecx-endpoints-configure-params.md) | Contains the configuration options specified by USB device emulation class extension (UdeCx) to the client driver when the class extension invokes EVT_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE. |
| [UDECX_USB_ENDPOINT_INIT_AND_METADATA structure](..\udecxusbdevice\ns-udecxusbdevice--udecx-usb-endpoint-init-and-metadata.md) | Contains the descriptors supported by an endpoint of a virtual USB device. |
| [UDECX_USB_DEVICE_PLUG_IN_OPTIONS structure](..\udecxusbdevice\ns-udecxusbdevice--udecx-usb-device-plug-in-options.md) | Contains the port numbers to which a virtual USB device is connected. Initialize this structure by calling the UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT method. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [UdecxUsbDeviceSetFunctionSuspendAndWakeComplete function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdevicesetfunctionsuspendandwakecomplete.md) | Completes an asynchronous request for changing the power state of a particular function of a virtual USB 3.0 device. |
| [UdecxUsbDeviceCreate function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdevicecreate.md) | Creates a USB Device Emulation (UDE) device object. |
| [UdecxUsbDeviceInitAddDescriptorWithIndex function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdeviceinitadddescriptorwithindex.md) | Adds a USB descriptor to the initialization parameters used to create a virtual USB device. |
| [UdecxUsbDeviceInitAddDescriptor function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdeviceinitadddescriptor.md) | Adds a USB descriptor to the initialization parameters used to create a virtual USB device. |
| [UdecxUsbDevicePlugIn function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdeviceplugin.md) | Notifies the USB device emulation class extension (UdeCx) that the USB device has been plugged in the specified port. |
| [UDECX_USB_DEVICE_PLUG_IN_OPTIONS_INIT function](..\udecxusbdevice\nf-udecxusbdevice-udecx-usb-device-plug-in-options-init.md) | Initializes a UDECX_USB_DEVICE_PLUG_IN_OPTIONS structure. |
| [UdecxUsbDeviceSignalWake function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdevicesignalwake.md) | Initiates wake up from a low link power state for a virtual USB 2.0 device. |
| [UdecxUsbDeviceInitAllocate function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdeviceinitallocate.md) | Allocates memory for a UDECXUSBDEVICE_INIT structure that is used to initialize a virtual USB device. |
| [UdecxUsbDeviceInitAddStringDescriptor function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdeviceinitaddstringdescriptor.md) | Adds a USB string descriptor to the initialization parameters used to create a virtual USB device. |
| [UDECX_USB_DEVICE_CALLBACKS_INIT function](..\udecxusbdevice\nf-udecxusbdevice-udecx-usb-device-callbacks-init.md) | Initializes a UDECX_USB_DEVICE_STATE_CHANGE_CALLBACKS structure before a UdecxUsbDeviceCreate call. |
| [UdecxUsbDeviceLinkPowerEntryComplete function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdevicelinkpowerentrycomplete.md) | Completes an asynchronous request for bringing the device out of a low power state. |
| [UdecxUsbDeviceInitSetStateChangeCallbacks function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdeviceinitsetstatechangecallbacks.md) | Initializes a WDF-allocated structure with pointers to callback functions. |
| [UdecxUsbDeviceSignalFunctionWake function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdevicesignalfunctionwake.md) | Initiates wake up of the specified function from a low power state. This applies to virtual USB 3.0 devices. |
| [UdecxUsbDeviceLinkPowerExitComplete function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdevicelinkpowerexitcomplete.md) | Completes an asynchronous request for sending the device to a low power state. |
| [UdecxUsbDeviceInitFree function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdeviceinitfree.md) | Releases the resources that were allocated by the UdecxUsbDeviceInitAllocate call. |
| [UdecxUsbDeviceInitSetEndpointsType function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdeviceinitsetendpointstype.md) | Indicates the type of endpoint (simple or dynamic) in the initialization parameters that the client driver uses to create the virtual USB device. |
| [UdecxUsbDeviceInitSetSpeed function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdeviceinitsetspeed.md) | Sets the USB speed of the virtual USB device to create. |
| [UdecxUsbDevicePlugOutAndDelete function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdeviceplugoutanddelete.md) | Disconnects the virtual USB device. |
| [UdecxUsbDeviceInitAddStringDescriptorRaw function](..\udecxusbdevice\nf-udecxusbdevice-udecxusbdeviceinitaddstringdescriptorraw.md) | Adds a USB string descriptor to the initialization parameters used to create a virtual USB device. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_UDECX_USB_DEVICE_ENDPOINTS_CONFIGURE callback](..\udecxusbdevice\nc-udecxusbdevice-evt-udecx-usb-device-endpoints-configure.md) | The USB device emulation class extension (UdeCx) invokes this callback function to change the configuration by selecting an alternate setting, disabling current endpoints, or adding dynamic endpoints. |
| [EVT_UDECX_USB_DEVICE_ENDPOINT_ADD callback](..\udecxusbdevice\nc-udecxusbdevice-evt-udecx-usb-device-endpoint-add.md) | The USB device emulation class extension (UdeCx) invokes this callback function to request the client driver to create a dynamic endpoint on the virtual USB device. |
| [EVT_UDECX_USB_DEVICE_DEFAULT_ENDPOINT_ADD callback](..\udecxusbdevice\nc-udecxusbdevice-evt-udecx-usb-device-default-endpoint-add.md) | The USB device emulation class extension (UdeCx) invokes this callback function to request the client driver to create the default control endpoint on the virtual USB device. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [UDECX_USB_DEVICE_SPEED enumeration](..\udecxusbdevice\ne-udecxusbdevice--udecx-usb-device-speed.md) | Defines values for USB device speeds. |
| [UDECX_USB_DEVICE_WAKE_SETTING enumeration](..\udecxusbdevice\ne-udecxusbdevice--udecx-usb-device-wake-setting.md) | Defines values for remote wake capability of a virtual USB device. |
| [UDECX_USB_DEVICE_FUNCTION_POWER enumeration](..\udecxusbdevice\ne-udecxusbdevice--udecx-usb-device-function-power.md) | Defines values for function wake capability of a virtual USB 3.0 device. |
| [UDECX_ENDPOINT_TYPE enumeration](..\udecxusbdevice\ne-udecxusbdevice--udecx-endpoint-type.md) | Defines values for endpoint types supported by a virtual USB device. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_UDECX_USB_ENDPOINT_START callback](..\udecxusbendpoint\nc-udecxusbendpoint-evt-udecx-usb-endpoint-start.md) | The USB device emulation class extension (UdeCx) invokes this callback function to start processing I/O requests on the specified endpoint of the virtual USB device. |
| [EVT_UDECX_USB_ENDPOINT_PURGE callback](..\udecxusbendpoint\nc-udecxusbendpoint-evt-udecx-usb-endpoint-purge.md) | The USB device emulation class extension (UdeCx) invokes this callback function to stop queuing I/O requests to the endpoint's queue and cancel unprocessed requests. |
| [EVT_UDECX_USB_ENDPOINT_RESET callback](..\udecxusbendpoint\nc-udecxusbendpoint-evt-udecx-usb-endpoint-reset.md) | The USB device emulation class extension (UdeCx) invokes this callback function to reset an endpoint of the virtual USB device. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [UdecxWdfDeviceTryHandleUserIoctl function](..\udecxwdfdevice\nf-udecxwdfdevice-udecxwdfdevicetryhandleuserioctl.md) | Attempts to handle an IOCTL request sent by a user-mode software. |
| [UdecxWdfDeviceResetComplete function](..\udecxwdfdevice\nf-udecxwdfdevice-udecxwdfdeviceresetcomplete.md) | Informs the USB device emulation class extension (UdeCx) that the reset operation on the specified controller has competed. |
| [UdecxWdfDeviceAddUsbDeviceEmulation function](..\udecxwdfdevice\nf-udecxwdfdevice-udecxwdfdeviceaddusbdeviceemulation.md) | Initializes a framework device object to support operations related to a host controller and a virtual USB device attached to the controller. |
| [UdecxInitializeWdfDeviceInit function](..\udecxwdfdevice\nf-udecxwdfdevice-udecxinitializewdfdeviceinit.md) | Initializes device initialization operations when the Plug and Play (PnP) manager reports the existence of a device. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [UDECX_WDF_DEVICE_RESET_ACTION enumeration](..\udecxwdfdevice\ne-udecxwdfdevice--udecx-wdf-device-reset-action.md) | Defines values that indicate the types of reset operation supported by an emulated USB host controller. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_UDECX_WDF_DEVICE_QUERY_USB_CAPABILITY callback](..\udecxwdfdevice\nc-udecxwdfdevice-evt-udecx-wdf-device-query-usb-capability.md) | The UDE client driver's implementation to determine the capabilities that are supported by the emulated USB host controller. |
| [EVT_UDECX_WDF_DEVICE_RESET callback](..\udecxwdfdevice\nc-udecxwdfdevice-evt-udecx-wdf-device-reset.md) | The UDE client driver's implementation to reset the emulated host controller or the devices attached to it. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_INTERNAL_USBFN_DESCRIPTOR_UPDATE IOCTL](..\ufxbase\ni-ufxbase-ioctl-internal-usbfn-descriptor-update.md) | The USB function class extension sends this request to the client driver to update to the endpoint descriptor for the specified endpoint. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UFX_DEVICE_CAPABILITIES structure](..\ufxbase\ns-ufxbase--ufx-device-capabilities.md) | The UFX_DEVICE_CAPABILITIES structure is used USB to define properties of the Universal Serial Bus (USB) device created by the controller. |
| [UFX_HARDWARE_FAILURE_CONTEXT structure](..\ufxbase\ns-ufxbase--ufx-hardware-failure-context.md) | The UFX_HARDWARE_FAILURE_CONTEXT structure is used to define controller-specific hardware failure properties. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [USBFN_ACTION enumeration](..\ufxbase\ne-ufxbase--usbfn-action.md) | Defines special actions UFX should take when the client driver calls the UfxDevicePortDetectCompleteEx function. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [EVT_UFX_DEVICE_TEST_MODE_SET callback](..\ufxclient\nc-ufxclient-evt-ufx-device-test-mode-set.md) | The client driver's implementation to set the test mode of the function controller. |
| [EVT_UFX_DEVICE_PORT_CHANGE callback](..\ufxclient\nc-ufxclient-evt-ufx-device-port-change.md) | The client driver's implementation to update the type of the new port to which the USB device is connected. |
| [EVT_UFX_DEVICE_ADDRESSED callback](..\ufxclient\nc-ufxclient-evt-ufx-device-addressed.md) | The client driver's implementation to assign an address on the function controller. |
| [EVT_UFX_DEVICE_PROPRIETARY_CHARGER_RESET callback](..\ufxclient\nc-ufxclient-evt-ufx-device-proprietary-charger-reset.md) | The client driver's implementation to resets proprietary charger. |
| [EVT_UFX_DEVICE_DEFAULT_ENDPOINT_ADD callback](..\ufxclient\nc-ufxclient-evt-ufx-device-default-endpoint-add.md) | The client driver's implementation to create a default control endpoint. |
| [EVT_UFX_DEVICE_PORT_DETECT callback](..\ufxclient\nc-ufxclient-evt-ufx-device-port-detect.md) | The client driver's implementation to initiate port detection. |
| [EVT_UFX_DEVICE_HOST_CONNECT callback](..\ufxclient\nc-ufxclient-evt-ufx-device-host-connect.md) | The client driver's implementation to initiate connection with the host. |
| [EVT_UFX_DEVICE_REMOTE_WAKEUP_SIGNAL callback](..\ufxclient\nc-ufxclient-evt-ufx-device-remote-wakeup-signal.md) | The client driver's implementation to initiate remote wake-up on the function controller. |
| [EVT_UFX_DEVICE_ENDPOINT_ADD callback](..\ufxclient\nc-ufxclient-evt-ufx-device-endpoint-add.md) | The client driver's implementation to create a default endpoint object. |
| [EVT_UFX_DEVICE_CONTROLLER_RESET callback](..\ufxclient\nc-ufxclient-evt-ufx-device-controller-reset.md) | The client driver's implementation to reset the function controller to its initial state. |
| [EVT_UFX_DEVICE_HOST_DISCONNECT callback](..\ufxclient\nc-ufxclient-evt-ufx-device-host-disconnect.md) | The client driver's implementation to disable the function controller's communication with the host. |
| [EVT_UFX_DEVICE_PROPRIETARY_CHARGER_SET_PROPERTY callback](..\ufxclient\nc-ufxclient-evt-ufx-device-proprietary-charger-set-property.md) | The client driver's implementation to set charger information that it uses to enable charging over USB. |
| [EVT_UFX_DEVICE_SUPER_SPEED_POWER_FEATURE callback](..\ufxclient\nc-ufxclient-evt-ufx-device-super-speed-power-feature.md) | The client driver's implementation to set or clear the specified power feature on the function controller. |
| [EVT_UFX_DEVICE_USB_STATE_CHANGE callback](..\ufxclient\nc-ufxclient-evt-ufx-device-usb-state-change.md) | The client driver's implementation to update the state of the USB device. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UFX_ENDPOINT_CALLBACKS structure](..\ufxclient\ns-ufxclient--ufx-endpoint-callbacks.md) | The UFX_ENDPOINT_CALLBACKS structure is used to define then event callback functions supported by the client driver. |
| [UFX_DEVICE_CALLBACKS structure](..\ufxclient\ns-ufxclient--ufx-device-callbacks.md) | The UFX_DEVICE_CALLBACKS structure is used to define then event callback functions supported by the client driver. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [UFX_DEVICE_CAPABILITIES_INIT function](..\ufxclient\nf-ufxclient-ufx-device-capabilities-init.md) | The UFX_DEVICE_CAPABILITIES_INIT macro the initializes the UFX_DEVICE_CAPABILITIES structure. |
| [UFX_DEVICE_CALLBACKS_INIT function](..\ufxclient\nf-ufxclient-ufx-device-callbacks-init.md) | The UFX_DEVICE_CALLBACKS_INIT macro initializes the UFX_DEVICE_CALLBACKS structure. |
| [UFX_ENDPOINT_CALLBACKS_INIT function](..\ufxclient\nf-ufxclient-ufx-endpoint-callbacks-init.md) | The UFX_ENDPOINT_CALLBACKS_INIT macro initializes the UFX_ENDPOINT_CALLBACKS structure. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [UFX_PROPRIETARY_CHARGER structure](..\ufxproprietarycharger\ns-ufxproprietarycharger--ufx-proprietary-charger.md) | Describes the proprietary charger's device power requirements. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [UFX_PROPRIETARY_CHARGER_ABORT_OPERATION callback](..\ufxproprietarycharger\nc-ufxproprietarycharger-ufx-proprietary-charger-abort-operation.md) | The filter driver's implementation to abort a charger operation. |
| [UFX_PROPRIETARY_CHARGER_SET_PROPERTY callback](..\ufxproprietarycharger\nc-ufxproprietarycharger-ufx-proprietary-charger-set-property.md) | The filter driver's implementation to set a configurable property on the charger. |
| [UFX_PROPRIETARY_CHARGER_DETECT callback](..\ufxproprietarycharger\nc-ufxproprietarycharger-ufx-proprietary-charger-detect.md) | The filter driver's implementation to detect if a charger is attached and get details about the charger. |
| [UFX_PROPRIETARY_CHARGER_RESET_OPERATION callback](..\ufxproprietarycharger\nc-ufxproprietarycharger-ufx-proprietary-charger-reset-operation.md) | The filter driver's implementation to reset a charger operation. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [UrsDeviceInitialize function](..\ursdevice\nf-ursdevice-ursdeviceinitialize.md) | Initializes a framework device object to support operations related to a USB dual-role controller and registers the relevant event callback functions with the USB dual-role controller class extension. |
| [UrsDeviceInitInitialize function](..\ursdevice\nf-ursdevice-ursdeviceinitinitialize.md) | Initializes device initialization operations when the Plug and Play (PnP) manager reports the existence of a device. |
| [UrsReportHardwareEvent function](..\ursdevice\nf-ursdevice-ursreporthardwareevent.md) | Notifies the USB dual-role class extension about a new hardware event. |
| [UrsIoResourceListAppendDescriptor function](..\ursdevice\nf-ursdevice-ursioresourcelistappenddescriptor.md) | Appends the specified resource descriptor to the specified I/O resource list object that maintains resource descriptors for the host or function role. |
| [UrsSetPoHandle function](..\ursdevice\nf-ursdevice-urssetpohandle.md) | Registers and deletes the client driver's registration with the power management framework (PoFx). |
| [URS_CONFIG_INIT function](..\ursdevice\nf-ursdevice-urs-config-init.md) | Initializes a URS_CONFIG structure. |
| [UrsSetHardwareEventSupport function](..\ursdevice\nf-ursdevice-urssethardwareeventsupport.md) | Indicates the client driver's support for reporting new hardware events. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [URS_CONFIG structure](..\ursdevice\ns-ursdevice--urs-config.md) | Contains pointers to event callback functions implemented by the URS client driver for a USB dual-role controller. Initialize this structure by calling URS_CONFIG_INIT. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [URS_ROLE enumeration](..\urstypes\ne-urstypes--urs-role.md) | Defines values for roles supported by a USB dual-role controller. |
| [URS_HARDWARE_EVENT enumeration](..\urstypes\ne-urstypes--urs-hardware-event.md) | Defines values for the hardware events that a client driver for a USB dual-role controller can report. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [URB structure](..\usb\ns-usb--urb.md) | The URB structure is used by USB client drivers to describe USB request blocks (URBs) that send requests to the USB driver stack. The URB structure defines a format for all possible commands that can be sent to a USB device. |
| [USBD_INTERFACE_INFORMATION structure](..\usb\ns-usb--usbd-interface-information.md) | The USBD_INTERFACE_INFORMATION structure holds information about an interface for a configuration on a USB device. |
| [USBD_ENDPOINT_OFFLOAD_INFORMATION structure](..\usb\ns-usb--usbd-endpoint-offload-information.md) | Stores xHCI-specific information that is used by client drivers to transfer data to and from the offloaded endpoints. |
| [USBD_VERSION_INFORMATION structure](..\usb\ns-usb--usbd-version-information.md) | The USBD_VERSION_INFORMATION structure is used by the GetUSBDIVersion function to report its output data. |
| [USBD_PIPE_INFORMATION structure](..\usb\ns-usb--usbd-pipe-information.md) | The USBD_PIPE_INFORMATION structure is used by USB client drivers to hold information about a pipe from a specific interface. |
| [USBD_ISO_PACKET_DESCRIPTOR structure](..\usb\ns-usb--usbd-iso-packet-descriptor.md) | The USBD_ISO_PACKET_DESCRIPTOR structure is used by USB client drivers to describe an isochronous transfer packet. |
| [USBD_STREAM_INFORMATION structure](..\usb\ns-usb--usbd-stream-information.md) | The USBD_STREAM_INFORMATION structure stores information about a stream associated with a bulk endpoint. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [USBD_PIPE_TYPE enumeration](..\usb\ne-usb--usbd-pipe-type.md) | The USBD_PIPE_TYPE enumerator indicates the type of pipe. |
| [USB_CONTROLLER_FLAVOR enumeration](..\usb\ne-usb--usb-controller-flavor.md) | The USB_CONTROLLER_FLAVOR enumeration specifies the type of USB host controller. |
| [USBD_ENDPOINT_OFFLOAD_MODE enumeration](..\usb\ne-usb--usbd-endpoint-offload-mode.md) | Defines values for endpoint offloading options in the USB device or host controller. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [USB_BUS_INTERFACE_USBDI_V0 structure](..\usbbusif\ns-usbbusif--usb-bus-interface-usbdi-v0.md) | The USB_BUS_INTERFACE_USBDI_V0 structure is provided by the USB hub driver to allow USB clients to make direct calls to the hub driver without allocating IRPs. |
| [USB_BUS_INTERFACE_USBDI_V2 structure](..\usbbusif\ns-usbbusif--usb-bus-interface-usbdi-v2.md) | The USB_BUS_INTERFACE_USBDI_V2 structure is provided by the USB hub driver to allow USB clients to make direct calls to the hub driver without allocating IRPs. |
| [USB_BUS_INFORMATION_LEVEL_1 structure](..\usbbusif\ns-usbbusif--usb-bus-information-level-1.md) | The USB_BUS_INFORMATION_LEVEL_1 structure is used in conjunction with the QueryBusInformation interface routine to report information about the bus. |
| [USBC_FUNCTION_DESCRIPTOR structure](..\usbbusif\ns-usbbusif--usbc-function-descriptor.md) | The USBC_FUNCTION_DESCRIPTOR structure describes a USB function and its associated interface collection. |
| [USB_BUS_INTERFACE_USBDI_V3 structure](..\usbbusif\ns-usbbusif--usb-bus-interface-usbdi-v3.md) | The USB_BUS_INTERFACE_USBDI_V3 structure is provided by the USB hub driver to allow USB clients to make direct calls to the hub driver without allocating IRPs. |
| [USB_BUS_INTERFACE_USBDI_V1 structure](..\usbbusif\ns-usbbusif--usb-bus-interface-usbdi-v1.md) | The USB_BUS_INTERFACE_USBDI_V1 structure is provided by the USB hub driver to allow USB clients to make direct calls to the hub driver without allocating IRPs. |
| [USB_BUS_INFORMATION_LEVEL_0 structure](..\usbbusif\ns-usbbusif--usb-bus-information-level-0.md) | The USB_BUS_INFORMATION_LEVEL_0 structure is used in conjunction with the QueryBusInformation interface routine to report information about the bus. |
| [USBC_DEVICE_CONFIGURATION_INTERFACE_V1 structure](..\usbbusif\ns-usbbusif--usbc-device-configuration-interface-v1.md) | The USBC_DEVICE_CONFIGURATION_INTERFACE_V1 structure is exposed by the vendor-supplied filter drivers to assist the USB generic parent driver in defining interface collections. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [USBC_START_DEVICE_CALLBACK callback](..\usbbusif\nc-usbbusif-usbc-start-device-callback.md) | The USBC_START_DEVICE_CALLBACK routine allows a USB client driver to provide a custom definition of the interface collections on a device. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [USBD_CreateHandle function](..\usbdlib\nf-usbdlib-usbd-createhandle.md) | The USBD_CreateHandle routine is called by a WDM USB client driver to obtain a USBD handle. The routine registers the client driver with the underlying USB driver stack. |
| [USBD_GetPdoRegistryParameter function](..\usbdlib\nf-usbdlib-usbd-getpdoregistryparameter.md) | The USBD_GetPdoRegistryParameter routine retrieves the value from the specified key in the USB device's hardware registry. |
| [USBD_QueryBusTime function](..\usbdlib\nf-usbdlib-usbd-querybustime.md) | The USBD_QueryBusTime routine has been deprecated in Windows XP and later operating systems. Do not use. |
| [USBD_ParseConfigurationDescriptor function](..\usbdlib\nf-usbdlib-usbd-parseconfigurationdescriptor.md) | The USBD_ParseConfigurationDescriptor routine has been deprecated. Use USBD_ParseConfigurationDescriptorEx instead. |
| [COMPOSITE_DEVICE_CAPABILITIES_INIT function](..\usbdlib\nf-usbdlib-composite-device-capabilities-init.md) | The COMPOSITE_DEVICE_CAPABILITIES_INIT macro initializes the COMPOSITE_DEVICE_CAPABILITIES structure. |
| [UsbBuildGetStatusRequest function](..\usbdlib\nf-usbdlib-usbbuildgetstatusrequest.md) | The UsbBuildGetStatusRequest macro formats an URB to obtain status from a device, interface, endpoint, or other device-defined target on a USB device. |
| [USBD_CreateConfigurationRequest function](..\usbdlib\nf-usbdlib-usbd-createconfigurationrequest.md) | The USBD_CreateConfigurationRequest routine has been deprecated. Use USBD_CreateConfigurationRequestEx instead. |
| [USBD_CreateConfigurationRequestEx function](..\usbdlib\nf-usbdlib-usbd-createconfigurationrequestex.md) | The USBD_CreateConfigurationRequestEx routine allocates and formats a URB to select a configuration for a USB device.USBD_CreateConfigurationRequestEx replaces USBD_CreateConfigurationRequest. |
| [USBD_UrbFree function](..\usbdlib\nf-usbdlib-usbd-urbfree.md) | The USBD_UrbFree routine releases the URB that is allocated by USBD_UrbAllocate, USBD_IsochUrbAllocate, USBD_SelectConfigUrbAllocateAndBuild, or USBD_SelectInterfaceUrbAllocateAndBuild. |
| [USBD_ValidateConfigurationDescriptor function](..\usbdlib\nf-usbdlib-usbd-validateconfigurationdescriptor.md) | The USBD_ValidateConfigurationDescriptor routine validates all descriptors returned by a device in its response to a configuration descriptor request. |
| [USBD_ParseConfigurationDescriptorEx function](..\usbdlib\nf-usbdlib-usbd-parseconfigurationdescriptorex.md) | The USBD_ParseConfigurationDescriptorEx routine searches a given configuration descriptor and returns a pointer to an interface that matches the given search criteria. |
| [USBD_CalculateUsbBandwidth function](..\usbdlib\nf-usbdlib-usbd-calculateusbbandwidth.md) | The USBD_CalculateUsbBandwidth routine has been deprecated in Windows XP and later operating systems. Do not use. |
| [UsbBuildInterruptOrBulkTransferRequest function](..\usbdlib\nf-usbdlib-usbbuildinterruptorbulktransferrequest.md) | The UsbBuildInterruptOrBulkTransferRequest macro formats an URB to send or receive data on a bulk pipe, or to receive data from an interrupt pipe. |
| [USBD_GetInterfaceLength function](..\usbdlib\nf-usbdlib-usbd-getinterfacelength.md) | The USBD_GetInterfaceLength routine obtains the length of a given interface descriptor, including the length of all endpoint descriptors contained within the interface. |
| [USBD_SelectConfigUrbAllocateAndBuild function](..\usbdlib\nf-usbdlib-usbd-selectconfigurballocateandbuild.md) | The USBD_SelectConfigUrbAllocateAndBuild routine allocates and formats a URB structure that is required to select a configuration for a USB device. |
| [USBD_AssignUrbToIoStackLocation function](..\usbdlib\nf-usbdlib-usbd-assignurbtoiostacklocation.md) | The USBD_AssignUrbToIoStackLocation routine is called by a client driver to associate an URB with the IRP's next stack location. |
| [USBD_RegisterHcFilter function](..\usbdlib\nf-usbdlib-usbd-registerhcfilter.md) | The USBD_RegisterHcFilter routine has been deprecated in Windows XP and later operating systems. |
| [USBD_IsochUrbAllocate function](..\usbdlib\nf-usbdlib-usbd-isochurballocate.md) | The USBD_IsochUrbAllocate routine allocates and formats a URB structure for an isochronous transfer request. |
| [USBD_BuildRegisterCompositeDevice function](..\usbdlib\nf-usbdlib-usbd-buildregistercompositedevice.md) | The USBD_BuildRegisterCompositeDevice routine is called by the driver of a USB multi-function device (composite driver) to initialize a REGISTER_COMPOSITE_DEVICE structure with the information required for registering the driver with the USB driver stack. |
| [USBD_SelectInterfaceUrbAllocateAndBuild function](..\usbdlib\nf-usbdlib-usbd-selectinterfaceurballocateandbuild.md) | The USBD_SelectInterfaceUrbAllocateAndBuild routine allocates and formats a URB structure that is required for a request to select an interface or change its alternate setting. |
| [UsbBuildOpenStaticStreamsRequest function](..\usbdlib\nf-usbdlib-usbbuildopenstaticstreamsrequest.md) | The UsbBuildOpenStaticStreamsRequest inline function formats an URB structure for an open-streams request. The request opens streams associated with the specified bulk endpoint. |
| [USBD_GetUSBDIVersion function](..\usbdlib\nf-usbdlib-usbd-getusbdiversion.md) | The USBD_GetUSBDIVersion routine returns version information about the host controller driver (HCD) that controls the client's USB device.Note  USBD_IsInterfaceVersionSupported replaces the USBD_GetUSBDIVersion routine |
| [USBD_IsInterfaceVersionSupported function](..\usbdlib\nf-usbdlib-usbd-isinterfaceversionsupported.md) | The USBD_IsInterfaceVersionSupported routine is called by a USB client driver to check whether the underlying USB driver stack supports a particular USBD interface version. |
| [USBD_CloseHandle function](..\usbdlib\nf-usbdlib-usbd-closehandle.md) | The USBD_CloseHandle routine is called by a USB client driver to close a USBD handle and release all resources associated with the driver's registration. |
| [USBD_ParseDescriptors function](..\usbdlib\nf-usbdlib-usbd-parsedescriptors.md) | The USBD_ParseDescriptors routine searches a given configuration descriptor and returns a pointer to the first descriptor that matches the search criteria. |
| [USBD_UrbAllocate function](..\usbdlib\nf-usbdlib-usbd-urballocate.md) | The USBD_UrbAllocate routine allocates a USB Request Block (URB). |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [REQUEST_REMOTE_WAKE_NOTIFICATION structure](..\usbdlib\ns-usbdlib--request-remote-wake-notification.md) | The purpose of the REQUEST_REMOTE_WAKE_NOTIFICATION structure is to specify input parameters for the IOCTL_INTERNAL_USB_REQUEST_REMOTE_WAKE_NOTIFICATION I/O control request. |
| [USBD_INTERFACE_LIST_ENTRY structure](..\usbdlib\ns-usbdlib--usbd-interface-list-entry.md) | The USBD_INTERFACE_LIST_ENTRY structure is used by USB client drivers to create an array of interfaces to be inserted into a configuration request. |
| [REGISTER_COMPOSITE_DEVICE structure](..\usbdlib\ns-usbdlib--register-composite-device.md) | The REGISTER_COMPOSITE_DEVICE structure is used with the IOCTL_INTERNAL_USB_REGISTER_COMPOSITE_DEVICE I/O control request to register a parent driver of a Universal Serial Bus (USB) multi-function device (composite driver) with the USB driver stack. |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [USBFN_GET_ATTACH_ACTION_ABORT callback](..\usbfnattach\nc-usbfnattach-usbfn-get-attach-action-abort.md) | The filter driver's implementation to abort an attach-detect operation. |
| [USBFN_GET_ATTACH_ACTION callback](..\usbfnattach\nc-usbfnattach-usbfn-get-attach-action.md) | The filter driver's implementation that gets invoked when charger is attached to the port. |
| [USBFN_SET_DEVICE_STATE callback](..\usbfnattach\nc-usbfnattach-usbfn-set-device-state.md) | The filter driver's implementation to set the device state and operating bus speed. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [USBFN_ATTACH_ACTION enumeration](..\usbfnattach\ne-usbfnattach--usbfn-attach-action.md) | Defines the actions that the Universal Serial Bus (USB) function stack takes when a device is attached to a USB port. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [USBFN_INTERFACE_ATTACH structure](..\usbfnattach\ns-usbfnattach--usbfn-interface-attach.md) | Stores pointers to driver-implemented callback functions for handling attach and detach operations. |
| [USBFN_ON_ATTACH structure](..\usbfnattach\ns-usbfnattach--usbfn-on-attach.md) | Describes the detected port type and attach action. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [USBFN_BUS_CONFIGURATION_INFO structure](..\usbfnbase\ns-usbfnbase--usbfn-bus-configuration-info.md) | Configuration packet that stores information about an available USB configuration. |
| [USBFN_NOTIFICATION structure](..\usbfnbase\ns-usbfnbase--usbfn-notification.md) | Describes information about a Universal Serial Bus (USB) event notification that was received by using IOCTL_INTERNAL_USBFN_BUS_EVENT_NOTIFICATION. |
| [USBFN_CLASS_INFORMATION_PACKET_EX structure](..\usbfnbase\ns-usbfnbase--usbfn-class-information-packet-ex.md) | Describes device interface class information associated with a USB interface. This structure can be used to describe single and multi-interface functions. |
| [USBFN_CLASS_INTERFACE structure](..\usbfnbase\ns-usbfnbase--usbfn-class-interface.md) | Describes an interface and its endpoints. |
| [USBFN_INTERFACE_INFO structure](..\usbfnbase\ns-usbfnbase--usbfn-interface-info.md) | Describes an interface and its endpoints. |
| [USBFN_USB_STRING structure](..\usbfnbase\ns-usbfnbase--usbfn-usb-string.md) | Describes a USB string descriptor and the associated string index. |
| [ALTERNATE_INTERFACE structure](..\usbfnbase\ns-usbfnbase--alternate-interface.md) | The ALTERNATE_INTERFACE structure provides information about alternate settings for a Universal Serial Bus (USB) interface. |
| [USBFN_CLASS_INFORMATION_PACKET structure](..\usbfnbase\ns-usbfnbase--usbfn-class-information-packet.md) | Describes device interface class information associated with a USB interface. This structure can only hold information about a single function interface. |
| [USBFN_PIPE_INFORMATION structure](..\usbfnbase\ns-usbfnbase--usbfn-pipe-information.md) | Describes attributes of a pipe associated with an endpoint on a specific interface. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [USBFN_PORT_TYPE enumeration](..\usbfnbase\ne-usbfnbase--usbfn-port-type.md) | Defines the possible port types that can be returned by the client driver during port detection. |
| [USBFN_DEVICE_STATE enumeration](..\usbfnbase\ne-usbfnbase--usbfn-device-state.md) | Defines the Universal Serial Bus (USB) device states for the device/controller. These states correspond to the USB device states as defined in section 9.1 of the USB 2.0 Specification. |
| [USBFN_EVENT enumeration](..\usbfnbase\ne-usbfnbase--usbfn-event.md) | Defines notifications sent to class drivers. |
| [USBFN_DIRECTION enumeration](..\usbfnbase\ne-usbfnbase--usbfn-direction.md) | Defines the USB data transfer direction types. |
| [USBFN_BUS_SPEED enumeration](..\usbfnbase\ne-usbfnbase--usbfn-bus-speed.md) | The USBFN_BUS_SPEED enumeration defines possible bus speeds. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_INTERNAL_USBFN_ACTIVATE_USB_BUS IOCTL](..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-activate-usb-bus.md) | The USB class driver sends this request to activate the bus so that the driver can prepare to process bus events and handle traffic. |
| [IOCTL_INTERNAL_USBFN_BUS_EVENT_NOTIFICATION IOCTL](..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-bus-event-notification.md) | The USB class driver sends this request to prepare for notifications received from the USB function class extension (UFX) in response to an event on the bus, such as a change in the port type or a receipt of a non-standard setup packet. |
| [IOCTL_INTERNAL_USBFN_CONTROL_STATUS_HANDSHAKE_IN IOCTL](..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-control-status-handshake-in.md) | The class driver sends this request to send a zero-length control status handshake on endpoint 0 in the IN direction. |
| [IOCTL_INTERNAL_USBFN_REGISTER_USB_STRING IOCTL](..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-register-usb-string.md) | The class driver sends this request to register a USB string descriptor. |
| [IOCTL_INTERNAL_USBFN_TRANSFER_IN IOCTL](..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-transfer-in.md) | The class driver sends this request to initiate a data transfer to the host on the specified pipe. |
| [IOCTL_INTERNAL_USBFN_GET_INTERFACE_DESCRIPTOR_SET IOCTL](..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-get-interface-descriptor-set.md) | The class driver sends this request to get the entire USB interface descriptor set for a function on the device. |
| [IOCTL_INTERNAL_USBFN_CONTROL_STATUS_HANDSHAKE_OUT IOCTL](..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-control-status-handshake-out.md) | The class driver sends this request to send a zero-length control status handshake on endpoint 0 in the OUT direction. |
| [IOCTL_INTERNAL_USBFN_SET_PIPE_STATE IOCTL](..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-set-pipe-state.md) | The class driver sends this request to set the stall state of the specified USB pipe. |
| [IOCTL_INTERNAL_USBFN_SIGNAL_REMOTE_WAKEUP IOCTL](..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-signal-remote-wakeup.md) | The class driver sends this request to get remote wake-up notifications from endpoints. |
| [IOCTL_INTERNAL_USBFN_GET_CLASS_INFO IOCTL](..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-get-class-info.md) | The class driver sends this request IO control code to retrieve information about the available pipes for a device, as configured in the registry. |
| [IOCTL_INTERNAL_USBFN_TRANSFER_IN_APPEND_ZERO_PKT IOCTL](..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-transfer-in-append-zero-pkt.md) | The class driver sends this request to initiate an IN transfer to the specified pipe and appends a zero-length packet to indicate the end of the transfer. |
| [IOCTL_INTERNAL_USBFN_TRANSFER_OUT IOCTL](..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-transfer-out.md) | The class driver sends this request to initiate a data transfer from the host on the specified pipe. |
| [IOCTL_INTERNAL_USBFN_GET_PIPE_STATE IOCTL](..\usbfnioctl\ni-usbfnioctl-ioctl-internal-usbfn-get-pipe-state.md) | The class driver sends this request to get the stall state of the specified pipe. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [USB_TRANSPORT_CHARACTERISTICS structure](..\usbioctl\ns-usbioctl--usb-transport-characteristics.md) | Stores the transport characteristics at relevant points in time. This structure is used in the IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS request. |
| [USB_PORT_CONNECTOR_PROPERTIES structure](..\usbioctl\ns-usbioctl--usb-port-connector-properties.md) | The USB_PORT_CONNECTOR_PROPERTIES structure is used with the IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES I/O control request to retrieve information about a port on a particular SuperSpeed hub. |
| [USB_NODE_CONNECTION_INFORMATION_EX structure](..\usbioctl\ns-usbioctl--usb-node-connection-information-ex.md) | The USB_NODE_CONNECTION_INFORMATION_EX structure is used in conjunction with the IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX request to obtain information about the connection associated with the indicated USB port. |
| [USB_TRANSPORT_CHARACTERISTICS_CHANGE_REGISTRATION structure](..\usbioctl\ns-usbioctl--usb-transport-characteristics-change-registration.md) | Contains registration information for the IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE request. |
| [USB_START_TRACKING_FOR_TIME_SYNC_INFORMATION structure](..\usbioctl\ns-usbioctl--usb-start-tracking-for-time-sync-information.md) | The input and output buffer for the IOCTL_USB_START_TRACKING_FOR_TIME_SYNC request. |
| [USB_NODE_CONNECTION_INFORMATION structure](..\usbioctl\ns-usbioctl--usb-node-connection-information.md) | The USB_NODE_CONNECTION_INFORMATION structure is used with the IOCTL_USB_GET_NODE_CONNECTION_INFORMATION request to retrieve information about a USB port and connected device. |
| [USB_HUB_INFORMATION_EX structure](..\usbioctl\ns-usbioctl--usb-hub-information-ex.md) | The USB_HUB_INFORMATION_EX structure is used with the IOCTL_USB_GET_HUB_INFORMATION_EX I/O control request to retrieve information about a Universal Serial Bus (USB) hub. |
| [USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS structure](..\usbioctl\ns-usbioctl--usb-node-connection-information-ex-v2-flags.md) | The USB_NODE_CONNECTION_INFORMATION_EX_V2_FLAGS union is used to indicate the speed at which a USB 3.0 device is currently operating and whether it can operate at higher speed, when attached to a particular port. |
| [USB_HUB_NAME structure](..\usbioctl\ns-usbioctl--usb-hub-name.md) | The USB_HUB_NAME structure stores the hub's symbolic device name. |
| [USB_HUB_CAP_FLAGS structure](..\usbioctl\ns-usbioctl--usb-hub-cap-flags.md) | The USB_HUB_CAP_FLAGS structure is used to report the capabilities of a hub. |
| [USB_PORT_PROPERTIES structure](..\usbioctl\ns-usbioctl--usb-port-properties.md) | The USB_PORT_PROPERTIES union is used to report the capabilities of a Universal Serial Bus (USB) port.The port capabilities are retrieved in the USB_PORT_CONNECTOR_PROPERTIES structure by the IOCTL_USB_GET_PORT_CONNECTOR_PROPERTIES I/O control request. |
| [USB_NODE_INFORMATION structure](..\usbioctl\ns-usbioctl--usb-node-information.md) | The USB_NODE_INFORMATION structure is used with the IOCTL_USB_GET_NODE_INFORMATION I/O control request to retrieve information about a parent device. |
| [USB_TRANSPORT_CHARACTERISTICS_CHANGE_NOTIFICATION structure](..\usbioctl\ns-usbioctl--usb-transport-characteristics-change-notification.md) | Contains registration information filled when the IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE request completes. |
| [USB_NODE_CONNECTION_INFORMATION_EX_V2 structure](..\usbioctl\ns-usbioctl--usb-node-connection-information-ex-v2.md) | The USB_NODE_CONNECTION_INFORMATION_EX_V2 structure is used with the IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX_V2 I/O control request to retrieve speed information about a Universal Serial Bus (USB) device that is attached to a particular port. |
| [USB_TRANSPORT_CHARACTERISTICS_CHANGE_UNREGISTRATION structure](..\usbioctl\ns-usbioctl--usb-transport-characteristics-change-unregistration.md) | Contains unregistration information for the IOCTL_USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE request. |
| [USB_NODE_CONNECTION_NAME structure](..\usbioctl\ns-usbioctl--usb-node-connection-name.md) | The USB_NODE_CONNECTION_NAME structure is used with the IOCTL_USB_GET_NODE_CONNECTION_NAME I/O control request to retrieve the symbolic link of the downstream hub that is attached to the port. |
| [USB_PROTOCOLS structure](..\usbioctl\ns-usbioctl--usb-protocols.md) | The USB_PROTOCOLS union is used to report the Universal Serial Bus (USB) signaling protocols that are supported by the port. |
| [USB_NODE_CONNECTION_DRIVERKEY_NAME structure](..\usbioctl\ns-usbioctl--usb-node-connection-driverkey-name.md) | The USB_NODE_CONNECTION_DRIVERKEY_NAME structure is used with the IOCTL_USB_GET_NODE_CONNECTION_DRIVERKEY_NAME I/O control request to retrieve the driver key name for the device that is connected to the indicated port. |
| [USB_DESCRIPTOR_REQUEST structure](..\usbioctl\ns-usbioctl--usb-descriptor-request.md) | The USB_DESCRIPTOR_REQUEST structure is used with the IOCTL_USB_GET_DESCRIPTOR_FROM_NODE_CONNECTION I/O control request to retrieve one or more descriptors for the device that is associated with the indicated connection index. |
| [USB_TOPOLOGY_ADDRESS structure](..\usbioctl\ns-usbioctl--usb-topology-address.md) | The USB_TOPOLOGY_ADDRESS structure is used with the IOCTL_INTERNAL_USB_GET_TOPOLOGY_ADDRESS I/O request to retrieve information about a USB device?s location in the USB device tree. |
| [USB_HUB_INFORMATION structure](..\usbioctl\ns-usbioctl--usb-hub-information.md) | The USB_HUB_INFORMATION structure contains information about a hub. |
| [HUB_DEVICE_CONFIG_INFO_V1 structure](..\usbioctl\ns-usbioctl--hub-device-config-info-v1.md) | The HUB_DEVICE_CONFIG_INFO structure is used in conjunction with the kernel-mode IOCTL, IOCTL_INTERNAL_USB_GET_DEVICE_CONFIG_INFO to request to report information about a USB device and the hub to which the device is attached. |
| [USB_NODE_CONNECTION_ATTRIBUTES structure](..\usbioctl\ns-usbioctl--usb-node-connection-attributes.md) | The USB_NODE_CONNECTION_ATTRIBUTES structure is used with the IOCTL_USB_GET_NODE_CONNECTION_ATTRIBUTES I/O control request to retrieve the attributes of a connection. |
| [USB_HUB_CAPABILITIES_EX structure](..\usbioctl\ns-usbioctl--usb-hub-capabilities-ex.md) | The USB_HUB_CAPABILITIES_EX structure is used with the IOCTL_USB_GET_HUB_CAPABILITIES I/O control request to retrieve the capabilities of a particular USB hub. |
| [USB_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC_INFORMATION structure](..\usbioctl\ns-usbioctl--usb-frame-number-and-qpc-for-time-sync-information.md) | Stores the frame and microframe numbers and the calculated system QPC values. This structure is used in the IOCTL_USB_GET_FRAME_NUMBER_AND_QPC_FOR_TIME_SYNC request. |
| [USB_PIPE_INFO structure](..\usbioctl\ns-usbioctl--usb-pipe-info.md) | The USB_PIPE_INFO structure is used in conjunction with the USB_NODE_CONNECTION_INFORMATION_EX structure and the IOCTL_USB_GET_NODE_CONNECTION_INFORMATION_EX request to obtain information about a connection and its associated pipes. |
| [USB_HCD_DRIVERKEY_NAME structure](..\usbioctl\ns-usbioctl--usb-hcd-driverkey-name.md) | The USB_HCD_DRIVERKEY_NAME structure is used with the IOCTL_GET_HCD_DRIVERKEY_NAME I/O control request to retrieve the driver key in the registry for the USB host controller driver. |
| [USB_MI_PARENT_INFORMATION structure](..\usbioctl\ns-usbioctl--usb-mi-parent-information.md) | The USB_MI_PARENT_INFORMATION structure contains information about a composite device. |
| [USB_ROOT_HUB_NAME structure](..\usbioctl\ns-usbioctl--usb-root-hub-name.md) | The USB_ROOT_HUB_NAME structure stores the root hub's symbolic device name. |
| [USB_ID_STRING structure](..\usbioctl\ns-usbioctl--usb-id-string.md) | The USB_ID_STRING structure is used to store a string or multi-string. |
| [USB_DEVICE_CHARACTERISTICS structure](..\usbioctl\ns-usbioctl--usb-device-characteristics.md) | Contains information about the USB device’s characteristics, such as the maximum send and receive delays for any request. This structure is used in the IOCTL_USB_GET_DEVICE_CHARACTERISTICS request. |
| [USB_HUB_CAPABILITIES structure](..\usbioctl\ns-usbioctl--usb-hub-capabilities.md) | The USB_HUB_CAPABILITIES structure has been deprecated. Use USB_HUB_CAPABILITIES_EX instead. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_USB_GET_TRANSPORT_CHARACTERISTICS IOCTL](..\usbioctl\ni-usbioctl-ioctl-usb-get-transport-characteristics.md) | The client driver sends this request to retrieve the transport characteristics. |
| [IOCTL_USB_REGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE IOCTL](..\usbioctl\ni-usbioctl-ioctl-usb-register-for-transport-characteristics-change.md) | This request registers for notifications about the changes in transport characteristics. |
| [IOCTL_USB_UNREGISTER_FOR_TRANSPORT_CHARACTERISTICS_CHANGE IOCTL](..\usbioctl\ni-usbioctl-ioctl-usb-unregister-for-transport-characteristics-change.md) | This request unregisters the caller from getting notifications about transport characteristics changes. |
| [IOCTL_USB_START_TRACKING_FOR_TIME_SYNC IOCTL](..\usbioctl\ni-usbioctl-ioctl-usb-start-tracking-for-time-sync.md) | This request registers the caller with USB driver stack for time sync services. |
| [IOCTL_USB_NOTIFY_ON_TRANSPORT_CHARACTERISTICS_CHANGE IOCTL](..\usbioctl\ni-usbioctl-ioctl-usb-notify-on-transport-characteristics-change.md) | This request notifies the caller of change in transport characteristics. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [USB_HUB_NODE enumeration](..\usbioctl\ne-usbioctl--usb-hub-node.md) | The USB_HUB_NODE enumerator indicates whether a device is a hub or a composite device. |
| [USB_CONNECTION_STATUS enumeration](..\usbioctl\ne-usbioctl--usb-connection-status.md) | The USB_CONNECTION_STATUS enumerator indicates the status of the connection to a device on a USB hub port. |
| [USB_CONNECTION_STATUS enumeration](..\usbioctl\ne-usbioctl--usb-connection-status~r2.md) | The USB_CONNECTION_STATUS enumerator indicates the status of the connection to a device on a USB hub port. |
| [USB_CONNECTION_STATUS enumeration](..\usbioctl\ne-usbioctl--usb-connection-status~r1.md) | The USB_CONNECTION_STATUS enumerator indicates the status of the connection to a device on a USB hub port. |
| [USB_HUB_TYPE enumeration](..\usbioctl\ne-usbioctl--usb-hub-type.md) | The USB_HUB_TYPE enumeration defines constants that indicate the type of USB hub. The hub type is retrieved by the IOCTL_USB_GET_HUB_INFORMATION_EX I/O control request. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [USB_30_HUB_DESCRIPTOR structure](..\usbspec\ns-usbspec--usb-30-hub-descriptor.md) | The USB_30_HUB_DESCRIPTOR structure contains a SuperSpeed hub descriptor. For information about the structure members, see Universal Serial Bus Revision 3.0 Specification, 10.13.2.1 Hub Descriptor, Table 10-3. SuperSpeed Hub Descriptor. |
| [USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR structure](..\usbspec\ns-usbspec--usb-superspeed-endpoint-companion-descriptor.md) | The USB_SUPERSPEED_ENDPOINT_COMPANION_DESCRIPTOR structure is used by USB client drivers to retrieve a USB-defined SuperSpeed Endpoint Companion descriptor. For more information, see section 9.6.7 and Table 9-20 in the official USB 3.0 specification. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [USB_DEVICE_SPEED enumeration](..\usbspec\ne-usbspec--usb-device-speed.md) | The USB_DEVICE_SPEED enumeration defines constants for USB device speeds. |


This technology is in the following headers:


| Header        | 

| [hubbusif](..\hubbusif\~PORTAL~hubbusif.md) | 

| [kusbfnclasslib](..\kusbfnclasslib\~PORTAL~kusbfnclasslib.md) | 

| [ucmcx](..\ucmcx\~PORTAL~ucmcx.md) | 

| [ucmfuncenum](..\ucmfuncenum\~PORTAL~ucmfuncenum.md) | 

| [ucmglobals](..\ucmglobals\~PORTAL~ucmglobals.md) | 

| [ucmmanager](..\ucmmanager\~PORTAL~ucmmanager.md) | 

| [ucmtcpciportcontrollerrequests](..\ucmtcpciportcontrollerrequests\~PORTAL~ucmtcpciportcontrollerrequests.md) | 

| [ucmtypes](..\ucmtypes\~PORTAL~ucmtypes.md) | 

| [ucxclass](..\ucxclass\~PORTAL~ucxclass.md) | 

| [ucxcontroller](..\ucxcontroller\~PORTAL~ucxcontroller.md) | 

| [ucxendpoint](..\ucxendpoint\~PORTAL~ucxendpoint.md) | 

| [ucxusbdevice](..\ucxusbdevice\~PORTAL~ucxusbdevice.md) | 

| [udecxfuncenum](..\udecxfuncenum\~PORTAL~udecxfuncenum.md) | 

| [udecxtypes](..\udecxtypes\~PORTAL~udecxtypes.md) | 

| [udecxurb](..\udecxurb\~PORTAL~udecxurb.md) | 

| [udecxusbdevice](..\udecxusbdevice\~PORTAL~udecxusbdevice.md) | 

| [udecxusbendpoint](..\udecxusbendpoint\~PORTAL~udecxusbendpoint.md) | 

| [udecxwdfdevice](..\udecxwdfdevice\~PORTAL~udecxwdfdevice.md) | 

| [ufxbase](..\ufxbase\~PORTAL~ufxbase.md) | 

| [ufxclient](..\ufxclient\~PORTAL~ufxclient.md) | 

| [ufxproprietarycharger](..\ufxproprietarycharger\~PORTAL~ufxproprietarycharger.md) | 

| [upssvc](..\upssvc\~PORTAL~upssvc.md) | 

| [urscx](..\urscx\~PORTAL~urscx.md) | 

| [ursdevice](..\ursdevice\~PORTAL~ursdevice.md) | 

| [ursfuncenum](..\ursfuncenum\~PORTAL~ursfuncenum.md) | 

| [ursglobals](..\ursglobals\~PORTAL~ursglobals.md) | 

| [urstypes](..\urstypes\~PORTAL~urstypes.md) | 

| [usb](..\usb\~PORTAL~usb.md) | 

| [usbbusif](..\usbbusif\~PORTAL~usbbusif.md) | 

| [usbcamdi](..\usbcamdi\~PORTAL~usbcamdi.md) | 

| [usbdlib](..\usbdlib\~PORTAL~usbdlib.md) | 

| [usbfnattach](..\usbfnattach\~PORTAL~usbfnattach.md) | 

| [usbfnbase](..\usbfnbase\~PORTAL~usbfnbase.md) | 

| [usbfnioctl](..\usbfnioctl\~PORTAL~usbfnioctl.md) | 

| [usbioctl](..\usbioctl\~PORTAL~usbioctl.md) | 

| [usbspec](..\usbspec\~PORTAL~usbspec.md) | 
