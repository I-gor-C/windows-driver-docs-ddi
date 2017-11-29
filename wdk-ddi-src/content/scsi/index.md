# Scsi.h header


This header is used by Storage. For more information, see
- [Storage](../_storage/index.md)

Scsi.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [INQUIRYDATA structure](ns-scsi--inquirydata.md) | The INQUIRYDATA structure is used in conjunction with the TapeMiniExtensionInit and TapeMiniVerifyInquiry routines to report SCSI inquiry data associated with a tape device. |
| [INQUIRYDATA structure](ns-scsi--inquirydata~r1.md) | The INQUIRYDATA structure is used in conjunction with the TapeMiniExtensionInit and TapeMiniVerifyInquiry routines to report SCSI inquiry data associated with a tape device. |
| [PBLOCK_DEVICE_RANGE_DESCRIPTOR structure](ns-scsi-pblock-device-range-descriptor.md) | The BLOCK_DEVICE_RANGE_DESCRIPTOR structure describes a range of logical blocks associated with various fragments of a file for an offload copy operation. |
| [PBLOCK_DEVICE_TOKEN_DESCRIPTOR structure](ns-scsi-pblock-device-token-descriptor.md) | BLOCK_DEVICE_TOKEN_DESCRIPTOR contains the token returned from a the POPULATE TOKEN command for an offload read data operation. |
| [PPOPULATE_TOKEN_HEADER structure](ns-scsi-ppopulate-token-header.md) | A populate token parameter list starts with a POPULATE_TOKEN_HEADER structure. This is the header for the parameters in a command data block (CDB) of the POPULATE TOKEN command. |
| [PRECEIVE_TOKEN_INFORMATION_HEADER structure](ns-scsi-preceive-token-information-header.md) | The RECEIVE_TOKEN_INFORMATION_HEADER structure contains information returned as status from an offload data transfer operation. |
| [PRECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER structure](ns-scsi-preceive-token-information-response-header.md) | A token, created as a representation of data (ROD), for an offload read data operation is returned in a RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER structure. |
| [PRT_PARAMETER_DATA structure](ns-scsi-prt-parameter-data.md) | The RT_PARAMETER_DATA structure contains the parameter data for the report timestamp command. |
| [PST_PARAMETER_DATA structure](ns-scsi-pst-parameter-data.md) | The ST_PARAMETER_DATA structure contains the parameter list for the set timestamp command. |
| [PWRITE_USING_TOKEN_HEADER structure](ns-scsi-pwrite-using-token-header.md) | The WRITE_USING_TOKEN_HEADER structure describes the destination data locations for an offload write data operation. |
| [REPORT_ZONES_DATA structure](ns-scsi--report-zones-data.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [SES_CONFIGURATION_DIAGNOSTIC_PAGE structure](ns-scsi--ses-configuration-diagnostic-page.md) | TBD. |
| [SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure](ns-scsi--ses-download-microcode-control-diagnostic-page.md) | The SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure contains a vendor specific microcode (i.e., firmware) image for use by the enclosure services process. |
| [SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure](ns-scsi--ses-download-microcode-status-descriptor.md) | The SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure specifies the status and additional status of a download microcode. |
| [SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE structure](ns-scsi--ses-download-microcode-status-diagnostic-page.md) | The Download Microcode Status diagnostic page includes information about the status of one or more download microcode operations. |
| [STOR_ADDRESS structure](ns-scsi--stor-address.md) | A general structure for holding a storage device address. |
| [STOR_ADDR_BTL8 structure](ns-scsi--stor-addr-btl8.md) | The STOR_ADDR_BTL8 address structure contains the addressing information for an 8-bit Bus-Target-LUN (BTL8) address. |
| [TRACK_INFORMATION2 structure](ns-scsi--track-information2.md) | The TRACK_INFORMATION2 structure is used to report track information. |
| [VPD_THIRD_PARTY_COPY_PAGE structure](ns-scsi--vpd-third-party-copy-page.md) | The VPD_THIRD_PARTY_COPY_PAGE structure defines the vital product data (VPD) page for offload data transfer operations. |
| [VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE structure](ns-scsi--vpd-zoned-block-device-characteristics-page.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR structure](ns-scsi--windows-block-device-token-limits-descriptor.md) | The WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR structure is the third party copy descriptor for Windows systems. |
| [ZONE_DESCRIPTIOR structure](ns-scsi--zone-descriptior.md) | Note  This structure is for internal use only and should not be called from your code. . |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [SES_DOWNLOAD_MICROCODE_STATE enumeration](ne-scsi--ses-download-microcode-state.md) | TBD. |
