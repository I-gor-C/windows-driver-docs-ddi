---
UID: NI.ntddvol.IOCTL_VOLUME_LOGICAL_TO_PHYSICAL
title: IOCTL_VOLUME_LOGICAL_TO_PHYSICAL
author: windows-driver-content
description: Returns physical offsets and physical disk numbers for a given volume logical offset.
old-location: storage\ioctl_volume_logical_to_physical.htm
old-project: storage
ms.assetid: deadee81-4a6d-4c8b-80fd-46c29becc2cf
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _VIDEO_WIN32K_CALLBACKS_PARAMS, *PVIDEO_WIN32K_CALLBACKS_PARAMS, VIDEO_WIN32K_CALLBACKS_PARAMS
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddvol.h
req.include-header: Ntddvol.h
req.target-type: Windows
req.target-min-winverclnt: Available starting with Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_VOLUME_LOGICAL_TO_PHYSICAL
req.alt-loc: Ntddvol.h
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

# IOCTL_VOLUME_LOGICAL_TO_PHYSICAL IOCTL



## -description

Returns physical offsets and physical disk numbers for a given volume logical offset. 

For example, a logical volume offset inside a mirrored volume with two <a href="wdkgloss.p#wdkgloss.plex#wdkgloss.plex"><i>plex</i></a> corresponds to two physical offsets, one in each of the two disks participating in the mirror. In response to this IOCTL, the volume manager returns two physical offsets and two physical disk numbers for the logical volume offset. 

The volume manager supports this IOCTL for all types of basic and dynamic volumes.



Returns physical offsets and physical disk numbers for a given volume logical offset. 

For example, a logical volume offset inside a mirrored volume with two <a href="wdkgloss.p#wdkgloss.plex#wdkgloss.plex"><i>plex</i></a> corresponds to two physical offsets, one in each of the two disks participating in the mirror. In response to this IOCTL, the volume manager returns two physical offsets and two physical disk numbers for the logical volume offset. 

The volume manager supports this IOCTL for all types of basic and dynamic volumes.



## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
<b>
       Parameters.DeviceIoControl.InputBufferLength</b> in the I/O stack location of the IRP indicates the size, in bytes, of the input buffer, which must be greater than or equal to the value of <b>sizeof</b>(VOLUME_LOGICAL_OFFSET).
<b>
       Parameters.DeviceIoControl.InputBufferLength</b>
       Parameters.DeviceIoControl.InputBufferLength in the I/O stack location of the IRP indicates the size, in bytes, of the input buffer, which must be greater than or equal to the value of <b>sizeof</b>sizeof(VOLUME_LOGICAL_OFFSET).
Caller inserts the <a href="storage.volume_logical_offset">VOLUME_LOGICAL_OFFSET</a> structure containing the logical offset at the beginning of the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>. </p>Caller inserts the <a href="storage.volume_logical_offset">VOLUME_LOGICAL_OFFSET</a><b>VOLUME_LOGICAL_OFFSET</b>VOLUME_LOGICAL_OFFSET structure containing the logical offset at the beginning of the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer. 


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
<b>Parameters.DeviceIoControl.OutputBufferLength</b> in the I/O stack location of the IRP indicates the size, in bytes, of the output buffer.
<b>Parameters.DeviceIoControl.OutputBufferLength</b>Parameters.DeviceIoControl.OutputBufferLength in the I/O stack location of the IRP indicates the size, in bytes, of the output buffer.
The output buffer size must be large enough to hold the structure <a href="storage.volume_physical_offsets">VOLUME_PHYSICAL_OFFSETS</a>, which contains a variable-length array of structures of type <a href="storage.volume_physical_offset">VOLUME_PHYSICAL_OFFSET</a>. </p>The output buffer size must be large enough to hold the structure <a href="storage.volume_physical_offsets">VOLUME_PHYSICAL_OFFSETS</a><b>VOLUME_PHYSICAL_OFFSETS</b>VOLUME_PHYSICAL_OFFSETS, which contains a variable-length array of structures of type <a href="storage.volume_physical_offset">VOLUME_PHYSICAL_OFFSET</a><b>VOLUME_PHYSICAL_OFFSET</b>VOLUME_PHYSICAL_OFFSET. 
The volume manager returns one or more physical offsets and disk numbers in the VOLUME_PHYSICAL_OFFSETS structure at the beginning of the buffer, at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>. </p>The volume manager returns one or more physical offsets and disk numbers in the VOLUME_PHYSICAL_OFFSETS structure at the beginning of the buffer, at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer. 


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
If the operation is successful, the <b>Status</b> member is set to STATUS_SUCCESS. Otherwise, the <b>Status</b> member is set to the appropriate error code. Possible error codes include the following: </p>If the operation is successful, the <b>Status</b>Status member is set to STATUS_SUCCESS. Otherwise, the <b>Status</b>Status member is set to the appropriate error code. Possible error codes include the following: 


<dl>
<dt><a id="STATUS_INVALID_PARAMETER"></a><a id="status_invalid_parameter"></a>STATUS_INVALID_PARAMETER</dt>
<dd>
The input buffer is too small. 

</dd>
</dl>
<dt><a id="STATUS_INVALID_PARAMETER"></a><a id="status_invalid_parameter"></a>STATUS_INVALID_PARAMETER</dt><a id="STATUS_INVALID_PARAMETER"></a><a id="status_invalid_parameter"></a>STATUS_INVALID_PARAMETER
<dd>
The input buffer is too small. 

</dd>
The input buffer is too small. </p>The input buffer is too small. 




<dl>
<dt><a id="STATUS_BUFFER_TOO_SMALL_"></a><a id="status_buffer_too_small_"></a>STATUS_BUFFER_TOO_SMALL </dt>
<dd>
The output buffer is too small. The volume manager sets the <b>Irp-&gt;IoStatus.Information</b> member to the size of the output buffer the caller should have provided. 

</dd>
</dl>
<dt><a id="STATUS_BUFFER_TOO_SMALL_"></a><a id="status_buffer_too_small_"></a>STATUS_BUFFER_TOO_SMALL </dt><a id="STATUS_BUFFER_TOO_SMALL_"></a><a id="status_buffer_too_small_"></a>STATUS_BUFFER_TOO_SMALL 
<dd>
The output buffer is too small. The volume manager sets the <b>Irp-&gt;IoStatus.Information</b> member to the size of the output buffer the caller should have provided. 

</dd>
The output buffer is too small. The volume manager sets the <b>Irp-&gt;IoStatus.Information</b> member to the size of the output buffer the caller should have provided. </p>The output buffer is too small. The volume manager sets the <b>Irp-&gt;IoStatus.Information</b>Irp->IoStatus.Information member to the size of the output buffer the caller should have provided. 


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows XP.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ntddvol.h (include Ntddvol.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ntddvol\ni-ntddvol-ioctl_volume_physical_to_logical.md">IOCTL_VOLUME_PHYSICAL_TO_LOGICAL</a>
</dt>
<dt>
<a href="storage.volume_logical_offset">VOLUME_LOGICAL_OFFSET</a>
</dt>
<dt>
<a href="storage.volume_physical_offsets">VOLUME_PHYSICAL_OFFSETS</a>
</dt>
<dt>
<a href="storage.volume_physical_offset">VOLUME_PHYSICAL_OFFSET</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_VOLUME_LOGICAL_TO_PHYSICAL control code%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

