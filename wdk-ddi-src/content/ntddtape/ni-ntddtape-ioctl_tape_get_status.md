---
UID: NI.ntddtape.IOCTL_TAPE_GET_STATUS
title: IOCTL_TAPE_GET_STATUS
author: windows-driver-content
description: Returns the current status of the drive in the Status field of the I/O status block.
old-location: storage\ioctl_tape_get_status.htm
old-project: storage
ms.assetid: d5e491b8-d40c-4f2c-9117-5c3cb71913f7
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _TAPE_DRIVE_PROBLEM_TYPE, TAPE_DRIVE_PROBLEM_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddtape.h
req.include-header: Ntddtape.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_TAPE_GET_STATUS
req.alt-loc: Ntddtape.h
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
---

# IOCTL_TAPE_GET_STATUS IOCTL



## -description

Returns the current status of the drive in the <b>Status</b> field of the I/O status block. 



Returns the current status of the drive in the <b>Status</b> field of the I/O status block. 



## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
None</p>None


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
None</p>None


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
The <b>Information</b> field is set to zero. The <b>Status</b> field is set to one of the following NT status values: </p>The <b>Information</b>Information field is set to zero. The <b>Status</b>Status field is set to one of the following NT status values: 
<ul>
<li>
STATUS_SUCCESS

</li>
<li>
STATUS_INSUFFICIENT_RESOURCES

</li>
<li>
STATUS_NOT_IMPLEMENTED

</li>
<li>
STATUS_INVALID_DEVICE_REQUEST

</li>
<li>
STATUS_INVALID_PARAMETER

</li>
<li>
STATUS_VERIFY_REQUIRED

</li>
<li>
STATUS_BUS_RESET

</li>
<li>
STATUS_SETMARK_DETECTED

</li>
<li>
STATUS_FILEMARK_DETECTED

</li>
<li>
STATUS_BEGINNING_OF_MEDIA

</li>
<li>
STATUS_END_OF_MEDIA

</li>
<li>
STATUS_BUFFER_OVERFLOW

</li>
<li>
STATUS_NO_DATA_DETECTED

</li>
<li>
STATUS_EOM_OVERFLOW

</li>
<li>
STATUS_NO_MEDIA

</li>
<li>
STATUS_IO_DEVICE_ERROR

</li>
<li>
STATUS_UNRECOGNIZED_MEDIA

</li>
<li>
STATUS_DEVICE_NOT_READY

</li>
<li>
STATUS_MEDIA_WRITE_PROTECTED

</li>
<li>
STATUS_DEVICE_DATA_ERROR

</li>
<li>
STATUS_NO_SUCH_DEVICE

</li>
<li>
STATUS_INVALID_BLOCK_LENGTH

</li>
<li>
STATUS_IO_TIMEOUT

</li>
<li>
STATUS_DEVICE_NOT_CONNECTED

</li>
<li>
STATUS_DATA_OVERRUN

</li>
<li>
STATUS_DEVICE_BUSY

</li>
<li>
STATUS_DEVICE_REQUIRES_CLEANING

</li>
<li>
STATUS_CLEANER_CARTRIDGE_INSTALLED

</li>
</ul>
<li>
STATUS_SUCCESS

</li>
STATUS_SUCCESS</p>STATUS_SUCCESS

<li>
STATUS_INSUFFICIENT_RESOURCES

</li>
STATUS_INSUFFICIENT_RESOURCES</p>STATUS_INSUFFICIENT_RESOURCES

<li>
STATUS_NOT_IMPLEMENTED

</li>
STATUS_NOT_IMPLEMENTED</p>STATUS_NOT_IMPLEMENTED

<li>
STATUS_INVALID_DEVICE_REQUEST

</li>
STATUS_INVALID_DEVICE_REQUEST</p>STATUS_INVALID_DEVICE_REQUEST

<li>
STATUS_INVALID_PARAMETER

</li>
STATUS_INVALID_PARAMETER</p>STATUS_INVALID_PARAMETER

<li>
STATUS_VERIFY_REQUIRED

</li>
STATUS_VERIFY_REQUIRED</p>STATUS_VERIFY_REQUIRED

<li>
STATUS_BUS_RESET

</li>
STATUS_BUS_RESET</p>STATUS_BUS_RESET

<li>
STATUS_SETMARK_DETECTED

