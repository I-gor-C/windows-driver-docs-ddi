# Minitape.h header


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
| [TAPE_ERROR_ROUTINE callback](nc-minitape-tape-error-routine.md) | TapeMiniTapeError provides device-specific error handling when an SRB is completed with an error status. This routine is optional. |
| [TAPE_EXTENSION_INIT_ROUTINE callback](nc-minitape-tape-extension-init-routine.md) | TapeMiniExtensionInit initializes an optional, driver-specific context area. This routine is called by TapeClassInitialize when the tape miniclass driver is loaded. This routine is optional. |
| [TAPE_PROCESS_COMMAND_ROUTINE callback](nc-minitape-tape-process-command-routine.md) | TapeMiniCreatePartition handles the device-specific aspects of an IOCTL_TAPE_CREATE_PARTITION request. This routine is required. |
| [TAPE_VERIFY_INQUIRY_ROUTINE callback](nc-minitape-tape-verify-inquiry-routine.md) | TapeMiniVerifyInquiry determines whether the tape miniclass driver recognizes and supports a given device. This routine is required. |

## Structures

| Title   | Description   |
| ---- |:---- |
| [PRT_PARAMETER_DATA structure](ns-minitape-prt-parameter-data.md) | The RT_PARAMETER_DATA structure contains the parameter data for the report timestamp command. |
| [PST_PARAMETER_DATA structure](ns-minitape-pst-parameter-data.md) | The ST_PARAMETER_DATA structure contains the parameter list for the set timestamp command. |
| [REPORT_ZONES_DATA structure](ns-minitape--report-zones-data.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [SES_CONFIGURATION_DIAGNOSTIC_PAGE structure](ns-minitape--ses-configuration-diagnostic-page.md) | TBD. |
| [SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure](ns-minitape--ses-download-microcode-control-diagnostic-page.md) | The SES_DOWNLOAD_MICROCODE_CONTROL_DIAGNOSTIC_PAGE structure contains a vendor specific microcode (i.e., firmware) image for use by the enclosure services process. |
| [SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure](ns-minitape--ses-download-microcode-status-descriptor.md) | The SES_DOWNLOAD_MICROCODE_STATUS_DESCRIPTOR structure specifies the status and additional status of a download microcode. |
| [SES_DOWNLOAD_MICROCODE_STATUS_DIAGNOSTIC_PAGE structure](ns-minitape--ses-download-microcode-status-diagnostic-page.md) | The Download Microcode Status diagnostic page includes information about the status of one or more download microcode operations. |
| [TAPE_INIT_DATA structure](ns-minitape--tape-init-data.md) | TAPE_INIT_DATA is used only by legacy tape miniclass drivers. Use TAPE_INIT_DATA_EX instead. |
| [TAPE_INIT_DATA_EX structure](ns-minitape--tape-init-data-ex.md) | TAPE_INIT_DATA_EX defines values and routines that are specific to a Windows 2000 tape miniclass driver. The tape miniclass DriverEntry routine passes this information to the tape class driver to complete miniclass driver initialization. |
| [VPD_ZONED_BLOCK_DEVICE_CHARACTERISTICS_PAGE structure](ns-minitape--vpd-zoned-block-device-characteristics-page.md) | Note  This structure is for internal use only and should not be called from your code. . |
| [ZONE_DESCRIPTIOR structure](ns-minitape--zone-descriptior.md) | Note  This structure is for internal use only and should not be called from your code. . |

## Enumerations

| Title   | Description   |
| ---- |:---- |
| [SES_DOWNLOAD_MICROCODE_STATE enumeration](ne-minitape--ses-download-microcode-state.md) | TBD. |
| [TAPE_STATUS enumeration](ne-minitape--tape-status.md) | The TAPE_STATUS enumeration provides a list of the status codes that the tape class driver uses to report the status of a tape device. |
