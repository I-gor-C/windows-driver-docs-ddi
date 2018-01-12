---
UID: NA:ucxcontroller
---

# Ucxcontroller.h header

## -description

This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Ucxcontroller.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [UCX_CONTROLLER_CONFIG_SET_ACPI_INFO function](nf-ucxcontroller-ucx_controller_config_set_acpi_info.md) | Initializes a UCX_CONTROLLER_CONFIG structure with the specified values for the controller with ACPI as the parent. |
| [UCX_CONTROLLER_CONFIG_SET_PCI_INFO function](nf-ucxcontroller-ucx_controller_config_set_pci_info.md) | Initializes a UCX_CONTROLLER_CONFIG structure with the specified values for the controller with PCI as the parent bus type. |
| [UcxControllerNeedsReset function](nf-ucxcontroller-ucxcontrollerneedsreset.md) | Initiates a non-Plug and Play (PnP) controller reset operation by queuing an event into the controller reset state machine. |
| [UcxControllerNotifyTransportCharacteristicsChange function](nf-ucxcontroller-ucxcontrollernotifytransportcharacteristicschange.md) | Notifies UCX about a new port change event from host controller. |
| [UcxControllerResetComplete function](nf-ucxcontroller-ucxcontrollerresetcomplete.md) | Informs USB Host Controller Extension (UCX) that the reset operation has competed. |
| [UcxControllerSetFailed function](nf-ucxcontroller-ucxcontrollersetfailed.md) | Informs USB Host Controller Extension (UCX) that the controller has encountered a critical failure. |
| [UcxControllerSetIdStrings function](nf-ucxcontroller-ucxcontrollersetidstrings.md) | Updates the identifier strings of a controller after the controller has been initialized. |
| [UcxIoDeviceControl function](nf-ucxcontroller-ucxiodevicecontrol.md) | Allows USB host controller extension (UCX) to handle an I/O control code (IOCTL) request from user mode. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [_UCX_CONTROLLER_ACPI_INFORMATION structure](ns-ucxcontroller-_ucx_controller_acpi_information.md) | This structure provides information about an advanced Configuration and power interface (ACPI) USB controller. |
| [_UCX_CONTROLLER_CONFIG structure](ns-ucxcontroller-_ucx_controller_config.md) | This structure configuration data for a USB controller. |
| [_UCX_CONTROLLER_PCI_INFORMATION structure](ns-ucxcontroller-_ucx_controller_pci_information.md) | This structure provides information about a PCI USB controller. |
| [_UCX_CONTROLLER_RESET_COMPLETE_INFO structure](ns-ucxcontroller-_ucx_controller_reset_complete_info.md) | Contains information about the operation to reset the controller. This is used by the client driver in its EVT_UCX_CONTROLLER_RESET callback function. |
| [_UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS structure](ns-ucxcontroller-_ucx_controller_transport_characteristics.md) | Stores the transport characteristics at relevant points in time. This structure is used in the EVT_UCX_CONTROLLER_GET_TRANSPORT_CHARACTERISTICS callback function. |
| [_UCX_CONTROLLER_TRANSPORT_CHARACTERISTICS_CHANGE_FLAGS structure](ns-ucxcontroller-_ucx_controller_transport_characteristics_change_flags.md) | Defines flags for the transport characteristics changes. This structure is used in the EVT_UCX_CONTROLLER_SET_TRANSPORT_CHARACTERISTICS_CHANGE_NOTIFICATION callback function. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_UCX_CONTROLLER_PARENT_BUS_TYPE enumeration](ne-ucxcontroller-_ucx_controller_parent_bus_type.md) | The UCX_CONTROLLER_PARENT_BUS_TYPE enumeration defines the parent bus type. |
| [_UCX_CONTROLLER_STATE enumeration](ne-ucxcontroller-_ucx_controller_state.md) | This enumeration provides values to specify the UCX controller state after a reset. |
