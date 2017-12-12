---
UID: NI.ntddcdrm.IOCTL_CDROM_SET_SPEED
title: IOCTL_CDROM_SET_SPEED
author: windows-driver-content
description: Sets the spindle speed of the CD-ROM drive.
old-location: storage\ioctl_cdrom_set_speed.htm
old-project: storage
ms.assetid: 14acc5f4-1346-4da4-b692-01396cff776e
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: _WRITE_ROTATION, WRITE_ROTATION, *PWRITE_ROTATION
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



## -ioctlparameters

### -input-buffer
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains either a <a href="storage.cdrom_set_speed">CDROM_SET_SPEED</a> structure or a <a href="storage.cdrom_set_streaming">CDROM_SET_STREAMING</a> structure. These two structures have the same first member: an <a href="storage.cdrom_speed_request">CDROM_SPEED_REQUEST</a> enumeration value. Caller uses this enumeration value to specify which of these two structures is in the input buffer.


### -input-buffer-length
<b>Parameters.DeviceIoControl.InputBufferLength</b> in the I/O stack location indicates the size, in bytes, of the buffer.


### -output-buffer
None.


### -output-buffer-length
None.


### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
The <b>Information</b> field is set to zero. The <b>Status</b> field is set to STATUS_SUCCESS, if the operation succeeds, to STATUS_INFO_LENGTH_MISMATCH (ERROR_BAD_LENGTH) if the input buffer was too small, to STATUS_INVALID_DEVICE_REQUEST (ERROR_INVALID_FUNCTION), if the device does not support the request, or the device is not a Mount Ranier reWriteable (MRW)-compliant device, and to STATUS_INVALID_PARAMETER (ERROR_INVALID_PARAMETER, if the indicated request type is invalid.


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