# Ntddvol.h header


This header is used by Storage. For more information, see
- [Storage](../_storage/index.md)

Ntddvol.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [DISK_EXTENT structure](ns-ntddvol--disk-extent.md) | The DISK_EXTENT structure contains information defining the location and length of a volume extent on a disk. |
| [VOLUME_DISK_EXTENTS structure](ns-ntddvol--volume-disk-extents.md) | The VOLUME_DISK_EXTENTS structure is used in conjunction with the IOCTL_VOLUME_GET_VOLUME_DISK_EXTENTS request to retrieve information about all the extents on a given volume. |
| [VOLUME_LOGICAL_OFFSET structure](ns-ntddvol--volume-logical-offset.md) | The VOLUME_LOGICAL_OFFSET structure contains a logical offset into a volume. |
| [VOLUME_PHYSICAL_OFFSET structure](ns-ntddvol--volume-physical-offset.md) | The VOLUME_PHYSICAL_OFFSET structure contains a physical offset into a volume and its accompanying physical disk number and is used with IOCTL_VOLUME_PHYSICAL_TO_LOGICAL and IOCTL_VOLUME_LOGICAL_TO_PHYSICAL to request a logical offset equivalent of a physical offset or a physical offset equivalent of a logical offset, respectively. |
| [VOLUME_PHYSICAL_OFFSETS structure](ns-ntddvol--volume-physical-offsets.md) | The VOLUME_PHYSICAL_OFFSETS structure contains an array of physical offsets and accompanying physical disk numbers and is used with IOCTL_VOLUME_LOGICAL_TO_PHYSICAL to request a series of pairs of physical offsets and disk numbers that correspond to a single logical offset. |
| [VOLUME_READ_PLEX_INPUT structure](ns-ntddvol--volume-read-plex-input.md) | This structure is used in conjunction with IOCTL_VOLUME_READ_PLEX to read data from a specific plex in a volume. |
