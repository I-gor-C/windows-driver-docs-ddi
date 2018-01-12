---
UID: NA:minitape
---

# Minitape.h header

## -description

This header is used by Storage. For more information, see
- [Storage](../_storage/index.md)

Minitape.h contain these programming interfaces:


## Functions

| Title   | Description   |
| ---- |:---- |
| [TapeClassAllocateSrbBuffer function](nf-minitape-tapeclassallocatesrbbuffer.md) | The TapeClassAllocateSrbBuffer routine allocates an Srb-&gt;DataBuffer. |
| [TapeClassCompareMemory function](nf-minitape-tapeclasscomparememory.md) | The TapeClassCompareMemory routine compares two memory buffers and returns the number of bytes that are equivalent. |
| [TapeClassInitialize function](nf-minitape-tapeclassinitialize.md) | The TapeClassInitialize routine performs much of the driver and device initialization on behalf of a miniclass driver. |
| [TapeClassLiDiv function](nf-minitape-tapeclasslidiv.md) | The TapeClassLiDiv routine performs a division of the two indicated integers. |
| [TapeClassLogicalBlockToPhysicalBlock function](nf-minitape-tapeclasslogicalblocktophysicalblock.md) | The TapeClassLogicalBlockToPhysicalBlock routine translates a pseudological block address to a physical block address. This routine is for SCSI-1 devices. |
| [TapeClassPhysicalBlockToLogicalBlock function](nf-minitape-tapeclassphysicalblocktologicalblock.md) | The TapeClassPhysicalBlockToLogicalBlock routine translates a physical block address to a pseudological block address. This routine is for SCSI-1 devices. |
| [TapeClassZeroMemory function](nf-minitape-tapeclasszeromemory.md) | The TapeClassZeroMemory routine fills a buffer with zeros. |
| [TapeDebugPrint function](nf-minitape-tapedebugprint.md) | The TapeDebugPrint routine prints the indicated string. |

## Callback functions

| Title   | Description   |
| ---- |:---- |
| [TAPE_ERROR_ROUTINE callback](nc-minitape-tape_error_routine.md) | TAPE_ERROR_ROUTINE provides device-specific error handling when an SRB is completed with an error status. This routine is optional. |
| [TAPE_EXTENSION_INIT_ROUTINE callback](nc-minitape-tape_extension_init_routine.md) | ExtensionInit initializes an optional, driver-specific context area. This routine is called by TapeClassInitialize when the tape miniclass driver is loaded. This routine is optional. |
| [TAPE_PROCESS_COMMAND_ROUTINE callback](nc-minitape-tape_process_command_routine.md) | TAPE_PROCESS_COMMAND_ROUTINE handles the device-specific aspects of an IOCTL request. |
| [TAPE_VERIFY_INQUIRY_ROUTINE callback](nc-minitape-tape_verify_inquiry_routine.md) | TAPE_VERIFY_INQUIRY_ROUTINE determines whether the tape miniclass driver recognizes and supports a given device. This routine is required. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [RT_PARAMETER_DATA structure](ns-minitape-rt_parameter_data.md) | The RT_PARAMETER_DATA structure contains the parameter data for the report timestamp command. |
| [ST_PARAMETER_DATA structure](ns-minitape-st_parameter_data.md) | The ST_PARAMETER_DATA structure contains the parameter list for the set timestamp command. |
| [_REPORT_ZONES_DATA structure](ns-minitape-_report_zones_data.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [_SES_CONFIGURATION_DIAGNOSTIC_PAGE structure](ns-minitape-_ses_configuration_diagnostic_page.md) | TBD. |
| [_SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure](ns-minitape-_ses_download_microcode_control_diagnostic_page.md) | The SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure contains a vendor specific microcode (i.e., firmware) image for use by the enclosure services process. |
| [_SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure](ns-minitape-_ses_download_microcode_status_descriptor.md) | The SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure specifies the status and additional status of a download microcode. |
| [_SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE structure](ns-minitape-_ses_download_microcode_status_diagnostic_page.md) | The Download Microcode Status diagnostic page includes information about the status of one or more download microcode operations. |
| [_TAPE_INIT_DATA structure](ns-minitape-_tape_init_data.md) | TAPE_INIT_DATA is used only by legacy tape miniclass drivers. Use TAPE_INIT_DATA_EX instead. |
| [_TAPE_INIT_DATA_EX structure](ns-minitape-_tape_init_data_ex.md) | TAPE_INIT_DATA_EX defines values and routines that are specific to a Windows 2000 tape miniclass driver. The tape miniclass DriverEntry routine passes this information to the tape class driver to complete miniclass driver initialization. |
| [_VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE structure](ns-minitape-_vpd_zoned_block_device_characteristics_page.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [_ZONE_DESCRIPTIOR structure](ns-minitape-_zone_descriptior.md) | Note  This structure is for internal use only and should not be called from your code. . |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [_SES_DOWNLOAD_MICROCODE_STATE enumeration](ne-minitape-_ses_download_microcode_state.md) | TBD. |
| [_TAPE_STATUS enumeration](ne-minitape-_tape_status.md) | The TAPE_STATUS enumeration provides a list of the status codes that the tape class driver uses to report the status of a tape device. |
