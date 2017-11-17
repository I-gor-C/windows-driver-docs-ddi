# Declarations in the ntddscsi header
This header Ntddscsi contains these programming interfaces:

Struct

| Title        | Description    |
| ------------- |:-------------:|
| [STORAGE_FIRMWARE_ACTIVATE structure](ns-ntddscsi--storage-firmware-activate.md) | TBD |
| [FIRMWARE_REQUEST_BLOCK structure](ns-ntddscsi--firmware-request-block.md) | TBD |
| [STORAGE_DIAGNOSTIC_MP_REQUEST structure](ns-ntddscsi--storage-diagnostic-mp-request.md) | Describes a diagnostic request to Miniport. The STORAGE_DIAGNOSTIC_MP_REQUEST structure is provided in the input/output buffer of an IOCTL_SCSI_MINIPORT_DIAGNOSTIC request. |
| [NVCACHE_HINT_PAYLOAD structure](ns-ntddscsi--nvcache-hint-payload.md) | TBD |
| [STORAGE_FIRMWARE_INFO_V2 structure](ns-ntddscsi--storage-firmware-info-v2.md) | TBD |
| [HYBRID_DEMOTE_BY_SIZE structure](ns-ntddscsi--hybrid-demote-by-size.md) | TBD |
| [MPIO_PASS_THROUGH_PATH32_EX structure](ns-ntddscsi--mpio-pass-through-path32-ex.md) | TBD |
| [SCSI_PASS_THROUGH_DIRECT32 structure](ns-ntddscsi--scsi-pass-through-direct32.md) | TBD |
| [ADAPTER_OBJECT structure](ns-ntddscsi--adapter-object.md) | TBD |
| [DUMP_POINTERS_VERSION structure](ns-ntddscsi--dump-pointers-version.md) | TBD |
| [SCSI_PASS_THROUGH32_EX structure](ns-ntddscsi--scsi-pass-through32-ex.md) | TBD |
| [SCSI_ADDRESS structure](ns-ntddscsi--scsi-address.md) | The SCSI_ADDRESS structure is used in conjunction with the IOCTL_SCSI_GET_ADDRESS request to retrieve the address information, such as the target ID (TID) and the logical unit number (LUN) of a particular SCSI target. |
| [MPIO_PASS_THROUGH_PATH_DIRECT structure](ns-ntddscsi--mpio-pass-through-path-direct.md) | The MPIO_PASS_THROUGH_PATH_DIRECT structure is used together with an IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT request to instruct the port driver to send an embedded SCSI command to the target device. |
| [STORAGE_FIRMWARE_DOWNLOAD structure](ns-ntddscsi--storage-firmware-download.md) | TBD |
| [SCSI_PASS_THROUGH_DIRECT_EX structure](ns-ntddscsi--scsi-pass-through-direct-ex.md) | The SCSI_PASS_THROUGH_DIRECT_EX structure is used in conjunction with an IOCTL_SCSI_PASS_THROUGH_DIRECT_EX request to instruct the port driver to send an embedded SCSI command to the target device. |
| [SCSI_PASS_THROUGH_DIRECT structure](ns-ntddscsi--scsi-pass-through-direct.md) | The SCSI_PASS_THROUGH_DIRECT structure is used in conjunction with an IOCTL_SCSI_PASS_THROUGH_DIRECT request to instruct the port driver to send an embedded SCSI command to the target device. |
| [MPIO_PASS_THROUGH_PATH_EX structure](ns-ntddscsi--mpio-pass-through-path-ex.md) | The MPIO_PASS_THROUGH_PATH_EX structure is used together with an IOCTL_MPIO_PASS_THROUGH_PATH_EX request to instruct the port driver to send an embedded SCSI command to the target device. |
| [NVCACHE_PRIORITY_LEVEL_DESCRIPTOR structure](ns-ntddscsi--nvcache-priority-level-descriptor.md) | TBD |
| [STORAGE_FIRMWARE_SLOT_INFO_V2 structure](ns-ntddscsi--storage-firmware-slot-info-v2.md) | TBD |
| [IDE_IO_CONTROL structure](ns-ntddscsi--ide-io-control.md) | TBD |
| [HYBRID_DIRTY_THRESHOLDS structure](ns-ntddscsi--hybrid-dirty-thresholds.md) | TBD |
| [ATA_PASS_THROUGH_EX structure](ns-ntddscsi--ata-pass-through-ex.md) | The ATA_PASS_THROUGH_EX structure is used in conjunction with an IOCTL_ATA_PASS_THROUGH request to instruct the port driver to send an embedded ATA command to the target device. |
| [SCSI_PASS_THROUGH_DIRECT32_EX structure](ns-ntddscsi--scsi-pass-through-direct32-ex.md) | TBD |
| [SRB_IO_CONTROL structure](ns-ntddscsi--srb-io-control.md) | SRB_IO_CONTROL structure |
| [MPIO_PASS_THROUGH_PATH_DIRECT_EX structure](ns-ntddscsi--mpio-pass-through-path-direct-ex.md) | The MPIO_PASS_THROUGH_PATH_DIRECT_EX structure is used together with an IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX request to instruct the port driver to send an embedded SCSI command to the target device. |
| [ATA_PASS_THROUGH_DIRECT32 structure](ns-ntddscsi--ata-pass-through-direct32.md) | TBD |
| [MPIO_PASS_THROUGH_PATH32 structure](ns-ntddscsi--mpio-pass-through-path32.md) | TBD |
| [MP_DEVICE_DATA_SET_RANGE structure](ns-ntddscsi--mp-device-data-set-range.md) | TBD |
| [DSM_NOTIFICATION_REQUEST_BLOCK structure](ns-ntddscsi--dsm-notification-request-block.md) | TBD |
| [SCSI_INQUIRY_DATA structure](ns-ntddscsi--scsi-inquiry-data.md) | The SCSI_INQUIRY_DATA structure is used in conjunction with the IOCTL_SCSI_GET_INQUIRY_DATA request to retrieve the SCSI inquiry data for all devices on a given SCSI bus. |
| [HYBRID_INFORMATION structure](ns-ntddscsi--hybrid-information.md) | The HYBRID_INFORMATION structure contains hybrid disk capability information. |
| [IO_SCSI_CAPABILITIES structure](ns-ntddscsi--io-scsi-capabilities.md) | The IO_SCSI_CAPABILITIES structure is used in conjunction with the IOCTL_SCSI_GET_CAPABILITIES request to retrieve the capabilities and limitations of the underlying SCSI host adapter.Note  The SCSI port driver and SCSI miniport driver models may be altered or unavailable in the future. Instead, we recommend using the Storport driver and Storport miniport driver models. |
| [NVCACHE_REQUEST_BLOCK structure](ns-ntddscsi--nvcache-request-block.md) | The NVCACHE_REQUEST_BLOCK structure is used in conjunction with the IOCTL_SCSI_MINIPORT request to manage hybrid-hard disk drive (H-HDD) devices (for example, Microsoft ReadyDrive technology). |
| [DUMP_POINTERS_EX structure](ns-ntddscsi--dump-pointers-ex.md) | TBD |
| [MPIO_PASS_THROUGH_PATH_DIRECT32 structure](ns-ntddscsi--mpio-pass-through-path-direct32.md) | TBD |
| [MPIO_PASS_THROUGH_PATH_DIRECT32_EX structure](ns-ntddscsi--mpio-pass-through-path-direct32-ex.md) | TBD |
| [SCSI_PASS_THROUGH32 structure](ns-ntddscsi--scsi-pass-through32.md) | TBD |
| [DUMP_DRIVER structure](ns-ntddscsi--dump-driver.md) | TBD |
| [STORAGE_FIRMWARE_SLOT_INFO structure](ns-ntddscsi--storage-firmware-slot-info.md) | TBD |
| [SCSI_PASS_THROUGH_EX structure](ns-ntddscsi--scsi-pass-through-ex.md) | The SCSI_PASS_THROUGH_EX structure is used in conjunction with an IOCTL_SCSI_PASS_THROUGH_EX request to instruct the port driver to send an embedded SCSI command to the target device. |
| [ATA_PASS_THROUGH_EX32 structure](ns-ntddscsi--ata-pass-through-ex32.md) | TBD |
| [HYBRID_REQUEST_BLOCK structure](ns-ntddscsi--hybrid-request-block.md) | TBD |
| [NV_FEATURE_PARAMETER structure](ns-ntddscsi--nv-feature-parameter.md) | The NV_FEATURE_PARAMETER structure is used in conjunction with the IOCTL_SCSI_MINIPORT_NVCACHE request to get NV Cache Manager feature support information from the device. |
| [MPIO_PASS_THROUGH_PATH structure](ns-ntddscsi--mpio-pass-through-path.md) | The MPIO_PASS_THROUGH_PATH structure is used together with an IOCTL_MPIO_PASS_THROUGH_PATH request to instruct the port driver to send an embedded SCSI command to the target device. |
| [ATA_PASS_THROUGH_DIRECT structure](ns-ntddscsi--ata-pass-through-direct.md) | The ATA_PASS_THROUGH_DIRECT structure is used in conjunction with an IOCTL_ATA_PASS_THROUGH_DIRECT request to instruct the port driver to send an embedded ATA command to the target device. |
| [SCSI_ADAPTER_BUS_INFO structure](ns-ntddscsi--scsi-adapter-bus-info.md) | The SCSI_ADAPTER_BUS_INFO structure is used in conjunction with the IOCTL_SCSI_GET_INQUIRY_DATA request to retrieve the SCSI inquiry data for all devices on a given SCSI bus. |
| [STORAGE_FIRMWARE_DOWNLOAD_V2 structure](ns-ntddscsi--storage-firmware-download-v2.md) | TBD |
| [SCSI_PASS_THROUGH structure](ns-ntddscsi--scsi-pass-through.md) | The SCSI_PASS_THROUGH structure is used in conjunction with an IOCTL_SCSI_PASS_THROUGH request to instruct the port driver to send an embedded SCSI command to the target device. |
| [STORAGE_FIRMWARE_INFO structure](ns-ntddscsi--storage-firmware-info.md) | TBD |
| [NV_SEP_CACHE_PARAMETER structure](ns-ntddscsi--nv-sep-cache-parameter.md) | TBD |
| [SCSI_BUS_DATA structure](ns-ntddscsi--scsi-bus-data.md) | The SCSI_BUS_DATA structure is used in conjunction with the IOCTL_SCSI_GET_INQUIRY_DATA request and the SCSI_ADAPTER_BUS_INFO structure to retrieve the SCSI inquiry data for all devices on a given SCSI bus. |
| [DUMP_POINTERS structure](ns-ntddscsi--dump-pointers.md) | TBD |
Ioctl

