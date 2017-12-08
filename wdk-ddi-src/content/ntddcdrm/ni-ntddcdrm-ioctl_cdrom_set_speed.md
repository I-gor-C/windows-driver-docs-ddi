---
UID: NI.ntddcdrm.IOCTL_CDROM_SET_SPEED
title: IOCTL_CDROM_SET_SPEED
author: windows-driver-content
description: Sets the spindle speed of the CD-ROM drive.
old-location: storage\ioctl_cdrom_set_speed.htm
old-project: storage
ms.assetid: 14acc5f4-1346-4da4-b692-01396cff776e
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
req.alt-api: IOCTL_CDROM_SET_SPEED
req.alt-loc: Ntddcdrm.h
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

# IOCTL_CDROM_SET_SPEED IOCTL



## -description
Sets the spindle speed of the CD-ROM drive.
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains either a <a href="storage.cdrom_set_speed">CDROM_SET_SPEED</a> structure or a <a href="storage.cdrom_set_streaming">CDROM_SET_STREAMING</a> structure. These two structures have the same first member: an <a href="storage.cdrom_speed_request">CDROM_SPEED_REQUEST</a> enumeration value. Caller uses this enumeration value to specify which of these two structures is in the input buffer.
<b>Parameters.DeviceIoControl.InputBufferLength</b> in the I/O stack location indicates the size, in bytes, of the buffer.
None.
The <b>Information</b> field is set to zero. The <b>Status</b> field is set to STATUS_SUCCESS, if the operation succeeds, to STATUS_INFO_LENGTH_MISMATCH (ERROR_BAD_LENGTH) if the input buffer was too small, to STATUS_INVALID_DEVICE_REQUEST (ERROR_INVALID_FUNCTION), if the device does not support the request, or the device is not a Mount Ranier reWriteable (MRW)-compliant device, and to STATUS_INVALID_PARAMETER (ERROR_INVALID_PARAMETER, if the indicated request type is invalid.


## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains either a <a href="storage.cdrom_set_speed">CDROM_SET_SPEED</a> structure or a <a href="storage.cdrom_set_streaming">CDROM_SET_STREAMING</a> structure. These two structures have the same first member: an <a href="storage.cdrom_speed_request">CDROM_SPEED_REQUEST</a> enumeration value. Caller uses this enumeration value to specify which of these two structures is in the input buffer.The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer contains either a <a href="storage.cdrom_set_speed">CDROM_SET_SPEED</a><b>CDROM_SET_SPEED</b>CDROM_SET_SPEED structure or a <a href="storage.cdrom_set_streaming">CDROM_SET_STREAMING</a><b>CDROM_SET_STREAMING</b>CDROM_SET_STREAMING structure. These two structures have the same first member: an <a href="storage.cdrom_speed_request">CDROM_SPEED_REQUEST</a><b>CDROM_SPEED_REQUEST</b>CDROM_SPEED_REQUEST enumeration value. Caller uses this enumeration value to specify which of these two structures is in the input buffer.
<b>Parameters.DeviceIoControl.InputBufferLength</b> in the I/O stack location indicates the size, in bytes, of the buffer.
<b>Parameters.DeviceIoControl.InputBufferLength</b>Parameters.DeviceIoControl.InputBufferLength in the I/O stack location indicates the size, in bytes, of the buffer.


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
None.None.


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
The <b>Information</b> field is set to zero. The <b>Status</b> field is set to STATUS_SUCCESS, if the operation succeeds, to STATUS_INFO_LENGTH_MISMATCH (ERROR_BAD_LENGTH) if the input buffer was too small, to STATUS_INVALID_DEVICE_REQUEST (ERROR_INVALID_FUNCTION), if the device does not support the request, or the device is not a Mount Ranier reWriteable (MRW)-compliant device, and to STATUS_INVALID_PARAMETER (ERROR_INVALID_PARAMETER, if the indicated request type is invalid.The <b>Information</b>Information field is set to zero. The <b>Status</b>Status field is set to STATUS_SUCCESS, if the operation succeeds, to STATUS_INFO_LENGTH_MISMATCH (ERROR_BAD_LENGTH) if the input buffer was too small, to STATUS_INVALID_DEVICE_REQUEST (ERROR_INVALID_FUNCTION), if the device does not support the request, or the device is not a Mount Ranier reWriteable (MRW)-compliant device, and to STATUS_INVALID_PARAMETER (ERROR_INVALID_PARAMETER, if the indicated request type is invalid.


## -remarks
For an explanation of function and purpose of this request, see <a href="storage.cd_rom_set_speed">CD-ROM Set Speed</a>.

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