---
UID: NI.ntddcdrm.IOCTL_CDROM_SEEK_AUDIO_MSF
title: IOCTL_CDROM_SEEK_AUDIO_MSF
author: windows-driver-content
description: Moves the heads to the specified MSF on the media. Obsolete, beginning with Windows Vista.
old-location: storage\ioctl_cdrom_seek_audio_msf.htm
old-project: storage
ms.assetid: 081a5d8d-7cc7-4499-9360-dfaa5a7c436b
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: _WRITE_ROTATION, *PWRITE_ROTATION, WRITE_ROTATION
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddcdrm.h
req.include-header: Ntddcdrm.h
req.target-type: Windows
req.target-min-winverclnt: Obsolete, beginning with Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_CDROM_SEEK_AUDIO_MSF
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

# IOCTL_CDROM_SEEK_AUDIO_MSF IOCTL



## -description

Moves the heads to the specified MSF on the media.  Obsolete, beginning with Windows Vista.

Moves the heads to the specified MSF on the media.  Obsolete, beginning with Windows Vista.


## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
The buffer at <i>Irp-&gt;AssociatedIrp.SystemBuffer</i> contains the <a href="storage.cdrom_seek_audio_msf">CDROM_SEEK_AUDIO_MSF</a> specification. <i>Parameters.DeviceIoControl.InputBufferLength</i> indicates the size, in bytes, of the buffer.The buffer at <i>Irp-&gt;AssociatedIrp.SystemBuffer</i>Irp->AssociatedIrp.SystemBuffer contains the <a href="storage.cdrom_seek_audio_msf">CDROM_SEEK_AUDIO_MSF</a><b>CDROM_SEEK_AUDIO_MSF</b>CDROM_SEEK_AUDIO_MSF specification. <i>Parameters.DeviceIoControl.InputBufferLength</i>Parameters.DeviceIoControl.InputBufferLength indicates the size, in bytes, of the buffer.


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
The <b>Information</b> field is set to zero. The <b>Status</b> field is set to STATUS_SUCCESS, or possibly to STATUS_BUFFER_TOO_SMALL, STATUS_INVALID_DEVICE_REQUEST, STATUS_IO_DEVICE_ERROR, STATUS_NO_MEDIA_IN_DEVICE, STATUS_DEVICE_NOT_READY, STATUS_IO_TIME_OUT, or STATUS_VERIFY_REQUIRED.The <b>Information</b>Information field is set to zero. The <b>Status</b>Status field is set to STATUS_SUCCESS, or possibly to STATUS_BUFFER_TOO_SMALL, STATUS_INVALID_DEVICE_REQUEST, STATUS_IO_DEVICE_ERROR, STATUS_NO_MEDIA_IN_DEVICE, STATUS_DEVICE_NOT_READY, STATUS_IO_TIME_OUT, or STATUS_VERIFY_REQUIRED.


## -remarks
Beginning with Windows Vista, CDROM class drivers do not use this IOCTL. Prior to Windows Vista, this IOCTL was used for audio playback on older CD-ROM drives that supported direct audio output in hardware.

Client applications should use the <i>Media Control Interface (MCI) API</i> rather than issuing this IOCTL.

## -requirements
<table>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Obsolete, beginning with Windows Vista.
</td>
</tr>
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
<a href="storage.cdrom_seek_audio_msf">CDROM_SEEK_AUDIO_MSF</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_CDROM_SEEK_AUDIO_MSF control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