| Title        | Description    |
| ------------- |:-------------:|
| [IOCTL_MINIPORT_SIGNATURE_SCSIDISK IOCTL](ni-ntddscsi-ioctl-miniport-signature-scsidisk.md) | TBD |
| [IOCTL_ATA_PASS_THROUGH_DIRECT IOCTL](ni-ntddscsi-ioctl-ata-pass-through-direct.md) | TBD |
| [IOCTL_MINIPORT_SIGNATURE_QUERY_PHYSICAL_TOPOLOGY IOCTL](ni-ntddscsi-ioctl-miniport-signature-query-physical-topology.md) | TBD |
| [IOCTL_SCSI_MINIPORT_DIAGNOSTIC IOCTL](ni-ntddscsi-ioctl-scsi-miniport-diagnostic.md) | TBD |
| [IOCTL_SCSI_MINIPORT_FIRMWARE IOCTL](ni-ntddscsi-ioctl-scsi-miniport-firmware.md) | TBD |
| [IOCTL_SCSI_RESCAN_BUS IOCTL](ni-ntddscsi-ioctl-scsi-rescan-bus.md) | TBD |
| [IOCTL_ATA_MINIPORT IOCTL](ni-ntddscsi-ioctl-ata-miniport.md) | TBD |
| [IOCTL_MPIO_PASS_THROUGH_PATH_EX IOCTL](ni-ntddscsi-ioctl-mpio-pass-through-path-ex.md) | TBD |
| [IOCTL_MINIPORT_SIGNATURE_QUERY_TEMPERATURE IOCTL](ni-ntddscsi-ioctl-miniport-signature-query-temperature.md) | TBD |
| [IOCTL_SCSI_GET_INQUIRY_DATA IOCTL](ni-ntddscsi-ioctl-scsi-get-inquiry-data.md) | TBD |
| [IOCTL_MPIO_PASS_THROUGH_PATH IOCTL](ni-ntddscsi-ioctl-mpio-pass-through-path.md) | TBD |
| [IOCTL_SCSI_PASS_THROUGH IOCTL](ni-ntddscsi-ioctl-scsi-pass-through.md) | TBD |
| [IOCTL_ATA_PASS_THROUGH IOCTL](ni-ntddscsi-ioctl-ata-pass-through.md) | TBD |
| [IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT IOCTL](ni-ntddscsi-ioctl-mpio-pass-through-path-direct.md) | TBD |
| [IOCTL_IDE_PASS_THROUGH IOCTL](ni-ntddscsi-ioctl-ide-pass-through.md) | TBD |
| [IOCTL_SCSI_MINIPORT IOCTL](ni-ntddscsi-ioctl-scsi-miniport.md) | TBD |
| [IOCTL_MINIPORT_SIGNATURE_DSM_NOTIFICATION IOCTL](ni-ntddscsi-ioctl-miniport-signature-dsm-notification.md) | TBD |
| [IOCTL_SCSI_FREE_DUMP_POINTERS IOCTL](ni-ntddscsi-ioctl-scsi-free-dump-pointers.md) | TBD |
| [IOCTL_MINIPORT_SIGNATURE_QUERY_PROTOCOL IOCTL](ni-ntddscsi-ioctl-miniport-signature-query-protocol.md) | TBD |
| [IOCTL_SCSI_GET_ADDRESS IOCTL](ni-ntddscsi-ioctl-scsi-get-address.md) | TBD |
| [IOCTL_SCSI_GET_CAPABILITIES IOCTL](ni-ntddscsi-ioctl-scsi-get-capabilities.md) | TBD |
| [IOCTL_MINIPORT_SIGNATURE_FIRMWARE IOCTL](ni-ntddscsi-ioctl-miniport-signature-firmware.md) | TBD |
| [IOCTL_SCSI_MINIPORT_HYBRID IOCTL](ni-ntddscsi-ioctl-scsi-miniport-hybrid.md) | TBD |
| [IOCTL_MINIPORT_SIGNATURE_SET_TEMPERATURE_THRESHOLD IOCTL](ni-ntddscsi-ioctl-miniport-signature-set-temperature-threshold.md) | TBD |
| [IOCTL_MINIPORT_SIGNATURE_DSM_GENERAL IOCTL](ni-ntddscsi-ioctl-miniport-signature-dsm-general.md) | TBD |
| [IOCTL_MINIPORT_SIGNATURE_HYBRDISK IOCTL](ni-ntddscsi-ioctl-miniport-signature-hybrdisk.md) | TBD |
| [IOCTL_SCSI_PASS_THROUGH_EX IOCTL](ni-ntddscsi-ioctl-scsi-pass-through-ex.md) | TBD |
| [IOCTL_SCSI_BASE IOCTL](ni-ntddscsi-ioctl-scsi-base.md) | TBD |
| [IOCTL_MINIPORT_PROCESS_SERVICE_IRP IOCTL](ni-ntddscsi-ioctl-miniport-process-service-irp.md) | TBD |
| [IOCTL_SCSI_PASS_THROUGH_DIRECT_EX IOCTL](ni-ntddscsi-ioctl-scsi-pass-through-direct-ex.md) | TBD |
| [IOCTL_MPIO_PASS_THROUGH_PATH_DIRECT_EX IOCTL](ni-ntddscsi-ioctl-mpio-pass-through-path-direct-ex.md) | TBD |
| [IOCTL_SCSI_GET_DUMP_POINTERS IOCTL](ni-ntddscsi-ioctl-scsi-get-dump-pointers.md) | TBD |
| [IOCTL_SCSI_MINIPORT_NVCACHE IOCTL](ni-ntddscsi-ioctl-scsi-miniport-nvcache.md) | TBD |
| [IOCTL_SCSI_PASS_THROUGH_DIRECT IOCTL](ni-ntddscsi-ioctl-scsi-pass-through-direct.md) | TBD |
Enum

| Title        | Description    |
| ------------- |:-------------:|
| [NV_SEP_WRITE_CACHE_TYPE enumeration](ne-ntddscsi--nv-sep-write-cache-type.md) | TBD |
| [NVCACHE_STATUS enumeration](ne-ntddscsi--nvcache-status.md) | TBD |
| [MP_STORAGE_DIAGNOSTIC_LEVEL enumeration](ne-ntddscsi--mp-storage-diagnostic-level.md) | The MP_STORAGE_DIAGNOSTIC_LEVEL enumeration allows the caller to control what kinds of data the provider should return. |
| [MP_STORAGE_DIAGNOSTIC_TARGET_TYPE enumeration](ne-ntddscsi--mp-storage-diagnostic-target-type.md) | The MP_STORAGE_DIAGNOSTIC_TARGET_TYPE enumeration specifies the target type of a storage diagnostic. |
| [NVCACHE_TYPE enumeration](ne-ntddscsi--nvcache-type.md) | TBD |

This header is used in these topics:

- [Storage](..content/_Storage)
