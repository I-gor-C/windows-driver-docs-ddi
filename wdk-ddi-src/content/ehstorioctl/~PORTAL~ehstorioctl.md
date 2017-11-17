# Declarations in the ehstorioctl header
This header Ehstorioctl contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [tagACT_AUTHZ_STATE structure](ns-ehstorioctl-tagact-authz-state.md) | This structure describes the Addressable Command Target (ACT) authorization state. |
| [ENUM_PDO_ENTRY structure](ns-ehstorioctl--enum-pdo-entry.md) | This structure describes a single entry in a result set of Physical Device Objects (PDOs) that are enumerated with IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS. |
| [SILO_DRIVER_CAPABILITIES structure](ns-ehstorioctl--silo-driver-capabilities.md) | This structure is used to specify the capabilities and support for IOCTL redirection of a storage silo driver. SILO_DRIVER_CAPABILITIES is included in the system buffer of an IOCTL_EHSTOR_DRIVER_REPORT_CAPABILITIES request. |
| [LBA_FILTER_TABLE structure](ns-ehstorioctl--lba-filter-table.md) | The LBA_FILTER_TABLE structure contains the LBA ranges whose access is controlled by a silo driver. |
| [EHSTOR_DEVICE_PROPERTIES structure](ns-ehstorioctl--ehstor-device-properties.md) | TBD |
| [LBA_FILTER_TABLE_ENTRY structure](ns-ehstorioctl--lba-filter-table-entry.md) | The LBA_FILTER_TABLE_ENTRY structure contains an individual LBA range for the LBA_FILTER_TABLE sent in an IOCTL_EHSTOR_DRIVER_UPDATE_LBA_FILTER_TABLE request. |
| [tagSILO_COMMAND structure](ns-ehstorioctl-tagsilo-command.md) | This structure describes a storage silo driver command. |
| [ENUM_PDO_RESULTS structure](ns-ehstorioctl--enum-pdo-results.md) | This structure describes a result set of Physical Device Objects (PDOs) that are enumerated with IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS. |
| [AUTHZ_STATE structure](ns-ehstorioctl--authz-state.md) | TBD |
| [tagACT_QUEUE_STATE structure](ns-ehstorioctl-tagact-queue-state.md) | TBD |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_EHSTOR_DEVICE_SILO_COMMAND IOCTL](ni-ehstorioctl-ioctl-ehstor-device-silo-command.md) | TBD |
| [IOCTL_EHSTOR_DEVICE_QUERY_PROPERTIES IOCTL](ni-ehstorioctl-ioctl-ehstor-device-query-properties.md) | TBD |
| [IOCTL_EHSTOR_DRIVER_REPORT_CAPABILITIES IOCTL](ni-ehstorioctl-ioctl-ehstor-driver-report-capabilities.md) | TBD |
| [IOCTL_EHSTOR_DRIVER_UPDATE_LBA_FILTER_TABLE IOCTL](ni-ehstorioctl-ioctl-ehstor-driver-update-lba-filter-table.md) | TBD |
| [IOCTL_EHSTOR_DEVICE_GET_AUTHZ_STATE IOCTL](ni-ehstorioctl-ioctl-ehstor-device-get-authz-state.md) | TBD |
| [IOCTL_EHSTOR_DRIVER_PERFORM_AUTHZ IOCTL](ni-ehstorioctl-ioctl-ehstor-driver-perform-authz.md) | TBD |
| [IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS IOCTL](ni-ehstorioctl-ioctl-ehstor-device-enumerate-pdos.md) | TBD |
| [IOCTL_EHSTOR_DEVICE_GET_QUEUE_STATE IOCTL](ni-ehstorioctl-ioctl-ehstor-device-get-queue-state.md) | TBD |
| [IOCTL_EHSTOR_DEVICE_SET_AUTHZ_STATE IOCTL](ni-ehstorioctl-ioctl-ehstor-device-set-authz-state.md) | TBD |
| [IOCTL_EHSTOR_DEVICE_SET_QUEUE_STATE IOCTL](ni-ehstorioctl-ioctl-ehstor-device-set-queue-state.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [PDO_TYPE enumeration](ne-ehstorioctl--pdo-type.md) | This enumeration describes the types of Physical Device Objects (PDOs). |
| [PDO_STATE enumeration](ne-ehstorioctl--pdo-state.md) | This enumeration describes the states of Physical Device Objects (PDOs). |
| [PDO_CAPS enumeration](ne-ehstorioctl--pdo-caps.md) | This enumeration describes the capabilities of Physical Device Objects (PDOs). |
| [SILO_DRIVER_CAPS enumeration](ne-ehstorioctl--silo-driver-caps.md) | TBD |

This header is used in these topics:

- [Storage](..content/_Storage)
