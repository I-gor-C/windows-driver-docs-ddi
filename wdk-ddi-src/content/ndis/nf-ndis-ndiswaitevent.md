---
UID: NF.ndis.NdisWaitEvent
title: NdisWaitEvent
author: windows-driver-content
description: The NdisWaitEvent function puts the caller into a wait state until the given event is set to the Signaled state or the wait times out.
old-location: netvista\ndiswaitevent.htm
old-project: netvista
ms.assetid: fefdb56f-6689-4a4f-a198-6108190624f0
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisWaitEvent
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisWaitEvent (NDIS 5.1)) in Windows   Vista. Supported for NDIS 5.1 drivers (see    NdisWaitEvent (NDIS 5.1)) in Windows   XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisWaitEvent
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miscellaneous_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NdisWaitEvent function



## -description
<p>The
  <b>NdisWaitEvent</b> function puts the caller into a wait state until the given event is set to the Signaled
  state or the wait times out.</p>


## -syntax

````
BOOLEAN NdisWaitEvent(
  _In_ PNDIS_EVENT Event,
  _In_ UINT        MsToWait
);
````


## -parameters
<dl>

### -param <i>Event</i> [in]

<dd>
<p>A pointer to an initialized event object for which the caller provides the storage.</p>
</dd>

### -param <i>MsToWait</i> [in]

<dd>
<p>The number of milliseconds the caller will wait if the event is not set to the 
     <i>signaled</i> state within that interval. A value of zero specifies that the caller will wait for the
     event indefinitely.</p>
</dd>
</dl>

## -returns
<p><b>NdisWaitEvent</b> returns <b>TRUE</b> if the event is in the 
     <i>signaled</i> state when the wait is satisfied.</p>

## -remarks
<p><b>NdisWaitEvent</b> returns control to its caller when the given event is signaled or the specified 
    <i>MsToWait</i> interval expires, whichever is sooner. If the event is currently in the 
    <i>signaled</i> state when this call occurs, 
    <b>NdisWaitEvent</b> returns control immediately.</p>

<p>A miniport driver typically calls 
    <b>NdisWaitEvent</b> from its 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> and 
    <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> functions. A protocol
    driver typically calls 
    <b>NdisWaitEvent</b> from its 
    <a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a> and 
    <a href="..\ndis\nc-ndis-protocol-unbind-adapter-ex.md">
    ProtocolUnbindAdapterEx</a> functions.</p>

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
   <a href="https://msdn.microsoft.com/library/windows/hardware/ff554843">NdisWaitEvent (NDIS 5.1)</a>) in Windows
   Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisWaitEvent (NDIS 5.1)</b>) in Windows
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="devtest.ndis_irql_miscellaneous_function">Irql_Miscellaneous_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.driverentry_of_ndis_protocol_drivers">DriverEntry of NDIS Protocol
   Drivers</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisinitializeevent.md">NdisInitializeEvent</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisresetevent.md">NdisResetEvent</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndissetevent.md">NdisSetEvent</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol-unbind-adapter-ex.md">ProtocolUnbindAdapterEx</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisWaitEvent function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
