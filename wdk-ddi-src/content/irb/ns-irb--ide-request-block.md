---
UID: NS.irb._IDE_REQUEST_BLOCK
title: IDE_REQUEST_BLOCK
author: windows-driver-content
description: The IDE_REQUEST_BLOCK structure defines an IDE request block.Note  The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
old-location: storage\ide_request_block.htm
old-project: storage
ms.assetid: 9e112984-0a7e-4bb9-a10f-b50ab67ce4f3
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: IDE_REQUEST_BLOCK, IDE_REQUEST_BLOCK, *PIDE_REQUEST_BLOCK
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: irb.h
req.include-header: Irb.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IDE_REQUEST_BLOCK
req.alt-loc: irb.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# IDE_REQUEST_BLOCK structure



## -description
<p>The IDE_REQUEST_BLOCK structure defines an IDE request block.</p>


## -syntax

````
typedef struct _IDE_REQUEST_BLOCK {
  USHORT Function;
  UCHAR  IrbStatus;
  UCHAR  AtaStatus;
  UCHAR  AtaError;
  UCHAR  Channel;
  UCHAR  TargetId;
  UCHAR  Lun;
  UCHAR  CdbLength;
  UCHAR  SenseInfoBufferLength;
  UCHAR  SenseInfoBufferType;
  UCHAR  QueueTag;
  ULONG  ReservedAsUlong;
  ULONG  IrbFlags;
  ULONG  TimeOutValue;
  ULONG  DataTransferLength;
  PVOID  IrbExtension;
  PVOID  DataBuffer;
  PVOID  SenseInfoBuffer;
  PVOID  NextIrb;
  PVOID  Reserved;
  union {
    IDE_TASK_FILE  IdeTaskFile;
    UCHAR          Cdb[16];
    IDE_POWER_INFO PowerChange;
    UCHAR          AsUChar[16];
  };
} IDE_REQUEST_BLOCK, *PIDE_REQUEST_BLOCK;
````


## -struct-fields
<dl>

### -field <b>Function</b>

<dd>
<p>Specifies the category that the request belongs to. The table below describes the classification of the I/O requests.</p>
<table>
<tr>
<td>
<p><b>Function</b></p>
</td>
<td>
<p><b>Sub-commands</b></p>
</td>
<td>
<p><b>Description</b></p>
</td>
</tr>
<tr>
<td>
<p>IRB_FUNCTION_ATA_COMMAND</p>
</td>
<td>
<p>IRB_FUNCTION_ATA_IDENTIFY</p>
<p>IRB_FUNCTION_ATA_READ</p>
<p>IRB_FUNCTION_ATA_WRITE</p>
<p>IRB_FUNCTION_ATA_FLUSH</p>
<p>IRB_FUNCTION_ATA_SMART</p>
</td>
<td>
<p>Indicates that the IRB contains an IdeTaskFile that describes the ATA command. The sub-commands indicate finer grouping of request for faster lookup.</p>
</td>
</tr>
<tr>
<td>
<p>IRB_FUNCTION_ATAPI_COMMAND</p>
</td>
<td>
<p>IRB_FUNCTION_REQUEST_SENSE</p>
</td>
<td>
<p>Indicates that the IRB contains a CDB that describes the ATAPI command.</p>
</td>
</tr>
<tr>
<td>
<p>IRB_FUNCTION_MINIPORT_COMMAND</p>
</td>
<td>
<p>IRB_FUNCTION_ADAPTER_FLUSH</p>
<p>IRB_FUNCTION_SHUTDOWN</p>
<p>IRB_FUNCTION_POWER_CHANGE</p>
<p>IRB_FUNCTION_POWER_REBOOT</p>
<p>IRB_FUNCTION_LUN_RESET</p>
<p>IRB_FUNCTION_MINIPORT_IOCTL</p>
</td>
<td>
<p>Indicates that the IRB is for the miniport. It is the responsibility of the miniport to interpret the command appropriately.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>IrbStatus</b>

