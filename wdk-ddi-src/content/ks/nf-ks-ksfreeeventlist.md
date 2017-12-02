---
UID: NF.ks.KsFreeEventList
title: KsFreeEventList
author: windows-driver-content
description: The KsFreeEventList function handles freeing all events from a specified list, with the assumption that these events are composed of KSEVENT_ENTRY structures. This function can only be called at PASSIVE_LEVEL.
old-location: stream\ksfreeeventlist.htm
old-project: stream
ms.assetid: 3ccbbf07-7d8d-423a-b50d-d202e1cb7ab2
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsFreeEventList
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
req.alt-api: KsFreeEventList
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

# KsFreeEventList function



## -description
<p>The <b>KsFreeEventList</b> function handles freeing all events from a specified list, with the assumption that these events are composed of <b>KSEVENT_ENTRY</b> structures. This function can only be called at PASSIVE_LEVEL.</p>


## -syntax

````
VOID KsFreeEventList(
  _In_    PFILE_OBJECT      FileObject,
  _Inout_ PLIST_ENTRY       EventsList,
  _In_    KSEVENTS_LOCKTYPE EventsFlags,
  _In_    PVOID             EventsLock
);
````


## -parameters
<dl>

### -param FileObject [in]

<dd>
<p>Specifies the file object passed to the removal function for context information. The file object associated is used to compare against the file object originally specified when enabling the event. This allows a single event list to be used for multiple clients differentiated by file objects.</p>
</dd>

### -param EventsList [in, out]

<dd>
<p>Points to the head of the list of KSEVENT_ENTRY items to be freed. If any events on the list are currently being disabled, they are passed over. If any new elements are added to the list while it is being processed, they may not be freed.</p>
</dd>

### -param EventsFlags [in]

<dd>
<p>Specifies a <a href="..\ks\ne-ks-ksevents-locktype.md">KSEVENTS_LOCKTYPE</a> flag specifying the type of exclusion lock to be used in accessing the event list. If no flag is set, then no lock is taken.</p>
</dd>

### -param EventsLock [in]

<dd>
<p>Used to synchronize access to an element on the list. After the element has been accessed, it is marked as being deleted so subsequent removal requests fail. The lock is then released after calling the removal function, if any. The removal function must synchronize with event generation before actually removing the element from the list.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The <b>KsFreeEventList</b> function calls the remove handler, and then it calls <b>KsDiscardEvent</b> for each event. It does not assume that the caller is the event owner.</p>

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
<a href="..\ks\nf-ks-ksdiscardevent.md">KsDiscardEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsFreeEventList function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
