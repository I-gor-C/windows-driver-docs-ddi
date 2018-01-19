---
UID : NA:ucmtcpciportcontroller
ms.assetid : dd438fb7-2bf1-3024-8e33-e52b2795977c
ms.author : windowsdriverdev
ms.date : 01/18/18
ms.keywords : 
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : portal
---

# ucmtcpciportcontroller.h header



ucmtcpciportcontroller.h contains the following programming interfaces:





## Functions
| Title | Description |
| ---- |:---- |
| [UCMTCPCI_PORT_CONTROLLER_ALERT_DATA_INIT](nf-ucmtcpciportcontroller-ucmtcpci_port_controller_alert_data_init.md) | Initializes the UCMTCPCI_PORT_CONTROLLER_ALERT_DATA structure. |
| [UCMTCPCI_PORT_CONTROLLER_CAPABILITIES_INIT](nf-ucmtcpciportcontroller-ucmtcpci_port_controller_capabilities_init.md) | Initializes the UCMTCPCI_PORT_CONTROLLER_CAPABILITIES structure. |
| [UCMTCPCI_PORT_CONTROLLER_CONFIG_INIT](nf-ucmtcpciportcontroller-ucmtcpci_port_controller_config_init.md) | Initializes the UCMTCPCI_PORT_CONTROLLER_CONFIG structure. |
| [UCMTCPCI_PORT_CONTROLLER_IDENTIFICATION_INIT](nf-ucmtcpciportcontroller-ucmtcpci_port_controller_identification_init.md) | Initializes the UCMTCPCI_PORT_CONTROLLER_IDENTIFICATION structure. |
| [UcmTcpciPortControllerAlert](nf-ucmtcpciportcontroller-ucmtcpciportcontrolleralert.md) | Sends information about the hardware alerts that are received on the port controller to UcmTcpciCx. |
| [UcmTcpciPortControllerCreate](nf-ucmtcpciportcontroller-ucmtcpciportcontrollercreate.md) | Creates a port controller object to register with UcmTcpciCx. |
| [UcmTcpciPortControllerSetHardwareRequestQueue](nf-ucmtcpciportcontroller-ucmtcpciportcontrollersethardwarerequestqueue.md) | Assigns a framework queue object to which the UcmTcpciCx dispatches hardware requests for the port controller. |
| [UcmTcpciPortControllerStart](nf-ucmtcpciportcontroller-ucmtcpciportcontrollerstart.md) | Indicates to the UcmTcpciCx class extension that the client driver is now ready to service hardware requests for the port controller. |
| [UcmTcpciPortControllerStop](nf-ucmtcpciportcontroller-ucmtcpciportcontrollerstop.md) | Indicates to the UcmTcpciCx class extension to stop sending hardware requests to the port controller object. |



## Structures
| Title | Description |
| ---- |:---- |
| [_UCMTCPCI_PORT_CONTROLLER_ALERT_DATA](ns-ucmtcpciportcontroller-_ucmtcpci_port_controller_alert_data.md) | Contains information about hardware alerts received on the port controller object. This structure is used in the UcmTcpciPortControllerAlert call. Call UCMTCPCI_PORT_CONTROLLER_ALERT_DATA_INIT to initialize this structure. |
| [_UCMTCPCI_PORT_CONTROLLER_CAPABILITIES](ns-ucmtcpciportcontroller-_ucmtcpci_port_controller_capabilities.md) | Contains information about the capabilities of the port controller. |
| [_UCMTCPCI_PORT_CONTROLLER_CONFIG](ns-ucmtcpciportcontroller-_ucmtcpci_port_controller_config.md) | Contains configuration options for the port controller object, passed by the client driver in the call to UcmTcpciPortControllerCreate. Call UCMTCPCI_PORT_CONTROLLER_CONFIG_INIT to initialize this structure. |
| [_UCMTCPCI_PORT_CONTROLLER_IDENTIFICATION](ns-ucmtcpciportcontroller-_ucmtcpci_port_controller_identification.md) | Contains identification information and USB specification version information (in BCD format) about the port controller. |


## Enumerations
| Title | Description |
| ---- |:---- |
| [_UCMTCPCI_PORT_CONTROLLER_ALERT_TYPE](ne-ucmtcpciportcontroller-_ucmtcpci_port_controller_alert_type.md) | Defines generic alert values that are used to indicate the type of hardware alert received on the port controller. |