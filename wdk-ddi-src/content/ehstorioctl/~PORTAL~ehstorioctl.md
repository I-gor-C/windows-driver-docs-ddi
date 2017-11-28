# Ehstorioctl.h header


This header is used by unknown technology.

Ehstorioctl.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [ENUM_PDO_ENTRY structure](ns-ehstorioctl--enum-pdo-entry.md) | This structure describes a single entry in a result set of Physical Device Objects (PDOs) that are enumerated with IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS. |
| [ENUM_PDO_RESULTS structure](ns-ehstorioctl--enum-pdo-results.md) | This structure describes a result set of Physical Device Objects (PDOs) that are enumerated with IOCTL_EHSTOR_DEVICE_ENUMERATE_PDOS. |
| [LBA_FILTER_TABLE structure](ns-ehstorioctl--lba-filter-table.md) | The LBA_FILTER_TABLE structure contains the LBA ranges whose access is controlled by a silo driver. |
| [LBA_FILTER_TABLE_ENTRY structure](ns-ehstorioctl--lba-filter-table-entry.md) | The LBA_FILTER_TABLE_ENTRY structure contains an individual LBA range for the LBA_FILTER_TABLE sent in an IOCTL_EHSTOR_DRIVER_UPDATE_LBA_FILTER_TABLE request. |
| [SILO_DRIVER_CAPABILITIES structure](ns-ehstorioctl--silo-driver-capabilities.md) | This structure is used to specify the capabilities and support for IOCTL redirection of a storage silo driver. SILO_DRIVER_CAPABILITIES is included in the system buffer of an IOCTL_EHSTOR_DRIVER_REPORT_CAPABILITIES request. |
| [tagACT_AUTHZ_STATE structure](ns-ehstorioctl-tagact-authz-state.md) | This structure describes the Addressable Command Target (ACT) authorization state. |
| [tagSILO_COMMAND structure](ns-ehstorioctl-tagsilo-command.md) | This structure describes a storage silo driver command. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [PDO_CAPS enumeration](ne-ehstorioctl--pdo-caps.md) | This enumeration describes the capabilities of Physical Device Objects (PDOs). |
| [PDO_STATE enumeration](ne-ehstorioctl--pdo-state.md) | This enumeration describes the states of Physical Device Objects (PDOs). |
| [PDO_TYPE enumeration](ne-ehstorioctl--pdo-type.md) | This enumeration describes the types of Physical Device Objects (PDOs). |
