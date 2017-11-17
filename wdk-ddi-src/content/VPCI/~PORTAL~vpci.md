# Declarations in the vpci header
This header Vpci contains these programming interfaces:

Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_VPCI_WRITE_BLOCK IOCTL](ni-vpci-ioctl-vpci-write-block.md) | The driver for a PCI Express (PCIe) virtual function (VF) issues an IOCTL_VPCI_WRITE_BLOCK I/O control code (IOCTL) in order to write data to a VF configuration block. The driver issues this IOCTL to the next-lower driver in the driver stack. |
| [IOCTL_VPCI_INVALIDATE_BLOCK IOCTL](ni-vpci-ioctl-vpci-invalidate-block.md) | The driver for a PCI Express (PCIe) virtual function (VF) issues the IOCTL_VPCI_INVALIDATE_BLOCK IOCTL request in order to be notified of changes to data in one or more VF configuration blocks. |
| [IOCTL_VPCI_READ_BLOCK IOCTL](ni-vpci-ioctl-vpci-read-block.md) | The driver for a PCI Express (PCIe) virtual function (VF) issues an IOCTL_VPCI_READ_BLOCK I/O control code (IOCTL) in order to read data from a VF configuration block. The driver issues this IOCTL to the next-lower driver in the driver stack. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [VPCI_READ_BLOCK_INPUT structure](ns-vpci--vpci-read-block-input.md) | The VPCI_READ_BLOCK_INPUT structure is used in an IOCTL_VPCI_READ_BLOCK IOCTL request to read data from a specified configuration block of data for a PCI Express (PCIe) virtual function (VF). |
| [VPCI_WRITE_BLOCK_INPUT structure](ns-vpci--vpci-write-block-input.md) | The VPCI_WRITE_BLOCK_INPUT structure is used in an IOCTL_VPCI_WRITE_BLOCK IOCTL request to write data to a specified configuration block for a PCI Express (PCIe) virtual function (VF). |
| [VPCI_INVALIDATE_BLOCK_OUTPUT structure](ns-vpci--vpci-invalidate-block-output.md) | The VPCI_INVALIDATE_BLOCK_OUTPUT structure is used in an IOCTL_VPCI_INVALIDATE_BLOCK IOCTL request. |
| [VPCI_INTERFACE_STANDARD structure](ns-vpci--vpci-interface-standard.md) | TBD |
Callback

| Title        | Description    |
| ------------- |:-------------:|
| [VPCI_READ_BLOCK callback function](nc-vpci-vpci-read-block.md) | TBD |
| [VPCI_WRITE_BLOCK callback function](nc-vpci-vpci-write-block.md) | TBD |

This header is used in these topics:

- [kernel](..content/_kernel)
