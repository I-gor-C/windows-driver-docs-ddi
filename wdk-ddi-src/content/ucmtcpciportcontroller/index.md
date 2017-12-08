# Ucmtcpciportcontroller.h header


This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Ucmtcpciportcontroller.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [UCMTCPCI_PORT_CONTROLLER_ALERT_DATA_INIT function](nf-ucmtcpciportcontroller-ucmtcpci-port-controller-alert-data-init.md) | Initializes the UCMTCPCI_PORT_CONTROLLER_ALERT_DATA structure. |
| [UCMTCPCI_PORT_CONTROLLER_CAPABILITIES_INIT function](nf-ucmtcpciportcontroller-ucmtcpci-port-controller-capabilities-init.md) | Initializes the UCMTCPCI_PORT_CONTROLLER_CAPABILITIES structure. |
| [UCMTCPCI_PORT_CONTROLLER_CONFIG_INIT function](nf-ucmtcpciportcontroller-ucmtcpci-port-controller-config-init.md) | Initializes the UCMTCPCI_PORT_CONTROLLER_CONFIG structure. |
| [UCMTCPCI_PORT_CONTROLLER_IDENTIFICATION_INIT function](nf-ucmtcpciportcontroller-ucmtcpci-port-controller-identification-init.md) | Initializes the UCMTCPCI_PORT_CONTROLLER_IDENTIFICATION structure. |
| [UcmTcpciPortControllerAlert function](nf-ucmtcpciportcontroller-ucmtcpciportcontrolleralert.md) | Sends information about the hardware alerts that are received on the port controller to UcmTcpciCx. |
| [UcmTcpciPortControllerCreate function](nf-ucmtcpciportcontroller-ucmtcpciportcontrollercreate.md) | Creates a port controller object to register with UcmTcpciCx. |
| [UcmTcpciPortControllerSetHardwareRequestQueue function](nf-ucmtcpciportcontroller-ucmtcpciportcontrollersethardwarerequestqueue.md) | Assigns a framework queue object to which the UcmTcpciCx dispatches hardware requests for the port controller. |
| [UcmTcpciPortControllerStart function](nf-ucmtcpciportcontroller-ucmtcpciportcontrollerstart.md) | Indicates to the UcmTcpciCx class extension that the client driver is now ready to service hardware requests for the port controller. |
| [UcmTcpciPortControllerStop function](nf-ucmtcpciportcontroller-ucmtcpciportcontrollerstop.md) | Indicates to the UcmTcpciCx class extension to stop sending hardware requests to the port controller object. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [UCMTCPCI_PORT_CONTROLLER_ALERT_DATA structure](ns-ucmtcpciportcontroller--ucmtcpci-port-controller-alert-data.md) | Contains information about hardware alerts received on the port controller object. This structure is used in the UcmTcpciPortControllerAlert call. Call UCMTCPCI_PORT_CONTROLLER_ALERT_DATA_INIT to initialize this structure. |
| [UCMTCPCI_PORT_CONTROLLER_CAPABILITIES structure](ns-ucmtcpciportcontroller--ucmtcpci-port-controller-capabilities.md) | Contains information about the capabilities of the port controller. |
| [UCMTCPCI_PORT_CONTROLLER_CONFIG structure](ns-ucmtcpciportcontroller--ucmtcpci-port-controller-config.md) | Contains configuration options for the port controller object, passed by the client driver in the call to UcmTcpciPortControllerCreate. Call UCMTCPCI_PORT_CONTROLLER_CONFIG_INIT to initialize this structure. |
| [UCMTCPCI_PORT_CONTROLLER_IDENTIFICATION structure](ns-ucmtcpciportcontroller--ucmtcpci-port-controller-identification.md) | Contains identification information and USB specification version information (in BCD format) about the port controller. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [UCMTCPCI_PORT_CONTROLLER_ALERT_TYPE enumeration](ne-ucmtcpciportcontroller--ucmtcpci-port-controller-alert-type.md) | Defines generic alert values that are used to indicate the type of hardware alert received on the port controller. |
