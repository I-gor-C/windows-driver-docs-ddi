---
UID: NI.kbdmou.IOCTL_INTERNAL_MOUSE_DISCONNECT
title: IOCTL_INTERNAL_MOUSE_DISCONNECT
author: windows-driver-content
description: The IOCTL_INTERNAL_MOUSE_DISCONNECT request is completed by Moufiltr with an error status of STATUS_NOT_IMPLEMENTED.
old-location: hid\ioctl_internal_mouse_disconnect.htm
old-project: hid
ms.assetid: e62c61e7-ef64-4939-ad24-686d137b6319
ms.author: windowsdriverdev
ms.date: 11/20/2017
ms.keywords: MSiSCSI_SessionStatistics, MSiSCSI_SessionStatistics, *PMSiSCSI_SessionStatistics
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: kbdmou.h
req.include-header: Kbdmou.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_INTERNAL_MOUSE_DISCONNECT
req.alt-loc: kbdmou.h
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
req.iface: 
---

# IOCTL_INTERNAL_MOUSE_DISCONNECT IOCTL



## -description
<p>The IOCTL_INTERNAL_MOUSE_DISCONNECT request is completed by Moufiltr with an error status of STATUS_NOT_IMPLEMENTED. (Note that a Plug and Play mouse device can be added or removed by the Plug and Play manager.)</p>


## -ioctlparameters

### -input-buffer
<p>None.</p>

### -input-buffer-length
<p>None.</p>

<p>None.</p>

### -output-buffer
<p>None.</p>

<p>None.</p>

<p>None.</p>

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
<p>The <b>Status</b> member is set to STATUS_NOT_IMPLEMENTED.</p>

<p>The <b>Status</b> member is set to STATUS_NOT_IMPLEMENTED.</p>

<p>The <b>Status</b> member is set to STATUS_NOT_IMPLEMENTED.</p>

<p>The <b>Status</b> member is set to STATUS_NOT_IMPLEMENTED.</p>

<p>The <b>Status</b> member is set to STATUS_NOT_IMPLEMENTED.</p>

## -remarks


## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Kbdmou.h (include Kbdmou.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff541294">IOCTL_INTERNAL_MOUSE_CONNECT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [hid\hid]:%20IOCTL_INTERNAL_MOUSE_DISCONNECT control code%20 RELEASE:%20(11/20/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
