---
UID: NI.ntddcdvd.IOCTL_DVD_SEND_KEY
title: IOCTL_DVD_SEND_KEY
author: windows-driver-content
description: Sends the specified key to a DVD device to complete the related step in an authentication sequence.This IOCTL has only read access to the device and cannot send keys that make alterations to the hardware configuration.
old-location: storage\ioctl_dvd_send_key.htm
old-project: storage
ms.assetid: 8db0e6fe-1dfc-4f26-8fd7-7d170c33da0a
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
req.alt-api: IOCTL_DVD_SEND_KEY
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

# IOCTL_DVD_SEND_KEY IOCTL



## -description

Sends the specified key to a DVD device to complete the related step in an authentication sequence.
This IOCTL has only read access to the device and cannot send keys that make alterations to the hardware configuration. Therefore, this request is limited to sending key types <b>DvdChallengeKey</b>, <b>DvdBusKey2</b>, and <b>DvdInvalidateAGID</b>. 
The <a href="..\ntddcdvd\ni-ntddcdvd-ioctl_dvd_send_key2.md">IOCTL_DVD_SEND_KEY2</a> request has write access to the device and is not limited to these three key types. 
For more information, see <a href="..\ntddcdvd\ne-ntddcdvd-dvd_key_type.md">DVD_KEY_TYPE</a>.

Sends the specified key to a DVD device to complete the related step in an authentication sequence.
This IOCTL has only read access to the device and cannot send keys that make alterations to the hardware configuration. Therefore, this request is limited to sending key types <b>DvdChallengeKey</b>, <b>DvdBusKey2</b>, and <b>DvdInvalidateAGID</b>. 
The <a href="..\ntddcdvd\ni-ntddcdvd-ioctl_dvd_send_key2.md">IOCTL_DVD_SEND_KEY2</a> request has write access to the device and is not limited to these three key types. 
For more information, see <a href="..\ntddcdvd\ne-ntddcdvd-dvd_key_type.md">DVD_KEY_TYPE</a>.


## -ioctlparameters

### -input-buffer
<a id="Input_Buffer"></a><a id="input_buffer"></a><a id="INPUT_BUFFER"></a>Input Buffer
The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b> contains a <a href="storage.dvd_copy_protect_key">DVD_COPY_PROTECT_KEY</a> structure that indicates the session ID, key type, and key to be sent to the device.The buffer at <b>Irp-&gt;AssociatedIrp.SystemBuffer</b>Irp->AssociatedIrp.SystemBuffer contains a <a href="storage.dvd_copy_protect_key">DVD_COPY_PROTECT_KEY</a><b>DVD_COPY_PROTECT_KEY</b>DVD_COPY_PROTECT_KEY structure that indicates the session ID, key type, and key to be sent to the device.


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
The <b>Information</b> field is set to zero. The <b>Status</b> field is set to STATUS_SUCCESS, or possibly to STATUS_INSUFFICIENT_RESOURCES.The <b>Information</b>Information field is set to zero. The <b>Status</b>Status field is set to STATUS_SUCCESS, or possibly to STATUS_INSUFFICIENT_RESOURCES.


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
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [storage\storage]:%20IOCTL_DVD_SEND_KEY control code%20 RELEASE:%20(11/15/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
