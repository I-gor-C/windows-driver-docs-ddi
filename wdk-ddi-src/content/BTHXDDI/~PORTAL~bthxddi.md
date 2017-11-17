# Declarations in the bthxddi header
This header Bthxddi contains these programming interfaces:

Enum

| Title        | Description    |
| ------------- |:-------------:|
| [BTHX_SCO_SUPPORT enumeration](ne-bthxddi--bthx-sco-support.md) | The BTHX_SCO_SUPPORT enumeration lists the different types of SCO supported by the transport driver. |
| [BTHX_HCI_PACKET_TYPE enumeration](ne-bthxddi--bthx-hci-packet-type.md) | The BTHX_HCI_PACKET_TYPE enumeration lists the different types of packets being sent from the Bluetooth stack to the transport driver. |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_BTHX_WRITE_HCI IOCTL](ni-bthxddi-ioctl-bthx-write-hci.md) | IOCTL_BTHX_WRITE_HCI is used to write Bluetooth ACL Data and Commands to the transport layer. |
| [IOCTL_BTHX_QUERY_CAPABILITIES IOCTL](ni-bthxddi-ioctl-bthx-query-capabilities.md) | IOCTL_BTHX_QUERY_CAPABILITIES is used to query the capabilities of the transport driver. |
| [IOCTL_BTHX_READ_HCI IOCTL](ni-bthxddi-ioctl-bthx-read-hci.md) | IOCTL_BTHX_READ_HCI is used to read Bluetooth ACL Data and Events from the transport layer. |
| [IOCTL_BTHX_GET_VERSION IOCTL](ni-bthxddi-ioctl-bthx-get-version.md) | Profile drivers use IOCTL_BTHX_GET_VERSION to get the version supported by the transport driver. |
| [IOCTL_BTHX_SET_VERSION IOCTL](ni-bthxddi-ioctl-bthx-set-version.md) | IOCTL_BTHX_SET_VERSION is used to inform the transport driver of the version of the extensibility interface being used. |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [BTHX_VERSION structure](ns-bthxddi--bthx-version.md) | The BTHX_VERSION structure describes the version or versions that the transport driver supports. |
| [BTHX_HCI_READ_WRITE_CONTEXT structure](ns-bthxddi--bthx-hci-read-write-context.md) | The BTHX_HCI_READ_WRITE_CONTEXT structure is used as an input/output structure for the IOCTL_BTHX_READ_HCI and IOCTL_BTHX_WRITE_HCI IOCTLs. |
| [BTHX_CAPABILITIES structure](ns-bthxddi--bthx-capabilities.md) | The BTHX_CAPABILITIES structure describes the capabilities of the Bluetooth Extensible Transport Driver. |
Function

| Title        | Description    |
| ------------- |:-------------:|
| [BTHX_CTL function](nf-bthxddi-bthx-ctl.md) | TBD |

This header is used in these topics:

- [bltooth](..content/_bltooth)
