---
UID: NI.ntddcdrm.IOCTL_CDROM_GET_DRIVE_GEOMETRY_EX
title: IOCTL_CDROM_GET_DRIVE_GEOMETRY_EX
author: windows-driver-content
description: Returns information about a CD-ROM's geometry (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).The IOCTL_CDROM_GET_DRIVE_GEOMETRY_EX request differs from the older IOCTL_CDROM_GET_DRIVE_GEOMETRY request.
old-location: storage\ioctl_cdrom_get_drive_geometry_ex.htm
old-project: storage
ms.assetid: ef04ba90-698f-4ae2-9ac6-106d66b61080
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: _WRITE_ROTATION, *PWRITE_ROTATION, WRITE_ROTATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddcdrm.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_CDROM_GET_DRIVE_GEOMETRY_EX
req.alt-loc: ntddcdrm.h
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

# IOCTL_CDROM_GET_DRIVE_GEOMETRY_EX IOCTL



## -description

Returns information about a CD-ROM's geometry (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).
The IOCTL_CDROM_GET_DRIVE_GEOMETRY_EX request differs from the older <a href="..\ntddcdrm\ni-ntddcdrm-ioctl_cdrom_get_drive_geometry.md">IOCTL_CDROM_GET_DRIVE_GEOMETRY</a> request. The IOCTL_CDROM_GET_DRIVE_GEOMETRY_EX request can retrieve information from both Master Boot Record (MBR) and GUID Partition Table (GPT) partitioned media. However, IOCTL_CDROM_GET_DRIVE_GEOMETRY can read only MBR-style media.

Returns information about a CD-ROM's geometry (media type, number of cylinders, tracks per cylinder, sectors per track, and bytes per sector).
The IOCTL_CDROM_GET_DRIVE_GEOMETRY_EX request differs from the older <a href="..\ntddcdrm\ni-ntddcdrm-ioctl_cdrom_get_drive_geometry.md">IOCTL_CDROM_GET_DRIVE_GEOMETRY</a> request. The IOCTL_CDROM_GET_DRIVE_GEOMETRY_EX request can retrieve information from both Master Boot Record (MBR) and GUID Partition Table (GPT) partitioned media. However, IOCTL_CDROM_GET_DRIVE_GEOMETRY can read only MBR-style media.


## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
<b>Parameters.DeviceIoControl.OutputBufferLength</b> in the IO_STACK_LOCATION structure of the IRP indicates the size, in bytes, of the buffer, which must be &gt;= <b>sizeof</b>(DISK_GEOMETRY_EX).
<b>Parameters.DeviceIoControl.OutputBufferLength</b>Parameters.DeviceIoControl.OutputBufferLength in the IO_STACK_LOCATION structure of the IRP indicates the size, in bytes, of the buffer, which must be >= <b>sizeof</b>sizeof(DISK_GEOMETRY_EX).


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
The driver returns the <a href="storage.disk_geometry_ex">DISK_GEOMETRY_EX</a>-type information in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>.The driver returns the <a href="storage.disk_geometry_ex">DISK_GEOMETRY_EX</a><b>DISK_GEOMETRY_EX</b>DISK_GEOMETRY_EX-type information in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer.


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
The <b>Information</b> field is set to the size, in bytes, of the returned data. The <b>Status</b> field is set to STATUS_SUCCESS, or possibly to STATUS_UNRECOGNIZED_MEDIA, STATUS_INVALID_PARAMETER, STATUS_INFO_LENGTH_MISMATCH, or STATUS_BUFFER_TOO_SMALL.The <b>Information</b>Information field is set to the size, in bytes, of the returned data. The <b>Status</b>Status field is set to STATUS_SUCCESS, or possibly to STATUS_UNRECOGNIZED_MEDIA, STATUS_INVALID_PARAMETER, STATUS_INFO_LENGTH_MISMATCH, or STATUS_BUFFER_TOO_SMALL.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntddcdrm.h (include Ntddcdrm.h)</dt>
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
<a href="..\ntdddisk\ni-ntdddisk-ioctl_disk_get_drive_geometry_ex.md">IOCTL_DISK_GET_DRIVE_GEOMETRY_EX</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_CDROM_GET_DRIVE_GEOMETRY_EX control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
