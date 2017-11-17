# Declarations in the ntddcdvd header
This header Ntddcdvd contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [BD_PAC_HEADER structure](ns-ntddcdvd--bd-pac-header.md) | TBD |
| [DVD_DUAL_LAYER_RECORDING_INFORMATION structure](ns-ntddcdvd--dvd-dual-layer-recording-information.md) | TBD |
| [AACS_CERTIFICATE structure](ns-ntddcdvd--aacs-certificate.md) | The AACS_CERTIFICATE structure contains a cryptographically random 160-bit value, followed by a 92-byte certificate. |
| [DVD_RECORDING_MANAGEMENT_AREA_DATA structure](ns-ntddcdvd--dvd-recording-management-area-data.md) | TBD |
| [AACS_BINDING_NONCE structure](ns-ntddcdvd--aacs-binding-nonce.md) | The AACS_BINDING_NONCE structure contains the binding nonce. |
| [DVD_DUAL_LAYER_REMAPPING_INFORMATION structure](ns-ntddcdvd--dvd-dual-layer-remapping-information.md) | TBD |
| [DVD_UNIQUE_DISC_IDENTIFIER structure](ns-ntddcdvd--dvd-unique-disc-identifier.md) | TBD |
| [DVD_LIST_OF_RECOGNIZED_FORMAT_LAYERS structure](ns-ntddcdvd--dvd-list-of-recognized-format-layers.md) | TBD |
| [DVD_BD_SPARE_AREA_INFORMATION structure](ns-ntddcdvd--dvd-bd-spare-area-information.md) | TBD |
| [AACS_READ_BINDING_NONCE structure](ns-ntddcdvd--aacs-read-binding-nonce.md) | The AACS_READ_BINDING_NONCE structure is a wrapper for the Authentication Grant Identifier (AGID) and logical block address (LBA)/length pair that are required to read a nonce. |
| [DVD_DISC_CONTROL_BLOCK_LIST_DCB structure](ns-ntddcdvd--dvd-disc-control-block-list-dcb.md) | TBD |
| [DVD_DESCRIPTOR_HEADER structure](ns-ntddcdvd--dvd-descriptor-header.md) | TBD |
| [DVD_RPC_KEY structure](ns-ntddcdvd--dvd-rpc-key.md) | TBD |
| [DVD_SET_RPC_KEY structure](ns-ntddcdvd--dvd-set-rpc-key.md) | TBD |
| [BD_DISC_WRITE_PROTECT_PAC structure](ns-ntddcdvd--bd-disc-write-protect-pac.md) | TBD |
| [DVD_DISC_CONTROL_BLOCK_HEADER structure](ns-ntddcdvd--dvd-disc-control-block-header.md) | TBD |
| [DVD_COPYRIGHT_DESCRIPTOR structure](ns-ntddcdvd--dvd-copyright-descriptor.md) | The DVD_COPYRIGHT_DESCRIPTOR structure is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request to retrieve a DVD copyright descriptor. |
| [DVD_REGION structure](ns-ntddcdvd--dvd-region.md) | The DVD_REGION structure is used in conjunction with the IOCTL_DVD_GET_REGION request to retrieve region playback control (RPC) information for a DVD device. |
| [DVD_DISC_CONTROL_BLOCK_WRITE_INHIBIT structure](ns-ntddcdvd--dvd-disc-control-block-write-inhibit.md) | TBD |
| [DVD_COPYRIGHT_MANAGEMENT_DESCRIPTOR structure](ns-ntddcdvd--dvd-copyright-management-descriptor.md) | TBD |
| [HD_DVD_R_MEDIUM_STATUS structure](ns-ntddcdvd--hd-dvd-r-medium-status.md) | TBD |
| [DVD_LAYER_DESCRIPTOR structure](ns-ntddcdvd--dvd-layer-descriptor.md) | The DVD_LAYER_DESCRIPTOR structure is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request to retrieve a DVD layer descriptor. |
| [DVD_COPY_PROTECT_KEY structure](ns-ntddcdvd--dvd-copy-protect-key.md) | The DVD_COPY_PROTECT_KEY structure is used in conjunction with the IOCTL_DVD_READ_KEY request to execute a report key command of the specified type. |
| [AACS_CHALLENGE_KEY structure](ns-ntddcdvd--aacs-challenge-key.md) | The AACS_CHALLENGE_KEY structure contains the challenge key that the device sends to the host. |
| [DVD_STRUCTURE_LIST_ENTRY structure](ns-ntddcdvd--dvd-structure-list-entry.md) | TBD |
| [DVD_ASF structure](ns-ntddcdvd--dvd-asf.md) | TBD |
| [AACS_SERIAL_NUMBER structure](ns-ntddcdvd--aacs-serial-number.md) | The AACS_SERIAL_NUMBER structure contains an Advanced Access Content System (AACS) serial number and corresponding message authentication code (MAC). |
| [DVD_MANUFACTURER_DESCRIPTOR structure](ns-ntddcdvd--dvd-manufacturer-descriptor.md) | The DVD_MANUFACTURER_DESCRIPTOR structure is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request to retrieve a DVD manufacturer descriptor. |
| [DVD_DUAL_LAYER_MIDDLE_ZONE_START_ADDRESS structure](ns-ntddcdvd--dvd-dual-layer-middle-zone-start-address.md) | TBD |
| [DVD_DUAL_LAYER_MANUAL_LAYER_JUMP structure](ns-ntddcdvd--dvd-dual-layer-manual-layer-jump.md) | TBD |
| [DVD_DISK_KEY_DESCRIPTOR structure](ns-ntddcdvd--dvd-disk-key-descriptor.md) | The DVD_DISK_KEY_DESCRIPTOR structure is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request to retrieve a DVD disc key descriptor. |
| [AACS_SEND_CERTIFICATE structure](ns-ntddcdvd--aacs-send-certificate.md) | The AACS_SEND_CERTIFICATE structure is a wrapper for both an Advanced Access Content System (AACS) certificate and an Authentication Grant Identifier (AGID). |
| [DVD_WRITE_PROTECTION_STATUS structure](ns-ntddcdvd--dvd-write-protection-status.md) | TBD |
| [DVD_RAM_RECORDING_TYPE structure](ns-ntddcdvd--dvd-ram-recording-type.md) | TBD |
| [DVD_DUAL_LAYER_JUMP_INTERVAL_SIZE structure](ns-ntddcdvd--dvd-dual-layer-jump-interval-size.md) | TBD |
| [AACS_SEND_CHALLENGE_KEY structure](ns-ntddcdvd--aacs-send-challenge-key.md) | The AACS_SEND_CHALLENGE_KEY structure is defined as a challenge key that host software sends to an Advanced Access Content System (AACS) device. |
| [DVD_DISC_CONTROL_BLOCK_SESSION structure](ns-ntddcdvd--dvd-disc-control-block-session.md) | TBD |
| [DVD_RAM_MEDIUM_STATUS structure](ns-ntddcdvd--dvd-ram-medium-status.md) | TBD |
| [DVD_FULL_LAYER_DESCRIPTOR structure](ns-ntddcdvd--dvd-full-layer-descriptor.md) | TBD |
| [STORAGE_SET_READ_AHEAD structure](ns-ntddcdvd--storage-set-read-ahead.md) | The STORAGE_SET_READ_AHEAD structure is used in conjunction with the IOCTL_STORAGE_SET_READ_AHEAD request to instruct the device to skip to the target address upon reaching the trigger address. |
| [DVD_DISC_CONTROL_BLOCK_LIST structure](ns-ntddcdvd--dvd-disc-control-block-list.md) | TBD |
| [AACS_MEDIA_ID structure](ns-ntddcdvd--aacs-media-id.md) | The AACS_MEDIA_ID structure contains an Advanced Access Content System (AACS) media identifier and corresponding message authentication code (MAC). |
| [DVD_READ_STRUCTURE structure](ns-ntddcdvd-dvd-read-structure.md) | The DVD_READ_STRUCTURE structure is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request to retrieve a DVD descriptor containing information about a DVD disc. |
| [DVD_BCA_DESCRIPTOR structure](ns-ntddcdvd--dvd-bca-descriptor.md) | The DVD_BCA_DESCRIPTOR structure is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request to retrieve a DVD burst cutting area (BCA) descriptor. |
| [DVD_PRERECORDED_INFORMATION structure](ns-ntddcdvd--dvd-prerecorded-information.md) | TBD |
| [DVD_RAM_SPARE_AREA_INFORMATION structure](ns-ntddcdvd--dvd-ram-spare-area-information.md) | TBD |
| [DVD_DISC_CONTROL_BLOCK_SESSION_ITEM structure](ns-ntddcdvd--dvd-disc-control-block-session-item.md) | TBD |
| [AACS_VOLUME_ID structure](ns-ntddcdvd--aacs-volume-id.md) | The AACS_VOLUME_ID structure contains an Advanced Access Content System (AACS) volume ID and the corresponding message authentication code (MAC). |
| [DVD_LIST_OF_RECOGNIZED_FORMAT_LAYERS_TYPE_CODE structure](ns-ntddcdvd--dvd-list-of-recognized-format-layers-type-code.md) | TBD |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_AACS_READ_MEDIA_KEY_BLOCK_SIZE IOCTL](ni-ntddcdvd-ioctl-aacs-read-media-key-block-size.md) | TBD |
| [IOCTL_DVD_GET_REGION IOCTL](ni-ntddcdvd-ioctl-dvd-get-region.md) | TBD |
| [IOCTL_AACS_READ_MEDIA_ID IOCTL](ni-ntddcdvd-ioctl-aacs-read-media-id.md) | TBD |
| [IOCTL_AACS_GENERATE_BINDING_NONCE IOCTL](ni-ntddcdvd-ioctl-aacs-generate-binding-nonce.md) | TBD |
| [IOCTL_DVD_SEND_KEY2 IOCTL](ni-ntddcdvd-ioctl-dvd-send-key2.md) | TBD |
| [IOCTL_AACS_READ_BINDING_NONCE IOCTL](ni-ntddcdvd-ioctl-aacs-read-binding-nonce.md) | TBD |
| [IOCTL_DVD_READ_KEY IOCTL](ni-ntddcdvd-ioctl-dvd-read-key.md) | TBD |
| [IOCTL_AACS_READ_VOLUME_ID IOCTL](ni-ntddcdvd-ioctl-aacs-read-volume-id.md) | TBD |
| [IOCTL_DVD_BASE IOCTL](ni-ntddcdvd-ioctl-dvd-base.md) | TBD |
| [IOCTL_DVD_SET_READ_AHEAD IOCTL](ni-ntddcdvd-ioctl-dvd-set-read-ahead.md) | TBD |
| [IOCTL_AACS_READ_MEDIA_KEY_BLOCK IOCTL](ni-ntddcdvd-ioctl-aacs-read-media-key-block.md) | TBD |
| [IOCTL_DVD_SEND_KEY IOCTL](ni-ntddcdvd-ioctl-dvd-send-key.md) | TBD |
| [IOCTL_DVD_START_SESSION IOCTL](ni-ntddcdvd-ioctl-dvd-start-session.md) | TBD |
| [IOCTL_DVD_READ_STRUCTURE IOCTL](ni-ntddcdvd-ioctl-dvd-read-structure.md) | TBD |
| [IOCTL_AACS_SEND_CHALLENGE_KEY IOCTL](ni-ntddcdvd-ioctl-aacs-send-challenge-key.md) | TBD |
| [IOCTL_AACS_READ_SERIAL_NUMBER IOCTL](ni-ntddcdvd-ioctl-aacs-read-serial-number.md) | TBD |
| [IOCTL_AACS_END_SESSION IOCTL](ni-ntddcdvd-ioctl-aacs-end-session.md) | TBD |
| [IOCTL_STORAGE_SET_READ_AHEAD IOCTL](ni-ntddcdvd-ioctl-storage-set-read-ahead.md) | TBD |
| [IOCTL_AACS_SEND_CERTIFICATE IOCTL](ni-ntddcdvd-ioctl-aacs-send-certificate.md) | TBD |
| [IOCTL_AACS_START_SESSION IOCTL](ni-ntddcdvd-ioctl-aacs-start-session.md) | TBD |
| [IOCTL_DVD_END_SESSION IOCTL](ni-ntddcdvd-ioctl-dvd-end-session.md) | TBD |
| [IOCTL_AACS_GET_CERTIFICATE IOCTL](ni-ntddcdvd-ioctl-aacs-get-certificate.md) | TBD |
| [IOCTL_AACS_GET_CHALLENGE_KEY IOCTL](ni-ntddcdvd-ioctl-aacs-get-challenge-key.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [DVD_STRUCTURE_FORMAT enumeration](ne-ntddcdvd-dvd-structure-format.md) | The DVD_STRUCTURE_FORMAT enumeration type is used in conjunction with the IOCTL_DVD_READ_STRUCTURE request and the DVD_READ_STRUCTURE structure to retrieve a DVD descriptor. |
| [DVD_KEY_TYPE enumeration](ne-ntddcdvd-dvd-key-type.md) | The DVD_KEY_TYPE enumeration type is used in conjunction with the DVD_COPY_PROTECT_KEY structure to indicate a key to be read, to invalidate an authentication grant ID (AGID), and to request state information or region settings. |
| [DISC_CONTROL_BLOCK_TYPE enumeration](ne-ntddcdvd--disc-control-block-type.md) | TBD |

This header is used in these topics:

- [Storage](..content/_Storage)
