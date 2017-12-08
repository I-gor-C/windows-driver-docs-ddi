---
UID: NI.winsmcrd.IOCTL_SMARTCARD_SWALLOW
title: IOCTL_SMARTCARD_SWALLOW
author: windows-driver-content
description: The IOCTL_SMARTCARD_SWALLOW request causes the smart card reader to swallow the card.
old-location: smartcrd\ioctl_smartcard_swallow.htm
old-project: smartcrd
ms.assetid: c229769d-8798-436e-bd26-9dfd507fba9c
ms.author: windowsdriverdev
ms.date: 11/27/2017
ms.keywords: GdiStartPageEMF
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: ioctl
req.header: winsmcrd.h
req.include-header: Winsmcrd.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IOCTL_SMARTCARD_SWALLOW
req.alt-loc: Winsmcrd.h
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
req.product: Windows 10 or later.
---

# IOCTL_SMARTCARD_SWALLOW IOCTL



## -description
<p>
<p>The IOCTL_SMARTCARD_SWALLOW request causes the smart card reader to swallow the card.</p>
</p>
<p>The IOCTL_SMARTCARD_SWALLOW request causes the smart card reader to swallow the card.</p>


## -ioctlparameters

### -input-buffer
<p>None </p>

### -input-buffer-length

<text></text>

### -output-buffer
<p>None </p>

<p>None </p>

### -output-buffer-length

<text></text>

### -in-out-buffer

<text></text>

### -inout-buffer-length

<text></text>

### -status-block
I/O Status block
<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p>STATUS_SUCCESS</p>

<p>The smart card was swallowed.</p>

<p>STATUS_NO_MEDIA</p>

<p>No smart card is in the reader.</p>

<p>STATUS_IO_TIMEOUT</p>

<p>The operation timed out.</p>

<p>STATUS_NOT_SUPPORTED</p>

<p>The reader does not support swallowing.</p>

<p> </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p>STATUS_SUCCESS</p>

<p>The smart card was swallowed.</p>

<p>STATUS_NO_MEDIA</p>

<p>No smart card is in the reader.</p>

<p>STATUS_IO_TIMEOUT</p>

<p>The operation timed out.</p>

<p>STATUS_NOT_SUPPORTED</p>

<p>The reader does not support swallowing.</p>

<p> </p>

<p><b>Irp-&gt;IoStatus.Status</b> is set to <b>STATUS_SUCCESS</b> if the request is successful. Possible error codes are:</p>

<p>STATUS_SUCCESS</p>

<p>The smart card was swallowed.</p>

<p>STATUS_NO_MEDIA</p>

<p>No smart card is in the reader.</p>

<p>STATUS_IO_TIMEOUT</p>

<p>The operation timed out.</p>

<p>STATUS_NOT_SUPPORTED</p>

<p>The reader does not support swallowing.</p>

<p> </p>

## -remarks
<p>The <b>Information</b> member must be set to zero.</p>

<p>The <b>Status</b> member is set to one of the values in the status block table.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Winsmcrd.h (include Winsmcrd.h)</dt>
</dl>
</td>
</tr>
</table>