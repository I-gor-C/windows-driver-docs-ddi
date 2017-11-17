---
UID: NF.ndis.NdisMFreePort
title: NdisMFreePort
author: windows-driver-content
description: The NdisMFreePort function frees an NDIS port that was previously allocated with the NdisMAllocatePort function.
old-location: netvista\ndismfreeport.htm
ms.assetid: 38d53977-ada2-41b9-8b6a-a3bd691f4525
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMFreePort
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miniport_Driver_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisMFreePort
req.iface: 
---

# NdisMFreePort function



## -description
<p>The 
  <b>NdisMFreePort</b> function frees an NDIS port that was previously allocated with the 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff562779">NdisMAllocatePort</a> function.</p>


## -syntax

````
NDIS_STATUS NdisMFreePort(
  _In_ NDIS_HANDLE      MiniportAdapterHandle,
  _In_ NDIS_PORT_NUMBER PortNumber
);
````


## -parameters
<dl>

### -param <i>MiniportAdapterHandle</i> [in]

<dd>
<p>The miniport adapter handle that NDIS passed to the 
     <i>MiniportAdapterHandle</i> parameter of the 
     <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">
     MiniportInitializeEx</a> function.</p>
</dd>

### -param <i>PortNumber</i> [in]

<dd>
<p>The number of the NDIS port that NDIS should free. The 
     <i>PortNumber</i> value is an NDIS_PORT_NUMBER value, which has a ULONG data type. NDIS provided the port
     number in the 
     <b>PortNumber</b> member of the 
     <a href="https://msdn.microsoft.com/fd602dd6-c216-413a-a4da-292739774937">
     NDIS_PORT_CHARACTERISTICS</a> structure when the miniport driver called the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff562779">NdisMAllocatePort</a> function. 
     </p>
<p>The port number can be a number from 1 through 0xffffff. You cannot set 
     <i>PortNumber</i> to zero, which indicates the default port.</p>
</dd>
</dl>

## -returns
<p><b>NdisMFreePort</b> can return one of the following values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>NDIS successfully freed the resources for the port.</p><dl>
<dt><b>NDIS_STATUS_INVALID_PORT</b></dt>
</dl><p>NDIS could not free the resources for the port because the port number was invalid.</p><dl>
<dt><b>NDIS_STATUS_INVALID_PORT_STATE</b></dt>
</dl><p>NDIS could not free the resources for the port because the port was is in a state where the free
       operation is invalid. To free the port, the port must be in the allocated state.</p><dl>
<dt><b>NDIS_STATUS_INVALID_DATA</b></dt>
</dl><p>The port number that was supplied at the 
       <i>PortNumber</i> parameter was invalid.</p>

<p> </p>

## -remarks
<p>If a miniport driver allocated a port by calling the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562779">NdisMAllocatePort</a> function, the driver
    must free the port before it returns from its 
    <a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a> function. If the miniport
    driver activated the port by issuing a 
    <b>NetEventPortActivation</b> Plug and Play (PnP) event, the driver must issue a 
    <b>NetEventPortDeactivation</b> PnP event for the port before freeing the port.</p>

<p>When a miniport driver calls <b>NdisMFreePort</b> to free a port, NDIS also frees the port number that is assigned to the freed port so that NDIS can reuse the port number.</p>

<p>The miniport driver must not attempt to free the default port.</p>

<p>If a miniport driver allocated a port by calling the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562779">NdisMAllocatePort</a> function, the driver
    must free the port before it returns from its 
    <a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a> function. If the miniport
    driver activated the port by issuing a 
    <b>NetEventPortActivation</b> Plug and Play (PnP) event, the driver must issue a 
    <b>NetEventPortDeactivation</b> PnP event for the port before freeing the port.</p>

<p>When a miniport driver calls <b>NdisMFreePort</b> to free a port, NDIS also frees the port number that is assigned to the freed port so that NDIS can reuse the port number.</p>

<p>The miniport driver must not attempt to free the default port.</p>

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
<p>Supported in NDIS 6.0 and later.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547979">Irql_Miniport_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566791">NDIS_PORT_CHARACTERISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562779">NdisMAllocatePort</a>
</dt>
<dt>
<a href="NULL">Default NDIS Port</a>
</dt>
<dt>
<a href="NULL">Freeing an NDIS Port</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMFreePort function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
