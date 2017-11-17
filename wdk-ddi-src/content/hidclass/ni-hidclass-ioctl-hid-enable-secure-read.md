---
UID: NI.hidclass.IOCTL_HID_ENABLE_SECURE_READ
title: IOCTL_HID_ENABLE_SECURE_READ
author: windows-driver-content
description: The IOCTL_HID_ENABLE_SECURE_READ request enables a secure read for open files of a HID collection.
old-location: hid\ioctl_hid_enable_secure_read.htm
ms.assetid: 9ec1c4e9-8c98-4772-8657-3392ff0827b5
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: ioctl
ms.prod: windows-hardware
ms.technology: hid
req.header: hidclass.h
req.include-header: Hidclass.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_HID_ENABLE_SECURE_READ
req.alt-loc: hidclass.h
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
ms.keywords: HDAUDIO_STREAM_FORMAT, HDAUDIO_STREAM_FORMAT, *PHDAUDIO_STREAM_FORMAT
req.iface: 
---

# IOCTL_HID_ENABLE_SECURE_READ IOCTL



## -description
<p>The IOCTL_HID_ENABLE_SECURE_READ request enables a secure read for open files of a <a href="https://msdn.microsoft.com/2d3efb38-4eba-43db-8cff-9fac30209952">HID collection</a>. Only a "trusted" user-mode application (an application with SeTcbPrivilege privileges) can successfully use this request. Kernel-mode drivers have SeTcbPrivilege privileges by default, but user-mode applications do not.</p>
<p>A client uses an <a href="https://msdn.microsoft.com/library/windows/hardware/ff541077">IOCTL_HID_DISABLE_SECURE_READ</a> request to cancel an enable secure read request.</p>
<p>For information about how to use enable and disable secure read requests to enforce a secure read for a collection, see <a href="NULL">Enforcing a Secure Read For a HID Collection</a>.</p>


## -ioctlparameters

### -input-buffer
<p>
       None.</p>

### -input-buffer-length
<p>None.</p>

<p>None.</p>

### -output-buffer
<p>
       None.</p>

<p>
       None.</p>

<p>
       None.</p>

### -output-buffer-length
<p>None.</p>

<p>None.</p>

<p>None.</p>

<p>None.</p>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p>The HID class driver sets the <b>Status</b> field of <b>Irp-&gt;IoStatus</b> to STATUS_SUCCESS if the requester has SeTcbPrivilege privileges and the file is valid. Otherwise, it sets the <b>Status</b> field to STATUS_PRIVILEGE_NOT_HELD.</p>

<p>The HID class driver sets the <b>Status</b> field of <b>Irp-&gt;IoStatus</b> to STATUS_SUCCESS if the requester has SeTcbPrivilege privileges and the file is valid. Otherwise, it sets the <b>Status</b> field to STATUS_PRIVILEGE_NOT_HELD.</p>

<p>The HID class driver sets the <b>Status</b> field of <b>Irp-&gt;IoStatus</b> to STATUS_SUCCESS if the requester has SeTcbPrivilege privileges and the file is valid. Otherwise, it sets the <b>Status</b> field to STATUS_PRIVILEGE_NOT_HELD.</p>

<p>The HID class driver sets the <b>Status</b> field of <b>Irp-&gt;IoStatus</b> to STATUS_SUCCESS if the requester has SeTcbPrivilege privileges and the file is valid. Otherwise, it sets the <b>Status</b> field to STATUS_PRIVILEGE_NOT_HELD.</p>

<p>The HID class driver sets the <b>Status</b> field of <b>Irp-&gt;IoStatus</b> to STATUS_SUCCESS if the requester has SeTcbPrivilege privileges and the file is valid. Otherwise, it sets the <b>Status</b> field to STATUS_PRIVILEGE_NOT_HELD.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Hidclass.h (include Hidclass.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541077">IOCTL_HID_DISABLE_SECURE_READ</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20IOCTL_HID_ENABLE_SECURE_READ control code%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
