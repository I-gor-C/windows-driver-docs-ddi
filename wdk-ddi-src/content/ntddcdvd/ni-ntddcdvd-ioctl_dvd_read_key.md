---
UID: NI.ntddcdvd.IOCTL_DVD_READ_KEY
title: IOCTL_DVD_READ_KEY
author: windows-driver-content
description: Returns a copy-protection key of the specified type: challenge key, bus key, title key, read RPC key, set RPC key, or disk key.
old-location: storage\ioctl_dvd_read_key.htm
old-project: storage
ms.assetid: 42745dae-f472-4f64-8f16-9f4dec1e986a
ms.author: windowsdriverdev
ms.date: 11/15/2017
ms.keywords: DVD_STRUCTURE_FORMAT, *PDVD_STRUCTURE_FORMAT, DVD_STRUCTURE_FORMAT
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: ntddcdvd.h
req.include-header: Ntddcdvd.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_DVD_READ_KEY
req.alt-loc: Ntddcdvd.h
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

# IOCTL_DVD_READ_KEY IOCTL



## -description

Returns a copy-protection key of the specified type: challenge key, bus key, title key, read RPC key, set RPC key, or disk key. A challenge key or bus key is sent back to the device to complete the related step in a DVD authentication sequence. After the authentication sequence is completed, a title key is used to encrypt and decrypt user data transferred from a DVD disc and a disk key is used to encrypt and decrypt title key data. If the drive region has not been set previously (if it is still at factory default) and if the inserted media has a region, the device region will be set to the current media region.

Returns a copy-protection key of the specified type: challenge key, bus key, title key, read RPC key, set RPC key, or disk key. A challenge key or bus key is sent back to the device to complete the related step in a DVD authentication sequence. After the authentication sequence is completed, a title key is used to encrypt and decrypt user data transferred from a DVD disc and a disk key is used to encrypt and decrypt title key data. If the drive region has not been set previously (if it is still at factory default) and if the inserted media has a region, the device region will be set to the current media region.


## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains a <a href="storage.dvd_copy_protect_key">DVD_COPY_PROTECT_KEY</a> structure that indicates the session ID of the DVD session and the type of key to return. <b>Parameters.DeviceIoControl.OutputBufferLength</b> indicates the size, in bytes, of the buffer, which must be &gt;= the size of one of the following: DVD_CHALLENGE_KEY_LENGTH, DVD_BUS_KEY_LENGTH, DVD_TITLE_KEY_LENGTH, DVD_RPC_KEY_LENGTH, DVD_SET_RPC_KEY_LENGTH, or DVD_DISK_KEY_LENGTH. The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer contains a <a href="storage.dvd_copy_protect_key">DVD_COPY_PROTECT_KEY</a><b>DVD_COPY_PROTECT_KEY</b>DVD_COPY_PROTECT_KEY structure that indicates the session ID of the DVD session and the type of key to return. <b>Parameters.DeviceIoControl.OutputBufferLength</b>Parameters.DeviceIoControl.OutputBufferLength indicates the size, in bytes, of the buffer, which must be >= the size of one of the following: DVD_CHALLENGE_KEY_LENGTH, DVD_BUS_KEY_LENGTH, DVD_TITLE_KEY_LENGTH, DVD_RPC_KEY_LENGTH, DVD_SET_RPC_KEY_LENGTH, or DVD_DISK_KEY_LENGTH. 


### -input-buffer-length

<text></text>

### -output-buffer
<a id="Output_Buffer"></a><a id="output_buffer"></a><a id="OUTPUT_BUFFER"></a>Output Buffer
The driver returns the DVD_COPY_PROTECT_KEY data in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>.The driver returns the DVD_COPY_PROTECT_KEY data in the buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer.


### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
<a id="I_O_Status_Block"></a><a id="i_o_status_block"></a><a id="I_O_STATUS_BLOCK"></a>I/O Status Block
The <b>Information</b> field is set to the number of bytes transferred. The <b>Status</b> field is set to STATUS_SUCCESS, or possibly to STATUS_INSUFFICIENT_RESOURCES.The <b>Information</b>Information field is set to the number of bytes transferred. The <b>Status</b>Status field is set to STATUS_SUCCESS, or possibly to STATUS_INSUFFICIENT_RESOURCES.


## -remarks


## -requirements
<table>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ntddcdvd.h (include Ntddcdvd.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="storage.dvd_copy_protect_key">DVD_COPY_PROTECT_KEY</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_DVD_READ_KEY control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
