# Ntddscsi.h header


This header is used by Storage. For more information, see
- [Storage](../_storage/index.md)

Ntddscsi.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [ATA_PASS_THROUGH_DIRECT structure](ns-ntddscsi--ata-pass-through-direct.md) | The ATA_PASS_THROUGH_DIRECT structure is used in conjunction with an IOCTL_ATA_PASS_THROUGH_DIRECT request to instruct the port driver to send an embedded ATA command to the target device. |
| [ATA_PASS_THROUGH_EX structure](ns-ntddscsi--ata-pass-through-ex.md) | The ATA_PASS_THROUGH_EX structure is used in conjunction with an IOCTL_ATA_PASS_THROUGH request to instruct the port driver to send an embedded ATA command to the target device. |
| [HYBRID_INFORMATION structure](ns-ntddscsi--hybrid-information.md) | The HYBRID_INFORMATION structure contains hybrid disk capability information. |
| [IO_SCSI_CAPABILITIES structure](ns-ntddscsi--io-scsi-capabilities.md) | The IO_SCSI_CAPABILITIES structure is used in conjunction with the IOCTL_SCSI_GET_CAPABILITIES request to retrieve the capabilities and limitations of the underlying SCSI host adapter.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models. |
| [MPIO_PASS_THROUGH_PATH structure](ns-ntddscsi--mpio-pass-through-path.md) | The MPIO_PASS_THROUGH_PATH structure is used together with an IOCTL_MPIO_PASS_THROUGH_PATH request to instruct the port driver to send an embedded SCSI command to the target device. |
| [MPIO_PASS_THROUGH_PATH_DIRECT structure](ns-ntddscsi--mpio-pass-through-path-direct.md) | The MPIO_PASS_THROUGH_PATH_DIRECT structure is used together with an IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT request to instruct the port driver to send an embedded SCSI command to the target device. |
| [MPIO_PASS_THROUGH_PATH_DIRECT_EX structure](ns-ntddscsi--mpio-pass-through-path-direct-ex.md) | The MPIO_PASS_THROUGH_PATH_DIRECT_EX structure is used together with an IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX request to instruct the port driver to send an embedded SCSI command to the target device. |
| [MPIO_PASS_THROUGH_PATH_EX structure](ns-ntddscsi--mpio-pass-through-path-ex.md) | The MPIO_PASS_THROUGH_PATH_EX structure is used together with an IOCTL_MPIO_PASS_THROUGH_PATH_EX request to instruct the port driver to send an embedded SCSI command to the target device. |
| [NVCACHE_REQUEST_BLOCK structure](ns-ntddscsi--nvcache-request-block.md) | The NVCACHE_REQUEST_BLOCK structure is used in conjunction with the IOCTL_SCSI_MINIPORT request to manage hybrid-hard disk drive (H-HDD) devices (for example, Microsoft ReadyDrive technology). |
| [NV_FEATURE_PARAMETER structure](ns-ntddscsi--nv-feature-parameter.md) | The NV_FEATURE_PARAMETER structure is used in conjunction with the IOCTL_SCSI_MINIPORT_NVCACHE request to get NV Cache Manager feature support information from the device. |
| [SCSI_ADAPTER_BUS_INFO structure](ns-ntddscsi--scsi-adapter-bus-info.md) | The SCSI_ADAPTER_BUS_INFO structure is used in conjunction with the IOCTL_SCSI_GET_INQUIRY_DATA request to retrieve the SCSI inquiry data for all devices on a given SCSI bus. |
| [SCSI_ADDRESS structure](ns-ntddscsi--scsi-address.md) | The SCSI_ADDRESS structure is used in conjunction with the IOCTL_SCSI_GET_ADDRESS request to retrieve the address information, such as the target ID (TID) and the logical unit number (LUN) of a particular SCSI target. |
| [SCSI_BUS_DATA structure](ns-ntddscsi--scsi-bus-data.md) | The SCSI_BUS_DATA structure is used in conjunction with the IOCTL_SCSI_GET_INQUIRY_DATA request and the SCSI_ADAPTER_BUS_INFO structure to retrieve the SCSI inquiry data for all devices on a given SCSI bus. |
| [SCSI_INQUIRY_DATA structure](ns-ntddscsi--scsi-inquiry-data.md) | The SCSI_INQUIRY_DATA structure is used in conjunction with the IOCTL_SCSI_GET_INQUIRY_DATA request to retrieve the SCSI inquiry data for all devices on a given SCSI bus. |
| [SCSI_PASS_THROUGH structure](ns-ntddscsi--scsi-pass-through.md) | The SCSI_PASS_THROUGH structure is used in conjunction with an IOCTL_SCSI_PASS_THROUGH request to instruct the port driver to send an embedded SCSI command to the target device. |
| [SCSI_PASS_THROUGH_DIRECT structure](ns-ntddscsi--scsi-pass-through-direct.md) | The SCSI_PASS_THROUGH_DIRECT structure is used in conjunction with an IOCTL_SCSI_PASS_THROUGH_DIRECT request to instruct the port driver to send an embedded SCSI command to the target device. |
| [SCSI_PASS_THROUGH_DIRECT_EX structure](ns-ntddscsi--scsi-pass-through-direct-ex.md) | The SCSI_PASS_THROUGH_DIRECT_EX structure is used in conjunction with an IOCTL_SCSI_PASS_THROUGH_DIRECT_EX request to instruct the port driver to send an embedded SCSI command to the target device. |
| [SCSI_PASS_THROUGH_EX structure](ns-ntddscsi--scsi-pass-through-ex.md) | The SCSI_PASS_THROUGH_EX structure is used in conjunction with an IOCTL_SCSI_PASS_THROUGH_EX request to instruct the port driver to send an embedded SCSI command to the target device. |
| [SRB_IO_CONTROL structure](ns-ntddscsi--srb-io-control.md) | SRB_IO_CONTROL structure |
| [STORAGE_DIAGNOSTIC_MP_REQUEST structure](ns-ntddscsi--storage-diagnostic-mp-request.md) | Describes a diagnostic request to Miniport. The STORAGE_DIAGNOSTIC_MP_REQUEST structure is provided in the input/output buffer of an IOCTL_SCSI_MINIPORT_DIAGNOSTIC request. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [MP_STORAGE_DIAGNOSTIC_LEVEL enumeration](ne-ntddscsi--mp-storage-diagnostic-level.md) | The MP_STORAGE_DIAGNOSTIC_LEVEL enumeration allows the caller to control what kinds of data the provider should return. |
| [MP_STORAGE_DIAGNOSTIC_TARGET_TYPE enumeration](ne-ntddscsi--mp-storage-diagnostic-target-type.md) | The MP_STORAGE_DIAGNOSTIC_TARGET_TYPE enumeration specifies the target type of a storage diagnostic. |
