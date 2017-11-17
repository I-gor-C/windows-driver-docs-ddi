# Declarations in the ufs header
This header Ufs contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [PUFS_DEVICE_DESCRIPTOR structure](ns-ufs-pufs-device-descriptor.md) | UFS_DEVICE_DESCRIPTOR is the main descriptor for Universal Flash Storage (UFS) devices and should be the first descriptor retrieved as it specifies the device class and sub-class and the protocol (command set) to use to access this device and the maximum number of logical units contained within the device. |
| [PUFS_UNIT_CONFIG_DESCRIPTOR structure](ns-ufs-pufs-unit-config-descriptor.md) | The UFS_UNIT_CONFIG_DESCRIPTOR structure describes the user configurable parameters within the UFS_CONFIG_DESCRIPTOR. |
| [PUFS_DEVICE_HEALTH_DESCRIPTOR structure](ns-ufs-pufs-device-health-descriptor.md) | The UFS_DEVICE_HEALTH_DESCRIPTOR structure describes the health of a device. |
| [PUFS_INTERCONNECT_DESCRIPTOR structure](ns-ufs-pufs-interconnect-descriptor.md) | UFS_INTERCONNECT_DESCRIPTOR contains the MIPI M-PHY® specification version number and the MIPI 6338 UniPro℠ specification version number. |
| [PUFS_UNIT_DESCRIPTOR structure](ns-ufs-pufs-unit-descriptor.md) | The UFS_UNIT_DESCRIPTOR structure describes a generic unit descriptor. |
| [PUFS_CONFIG_DESCRIPTOR structure](ns-ufs-pufs-config-descriptor.md) | The UFS_CONFIG_DESCRIPTOR structure describes the modifiable values of the default device configuration set by the manufacturer. |
| [PUFS_POWER_DESCRIPTOR structure](ns-ufs-pufs-power-descriptor.md) | UFS_POWER_DESCRIPTOR contains information about the power capabilities and power states of the device. |
| [PUFS_RPMB_UNIT_DESCRIPTOR structure](ns-ufs-pufs-rpmb-unit-descriptor.md) | The UFS_RPMB_UNIT_DESCRIPTOR structure describes the contents of a Replay Protected Memory Block (RBMB) Unit. |
| [UFS_STRING_DESCRIPTOR structure](ns-ufs--ufs-string-descriptor.md) | The UFS_STRING_DESCRIPTOR structure describes either the Manufacturer Name, Product Name, OEM ID, or Serial Number as a string. |
| [PUFS_GEOMETRY_DESCRIPTOR structure](ns-ufs-pufs-geometry-descriptor.md) | UFS_GEOMETRY_DESCRIPTOR describes a device's geometric parameters. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [UFS_PURGE_STATUS enumeration](ne-ufs-ufs-purge-status.md) | Specifies the current status of a purge operation. |
| [UFS_ATTRIBUTES_DESCRIPTOR enumeration](ne-ufs-ufs-attributes-descriptor.md) | UFS_ATTRIBUTES_DESCRIPTOR describes the different types of attributes used by Universal Flash Storage (UFS) descriptors. |
| [UFS_FLAGS_DESCRIPTOR enumeration](ne-ufs-ufs-flags-descriptor.md) | UFS_FLAGS_DESCRIPTOR describes the different types of flags used by Universal Flash Storage (UFS) descriptors. |

This header is used in these topics:

- [Storage](..content/_Storage)
