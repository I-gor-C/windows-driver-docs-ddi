---
UID: NI.ntdddisk.IOCTL_DISK_GET_DRIVE_GEOMETRY_EX
title: IOCTL_DISK_GET_DRIVE_GEOMETRY_EX
author: windows-driver-content
description: Returns information about the physical disk's geometry (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).The difference between IOCTL_DISK_GET_DRIVE_GEOMETRY_EX and the older IOCTL_DISK_GET_DRIVE_GEOMETRY request is that IOCTL_DISK_GET_DRIVE_GEOMETRY_EX can retrieve information from both Master Boot Record (MBR) and GUID Partition Table (GPT)-type partitioned media, whereas IOCTL_DISK_GET_DRIVE_GEOMETRY can only read MBR-style media.
old-location: storage\ioctl_disk_get_drive_geometry_ex.htm
old-project: storage
ms.assetid: c0cf6b73-3283-4a58-845a-79f3b078db46
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: _DETECTION_TYPE, DETECTION_TYPE
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntdddisk.h
req.include-header: Ntdddisk.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_DISK_GET_DRIVE_GEOMETRY_EX
req.alt-loc: Ntdddisk.h
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

# IOCTL_DISK_GET_DRIVE_GEOMETRY_EX IOCTL



## -description

Returns information about the physical disk's geometry (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).
The difference between IOCTL_DISK_GET_DRIVE_GEOMETRY_EX and the older <a href="..\ntdddisk\ni-ntdddisk-ioctl_disk_get_drive_geometry.md">IOCTL_DISK_GET_DRIVE_GEOMETRY</a> request is that IOCTL_DISK_GET_DRIVE_GEOMETRY_EX can retrieve information from both Master Boot Record (MBR) and GUID Partition Table (GPT)-type partitioned media, whereas IOCTL_DISK_GET_DRIVE_GEOMETRY can only read MBR-style media. 

Returns information about the physical disk's geometry (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).
The difference between IOCTL_DISK_GET_DRIVE_GEOMETRY_EX and the older <a href="..\ntdddisk\ni-ntdddisk-ioctl_disk_get_drive_geometry.md">IOCTL_DISK_GET_DRIVE_GEOMETRY</a> request is that IOCTL_DISK_GET_DRIVE_GEOMETRY_EX can retrieve information from both Master Boot Record (MBR) and GUID Partition Table (GPT)-type partitioned media, whereas IOCTL_DISK_GET_DRIVE_GEOMETRY can only read MBR-style media. 


## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
<b>Parameters.DeviceIoControl.OutputBufferLength</b> in the I/O stack location of the IRP indicates the size, in bytes, of the buffer, which must be at least (<b>sizeof</b>(DISK_GEOMETRY) + <b>sizeof</b>(LARGE_INTEGER)) and up to (<b>sizeof</b>(DISK_GEOMETRY) + <b>sizeof</b>(LARGE_INTEGER) + <b>sizeof</b>(DISK_PARTITION_INFO) + <b>sizeof</b>(DISK_DETECTION_INFO)).
<b>Parameters.DeviceIoControl.OutputBufferLength</b>Parameters.DeviceIoControl.OutputBufferLength in the I/O stack location of the IRP indicates the size, in bytes, of the buffer, which must be at least (<b>sizeof</b>sizeof(DISK_GEOMETRY) + <b>sizeof</b>sizeof(LARGE_INTEGER)) and up to (<b>sizeof</b>sizeof(DISK_GEOMETRY) + <b>sizeof</b>sizeof(LARGE_INTEGER) + <b>sizeof</b>sizeof(DISK_PARTITION_INFO) + <b>sizeof</b>sizeof(DISK_DETECTION_INFO)).


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
The driver returns the <a href="storage.disk_geometry_ex">DISK_GEOMETRY_EX</a> data in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>. The size of the output buffer may not be the same size as the input buffer.The driver returns the <a href="storage.disk_geometry_ex">DISK_GEOMETRY_EX</a><b>DISK_GEOMETRY_EX</b>DISK_GEOMETRY_EX data in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer. The size of the output buffer may not be the same size as the input buffer.


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
The <b>Information</b> field is set to the size, in bytes, of the returned data. The <b>Information</b>Information field is set to the size, in bytes, of the returned data. 
The <b>Status</b> field returns one of the following values:The <b>Status</b>Status field returns one of the following values:
<ul>
<li><b>STATUS_SUCCESS</b></li>
<li><b>STATUS_UNRECOGNIZED_MEDIA</b></li>
<li><b>STATUS_INVALID_PARAMETER</b></li>
<li><b>STATUS_INVALID_DEVICE_REQUEST</b></li>
<li><b>STATUS_INFO_LENGTH_MISMATCH</b></li>
<li><b>STATUS_INSUFFICIENT_RESOURCES</b></li>
<li><b>STATUS_BUFFER_TOO_SMALL</b></li>
</ul>
<li><b>STATUS_SUCCESS</b></li><b>STATUS_SUCCESS</b>STATUS_SUCCESS
<li><b>STATUS_UNRECOGNIZED_MEDIA</b></li><b>STATUS_UNRECOGNIZED_MEDIA</b>STATUS_UNRECOGNIZED_MEDIA
<li><b>STATUS_INVALID_PARAMETER</b></li><b>STATUS_INVALID_PARAMETER</b>STATUS_INVALID_PARAMETER
<li><b>STATUS_INVALID_DEVICE_REQUEST</b></li><b>STATUS_INVALID_DEVICE_REQUEST</b>STATUS_INVALID_DEVICE_REQUEST
<li><b>STATUS_INFO_LENGTH_MISMATCH</b></li><b>STATUS_INFO_LENGTH_MISMATCH</b>STATUS_INFO_LENGTH_MISMATCH
<li><b>STATUS_INSUFFICIENT_RESOURCES</b></li><b>STATUS_INSUFFICIENT_RESOURCES</b>STATUS_INSUFFICIENT_RESOURCES
<li><b>STATUS_BUFFER_TOO_SMALL</b></li><b>STATUS_BUFFER_TOO_SMALL</b>STATUS_BUFFER_TOO_SMALL

## -remarks
Only callers above Partmgr.sys may call this IOCTL as it contains disk partition information. 

This IOCTL uses <a href="https://msdn.microsoft.com/library/windows/hardware/ff560357">IOCTL_DISK_GET_DRIVE_GEOMETRY</a> to get the <a href="storage.disk_geometry">DISK_GEOMETRY</a> structure and <a href="..\ntdddisk\ni-ntdddisk-ioctl_disk_get_length_info.md">IOCTL_DISK_GET_LENGTH_INFO</a> to get the  <a href="storage.get_length_information">GET_LENGTH_INFORMATION</a> structure. Both of these IOCTL's are supported for use at the disk.sys level. 

## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntdddisk.h (include Ntdddisk.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.disk_geometry_ex">DISK_GEOMETRY_EX</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560357">IOCTL_DISK_GET_DRIVE_GEOMETRY</a>
</dt>
<dt>
<a href="..\ntdddisk\ni-ntdddisk-ioctl_disk_get_length_info.md">IOCTL_DISK_GET_LENGTH_INFO</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_DISK_GET_DRIVE_GEOMETRY_EX control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
