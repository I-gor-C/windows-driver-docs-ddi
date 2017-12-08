---
UID: NF.portcls.IPortEvents.AddEventToEventList
title: IPortEvents::AddEventToEventList
author: windows-driver-content
description: The AddEventToEventList method adds an event to the port driver's event list.
old-location: audio\iportevents_addeventtoeventlist.htm
old-project: audio
ms.assetid: 49b01942-3562-4fb2-907b-8863b2f09f8e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: IPortEvents, AddEventToEventList, IPortEvents::AddEventToEventList
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: portcls.h
req.include-header: Portcls.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: IPortEvents.AddEventToEventList
req.alt-loc: portcls.h
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
req.iface: IPortEvents
---

# IPortEvents::AddEventToEventList method



## -description
<p>The <code>AddEventToEventList</code> method adds an event to the port driver's event list.</p>


## -syntax

````
void AddEventToEventList(
  [in] PKSEVENT_ENTRY EventEntry
);
````


## -parameters
<dl>

### -param EventEntry [in]

<dd>
<p>Pointer to the event entry that describes the event. This is an opaque system structure of type <a href="..\ks\ns-ks--ksevent-entry.md">KSEVENT_ENTRY</a>.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>This method is used by a miniport driver's to add events to the event list that is maintained by the associated port object. The miniport driver's event handler typically calls this method in response to a PCEVENT_VERB_ADD request after the handler has validated support for the event being requested.</p>

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
<dt>Portcls.h (include Portcls.h)</dt>
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
<a href="..\portcls\nn-portcls-iportevents.md">IPortEvents</a>
</dt>
<dt>
<a href="..\ks\ns-ks--ksevent-entry.md">KSEVENT_ENTRY</a>
</dt>
<dt>
<a href="audio.iportevents_generateeventlist">IPortEvents::GenerateEventList</a>
</dt>
<dt>
<a href="..\portcls\nc-portcls-pcpfnevent-handler.md">EventHandler</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [audio\audio]:%20IPortEvents::AddEventToEventList method%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