</li>
STATUS_SETMARK_DETECTED</p>STATUS_SETMARK_DETECTED

<li>
STATUS_FILEMARK_DETECTED

</li>
STATUS_FILEMARK_DETECTED</p>STATUS_FILEMARK_DETECTED

<li>
STATUS_BEGINNING_OF_MEDIA

</li>
STATUS_BEGINNING_OF_MEDIA</p>STATUS_BEGINNING_OF_MEDIA

<li>
STATUS_END_OF_MEDIA

</li>
STATUS_END_OF_MEDIA</p>STATUS_END_OF_MEDIA

<li>
STATUS_BUFFER_OVERFLOW

</li>
STATUS_BUFFER_OVERFLOW</p>STATUS_BUFFER_OVERFLOW

<li>
STATUS_NO_DATA_DETECTED

</li>
STATUS_NO_DATA_DETECTED</p>STATUS_NO_DATA_DETECTED

<li>
STATUS_EOM_OVERFLOW

</li>
STATUS_EOM_OVERFLOW</p>STATUS_EOM_OVERFLOW

<li>
STATUS_NO_MEDIA

</li>
STATUS_NO_MEDIA</p>STATUS_NO_MEDIA

<li>
STATUS_IO_DEVICE_ERROR

</li>
STATUS_IO_DEVICE_ERROR</p>STATUS_IO_DEVICE_ERROR

<li>
STATUS_UNRECOGNIZED_MEDIA

</li>
STATUS_UNRECOGNIZED_MEDIA</p>STATUS_UNRECOGNIZED_MEDIA

<li>
STATUS_DEVICE_NOT_READY

</li>
STATUS_DEVICE_NOT_READY</p>STATUS_DEVICE_NOT_READY

<li>
STATUS_MEDIA_WRITE_PROTECTED

</li>
STATUS_MEDIA_WRITE_PROTECTED</p>STATUS_MEDIA_WRITE_PROTECTED

<li>
STATUS_DEVICE_DATA_ERROR

</li>
STATUS_DEVICE_DATA_ERROR</p>STATUS_DEVICE_DATA_ERROR

<li>
STATUS_NO_SUCH_DEVICE

</li>
STATUS_NO_SUCH_DEVICE</p>STATUS_NO_SUCH_DEVICE

<li>
STATUS_INVALID_BLOCK_LENGTH

</li>
STATUS_INVALID_BLOCK_LENGTH</p>STATUS_INVALID_BLOCK_LENGTH

<li>
STATUS_IO_TIMEOUT

</li>
STATUS_IO_TIMEOUT</p>STATUS_IO_TIMEOUT

<li>
STATUS_DEVICE_NOT_CONNECTED

</li>
STATUS_DEVICE_NOT_CONNECTED</p>STATUS_DEVICE_NOT_CONNECTED

<li>
STATUS_DATA_OVERRUN

</li>
STATUS_DATA_OVERRUN</p>STATUS_DATA_OVERRUN

<li>
STATUS_DEVICE_BUSY

</li>
STATUS_DEVICE_BUSY</p>STATUS_DEVICE_BUSY

<li>
STATUS_DEVICE_REQUIRES_CLEANING

</li>
STATUS_DEVICE_REQUIRES_CLEANING</p>STATUS_DEVICE_REQUIRES_CLEANING

<li>
STATUS_CLEANER_CARTRIDGE_INSTALLED

</li>
STATUS_CLEANER_CARTRIDGE_INSTALLED</p>STATUS_CLEANER_CARTRIDGE_INSTALLED


Each of these NT status values correspond to a value in the <a href="storage.tape_status">TAPE_STATUS</a> enumerator. For more information about the significance of these values and a mapping between the NT status values and the TAPE_STATUS values, see <a href="storage.processing_tape_device_control_requests">Processing Tape Device Control Requests</a>.</p>Each of these NT status values correspond to a value in the <a href="storage.tape_status">TAPE_STATUS</a><b>TAPE_STATUS</b>TAPE_STATUS enumerator. For more information about the significance of these values and a mapping between the NT status values and the TAPE_STATUS values, see <a href="storage.processing_tape_device_control_requests">Processing Tape Device Control Requests</a>Processing Tape Device Control Requests.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddtape.h (include Ntddtape.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.tape_status">TAPE_STATUS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_TAPE_GET_STATUS control code%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

