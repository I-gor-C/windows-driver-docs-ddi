---
UID: NF.ks.KsStreamPointerCancelTimeout
title: KsStreamPointerCancelTimeout
author: windows-driver-content
description: The KsStreamPointerCancelTimeout function cancels a previously scheduled time-out callback on the specified stream pointer.
old-location: stream\ksstreampointercanceltimeout.htm
old-project: stream
ms.assetid: 9e1dd010-0074-45fb-b3cb-f8ea7ad15e02
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsStreamPointerCancelTimeout
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsStreamPointerCancelTimeout
req.alt-loc: Ks.lib,Ks.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ks.lib
req.dll: 
req.irql: <=DISPATCH_LEVEL
req.iface: 
---

# KsStreamPointerCancelTimeout function



## -description
<p>The<b> KsStreamPointerCancelTimeout </b>function cancels a previously scheduled time-out callback on the specified stream pointer.</p>


## -syntax

````
void KsStreamPointerCancelTimeout(
  _In_ PKSSTREAM_POINTER StreamPointer
);
````


## -parameters
<dl>

### -param <i>StreamPointer</i> [in]

<dd>
<p>A pointer to a <a href="https://msdn.microsoft.com/library/windows/hardware/ff567139">KSSTREAM_POINTER</a> structure representing the stream pointer for which to cancel a registered time-out callback.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Minidrivers should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff567135">KsStreamPointerScheduleTimeout</a> to schedule a time-out callback on a specified stream pointer.</p>

<p>The <b>KsStreamPointerCancelTimeout</b> function does not affect stream pointers that have no currently scheduled time-out callback.</p>

<p>Minidrivers should use <a href="https://msdn.microsoft.com/library/windows/hardware/ff567135">KsStreamPointerScheduleTimeout</a> to schedule a time-out callback on a specified stream pointer.</p>

<p>The <b>KsStreamPointerCancelTimeout</b> function does not affect stream pointers that have no currently scheduled time-out callback.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ks.h (include Ks.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ks.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;=DISPATCH_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff567135">KsStreamPointerScheduleTimeout</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563512">KsPinGetFirstCloneStreamPointer</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsStreamPointerCancelTimeout function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
