---
UID: NF.ndis.NdisInitializeEvent
title: NdisInitializeEvent function
author: windows-driver-content
description: The NdisInitializeEvent function sets up an event object during driver initialization to be used subsequently as a synchronization mechanism.
old-location: netvista\ndisinitializeevent.htm
old-project: netvista
ms.assetid: 7f7eac7e-f512-4446-a83b-92d313c14420
ms.author: windowsdriverdev
ms.date: 12/6/2017
ms.keywords: NdisInitializeEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisInitializeEvent (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisInitializeEvent (NDIS   5.1)) in Windows XP.
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
---

# NdisInitializeEvent function



## -description
The 
  <b>NdisInitializeEvent</b> function sets up an event object during driver initialization to be used
  subsequently as a synchronization mechanism.


## -syntax

````
VOID NdisInitializeEvent(
  _Out_ PNDIS_EVENT Event
);
````


## -parameters

### -param Event [out]

A pointer to caller-supplied storage for the event object, which is opaque to drivers.

## -returns
None

## -remarks
The 
    <b>NdisInitializeEvent</b> function creates an event object that has an event type of 
    <b>NotificationEvent</b> and an initial state of 
    <i>not-signaled</i>. For more information about notification events, see 
    <a href="https://msdn.microsoft.com/4b7807f0-bbea-4402-b028-9ac73724717f">Defining and Using an Event
    Object</a>.

The 
    <i>Event</i> pointer passed to 
    <b>NdisInitializeEvent</b> is a required parameter to all other 
    <b>Ndis<i>Xxx</i>Event</b> functions.

While driver functions that must run at IRQL &lt;= DISPATCH_LEVEL can call the 
    <a href="netvista.ndissetevent">NdisSetEvent</a> and 
    <a href="netvista.ndisresetevent">NdisResetEvent</a> functions ,calling 
    <b>NdisWaitEvent</b> from any IRQL &gt; PASSIVE_LEVEL is a fatal error.

## -requirements
<table>
<tr>
<th width="30%">
Target platform
</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version
</th>
<td width="70%">
Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/2555e84e-705d-4516-ae20-1d43fa0fea04">NdisInitializeEvent (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisInitializeEvent (NDIS
   5.1)</b>) in Windows XP.
</td>
</tr>
<tr>
<th width="30%">
Header
</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL
</th>
<td width="70%">
Any level
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="netvista.ndisresetevent">NdisResetEvent</a>
</dt>
<dt>
<a href="netvista.ndissetevent">NdisSetEvent</a>
</dt>
<dt>
<a href="netvista.ndiswaitevent">NdisWaitEvent</a>
</dt>
</dl>
 
 
<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisInitializeEvent function%20 RELEASE:%20(12/6/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>
