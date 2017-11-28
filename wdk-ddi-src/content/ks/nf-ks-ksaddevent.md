---
UID: NF.ks.KsAddEvent
title: KsAddEvent
author: windows-driver-content
description: The KsAddEvent function adds an event to Object's event list.
old-location: stream\ksaddevent.htm
old-project: stream
ms.assetid: 75c909b1-8eb5-4887-b528-d3ac465ee12b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: KsAddEvent
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
req.alt-api: KsAddEvent
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
req.irql: PASSIVE_LEVEL
req.iface: 
---

# KsAddEvent function



## -description
<p>The<b> KsAddEvent </b>function adds an event to <i>Object</i>'s event list.</p>


## -syntax

````
void KsAddEvent(
  _In_ PVOID          Object,
  _In_ PKSEVENT_ENTRY EventEntry
);
````


## -parameters
<dl>

### -param <i>Object</i> [in]

<dd>
<p>The object to which to add the event.</p>
</dd>

### -param <i>EventEntry</i> [in]

<dd>
<p>A pointer to an <a href="https://msdn.microsoft.com/library/windows/hardware/ff561853">KSEVENT_ENTRY</a> structure describing the event to add to <i>Object</i>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Minidrivers typically do not call this routine directly; instead, they use <a href="https://msdn.microsoft.com/library/windows/hardware/ff562525">KsFilterAddEvent</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff563490">KsPinAddEvent</a>. </p>

<p>After events have been added to the event list, these events can be generated as data events by a <b>Ks</b><i>Xxx</i><b>GenerateEvents</b> call. Typecasting of the object (a filter or pin) to PVOID must be provided by the caller.</p>

<p>Minidrivers typically do not call this routine directly; instead, they use <a href="https://msdn.microsoft.com/library/windows/hardware/ff562525">KsFilterAddEvent</a> or <a href="https://msdn.microsoft.com/library/windows/hardware/ff563490">KsPinAddEvent</a>. </p>

<p>After events have been added to the event list, these events can be generated as data events by a <b>Ks</b><i>Xxx</i><b>GenerateEvents</b> call. Typecasting of the object (a filter or pin) to PVOID must be provided by the caller.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562525">KsFilterAddEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563490">KsPinAddEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561662">KsDefaultAddEventHandler</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562597">KsGenerateEvents</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561853">KSEVENT_ENTRY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsAddEvent function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
