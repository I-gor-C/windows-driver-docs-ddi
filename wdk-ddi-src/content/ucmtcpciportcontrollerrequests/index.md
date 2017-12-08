# Ucmtcpciportcontrollerrequests.h header


This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Ucmtcpciportcontrollerrequests.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_ENTERED_IN_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-alternate-mode-entered-in-params.md) | Stores information about the alternate mode that was detected. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_ENTERED request. |
| [UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_EXITED_IN_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-alternate-mode-exited-in-params.md) | Stores information about the alternate mode that was exited. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_EXITED request. |
| [UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_CONFIGURED_IN_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-displayport-configured-in-params.md) | Stores information about the pin assignment of the DisplayPort alternate mode that was configured. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_CONFIGURED request. |
| [UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED_IN_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-displayport-display-out-status-changed-in-params.md) | Stores information about display out status of the DisplayPort connection. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED request. |
| [UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS_CHANGED_IN_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-displayport-hpd-status-changed-in-params.md) | Stores information about hot plug detect status of the DisplayPort connection. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS_CHANGED request. |
| [UCMTCPCI_PORT_CONTROLLER_GET_CONTROL_IN_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-get-control-in-params.md) | This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL request. |
| [UCMTCPCI_PORT_CONTROLLER_GET_CONTROL_OUT_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-get-control-out-params.md) | Stores the values of all control registers of the port controller retrieved by the IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL request. |
| [UCMTCPCI_PORT_CONTROLLER_GET_STATUS_IN_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-get-status-in-params.md) | This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_STATUS request. |
| [UCMTCPCI_PORT_CONTROLLER_GET_STATUS_OUT_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-get-status-out-params.md) | Stores the values of all status registers of the port controller. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_STATUS request. |
| [UCMTCPCI_PORT_CONTROLLER_SET_COMMAND_IN_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-command-in-params.md) | Stores the specified command registers. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_COMMAND request. |
| [UCMTCPCI_PORT_CONTROLLER_SET_CONFIG_STANDARD_OUTPUT_IN_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-config-standard-output-in-params.md) | Stores the value of the CONFIG_STANDARD_OUTPUT Register. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONFIG_STANDARD_OUTPUT request. |
| [UCMTCPCI_PORT_CONTROLLER_SET_CONTROL_IN_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-control-in-params.md) | Stores the values of all control registers. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONTROL request. |
| [UCMTCPCI_PORT_CONTROLLER_SET_MESSAGE_HEADER_INFO_IN_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-message-header-info-in-params.md) | Stores the value of the VBUS_VOLTAGE_ALARM_LO_CFG Register. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_MESSAGE_HEADER_INFO request. |
| [UCMTCPCI_PORT_CONTROLLER_SET_RECEIVE_DETECT_IN_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-receive-detect-in-params.md) | Stores the value of the RECEIVE_DETECT Register. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_RECEIVE_DETECT request. |
| [UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_BUFFER_IN_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-transmit-buffer-in-params.md) | Stores the value of the TRANSMIT_BUFFER Register. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_BUFFER request. |
| [UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_IN_PARAMS structure](ns-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-set-transmit-in-params.md) | Stores the values of TRANSMIT Register. This structure is used in the IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT request. |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_ENTERED IOCTL](ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-alternate-mode-entered.md) | Notifies the client driver that an alternate mode is entered so that the driver can perform additional tasks. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_ALTERNATE_MODE_EXITED IOCTL](ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-alternate-mode-exited.md) | Notifies the client driver that an alternate mode is exited so that the driver can perform additional tasks. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_CONFIGURED IOCTL](ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-displayport-configured.md) | Notifies the client driver that the DisplayPort alternate mode on the partner device has been configured with pin assignment so that the driver can perform additional tasks. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS_CHANGED IOCTL](ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-displayport-display-out-status-changed.md) | Notifies the client driver that the display out status of the DisplayPort connection has changed so that the driver can perform additional tasks. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS_CHANGED IOCTL](ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-displayport-hpd-status-changed.md) | Notifies the client driver that the hot-plug detect status of the DisplayPort connection has changed so that the driver can perform additional tasks. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_CONTROL IOCTL](ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-get-control.md) | Gets the values of all control registers defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_GET_STATUS IOCTL](ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-get-status.md) | Gets values of all status registers as per the Universal Serial Bus Type-C Port Controller Interface Specification. The client driver must retrieve the values of the CC_STATUS, POWER_STATUS, and FAULT_STATUS registers. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_COMMAND IOCTL](ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-command.md) | Sets the value of a command register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONFIG_STANDARD_OUTPUT IOCTL](ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-config-standard-output.md) | Sets the CONFIG_STANDARD_OUTPUT Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_CONTROL IOCTL](ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-control.md) | Sets the value of a control register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_MESSAGE_HEADER_INFO IOCTL](ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-message-header-info.md) | Sets the value of the MESSAGE_HEADER_INFO Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_RECEIVE_DETECT IOCTL](ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-receive-detect.md) | Sets the RECEIVE_DETECT Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT IOCTL](ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-transmit.md) | Sets the TRANSMIT Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |
| [IOCTL_UCMTCPCI_PORT_CONTROLLER_SET_TRANSMIT_BUFFER IOCTL](ni-ucmtcpciportcontrollerrequests-ioctl-ucmtcpci-port-controller-set-transmit-buffer.md) | Sets the TRANSMIT_BUFER Register defined as per the Universal Serial Bus Type-C Port Controller Interface Specification. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_DISPLAY_OUT_STATUS enumeration](ne-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-displayport-display-out-status.md) | Defines values to determine whether a display out status for a DisplayPort device is enabled. |
| [UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_HPD_STATUS enumeration](ne-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-displayport-hpd-status.md) | Defines values to determine whether a DisplayPort device is plugged in. |
| [UCMTCPCI_PORT_CONTROLLER_DISPLAYPORT_PIN_ASSIGNMENT enumeration](ne-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-displayport-pin-assignment.md) | TBD. |
| [UCMTCPCI_PORT_CONTROLLER_IOCTL enumeration](ne-ucmtcpciportcontrollerrequests--ucmtcpci-port-controller-ioctl.md) | Defines the various device I/O control requests that are sent to the client driver for the port controller. This indicates the type of IOCTL in WPP. |
