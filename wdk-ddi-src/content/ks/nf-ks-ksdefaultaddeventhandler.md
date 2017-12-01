---
UID: NF.ks.KsDefaultAddEventHandler
title: KsDefaultAddEventHandler
author: windows-driver-content
description: The KsDefaultAddEventHandler function is a default routine to handle event 'add' requests.
old-location: stream\ksdefaultaddeventhandler.htm
old-project: stream
ms.assetid: 8e429a48-4e86-4673-aa32-85b640e2f64f
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsDefaultAddEventHandler
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
req.alt-api: KsDefaultAddEventHandler
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

# KsDefaultAddEventHandler function



## -description
<p>The<b> KsDefaultAddEventHandler </b>function is a default routine to handle event 'add' requests.</p>


## -syntax

````
NTSTATUS KsDefaultAddEventHandler(
  _In_    PIRP           Irp,
  _In_    PKSEVENTDATA   EventData,
  _Inout_ PKSEVENT_ENTRY EventEntry
);
````


## -parameters
<dl>

### -param <i>Irp</i> [in]

<dd>
<p>The event <a href="..\ntifs\ns-ntifs--irp.md">IRP</a>. This contains the object into which the event is inserted.</p>
</dd>

### -param <i>EventData</i> [in]

<dd>
<p>A pointer to a <a href="stream.kseventdata">KSEVENTDATA</a> structure that describes an event notification method.</p>
</dd>

### -param <i>EventEntry</i> [in, out]

<dd>
<p>The event entry that is to be inserted into the object's event list. The object is determined by <i>Irp</i>.</p>
</dd>
</dl>

## -returns
<p>Returns the success or failure of adding the event into the object's event list.</p>

## -remarks
<p><b>KsDefaultAddEventHandler</b> determines the relevant object from <i>Irp</i> and adds the specified event to the object's event list.</p>

<p>This is functionally equivalent to <a href="..\ks\nf-ks-ksaddevent.md">KsAddEvent</a> (or <b>Ks</b><i>Xxx</i><b>AddEvent</b>, see below) for the object that is associated with <i>Irp</i>. Use <b>KsDefaultAddEventHandler</b> from a minidriver-specified <i>AddEvent</i> handler to insert the event into the object's event list.</p>

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
<a href="..\ks\nf-ks-ksaddevent.md">KsAddEvent</a>
</dt>
<dt>
<a href="..\ks\nf-ks-ksfilteraddevent.md">KsFilterAddEvent</a>
</dt>
<dt>
<a href="..\ks\nf-ks-kspinaddevent.md">KsPinAddEvent</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsDefaultAddEventHandler function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
