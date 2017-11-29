# Ntddcdvd.h header


This header is used by Storage. For more information, see
- [Storage](../_storage/index.md)

Ntddcdvd.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [AACS_BINDING_NONCE structure](ns-ntddcdvd--aacs-binding-nonce.md) | The AACS_BINDING_NONCE structure contains the binding nonce. |
| [AACS_CERTIFICATE structure](ns-ntddcdvd--aacs-certificate.md) | The AACS_CERTIFICATE structure contains a cryptographically random 160-bit value, followed by a 92-byte certificate. |
| [AACS_CHALLENGE_KEY structure](ns-ntddcdvd--aacs-challenge-key.md) | The AACS_CHALLENGE_KEY structure contains the challenge key that the device sends to the host. |
| [AACS_MEDIA_ID structure](ns-ntddcdvd--aacs-media-id.md) | The AACS_MEDIA_ID structure contains an Advanced Access Content System (AACS) media identifier and corresponding message authentication code (MAC). |
| [AACS_READ_BINDING_NONCE structure](ns-ntddcdvd--aacs-read-binding-nonce.md) | The AACS_READ_BINDING_NONCE structure is a wrapper for the Authentication Grant Identifier (AGID) and logical block address (LBA)/length pair that are required to read a nonce. |
| [AACS_SEND_CERTIFICATE structure](ns-ntddcdvd--aacs-send-certificate.md) | The AACS_SEND_CERTIFICATE structure is a wrapper for both an Advanced Access Content System (AACS) certificate and an Authentication Grant Identifier (AGID). |
| [AACS_SEND_CHALLENGE_KEY structure](ns-ntddcdvd--aacs-send-challenge-key.md) | The AACS_SEND_CHALLENGE_KEY structure is defined as a challenge key that host software sends to an Advanced Access Content System (AACS) device. |
| [AACS_SERIAL_NUMBER structure](ns-ntddcdvd--aacs-serial-number.md) | The AACS_SERIAL_NUMBER structure contains an Advanced Access Content System (AACS) serial number and corresponding message authentication code (MAC). |
| [AACS_VOLUME_ID structure](ns-ntddcdvd--aacs-volume-id.md) | The AACS_VOLUME_ID structure contains an Advanced Access Content System (AACS) volume ID and the corresponding message authentication code (MAC). |
| [DVD_BCA_DESCRIPTOR structure](ns-ntddcdvd--dvd-bca-descriptor.md) | The DVD_BCA_DESCRIPTOR structure is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request to retrieve a DVD burst cutting area (BCA) descriptor. |
| [DVD_COPYRIGHT_DESCRIPTOR structure](ns-ntddcdvd--dvd-copyright-descriptor.md) | The DVD_COPYRIGHT_DESCRIPTOR structure is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request to retrieve a DVD copyright descriptor. |
| [DVD_COPY_PROTECT_KEY structure](ns-ntddcdvd--dvd-copy-protect-key.md) | The DVD_COPY_PROTECT_KEY structure is used in conjunction with the IOCTL_DVD_READ_KEY request to execute a report key command of the specified type. |
| [DVD_DISK_KEY_DESCRIPTOR structure](ns-ntddcdvd--dvd-disk-key-descriptor.md) | The DVD_DISK_KEY_DESCRIPTOR structure is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request to retrieve a DVD disc key descriptor. |
| [DVD_LAYER_DESCRIPTOR structure](ns-ntddcdvd--dvd-layer-descriptor.md) | The DVD_LAYER_DESCRIPTOR structure is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request to retrieve a DVD layer descriptor. |
| [DVD_MANUFACTURER_DESCRIPTOR structure](ns-ntddcdvd--dvd-manufacturer-descriptor.md) | The DVD_MANUFACTURER_DESCRIPTOR structure is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request to retrieve a DVD manufacturer descriptor. |
| [DVD_READ_STRUCTURE structure](ns-ntddcdvd-dvd-read-structure.md) | The DVD_READ_STRUCTURE structure is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request to retrieve a DVD descriptor containing information about a DVD disc. |
| [DVD_REGION structure](ns-ntddcdvd--dvd-region.md) | The DVD_REGION structure is used in conjunction with the IOCTL_DVD_GET_REGION request to retrieve region playback control (RPC) information for a DVD device. |
| [STORAGE_SET_READ_AHEAD structure](ns-ntddcdvd--storage-set-read-ahead.md) | The STORAGE_SET_READ_AHEAD structure is used in conjunction with the IOCTL_STORAGE_SET_READ_AHEAD request to instruct the device to skip to the target address upon reaching the trigger address. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [DVD_KEY_TYPE enumeration](ne-ntddcdvd-dvd-key-type.md) | The DVD_KEY_TYPE enumeration type is used in conjunction with the DVD_COPY_PROTECT_KEY structure to indicate a key to be read, to invalidate an authentication grant ID (AGID), and to request state information or region settings. |
| [DVD_STRUCTURE_FORMAT enumeration](ne-ntddcdvd-dvd-structure-format.md) | The DVD_STRUCTURE_FORMAT enumeration type is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request and the DVD_READ_STRUCTURE structure to retrieve a DVD descriptor. |
