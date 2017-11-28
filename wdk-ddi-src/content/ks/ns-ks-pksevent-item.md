---
UID: NS.ks.PKSEVENT_ITEM
title: PKSEVENT_ITEM
author: windows-driver-content
description: The KSEVENT_ITEM structure describe a minidriver's support for a specific event within an event set.
old-location: stream\ksevent_item.htm
old-project: stream
ms.assetid: a501a693-bea1-43eb-af8c-5512c8ee9d50
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: PKSEVENT_ITEM, KSEVENT_ITEM, *PKSEVENT_ITEM
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ks.h
req.include-header: Ks.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: KSEVENT_ITEM
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
req.irql: 
req.iface: 
---

# PKSEVENT_ITEM structure



## -description
<p>The KSEVENT_ITEM structure describe a minidriver's support for a specific event within an event set.</p>


## -syntax

````
typedef struct {
  ULONG            EventId;
  ULONG            DataInput;
  ULONG            ExtraEntryData;
  PFNKSADDEVENT    AddHandler;
  PFNKSREMOVEEVENT RemoveHandler;
  PFNKSHANDLER     SupportHandler;
} KSEVENT_ITEM, *PKSEVENT_ITEM;
````


## -struct-fields
<dl>

### -field <b>EventId</b>

<dd>
<p>Specifies the unique ID of the event within the event set.</p>
</dd>

### -field <b>DataInput</b>

<dd>
<p>Specifies the size in bytes of event data. The event data begins with a <a href="https://msdn.microsoft.com/library/windows/hardware/ff561750">KSEVENTDATA</a> structure that describes how the client should be notified when the event occurs, optionally followed by any additional parameters that specify when the event occurs. Must be at least <b>sizeof</b>(KSEVENTDATA).</p>
</dd>

### -field <b>ExtraEntryData</b>

<dd>
<p>Specifies the size in bytes of any additional memory that the system should allocate for each enable request for this event. The driver uses this memory to store any data it needs to keep track of the event request. The memory is allocated directly after the event enable request's <a href="https://msdn.microsoft.com/library/windows/hardware/ff561853">KSEVENT_ENTRY</a> structure.</p>
</dd>

### -field <b>AddHandler</b>

<dd>
<p>Pointer to a minidriver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff554260">AVStrMiniAddEvent</a> callback routine. Not used by the stream class driver. For AVStream minidrivers only.</p>
</dd>

### -field <b>RemoveHandler</b>

<dd>
<p>Pointer to a minidriver-supplied <a href="https://msdn.microsoft.com/library/windows/hardware/ff556361">AVStrMiniRemoveEvent</a> callback routine. Not used by the stream class driver. For AVStream minidrivers only.</p>
</dd>

### -field <b>SupportHandler</b>

<dd>
<p>Not used by the stream class driver.</p>
</dd>
</dl>

## -remarks
<p><i>A minidriver that specifies the </i><b>AddHandler</b><i> and </i><b>RemoveHandler</b><i> members and does not properly clean the events up can cause a resource (memory/handle) leak.</i></p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561750">KSEVENTDATA</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561853">KSEVENT_ENTRY</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561662">KsDefaultAddEventHandler</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff560802">IOCTL_KS_DISABLE_EVENT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSEVENT_ITEM structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
