# Ntddtape.h header


This header is used by Storage. For more information, see
- [Storage](../_storage/index.md)

Ntddtape.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [TAPE_CREATE_PARTITION structure](ns-ntddtape--tape-create-partition.md) | The TAPE_CREATE_PARTITION structure is used in conjunction with the IOCTL_TAPE_CREATE_PARTITION request to create a specified number of fixed, select, or initiator partitions of a given size on the tape media. |
| [TAPE_ERASE structure](ns-ntddtape--tape-erase.md) | The TAPE_ERASE structure is used in conjunction with the IOCTL_TAPE_ERASE request to erase the current tape partition. |
| [TAPE_GET_DRIVE_PARAMETERS structure](ns-ntddtape--tape-get-drive-parameters.md) | The TAPE_GET_DRIVE_PARAMETERS structure is used in conjunction with the IOCTL_TAPE_GET_DRIVE_PARAMS request to retrieve information about capabilities of the tape drive. |
| [TAPE_GET_MEDIA_PARAMETERS structure](ns-ntddtape--tape-get-media-parameters.md) | The TAPE_GET_MEDIA_PARAMETERS structure is used in conjunction with the TapeMiniGetMediaParameters routine to retrieve tape media parameters. |
| [TAPE_GET_POSITION structure](ns-ntddtape--tape-get-position.md) | The TAPE_GET_POSITION structure is used in conjunction with the IOCTL_TAPE_GET_POSITION request to retrieve the current absolute, logical, or pseudological partition and offset position on the tape. |
| [TAPE_PREPARE structure](ns-ntddtape--tape-prepare.md) | The TAPE_PREPARE structure is used in conjunction with the IOCTL_TAPE_PREPARE request to load or unload tape, reset the tape's tension, lock or unlock the ejection mechanism, or format the tape. |
| [TAPE_SET_DRIVE_PARAMETERS structure](ns-ntddtape--tape-set-drive-parameters.md) | The TAPE_SET_DRIVE_PARAMETERS structure is used in conjunction with the IOCTL_TAPE_SET_DRIVE_PARAMS request to adjust the configurable parameters of a tape drive. |
| [TAPE_SET_MEDIA_PARAMETERS structure](ns-ntddtape--tape-set-media-parameters.md) | The TAPE_SET_MEDIA_PARAMETERS structure is used in conjunction with the IOCTL_TAPE_SET_MEDIA_PARAMS request to reset the block size of the media in a tape drive. |
| [TAPE_SET_POSITION structure](ns-ntddtape--tape-set-position.md) | The TAPE_SET_POSITION structure is used in conjunction with the IOCTL_TAPE_SET_POSITION request to move the current position on the tape to the specified partition and offset. |
| [TAPE_WMI_OPERATIONS structure](ns-ntddtape--tape-wmi-operations.md) | The tape miniclass driver passes this structure to its TapeMiniWMIControl routine to indicate which WMI operation must be performed by the device. |
| [TAPE_WRITE_MARKS structure](ns-ntddtape--tape-write-marks.md) | The TAPE_WRITE_MARKS structure is used in conjunction with an IOCTL_TAPE_WRITE_MARKS request to write a setmark, a filemark, a short filemark, or a long filemark to tape. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [TAPE_DRIVE_PROBLEM_TYPE enumeration](ne-ntddtape--tape-drive-problem-type.md) | The TAPE_DRIVE_PROBLEM_TYPE enumerator is used to report problems with the tape drive. |
