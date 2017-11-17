---
UID: NF.ks.KsGenerateEventList
title: KsGenerateEventList
author: windows-driver-content
description: The KsGenerateEventList function enumerates the event list and searches for the specified event to generate.
old-location: stream\ksgenerateeventlist.htm
ms.assetid: 336dbbc1-0f3c-4a3f-b3b4-017f4d158bda
ms.author: windowsdriverdev
ms.date: 10/25/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: stream
req.header: ks.h
req.include-header: Ks.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KsGenerateEventList
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
req.irql: Any level (See Remarks section)
ms.keywords: KsGenerateEventList
req.iface: 
---

# KsGenerateEventList function



## -description
<p>The <b>KsGenerateEventList</b> function enumerates the event list and searches for the specified event to generate. </p>


## -syntax

````
VOID KsGenerateEventList(
  _In_opt_ GUID              *Set,
  _In_     ULONG             EventId,
  _In_     PLIST_ENTRY       EventsList,
  _In_     KSEVENTS_LOCKTYPE EventsFlags,
  _In_     PVOID             EventsLock
);
````


## -parameters
<dl>

### -param <i>Set</i> [in, optional]

<dd>
<p>Specifies an optional set that the event to be generated belongs to. If present, this value is compared against the set identifier for each event in the list. If not present, the set identifiers are ignored and just the specific event identifier is used in the comparison for matching events on the list. This comparison saves time when all events are known to be contained in a single set.</p>
</dd>

### -param <i>EventId</i> [in]

<dd>
<p>Specifies the specific event identifier to look for on the list.</p>
</dd>

### -param <i>EventsList</i> [in]

<dd>
<p>Points to the head of the list of KSEVENT_ENTRY items on which the event can be found.</p>
</dd>

### -param <i>EventsFlags</i> [in]

<dd>
<p>Specifies the <a href="https://msdn.microsoft.com/library/windows/hardware/ff561784">KSEVENTS_LOCKTYPE</a> flag specifying the exclusion lock type to be used in accessing the event list. If no flag is set, then no lock is taken.</p>
</dd>

### -param <i>EventsLock</i> [in]

<dd>
<p>Used to synchronize access to an element on the list. The lock is taken before enumerating the list and released after enumeration.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>This function can be called at any IRQL level if the locking mechanism permits it.</p>

<p>This function can be called at any IRQL level if the locking mechanism permits it.</p>

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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level (See Remarks section)</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562541">KsFilterGenerateEvents</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563500">KsPinGenerateEvents</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563490">KsPinAddEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562525">KsFilterAddEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGenerateEventList function%20 RELEASE:%20(10/25/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
