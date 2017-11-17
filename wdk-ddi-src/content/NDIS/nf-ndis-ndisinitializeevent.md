---
UID: NF.ndis.NdisInitializeEvent
title: NdisInitializeEvent
author: windows-driver-content
description: The NdisInitializeEvent function sets up an event object during driver initialization to be used subsequently as a synchronization mechanism.
old-location: netvista\ndisinitializeevent.htm
ms.assetid: 7f7eac7e-f512-4446-a83b-92d313c14420
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisInitializeEvent (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisInitializeEvent (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisInitializeEvent
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: Any level
ms.keywords: NdisInitializeEvent
req.iface: 
---

# NdisInitializeEvent function



## -description
<p>The 
  <b>NdisInitializeEvent</b> function sets up an event object during driver initialization to be used
  subsequently as a synchronization mechanism.</p>


## -syntax

````
VOID NdisInitializeEvent(
  _Out_ PNDIS_EVENT Event
);
````


## -parameters
<dl>

### -param <i>Event</i> [out]

<dd>
<p>A pointer to caller-supplied storage for the event object, which is opaque to drivers.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The 
    <b>NdisInitializeEvent</b> function creates an event object that has an event type of 
    <b>NotificationEvent</b> and an initial state of 
    <i>not-signaled</i>. For more information about notification events, see 
    <a href="https://msdn.microsoft.com/4b7807f0-bbea-4402-b028-9ac73724717f">Defining and Using an Event
    Object</a>.</p>

<p>The 
    <i>Event</i> pointer passed to 
    <b>NdisInitializeEvent</b> is a required parameter to all other 
    <b>Ndis<i>Xxx</i>Event</b> functions.</p>

<p>While driver functions that must run at IRQL &lt;= DISPATCH_LEVEL can call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564539">NdisSetEvent</a> and 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564526">NdisResetEvent</a> functions ,calling 
    <b>NdisWaitEvent</b> from any IRQL &gt; PASSIVE_LEVEL is a fatal error.</p>

<p>The 
    <b>NdisInitializeEvent</b> function creates an event object that has an event type of 
    <b>NotificationEvent</b> and an initial state of 
    <i>not-signaled</i>. For more information about notification events, see 
    <a href="https://msdn.microsoft.com/4b7807f0-bbea-4402-b028-9ac73724717f">Defining and Using an Event
    Object</a>.</p>

<p>The 
    <i>Event</i> pointer passed to 
    <b>NdisInitializeEvent</b> is a required parameter to all other 
    <b>Ndis<i>Xxx</i>Event</b> functions.</p>

<p>While driver functions that must run at IRQL &lt;= DISPATCH_LEVEL can call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564539">NdisSetEvent</a> and 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564526">NdisResetEvent</a> functions ,calling 
    <b>NdisWaitEvent</b> from any IRQL &gt; PASSIVE_LEVEL is a fatal error.</p>

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
   <a href="https://msdn.microsoft.com/2555e84e-705d-4516-ae20-1d43fa0fea04">NdisInitializeEvent (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisInitializeEvent (NDIS
   5.1)</b>) in Windows XP.</p>
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
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564526">NdisResetEvent</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisInitializeEvent function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
