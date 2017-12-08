---
UID: NI.ntdddisk.IOCTL_DISK_UPDATE_DRIVE_SIZE
title: IOCTL_DISK_UPDATE_DRIVE_SIZE
author: windows-driver-content
description: Updates device extension with drive size information for current media.
old-location: storage\ioctl_disk_update_drive_size.htm
old-project: storage
ms.assetid: a12c1082-c3ff-40b8-b756-be320ab98b30
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
req.alt-api: IOCTL_DISK_UPDATE_DRIVE_SIZE
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

# IOCTL_DISK_UPDATE_DRIVE_SIZE IOCTL



## -description

Updates device extension with drive size information for current media.

Updates device extension with drive size information for current media.


## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
NoneNone


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
<b>Parameters.DeviceIoControl.OutputBufferLength</b> in the I/O stack location of the IRP indicates the size, in bytes, of the buffer made available to the driver, which must be &gt;= <b>sizeof</b>(DISK_GEOMETRY). Otherwise, the driver returns with an error status of STATUS_BUFFER_TOO_SMALL.
<b>Parameters.DeviceIoControl.OutputBufferLength</b>Parameters.DeviceIoControl.OutputBufferLength in the I/O stack location of the IRP indicates the size, in bytes, of the buffer made available to the driver, which must be >= <b>sizeof</b>sizeof(DISK_GEOMETRY). Otherwise, the driver returns with an error status of STATUS_BUFFER_TOO_SMALL.
The device driver returns the <a href="storage.disk_geometry">DISK_GEOMETRY</a> structure in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>. The device driver returns the <a href="storage.disk_geometry">DISK_GEOMETRY</a><b>DISK_GEOMETRY</b>DISK_GEOMETRY structure in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer. 


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
The <b>Information</b> field is set to the size of the block of disk geometry information being returned,  <b>sizeof</b>(DISK_GEOMETRY). The <b>Status</b> field is set to STATUS_SUCCESS, or possibly to STATUS_BUFFER_TOO_SMALL, STATUS_INSUFFICIENT_RESOURCES, STATUS_IO_DEVICE_ERROR, or STATUS_DEVICE_NOT_READY.The <b>Information</b>Information field is set to the size of the block of disk geometry information being returned,  <b>sizeof</b>sizeof(DISK_GEOMETRY). The <b>Status</b>Status field is set to STATUS_SUCCESS, or possibly to STATUS_BUFFER_TOO_SMALL, STATUS_INSUFFICIENT_RESOURCES, STATUS_IO_DEVICE_ERROR, or STATUS_DEVICE_NOT_READY.


## -remarks


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
<a href="storage.disk_geometry">DISK_GEOMETRY</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_DISK_UPDATE_DRIVE_SIZE control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
