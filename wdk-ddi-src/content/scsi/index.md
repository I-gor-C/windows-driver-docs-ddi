---
UID: NA:scsi
---

# Scsi.h header

## -description

This header is used by Storage. For more information, see
- [Storage](../_storage/index.md)

Scsi.h contain these programming interfaces:


## Structures

| Title   | Description   |
| ---- |:---- |
| [BLOCK_DEVICE_RANGE_DESCRIPTOR structure](ns-scsi-block_device_range_descriptor.md) | The BLOCK_DEVICE_RANGE_DESCRIPTOR structure describes a range of logical blocks associated with various fragments of a file for an offload copy operation. |
| [BLOCK_DEVICE_TOKEN_DESCRIPTOR structure](ns-scsi-block_device_token_descriptor.md) | BLOCK_DEVICE_TOKEN_DESCRIPTOR contains the token returned from a the POPULATE TOKEN command for an offload read data operation. |
| [POPULATE_TOKEN_HEADER structure](ns-scsi-populate_token_header.md) | A populate token parameter list starts with a POPULATE_TOKEN_HEADER structure. This is the header for the parameters in a command data block (CDB) of the POPULATE TOKEN command. |
| [RECEIVE_TOKEN_INFORMATION_HEADER structure](ns-scsi-receive_token_information_header.md) | The RECEIVE_TOKEN_INFORMATION_HEADER structure contains information returned as status from an offload data transfer operation. |
| [RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER structure](ns-scsi-receive_token_information_response_header.md) | A token, created as a representation of data (ROD), for an offload read data operation is returned in a RECEIVE_TOKEN_INFORMATION_RESPONSE_HEADER structure. |
| [RT_PARAMETER_DATA structure](ns-scsi-rt_parameter_data.md) | The RT_PARAMETER_DATA structure contains the parameter data for the report timestamp command. |
| [ST_PARAMETER_DATA structure](ns-scsi-st_parameter_data.md) | The ST_PARAMETER_DATA structure contains the parameter list for the set timestamp command. |
| [WRITE_USING_TOKEN_HEADER structure](ns-scsi-write_using_token_header.md) | The WRITE_USING_TOKEN_HEADER structure describes the destination data locations for an offload write data operation. |
| [_INQUIRYDATA structure](ns-scsi-_inquirydata.md) | The INQUIRYDATA structure is used in conjunction with the TapeMiniExtensionInit and TapeMiniVerifyInquiry routines to report SCSI inquiry data associated with a tape device. |
| [_REPORT_ZONES_DATA structure](ns-scsi-_report_zones_data.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [_SES_CONFIGURATION_DIAGNOSTIC_PAGE structure](ns-scsi-_ses_configuration_diagnostic_page.md) | TBD. |
| [_SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure](ns-scsi-_ses_download_microcode_control_diagnostic_page.md) | The SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure contains a vendor specific microcode (i.e., firmware) image for use by the enclosure services process. |
| [_SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure](ns-scsi-_ses_download_microcode_status_descriptor.md) | The SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure specifies the status and additional status of a download microcode. |
| [_SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE structure](ns-scsi-_ses_download_microcode_status_diagnostic_page.md) | The Download Microcode Status diagnostic page includes information about the status of one or more download microcode operations. |
| [_STOR_ADDRESS structure](ns-scsi-_stor_address.md) | A general structure for holding a storage device address. |
| [_STOR_ADDR_BTL8 structure](ns-scsi-_stor_addr_btl8.md) | The STOR_ADDR_BTL8 address structure contains the addressing information for an 8-bit Bus-Target-LUN (BTL8) address. |
| [_TRACK_INFORMATION2 structure](ns-scsi-_track_information2.md) | The TRACK_INFORMATION2 structure is used to report track information. |
| [_VPD_THIRD_PARTY_COPY_PAGE structure](ns-scsi-_vpd_third_party_copy_page.md) | The VPD_THIRD_PARTY_COPY_PAGE structure defines the vital product data (VPD) page for offload data transfer operations. |
| [_VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE structure](ns-scsi-_vpd_zoned_block_device_characteristics_page.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [_WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR structure](ns-scsi-_windows_block_device_token_limits_descriptor.md) | The WINDOWS_BLOCK_DEVICE_TOKEN_LIMITS_DESCRIPTOR structure is the third party copy descriptor for Windows systems. |
| [_ZONE_DESCRIPTIOR structure](ns-scsi-_zone_descriptior.md) | Note  This structure is for internal use only and should not be called from your code. . |

## I/O control codes

| Title   | Description   |
| ---- |:---- |
| [IOCTL_SCSI_MINIPORT_DSM IOCTL](ni-scsi-ioctl_scsi_miniport_dsm.md) | A Data Set Management (DSM) notification is transferred to a miniport driver in a IOCTL_SCSI_MINIPORT_DSM control code request. |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_SES_DOWNLOAD_MICROCODE_STATE enumeration](ne-scsi-_ses_download_microcode_state.md) | TBD. |
