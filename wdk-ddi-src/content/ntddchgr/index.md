# Ntddchgr.h header


This header is used by Storage. For more information, see
- [Storage](../_storage/index.md)

Ntddchgr.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [CHANGER_ELEMENT structure](ns-ntddchgr--changer-element.md) | The CHANGER_ELEMENT structure contains a description of a changer element. |
| [CHANGER_ELEMENT_LIST structure](ns-ntddchgr--changer-element-list.md) | The CHANGER_ELEMENT_LIST structure indicates a range of elements of a single type. |
| [CHANGER_ELEMENT_STATUS structure](ns-ntddchgr--changer-element-status.md) | The ChangerGetElementStatus routine returns status information in this structure. |
| [CHANGER_ELEMENT_STATUS_EX structure](ns-ntddchgr--changer-element-status-ex.md) | The ChangerGetElementStatus routine returns status information in this structure. |
| [CHANGER_EXCHANGE_MEDIUM structure](ns-ntddchgr--changer-exchange-medium.md) | The CHANGER_EXCHANGE_MEDIUM structure is used with the IOCTL_CHANGER_EXCHANGE_MEDIUM request to exchange locations of two pieces of media. |
| [CHANGER_INITIALIZE_ELEMENT_STATUS structure](ns-ntddchgr--changer-initialize-element-status.md) | The CHANGER_INITIALIZE_ELEMENT_STATUS structure is used in conjunction with the IOCTL_CHANGER_INITIALIZE_ELEMENT_STATUS request to initialize the status of all elements or of a specified number of elements of a particular type. |
| [CHANGER_MOVE_MEDIUM structure](ns-ntddchgr--changer-move-medium.md) | The CHANGER_MOVE_MEDIUM structure is used in conjunction with the IOCTL_CHANGER_MOVE_MEDIUM request to move a piece of media from a source element to a destination. |
| [CHANGER_PRODUCT_DATA structure](ns-ntddchgr--changer-product-data.md) | The CHANGER_PRODUCT_DATA structure is used in conjunction with the IOCTL_CHANGER_GET_PRODUCT_DATA request to retrieve product data for a device. |
| [CHANGER_READ_ELEMENT_STATUS structure](ns-ntddchgr--changer-read-element-status.md) | The CHANGER_READ_ELEMENT_STATUS structure is used in conjunction with the IOCTL_CHANGER_GET_ELEMENT_STATUS request to retrieve the status of all elements or the status of a specified number of elements of a particular type. |
| [CHANGER_SEND_VOLUME_TAG_INFORMATION structure](ns-ntddchgr--changer-send-volume-tag-information.md) | This structure is passed to the ChangerQueryVolumeTags routine and is used to specify a search criterion for retrieving changer elements. |
| [CHANGER_SET_ACCESS structure](ns-ntddchgr--changer-set-access.md) | The CHANGER_SET_ACCESS structure is used in conjunction with theIOCTL_CHANGER_SET_ACCESS request to set the state of the device's import/export port (IEport), door, or keypad. |
| [CHANGER_SET_POSITION structure](ns-ntddchgr--changer-set-position.md) | The CHANGER_SET_POSITION structure is used in conjunction with theIOCTL_CHANGER_SET_POSITION request to set the changer's robotic transport mechanism to the specified element address. |
| [GET_CHANGER_PARAMETERS structure](ns-ntddchgr--get-changer-parameters.md) | Retrieves the characteristics of the changer. |
| [READ_ELEMENT_ADDRESS_INFO structure](ns-ntddchgr--read-element-address-info.md) | This structure is to retrieve changer elements based on a search criterion specified in a call to the ChangerQueryVolumeTags routine. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [CHANGER_DEVICE_PROBLEM_TYPE enumeration](ne-ntddchgr--changer-device-problem-type.md) | The CHANGER_DEVICE_PROBLEM_TYPE data type contains the values returned by the ChangerPerformDiagnostics routine. |
| [ELEMENT_TYPE enumeration](ne-ntddchgr--element-type.md) | The ELEMENT_TYPE enumeration provides a list of changer element types defined by the SCSI-3 specification. |