<dd>
<p>The miniport must set this member to indicates the status of the specified operation. The table below describes the various <b>IrbStatus</b> values and their meaning.</p>
<table>
<tr>
<td>
<p><b>Value</b></p>
</td>
<td>
<p><b>Meaning</b></p>
</td>
</tr>
<tr>
<td>
<p>IRB_STATUS_PENDING</p>
</td>
<td>
<p>Indicates that the request is in progress. The port driver initializes <b>IrbStatus</b> to this value. A miniport driver should never set the <b>IrbStatus</b> member to this value.</p>
</td>
</tr>
<tr>
<td>
<p>IRB_STATUS_SUCCESS</p>
</td>
<td>
<p>Indicates that the request was completed successfully.</p>
</td>
</tr>
<tr>
<td>
<p>IRB_STATUS_DATALENGTH_MISMATCH</p>
</td>
<td>
<p>Indicates that a data underrun or overrun error occurred. The miniport must update the DataTransferLength field in the IRB to indicate the actual amount of data that was transferred in the case of an underrun.</p>
</td>
</tr>
<tr>
<td>
<p>IRB_STATUS_DEVICE_ERROR</p>
</td>
<td>
<p>Indicates that the device returned an error. The miniport driver must update the <i>AtaStatus</i> and <i>AtaError</i> fields in the Irb to the contents of the device ATA status and error register at the completion of the command.</p>
</td>
</tr>
<tr>
<td>
<p>IRB_STATUS_INVALID_REQUEST</p>
</td>
<td>
<p>Indicates that the miniport does not support the given request.</p>
</td>
</tr>
<tr>
<td>
<p>IRB_STATUS_BUS_RESET</p>
</td>
<td>
<p>Indicates that a bus reset occurred while processing the given request.</p>
</td>
</tr>
<tr>
<td>
<p>IRB_STATUS_SELECTION_TIMEOUT</p>
</td>
<td>
<p>Indicates that the destination device could not be selected.</p>
</td>
</tr>
<tr>
<td>
<p>IRB_STATUS_BUSY</p>
</td>
<td>
<p>Indicates that the device is busy. The port driver retries any request completed with this status. A request completed with busy status is retried only once. It is the responsibility of the miniport driver to pause the request queue using <b>AtaPortDeviceBusy</b> if the device cannot handle request for a certain period of time.</p>
</td>
</tr>
<tr>
<td>
<p>IRB_STATUS_AUTOSENSE_VALID</p>
</td>
<td>
<p>IRB_STATUS_AUTOSENSE_VALID is a bitmask that indicates valid sense data in the <i>SenseInfoBuffer</i> member of the IRB. </p>
</td>
</tr>
<tr>
<td>
<p>IRB_STATUS_RETURN_TASKFILE_VALID</p>
</td>
<td>
<p>IRB_STATUS_RETURN_TASKFILE_VALID is a bitmask that indicates a valid return task file in the <i>SenseInfoBuffer</i> member of the IRB.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>AtaStatus</b>

<dd>
<p>Indicates the status returned by the device in its status register. The miniport driver should update this field when completing an IRB with <i>IRB_STATUS_DEVICE_ERROR</i>.</p>
</dd>

### -field <b>AtaError</b>

<dd>
<p>Indicates the error value returned by the device in its error register. The miniport driver should update this field when completing an IRB with <i>IRB_STATUS_DEVICE_ERROR</i>.</p>
</dd>

### -field <b>Channel</b>

<dd>
<p>Specifies the channel number.</p>
</dd>

### -field <b>TargetId</b>

<dd>
<p>Specifies the target ID of the device.</p>
</dd>

### -field <b>Lun</b>

<dd>
<p>Specifies the logical unit number of the device.</p>
</dd>

### -field <b>CdbLength</b>

<dd>
<p>Specifies the length in bytes of the buffer pointed to by <b>Cdb</b>.</p>
</dd>

### -field <b>SenseInfoBufferLength</b>

<dd>
<p>Specifies the length in bytes of the buffer pointed to by <b>SenseInfoBuffer</b>.</p>
</dd>

### -field <b>SenseInfoBufferType</b>

<dd>
<p>Specifies the type of data structure returned in <b>SenseInfoBuffer</b>. Because ATA commands don't have a need for the request sense command, ATA_PASS_THROUGH commands use <b>SenseInfoBuffer</b> to return task file information. For ATA_PASS_THROUGH commands, as identified in the <b>IrbFlags</b> member, the appropriate return <b>TaskFile</b> size should be reported as either SENSE_INFO_BUFFER_RETURN_TYPE_28BIT_TASKFILE or</p>
<p>SENSE_INFO_BUFFER_RETURN_TYPE_48BIT_TASKFILE.</p>
</dd>

### -field <b>QueueTag</b>

<dd>
<p>The queue tag for this IRB. The port driver sets this field to 0.</p>
</dd>

### -field <b>ReservedAsUlong</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>IrbFlags</b>

