---
UID: NF.ks.KsDiscardEvent
title: KsDiscardEvent
author: windows-driver-content
description: The KsDiscardEvent function discards the memory used by an event entry after the objects have been dereferenced.
old-location: stream\ksdiscardevent.htm
old-project: stream
ms.assetid: 14aaf96a-4d1f-4e4a-9fed-e493090157b8
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsDiscardEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsDiscardEvent
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
req.irql: 
req.iface: 
---

# KsDiscardEvent function



## -description
<p>The <b>KsDiscardEvent</b> function discards the memory used by an event entry after the objects have been dereferenced. The function can be called when manually disabling events that have not been disabled by the event owner (by calling the <b>KsFreeEventList</b> function to disable events). For example, the function can be called when asynchronously enabling an event fails and the event entry needs to be discarded.</p>


## -syntax

````
VOID KsDiscardEvent(
  _In_ PKSEVENT_ENTRY EventEntry
);
````


## -parameters
<dl>

### -param <i>EventEntry</i> [in]

<dd>
<p>Specifies the pointer to the entry to discard. This pointer is no longer valid after a successful call to this function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Typically, the <b>KsDiscardEvent</b> function is automatically called by the <a href="..\ks\nf-ks-ksdisableevent.md">KsDisableEvent</a> function when a request to disable an event occurs, or by the <a href="..\ks\nf-ks-ksfreeeventlist.md">KsFreeEventList</a> function when a request to free a list of events occurs. This function can only be called at PASSIVE_LEVEL.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="..\ks\nf-ks-ksdisableevent.md">KsDisableEvent</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksfreeeventlist.md">KsFreeEventList</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsDiscardEvent function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
