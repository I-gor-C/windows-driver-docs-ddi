---
UID: NF.ks.KsFilterAddEvent
title: KsFilterAddEvent
author: windows-driver-content
description: The KsFilterAddEvent function adds an event to Filter's event list.
old-location: stream\ksfilteraddevent.htm
old-project: stream
ms.assetid: e93491c1-bd6d-4d89-b55f-10439b0f5eec
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsFilterAddEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Desktop
req.target-min-winverclnt: Available in Microsoft Windows XP and later operating systems and DirectX 8.0 and later DirectX versions.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsFilterAddEvent
req.alt-loc: ks.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# KsFilterAddEvent function



## -description
<p>The<b> KsFilterAddEvent</b> function adds an event to <i>Filter</i>'s event list.</p>


## -syntax

````
void _inline KsFilterAddEvent(
  _In_ PKSFILTER      Filter,
  _In_ PKSEVENT_ENTRY EventEntry
);
````


## -parameters
<dl>

### -param <i>Filter</i> [in]

<dd>
<p><i>A pointer</i> to a <a href="..\ks\ns-ks--ksfilter.md">KSFILTER</a> structure representing the filter to which to add a specified event.</p>
</dd>

### -param <i>EventEntry</i> [in]

<dd>
<p><i>A pointer</i> to an <a href="..\ks\ns-ks--ksevent-entry.md">KSEVENT_ENTRY</a> structure describing the event to add to <i>Filter</i>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>This function is an inline function call to <a href="..\ks\nf-ks-ksaddevent.md">KsAddEvent</a>.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<a href="..\ks\nf-ks-ksaddevent.md">KsAddEvent</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksgenerateevents.md">KsGenerateEvents</a>
</dt>
<dt>
<a href="..\ks\ns-ks--ksevent-entry.md">KSEVENT_ENTRY</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFilterAddEvent function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
