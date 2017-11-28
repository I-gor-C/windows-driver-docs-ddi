# Ntdddisk.h header


This header is used by unknown technology.

Ntdddisk.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [CREATE_DISK structure](ns-ntdddisk--create-disk.md) | The CREATE_DISK structure is used with the IOCTL_DISK_CREATE_DISK IOCTL to initialize a disk with an empty partition table. The partition table styles are master boot record (MBR) or GUID partition table (GPT). |
| [CREATE_DISK_GPT structure](ns-ntdddisk--create-disk-gpt.md) | The CREATE_DISK_GPT structure is used with the IOCTL IOCTL_DISK_CREATE_DISK to initialize a disk with an empty GPT partition table. |
| [CREATE_DISK_MBR structure](ns-ntdddisk--create-disk-mbr.md) | The CREATE_DISK_MBR structure is used with the IOCTL IOCTL_DISK_CREATE_DISK to initialize a disk with an empty MBR partition table. |
| [DISK_CACHE_INFORMATION structure](ns-ntdddisk--disk-cache-information.md) | The DISK_CACHE_INFORMATION structure is used with the IOCTL_DISK_GET_CACHE_INFORMATION request to retrieve cache information. |
| [DISK_CONTROLLER_NUMBER structure](ns-ntdddisk--disk-controller-number.md) | DISK_CONTROLLER_NUMBER is used with IOCTL_DISK_CONTROLLER_NUMBER to retrieve the controller number and disk number of an IDE disk. |
| [DISK_COPY_DATA_PARAMETERS structure](ns-ntdddisk--disk-copy-data-parameters.md) | DISK_COPY_DATA_PARAMETERS is used with IOCTL_DISK_COPY_DATA to copy data from one area of the disk to another. |
| [DISK_DETECTION_INFO structure](ns-ntdddisk--disk-detection-info.md) | The DISK_DETECTION_INFO structure contains the detected drive parameters that are supplied by an x86 PC BIOS on boot. |
| [DISK_EX_INT13_INFO structure](ns-ntdddisk--disk-ex-int13-info.md) | The DISK_EX_INT13_INFO structure is used by the BIOS to report disk detection data for a partition with an extended INT13 format. |
| [DISK_GEOMETRY structure](ns-ntdddisk--disk-geometry.md) | The DISK_GEOMETRY structure is obsolete and provided only to support existing drivers. |
| [DISK_GEOMETRY_EX structure](ns-ntdddisk--disk-geometry-ex.md) | The DISK_GEOMETRY_EX structure is a variable-length structure composed of a DISK_GEOMETRY structure followed by a DISK_PARTITION_INFO structure followed, in turn, by a DISK_DETECTION_INFO structure. |
| [DISK_GROW_PARTITION structure](ns-ntdddisk--disk-grow-partition.md) | The DISK_GROW_PARTITION structure is used in conjunction with the IOCTL_DISK_GROW_PARTITION request to enlarge a partition. |
| [DISK_INT13_INFO structure](ns-ntdddisk--disk-int13-info.md) | The DISK_INT13_INFO structure is used by the BIOS to report disk detection data for a partition with an INT13 format. |
| [DISK_PARTITION_INFO structure](ns-ntdddisk--disk-partition-info.md) | The DISK_PARTITION_INFO structure is used to report information about the disk's partition table. |
| [DISK_PERFORMANCE structure](ns-ntdddisk--disk-performance.md) | The DISK_PERFORMANCE structure is used in conjunction with the IOCTL_DISK_PERFORMANCE request to collect summary disk statistics for purposes of measuring disk performance. |
| [DRIVERSTATUS structure](ns-ntdddisk--driverstatus.md) | The DRIVERSTATUS structure is used in conjunction with the SENDCMDOUTPARAMS structure and the SMART_SEND_DRIVE_COMMAND request to retrieve data returned by a Self-Monitoring Analysis and Reporting Technology (SMART) command. |
| [DRIVE_LAYOUT_INFORMATION structure](ns-ntdddisk--drive-layout-information.md) | The DRIVE_LAYOUT_INFORMATION structure is obsolete and is provided only to support existing drivers. |
| [DRIVE_LAYOUT_INFORMATION_EX structure](ns-ntdddisk--drive-layout-information-ex.md) | The DRIVE_LAYOUT_INFORMATION_EX structure is used to report information about the driver layout. |
| [DRIVE_LAYOUT_INFORMATION_GPT structure](ns-ntdddisk--drive-layout-information-gpt.md) | The DRIVE_LAYOUT_INFORMATION_GPT structure reports the drive signature for a GUID Partition Table partition. |
| [DRIVE_LAYOUT_INFORMATION_MBR structure](ns-ntdddisk--drive-layout-information-mbr.md) | The DRIVE_LAYOUT_INFORMATION_MBR structure reports the drive signature for a Master Boot Record partition. |
| [FORMAT_EX_PARAMETERS structure](ns-ntdddisk--format-ex-parameters.md) | The FORMAT_EX_PARAMETERS structure is used in conjunction with the IOCTL_DISK_FORMAT_TRACKS_EX request to format the specified set of contiguous tracks on the disk. |
| [FORMAT_PARAMETERS structure](ns-ntdddisk--format-parameters.md) | The FORMAT_PARAMETERS structure is used in conjunction with the IOCTL_DISK_FORMAT_TRACKS request to format the specified set of contiguous tracks on the disk. |
| [GETVERSIONINPARAMS structure](ns-ntdddisk--getversioninparams.md) | The GETVERSIONINPARAMS structure is used in conjunction with the SMART_GET_VERSION request to retrieve version information, a capabilities mask, and a bitmask for the indicated device. |
| [GET_LENGTH_INFORMATION structure](ns-ntdddisk--get-length-information.md) | The GET_LENGTH_INFORMATION structure is used with the IOCTL_DISK_GET_LENGTH_INFO to obtain the length, in bytes, of a disk, partition, or volume. |
| [IDEREGS structure](ns-ntdddisk--ideregs.md) | The IDEREGS structure is used to report the contents of the IDE controller registers. |
| [PARTITION_INFORMATION structure](ns-ntdddisk--partition-information.md) | The PARTITION_INFORMATION structure contains partition information for a partition with a traditional AT-style Master Boot Record (MBR). |
| [PARTITION_INFORMATION_EX structure](ns-ntdddisk--partition-information-ex.md) | PARTITION_INFORMATION_EX is the extended version of the PARTITION_INFORMATION structure. It holds information both for partitions with a Master Boot Record and for partitions with a GUID Partition Table. |
| [PARTITION_INFORMATION_GPT structure](ns-ntdddisk--partition-information-gpt.md) | PARTITION_INFORMATION_GPT contains information for a GUID Partition Table partition that is not held in common with a Master Boot Record partition. |
| [PARTITION_INFORMATION_MBR structure](ns-ntdddisk--partition-information-mbr.md) | PARTITION_INFORMATION_MBR contains information for a Master Boot Record partition that is not held in common with a GUID Partition Table partition. |
| [REASSIGN_BLOCKS structure](ns-ntdddisk--reassign-blocks.md) | The REASSIGN_BLOCKS structure is used in conjunction with the IOCTL_DISK_REASSIGN_BLOCKS request to instruct a disk device to reassign the block numbers of the indicated bad blocks to good blocks. |
| [REASSIGN_BLOCKS_EX structure](ns-ntdddisk--reassign-blocks-ex.md) | The REASSIGN_BLOCKS_EX structure is used in conjunction with the IOCTL_DISK_REASSIGN_BLOCKS_EX request to instruct a disk device to reassign the block numbers of the indicated bad blocks to good blocks. |
| [SENDCMDINPARAMS structure](ns-ntdddisk--sendcmdinparams.md) | The SENDCMDINPARAMS structure contains the input parameters for the SMART_SEND_DRIVE_COMMAND request. |
| [SENDCMDOUTPARAMS structure](ns-ntdddisk--sendcmdoutparams.md) | The SENDCMDOUTPARAMS structure is used in conjunction with the SMART_SEND_DRIVE_COMMAND request to retrieve data returned by a Self-Monitoring Analysis and Reporting Technology (SMART) command. |
| [SET_PARTITION_INFORMATION structure](ns-ntdddisk--set-partition-information.md) | SET_PARTITION_INFORMATION is used with IOCTL_DISK_SET_PARTITION_INFO to change the partition type of a specified Master Boot Record (MBR) disk partition. |
| [SET_PARTITION_INFORMATION_EX structure](ns-ntdddisk--set-partition-information-ex.md) | SET_PARTITION_INFORMATION_EX is used with the IOCTL IOCTL_DISK_SET_PARTITION_INFO_EX to set information for a specific partition. |
| [VERIFY_INFORMATION structure](ns-ntdddisk--verify-information.md) | The VERIFY_INFORMATION structure provides information used to verify the existence of a disk extent. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [DETECTION_TYPE enumeration](ne-ntdddisk--detection-type.md) | The DETECTION_TYPE enumeration type is used in conjunction with the IOCTL_DISK_GET_DRIVE_GEOMETRY_EX request and the DISK_GEOMETRY_EX structure to determine the type of formatting used by the BIOS to record the disk geometry. |
| [DISK_CACHE_RETENTION_PRIORITY enumeration](ne-ntdddisk-disk-cache-retention-priority.md) | The DISK_CACHE_RETENTION_PRIORITY enumeration is used in conjunction with the IOCTL_DISK_GET_CACHE_INFORMATION request and the structure DISK_CACHE_INFORMATION to indicate which kinds data are to be held in the cache on a preferential basis. |
