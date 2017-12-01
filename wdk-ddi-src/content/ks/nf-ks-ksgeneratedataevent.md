---
UID: NF.ks.KsGenerateDataEvent
title: KsGenerateDataEvent
author: windows-driver-content
description: The KsGenerateDataEvent function generates one of the standard event notifications when given an event entry structure and callback data.
old-location: stream\ksgeneratedataevent.htm
old-project: stream
ms.assetid: 3ba49134-e144-4212-9ef7-e16b9d5f90ea
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: KsGenerateDataEvent
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
req.alt-api: KsGenerateDataEvent
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

# KsGenerateDataEvent function



## -description
<p>The <b>KsGenerateDataEvent</b> function generates one of the standard event notifications when given an event entry structure and callback data. This allows a device to determine when event notifications should be generated, yet still use this helper function to perform the actual notification.</p>


## -syntax

````
NTSTATUS KsGenerateDataEvent(
  _In_ PKSEVENT_ENTRY EventEntry,
  _In_ ULONG          DataSize,
  _In_ PVOID          Data
);
````


## -parameters
<dl>

### -param <i>EventEntry</i> [in]

<dd>
<p>Specifies the event entry structure that references the event data. The information is used to determine what type of notification to perform. If the notification type is not one of the predefined standards, an error is returned. In the case of a single, nonrecurring event, this entry will be invalid when returned from the function. Therefore, any code that enumerates a list of events must preincrement to acquire the next event in the list before passing this event to the function.</p>
</dd>

### -param <i>DataSize</i> [in]

<dd>
<p>Specifies the size in bytes of the <i>Data</i> parameter passed.</p>
</dd>

### -param <i>Data</i> [in]

<dd>
<p>Points to data to be passed to the client callback. This data is copied to one of the preallocated buffer slots set up when the event was enabled. The size of the data must be less than whatever was originally allocated or the event will fail.</p>
</dd>
</dl>

## -returns
<p>The <b>KsGenerateDataEvent</b> function returns STATUS_SUCCESS if successful, or if unsuccessful it returns an exception or memory error.</p>

## -remarks
<p>It is assumed that the event list lock has been acquired before this function is called. This function can result in a call to the <b>RemoveHandler</b> for the event entry. Therefore, the function must not be called at higher than the IRQ level of the lock, or the <b>Remove</b> function must be able to handle being called at such an IRQ level.</p>

<p>This function is specifically for events that pass data back through a callback to a client.</p>

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
<a href="stream.ksbuffer_item">KSBUFFER_ITEM</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [stream\stream]:%20KsGenerateDataEvent function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
