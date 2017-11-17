# Declarations in the ntddtape header
This header Ntddtape contains these programming interfaces:

Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_TAPE_GET_STATUS IOCTL](ni-ntddtape-ioctl-tape-get-status.md) | TBD |
| [IOCTL_TAPE_ERASE IOCTL](ni-ntddtape-ioctl-tape-erase.md) | TBD |
| [IOCTL_TAPE_PREPARE IOCTL](ni-ntddtape-ioctl-tape-prepare.md) | TBD |
| [IOCTL_TAPE_SET_MEDIA_PARAMS IOCTL](ni-ntddtape-ioctl-tape-set-media-params.md) | TBD |
| [IOCTL_TAPE_GET_MEDIA_PARAMS IOCTL](ni-ntddtape-ioctl-tape-get-media-params.md) | TBD |
| [IOCTL_TAPE_BASE IOCTL](ni-ntddtape-ioctl-tape-base.md) | TBD |
| [IOCTL_TAPE_GET_POSITION IOCTL](ni-ntddtape-ioctl-tape-get-position.md) | TBD |
| [IOCTL_TAPE_MEDIA_REMOVAL IOCTL](ni-ntddtape-ioctl-tape-media-removal.md) | TBD |
| [IOCTL_TAPE_FIND_NEW_DEVICES IOCTL](ni-ntddtape-ioctl-tape-find-new-devices.md) | TBD |
| [IOCTL_TAPE_RESERVE IOCTL](ni-ntddtape-ioctl-tape-reserve.md) | TBD |
| [IOCTL_TAPE_CHECK_VERIFY IOCTL](ni-ntddtape-ioctl-tape-check-verify.md) | TBD |
| [IOCTL_TAPE_LOAD_MEDIA IOCTL](ni-ntddtape-ioctl-tape-load-media.md) | TBD |
| [IOCTL_TAPE_EJECT_MEDIA IOCTL](ni-ntddtape-ioctl-tape-eject-media.md) | TBD |
| [IOCTL_TAPE_WRITE_MARKS IOCTL](ni-ntddtape-ioctl-tape-write-marks.md) | TBD |
| [IOCTL_TAPE_SET_POSITION IOCTL](ni-ntddtape-ioctl-tape-set-position.md) | TBD |
| [IOCTL_TAPE_SET_DRIVE_PARAMS IOCTL](ni-ntddtape-ioctl-tape-set-drive-params.md) | TBD |
| [IOCTL_TAPE_GET_DRIVE_PARAMS IOCTL](ni-ntddtape-ioctl-tape-get-drive-params.md) | TBD |
| [IOCTL_TAPE_RELEASE IOCTL](ni-ntddtape-ioctl-tape-release.md) | TBD |
| [IOCTL_TAPE_CREATE_PARTITION IOCTL](ni-ntddtape-ioctl-tape-create-partition.md) | TBD |
Struct

| Title        | Description    |
| ------------- |:-------------:|
| [TAPE_GET_MEDIA_PARAMETERS structure](ns-ntddtape--tape-get-media-parameters.md) | The TAPE_GET_MEDIA_PARAMETERS structure is used in conjunction with the TapeMiniGetMediaParameters routine to retrieve tape media parameters. |
| [TAPE_PREPARE structure](ns-ntddtape--tape-prepare.md) | The TAPE_PREPARE structure is used in conjunction with the IOCTL_TAPE_PREPARE request to load or unload tape, reset the tape's tension, lock or unlock the ejection mechanism, or format the tape. |
| [TAPE_WRITE_MARKS structure](ns-ntddtape--tape-write-marks.md) | The TAPE_WRITE_MARKS structure is used in conjunction with an IOCTL_TAPE_WRITE_MARKS request to write a setmark, a filemark, a short filemark, or a long filemark to tape. |
| [TAPE_WMI_OPERATIONS structure](ns-ntddtape--tape-wmi-operations.md) | The tape miniclass driver passes this structure to its TapeMiniWMIControl routine to indicate which WMI operation must be performed by the device. |
| [TAPE_SET_POSITION structure](ns-ntddtape--tape-set-position.md) | The TAPE_SET_POSITION structure is used in conjunction with the IOCTL_TAPE_SET_POSITION request to move the current position on the tape to the specified partition and offset. |
| [TAPE_GET_POSITION structure](ns-ntddtape--tape-get-position.md) | The TAPE_GET_POSITION structure is used in conjunction with the IOCTL_TAPE_GET_POSITION request to retrieve the current absolute, logical, or pseudological partition and offset position on the tape. |
| [TAPE_CREATE_PARTITION structure](ns-ntddtape--tape-create-partition.md) | The TAPE_CREATE_PARTITION structure is used in conjunction with the IOCTL_TAPE_CREATE_PARTITION request to create a specified number of fixed, select, or initiator partitions of a given size on the tape media. |
| [TAPE_GET_DRIVE_PARAMETERS structure](ns-ntddtape--tape-get-drive-parameters.md) | The TAPE_GET_DRIVE_PARAMETERS structure is used in conjunction with the IOCTL_TAPE_GET_DRIVE_PARAMS request to retrieve information about capabilities of the tape drive. |
| [TAPE_ERASE structure](ns-ntddtape--tape-erase.md) | The TAPE_ERASE structure is used in conjunction with the IOCTL_TAPE_ERASE request to erase the current tape partition. |
| [TAPE_SET_MEDIA_PARAMETERS structure](ns-ntddtape--tape-set-media-parameters.md) | The TAPE_SET_MEDIA_PARAMETERS structure is used in conjunction with the IOCTL_TAPE_SET_MEDIA_PARAMS request to reset the block size of the media in a tape drive. |
| [TAPE_SET_DRIVE_PARAMETERS structure](ns-ntddtape--tape-set-drive-parameters.md) | The TAPE_SET_DRIVE_PARAMETERS structure is used in conjunction with the IOCTL_TAPE_SET_DRIVE_PARAMS request to adjust the configurable parameters of a tape drive. |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [TAPE_DRIVE_PROBLEM_TYPE enumeration](ne-ntddtape--tape-drive-problem-type.md) | The TAPE_DRIVE_PROBLEM_TYPE enumerator is used to report problems with the tape drive. |

This header is used in these topics:

- [Storage](..content/_Storage)
