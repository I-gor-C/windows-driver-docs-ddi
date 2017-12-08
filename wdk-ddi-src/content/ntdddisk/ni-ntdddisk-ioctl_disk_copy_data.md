---
UID: NI.ntdddisk.IOCTL_DISK_COPY_DATA
title: IOCTL_DISK_COPY_DATA
author: windows-driver-content
description: This IOCTL_DISK_COPY_DATA IOCTL is used to copy data from one area of the disk to another.
old-location: storage\ioctl_disk_copy_data.htm
old-project: storage
ms.assetid: 1434ee49-4c3d-4104-bca4-c0ea4299c9aa
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
req.alt-api: IOCTL_DISK_COPY_DATA
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

# IOCTL_DISK_COPY_DATA IOCTL



## -description

This IOCTL_DISK_COPY_DATA IOCTL is used to copy data from one area of the disk to another.

This IOCTL_DISK_COPY_DATA IOCTL is used to copy data from one area of the disk to another.
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains the <a href="storage.disk_copy_data_parameters">DISK_COPY_DATA_PARAMETERS</a> data. <b>Parameters.DeviceIoControl.InputBufferLength</b> in the I/O stack location of the IRP indicates the size, in bytes, of the buffer.
None
The <b>Status</b> field is set to STATUS_SUCCESS if the operation is successful.


## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains the <a href="storage.disk_copy_data_buffer">DISK_COPY_DATA_BUFFER</a> data. <b>Parameters.DeviceIoControl.InputBufferLength</b> in the I/O stack location of the IRP indicates the size, in bytes, of the buffer.The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer contains the <a href="storage.disk_copy_data_buffer">DISK_COPY_DATA_BUFFER</a><b>DISK_COPY_DATA_BUFFER</b>DISK_COPY_DATA_BUFFER data. <b>Parameters.DeviceIoControl.InputBufferLength</b>Parameters.DeviceIoControl.InputBufferLength in the I/O stack location of the IRP indicates the size, in bytes, of the buffer.


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
NoneNone


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
The <b>Status</b> field is set to STATUS_SUCCESS if the operation is successful.The <b>Status</b>Status field is set to STATUS_SUCCESS if the operation is successful.


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
<a href="storage.disk_copy_data_parameters">DISK_COPY_DATA_PARAMETERS</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_DISK_COPY_DATA control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
