---
UID: NS.KS.KSEVENT_ITEM
title: KSEVENT_ITEM
author: windows-driver-content
description: The KSEVENT_ITEM structure describe a minidriver's support for a specific event within an event set.
old-location: stream\ksevent_item.htm
old-project: stream
ms.assetid: a501a693-bea1-43eb-af8c-5512c8ee9d50
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: KSEVENT_ITEM, *PKSEVENT_ITEM, KSEVENT_ITEM, PKSEVENT_ITEM
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
---

# KSEVENT_ITEM structure



## -description
The KSEVENT_ITEM structure describe a minidriver's support for a specific event within an event set.



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

### -field EventId

Specifies the unique ID of the event within the event set.


### -field DataInput

Specifies the size in bytes of event data. The event data begins with a <a href="..\ks\ns-ks-kseventdata.md">KSEVENTDATA</a> structure that describes how the client should be notified when the event occurs, optionally followed by any additional parameters that specify when the event occurs. Must be at least <b>sizeof</b>(KSEVENTDATA).


### -field ExtraEntryData

Specifies the size in bytes of any additional memory that the system should allocate for each enable request for this event. The driver uses this memory to store any data it needs to keep track of the event request. The memory is allocated directly after the event enable request's <a href="stream.ksevent_entry">KSEVENT_ENTRY</a> structure.


### -field AddHandler

Pointer to a minidriver-supplied <a href="stream.avstrminiaddevent">AVStrMiniAddEvent</a> callback routine. Not used by the stream class driver. For AVStream minidrivers only.


### -field RemoveHandler

Pointer to a minidriver-supplied <a href="stream.avstrminiremoveevent">AVStrMiniRemoveEvent</a> callback routine. Not used by the stream class driver. For AVStream minidrivers only.


### -field SupportHandler

Not used by the stream class driver.


## -remarks
<i>A minidriver that specifies the </i><b>AddHandler</b><i> and </i><b>RemoveHandler</b><i> members and does not properly clean the events up can cause a resource (memory/handle) leak.</i>


## -requirements
<table>
<tr>
<th width="30%">
Header

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
<a href="..\ks\ns-ks-kseventdata.md">KSEVENTDATA</a>
</dt>
<dt>
<a href="stream.ksevent_entry">KSEVENT_ENTRY</a>
</dt>
<dt>
<a href="stream.ksdefaultaddeventhandler">KsDefaultAddEventHandler</a>
</dt>
<dt>
<a href="..\ks\ni-ks-ioctl_ks_disable_event.md">IOCTL_KS_DISABLE_EVENT</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KSEVENT_ITEM structure%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

