---
UID: NF.ndis.NdisResetEvent
title: NdisResetEvent
author: windows-driver-content
description: The NdisResetEvent function clears the Signaled state of a given event.
old-location: netvista\ndisresetevent.htm
ms.assetid: fba29b92-5735-4050-b690-3c25e4f57cd1
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisResetEvent (NDIS 5.1)) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisResetEvent (NDIS 5.1)) in
   Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisResetEvent
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
ms.keywords: NdisResetEvent
req.iface: 
---

# NdisResetEvent function



## -description
<p>The
  <b>NdisResetEvent</b> function clears the Signaled state of a given event.</p>


## -syntax

````
VOID NdisResetEvent(
  _In_ PNDIS_EVENT Event
);
````


## -parameters
<dl>

### -param <i>Event</i> [in]

<dd>
<p>A pointer to an initialized event object for which the caller provided the storage.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>NdisResetEvent</b> explicitly sets the state of the given event to 
    <i>not-signaled</i>.</p>

<p>When an event is set to the 
    <i>signaled</i> state with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564539">NdisSetEvent</a> function, it remains in that
    state until an explicit call to 
    <b>NdisResetEvent</b> occurs. While an event remains in the 
    <i>signaled</i> state, callers of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564651">NdisWaitEvent</a> function on that event are
    dispatched for execution without waiting.</p>

<p><b>NdisResetEvent</b> explicitly sets the state of the given event to 
    <i>not-signaled</i>.</p>

<p>When an event is set to the 
    <i>signaled</i> state with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564539">NdisSetEvent</a> function, it remains in that
    state until an explicit call to 
    <b>NdisResetEvent</b> occurs. While an event remains in the 
    <i>signaled</i> state, callers of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564651">NdisWaitEvent</a> function on that event are
    dispatched for execution without waiting.</p>

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
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff554697">NdisResetEvent (NDIS 5.1)</a>) in
   Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisResetEvent (NDIS 5.1)</b>) in
   Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564539">NdisSetEvent</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564651">NdisWaitEvent</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisResetEvent function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