<dd>
<p>Qualifies the request with ceratin actions that need to be performed. The table below describes them in detail.</p>
<table>
<tr>
<td>
<p><b>Flag</b></p>
</td>
<td>
<p><b>Description</b></p>
</td>
</tr>
<tr>
<td>
<p>IRB_FLAGS_DRDY_REQUIRED</p>
</td>
<td>
<p>Indicates that the miniport driver must wait for the device to set the DRDY bit in the ATA status register before issuing this command.</p>
</td>
</tr>
<tr>
<td>
<p>IRB_FLAGS_USE_DMA</p>
</td>
<td>
<p>Indicates that the request has an associated scatter/gather list and the miniport driver could use DMA to transfer data for this request. </p>
</td>
</tr>
<tr>
<td>
<p>IRB_FLAGS_MAP_BUFFERS</p>
</td>
<td>
<p>Indicates that the <b>DataBuffer</b> field in the IRB is mapped. The miniport can safely access <b>DataBuffer</b> when this flag is set. The miniport driver must not access <b>DataBuffer</b> if the flag is not set. The miniport driver could request the port driver to map the data buffer by setting this flag in the IRB in its <b>IdeHwBuildIo</b> routine.</p>
</td>
</tr>
<tr>
<td>
<p>IRB_FLAGS_48BIT</p>
</td>
<td>
<p>Indicates that the ATA command in the IRB belongs to the 48 bit LBA feature set. The <b>Previous</b> field in the <i>_IDE_TASK_FILE</i> structure is valid when this flag is set.</p>
</td>
</tr>
<tr>
<td>
<p>IRB_FLAGS_PIO_MULTIPLE</p>
</td>
<td>
<p>Indicates that the ATA command is to be transferred using the ATA PIO Multiple method.</p>
</td>
</tr>
<tr>
<td>
<p>IRB_FLAGS_RETURN_RESULTS</p>
</td>
<td>
<p>Indicates that the ATA return task file is to be copied to <b>SenseInfoBuffer</b>. </p>
</td>
</tr>
<tr>
<td>
<p>IRB_FLAGS_DATA_IN</p>
</td>
<td>
<p>Indicates that the data is to be transferred from the device to the host system (a read operation).</p>
</td>
</tr>
<tr>
<td>
<p>IRB_FLAGS_DATA_OUT</p>
</td>
<td>
<p>Indicates that the data is to be transferred to the device from the host system ( a write operation).</p>
</td>
</tr>
<tr>
<td>
<p>IRB_FLAGS_DISCARDABLE  </p>
</td>
<td>
<p>Indicates that the command shall be done in a best effort manner. (note: this is not currently employed by ATAport).</p>
</td>
</tr>
<tr>
<td>
<p>IRB_FLAGS_HIGH_PRIORITY</p>
</td>
<td>
<p>Indicates that this IRB is to be processed as soon as possible, before non-high-priority IRBs currently in the ATA miniport.</p>
</td>
</tr>
</table>
<p> </p>
</dd>

### -field <b>TimeOutValue</b>

<dd>
<p>Indicates the time in seconds after which the request will time out.</p>
</dd>

### -field <b>DataTransferLength</b>

<dd>
<p>Contains the length in bytes of the data buffer that contains data to be transferred.</p>
</dd>

### -field <b>IrbExtension</b>

<dd>
<p>Pointer to the per-request extension allocated by the port driver.</p>
</dd>

### -field <b>DataBuffer</b>

<dd>
<p>Pointer to the buffer where the data resides.</p>
</dd>

### -field <b>SenseInfoBuffer</b>

<dd>
<p>Pointer to the buffer which holds the sense data.</p>
</dd>

### -field <b>NextIrb</b>

<dd>
<p>Pointer to the next IRB to be processed. The port driver sets this to <b>NULL</b>. The miniport driver can use this field to link IRBs together.</p>
</dd>

### -field <b>Reserved</b>

<dd>
<p>Reserved for future use.</p>
</dd>

### -field <b>IdeTaskFile</b>

<dd>
<p>Contains a structure of type <a href="..\irb\ns-irb--ide-task-file.md">IDE_TASK_FILE</a> that holds the IDE task file for the indicated controller. This member is defined whenever the result of a bitwise AND between the <b>Function</b> member and IRB_FUNCTION_ATA_COMMAND is nonzero.</p>
</dd>

### -field <b>Cdb</b>

<dd>
<p>Contains a command descriptor block (CDB). This member is defined whenever the result of a bitwise AND between the <b>Function</b> member and IRB_FUNCTION_ATAPI_COMMAND is nonzero.</p>
</dd>

### -field <b>PowerChange</b>

<dd>
<p>Indicates an enumeration value of type <a href="storage.power_change_info">POWER_CHANGE_INFO</a> that defines a power state transition. This member is defined whenever <b>Function</b> is equal to IRB_FUNCTION_POWER_CHANGE.</p>
</dd>

### -field <b>AsUChar</b>

<dd>
<p>Provides a means of accessing members <b>IdeTaskFile</b>, <b>PowerChange</b>, and <b>Cdb</b> as unsigned character data.</p>
</dd>
</dl>

## -remarks
<p>The IDE_REQUEST_BLOCK structure provides a functionality similar to the <a href="..\srb\ns-srb--scsi-request-block.md">SCSI_REQUEST_BLOCK</a> but with characteristics more suitable for managing devices on an IDE bus.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Irb.h (include Irb.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\irb\nf-irb-ataportdevicebusy.md">AtaportDeviceBusy</a>
</dt>
<dt>
<a href="..\irb\ns-irb--ide-task-file.md">IDE_TASK_FILE</a>
</dt>
<dt>
<a href="storage.power_change_info">POWER_CHANGE_INFO</a>
</dt>
<dt>
<a href="..\srb\ns-srb--scsi-request-block.md">SCSI_REQUEST_BLOCK</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IDE_REQUEST_BLOCK structure%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
