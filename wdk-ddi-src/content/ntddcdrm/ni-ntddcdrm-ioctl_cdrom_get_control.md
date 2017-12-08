---
UID: NI.ntddcdrm.IOCTL_CDROM_GET_CONTROL
title: IOCTL_CDROM_GET_CONTROL
author: windows-driver-content
description: This IOCTL request is obsolete. Do not use.Determines the current audio playback mode.
old-location: storage\ioctl_cdrom_get_control.htm
old-project: storage
ms.assetid: 3d474eb7-6622-48fd-bf40-c17d03933828
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
req.alt-api: IOCTL_CDROM_GET_CONTROL
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

# IOCTL_CDROM_GET_CONTROL IOCTL



## -description

This IOCTL request is obsolete. Do not use.
Determines the current audio playback mode. 

This IOCTL request is obsolete. Do not use.
Determines the current audio playback mode. 


## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
<b>Parameters.DeviceIoControl.OutputBufferLength</b> in the I/O stack location indicates the size, in bytes, of the buffer, which must be &gt;= <b>sizeof</b>(CDROM_AUDIO_CONTROL).
<b>Parameters.DeviceIoControl.OutputBufferLength</b>Parameters.DeviceIoControl.OutputBufferLength in the I/O stack location indicates the size, in bytes, of the buffer, which must be >= <b>sizeof</b>sizeof(CDROM_AUDIO_CONTROL).


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
The driver returns the <a href="storage.cdrom_audio_control">CDROM_AUDIO_CONTROL</a> data in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>.The driver returns the <a href="storage.cdrom_audio_control">CDROM_AUDIO_CONTROL</a><b>CDROM_AUDIO_CONTROL</b>CDROM_AUDIO_CONTROL data in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer.


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
The <b>Information</b> field is set to the number of bytes returned. The <b>Status</b> field is set to STATUS_SUCCESS, or possibly to STATUS_BUFFER_TOO_SMALL, STATUS_DEVICE_NOT_READY, STATUS_IO_DEVICE_ERROR, STATUS_IO_TIMEOUT, STATUS_INSUFFICIENT_RESOURCES, STATUS_VERIFY_REQUIRED, or STATUS_INVALID_DEVICE_REQUEST.The <b>Information</b>Information field is set to the number of bytes returned. The <b>Status</b>Status field is set to STATUS_SUCCESS, or possibly to STATUS_BUFFER_TOO_SMALL, STATUS_DEVICE_NOT_READY, STATUS_IO_DEVICE_ERROR, STATUS_IO_TIMEOUT, STATUS_INSUFFICIENT_RESOURCES, STATUS_VERIFY_REQUIRED, or STATUS_INVALID_DEVICE_REQUEST.


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
<a href="storage.cdrom_audio_control">CDROM_AUDIO_CONTROL</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_CDROM_GET_CONTROL control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
