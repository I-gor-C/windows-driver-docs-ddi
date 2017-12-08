# Ucxroothub.h header


This header is used by Universal Serial Bus(USB). For more information, see
- [Universal Serial Bus(USB)](../_usbref/index.md)

Ucxroothub.h contain these programming interfaces:


## Callback functions

| Title   | Description   |
| ---- |:---- |
| [EVT_UCX_ROOTHUB_CONTROL_URB callback](nc-ucxroothub-evt-ucx-roothub-control-urb.md) | The client driver uses this callback type to implement handlers that UCX calls when it receives feature control requests on the USB hub. |
| [EVT_UCX_ROOTHUB_GET_20PORT_INFO callback](nc-ucxroothub-evt-ucx-roothub-get-20port-info.md) | The client driver's implementation that UCX calls when it receives a request for information about USB 2.0 ports on the root hub. |
| [EVT_UCX_ROOTHUB_GET_30PORT_INFO callback](nc-ucxroothub-evt-ucx-roothub-get-30port-info.md) | The client driver's implementation that UCX calls when it receives a request for information about USB 3.0 ports on the root hub. |
| [EVT_UCX_ROOTHUB_GET_INFO callback](nc-ucxroothub-evt-ucx-roothub-get-info.md) | The client driver's implementation that UCX calls when it receives a request for information about the root hub. |
| [EVT_UCX_ROOTHUB_INTERRUPT_TX callback](nc-ucxroothub-evt-ucx-roothub-interrupt-tx.md) | The client driver's implementation that UCX calls when it receives a request for information about changed ports. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [CONTROLLER_USB_20_HARDWARE_LPM_FLAGS structure](ns-ucxroothub--controller-usb-20-hardware-lpm-flags.md) | Describes supported protocol capabilities for Link Power Management (LPM) in as defined the USB 2.0 specification. |
| [HUB_INFO_FROM_PARENT structure](ns-ucxroothub--hub-info-from-parent.md) | Describes information about a hub from its parent device. |
| [PARENT_HUB_FLAGS structure](ns-ucxroothub--parent-hub-flags.md) | This structure is used by the HUB_INFO_FROM_PARENT structure to get hub information from the parent. |
| [ROOTHUB_20PORTS_INFO structure](ns-ucxroothub--roothub-20ports-info.md) | This structure that has an array of 2.0 ports supported by the root hub. This structure is provided by UCX in a framework request in the EVT_UCX_ROOTHUB_GET_20PORT_INFO callback function. |
| [ROOTHUB_20PORT_INFO structure](ns-ucxroothub--roothub-20port-info.md) | Provides information about a USB 2.0 root hub port. This structure is passed by UCX in the EVT_UCX_ROOTHUB_GET_20PORT_INFO callback function. |
| [ROOTHUB_30PORTS_INFO structure](ns-ucxroothub--roothub-30ports-info.md) | Provides information about USB 3.0 root hub ports. This structure is passed by UCX in the EVT_UCX_ROOTHUB_GET_30PORT_INFO callback function. |
| [ROOTHUB_30PORT_INFO structure](ns-ucxroothub--roothub-30port-info.md) | Provides information about a USB 3.0 root hub port. This structure is passed by UCX in the EVT_UCX_ROOTHUB_GET_30PORT_INFO callback function. |
| [ROOTHUB_30PORT_INFO_EX structure](ns-ucxroothub--roothub-30port-info-ex.md) | Provides extended USB 3.0 port information about speed. |
| [ROOTHUB_INFO structure](ns-ucxroothub--roothub-info.md) | Provides information about a USB root hub. This structure is passed by UCX in the EVT_UCX_ROOTHUB_GET_INFO callback function. |
| [UCX_ROOTHUB_CONFIG structure](ns-ucxroothub--ucx-roothub-config.md) | Contains pointers to event callback functions for creating the root hub by calling UcxRootHubCreate. Initialize this structure by calling UCX_ROOTHUB_CONFIG_INIT initialization function (see Ucxclass.h). |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [CONTROLLER_TYPE enumeration](ne-ucxroothub--controller-type.md) | This enumeration specifies if the USB host controller is an eXtensible Host Controller Interface (xHCI) controller. |
| [TRISTATE enumeration](ne-ucxroothub--tristate.md) | The TRISTATE enumeration indicates generic state values for true or false. |
