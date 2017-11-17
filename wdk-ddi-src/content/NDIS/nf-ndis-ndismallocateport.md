---
UID: NF.ndis.NdisMAllocatePort
title: NdisMAllocatePort
author: windows-driver-content
description: The NdisMAllocatePort function allocates an NDIS port that is associated with a miniport adapter.
old-location: netvista\ndismallocateport.htm
ms.assetid: ca3a2a12-ea80-4f77-9742-b0440fb441f7
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
req.alt-api: NdisMAllocatePort
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
req.irql: <= DISPATCH_LEVEL
ms.keywords: NdisMAllocatePort
req.iface: 
---

# NdisMAllocatePort function



## -description
<p>The 
  <b>NdisMAllocatePort</b> function allocates an NDIS port that is associated with a miniport adapter.</p>


## -syntax

````
NDIS_STATUS NdisMAllocatePort(
  _In_    NDIS_HANDLE                MiniportAdapterHandle,
  _Inout_ PNDIS_PORT_CHARACTERISTICS PortCharacteristics
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

### -param <i>PortCharacteristics</i> [in, out]

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/fd602dd6-c216-413a-a4da-292739774937">
     NDIS_PORT_CHARACTERISTICS</a> structure that defines the characteristics of the port.</p>
</dd>
</dl>

## -returns
<p><b>NdisMAllocatePort</b> can return one of the following values:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p>NDIS successfully allocated resources for the port.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p>NDIS could not allocate resources for the port.</p><dl>
<dt><b>NDIS_STATUS_CLOSING</b></dt>
</dl><p>The port allocation failed because the associated miniport adapter is closing.</p><dl>
<dt><b>NDIS_STATUS_INVALID_DATA</b></dt>
</dl><p>The data that was supplied at the 
       <i>PortCharacteristics</i> parameter was invalid.</p>

<p> </p>

## -remarks
<p>The 
    <b>NdisMAllocatePort</b> function allocates resources and a port number for a port that is associated with
    a miniport adapter. The port is not active until the miniport driver issues a 
    <b>NetEventPortActivation</b> Plug and Play (PnP) event for the port.</p>

<p>After the miniport driver activates the port, NDIS generates a PnP notification for the overlying
    drivers. If an overlying driver or user-mode application issues the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569583">OID_GEN_ENUMERATE_PORTS</a> OID to
    enumerate a miniport adapter's ports, NDIS does not include non-active allocated ports in the list of the
    ports.</p>

<p>When 
    <b>NdisMAllocatePort</b> successfully returns, the 
    <b>PortNumber</b> member of the 
    <a href="https://msdn.microsoft.com/fd602dd6-c216-413a-a4da-292739774937">
    NDIS_PORT_CHARACTERISTICS</a> structure that the 
    <i>PortCharacteristics</i> parameter specifies is set to the port number that NDIS assigned to the
    port.</p>

<p>After a port is no longer required, the miniport driver should call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563588">NdisMFreePort</a> function to free the port.</p>

<p>The 
    <b>NdisMAllocatePort</b> function allocates resources and a port number for a port that is associated with
    a miniport adapter. The port is not active until the miniport driver issues a 
    <b>NetEventPortActivation</b> Plug and Play (PnP) event for the port.</p>

<p>After the miniport driver activates the port, NDIS generates a PnP notification for the overlying
    drivers. If an overlying driver or user-mode application issues the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff569583">OID_GEN_ENUMERATE_PORTS</a> OID to
    enumerate a miniport adapter's ports, NDIS does not include non-active allocated ports in the list of the
    ports.</p>

<p>When 
    <b>NdisMAllocatePort</b> successfully returns, the 
    <b>PortNumber</b> member of the 
    <a href="https://msdn.microsoft.com/fd602dd6-c216-413a-a4da-292739774937">
    NDIS_PORT_CHARACTERISTICS</a> structure that the 
    <i>PortCharacteristics</i> parameter specifies is set to the port number that NDIS assigned to the
    port.</p>

<p>After a port is no longer required, the miniport driver should call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff563588">NdisMFreePort</a> function to free the port.</p>

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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566791">NDIS_PORT_CHARACTERISTICS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563588">NdisMFreePort</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569583">OID_GEN_ENUMERATE_PORTS</a>
</dt>
<dt>
<a href="NULL">Allocating an NDIS Port</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMAllocatePort function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
