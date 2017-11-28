---
UID: NF.ndis.NdisSetEvent
title: NdisSetEvent
author: windows-driver-content
description: The NdisSetEvent function sets a given event to the signaled state if it was not already Signaled.
old-location: netvista\ndissetevent.htm
old-project: netvista
ms.assetid: 3f45b8d0-2d5b-4601-a307-48257cdcb4ba
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisSetEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisSetEvent (NDIS 5.1)) in Windows
   Vista. Supported for NDIS 5.1 drivers (see 
   NdisSetEvent (NDIS 5.1)) in Windows
   XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisSetEvent
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Synch_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisSetEvent function



## -description
<p>The 
  <b>NdisSetEvent</b> function sets a given event to the signaled state if it was not already Signaled.</p>


## -syntax

````
VOID NdisSetEvent(
  _In_ PNDIS_EVENT Event
);
````


## -parameters
<dl>

### -param <i>Event</i> [in]

<dd>
<p>A pointer to an initialized event object for which the caller provides the storage.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>When an event attains the 
    <i>signaled</i> state, it causes waits on the event to be satisfied and any waiters to be dispatched for
    execution.</p>

<p>After a call to 
    <b>NdisSetEvent</b>, the event remains in the 
    <i>signaled</i> state until the driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564526">NdisResetEvent</a> function.</p>

<p>When an event attains the 
    <i>signaled</i> state, it causes waits on the event to be satisfied and any waiters to be dispatched for
    execution.</p>

<p>After a call to 
    <b>NdisSetEvent</b>, the event remains in the 
    <i>signaled</i> state until the driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564526">NdisResetEvent</a> function.</p>

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
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff554724">NdisSetEvent (NDIS 5.1)</a>) in Windows
   Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisSetEvent (NDIS 5.1)</b>) in Windows
   XP.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>&lt;= DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff548015">Irql_Synch_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562732">NdisInitializeEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564526">NdisResetEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564651">NdisWaitEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisSetEvent function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
