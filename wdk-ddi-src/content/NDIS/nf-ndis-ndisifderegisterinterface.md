---
UID: NF.ndis.NdisIfDeregisterInterface
title: NdisIfDeregisterInterface
author: windows-driver-content
description: The NdisIfDeregisterInterface function deregisters an NDIS network interface that was previously registered by a call to the NdisIfRegisterInterface function.
old-location: netvista\ndisifderegisterinterface.htm
ms.assetid: 696d0870-966e-44ac-859e-d530dd6c76b8
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Desktop
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisIfDeregisterInterface
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Interfaces_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: NdisIfDeregisterInterface
req.iface: 
---

# NdisIfDeregisterInterface function



## -description
<p>The 
  <b>NdisIfDeregisterInterface</b> function deregisters an NDIS network interface that was previously
  registered by a call to the 
  <a href="https://msdn.microsoft.com/d0b0ada7-afb1-4cb7-ada6-7c5c7abe7d19">
  NdisIfRegisterInterface</a> function.</p>


## -syntax

````
VOID NdisIfDeregisterInterface(
  _In_ NET_IFINDEX IfIndex
);
````


## -parameters
<dl>

### -param <i>IfIndex</i> [in]

<dd>
<p>An index that identifies the network interface to deregister. The interface provider obtained this
     index from a previous call to the 
     <a href="https://msdn.microsoft.com/d0b0ada7-afb1-4cb7-ada6-7c5c7abe7d19">
     NdisIfRegisterInterface</a> function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>NDIS interface providers call the 
    <b>NdisIfDeregisterInterface</b> function to deregister a network interface and to indicate that the
    interface should be removed from the list of known interfaces on the computer.</p>

<p>An interface provider calls the 
    <b>NdisIfDeregisterInterface</b> function, for example, because the interface has been uninstalled.
    Interface providers do not call 
    <b>NdisIfDeregisterInterface</b> to indicate that an interface has changed state.</p>

<p><b>NdisIfDeregisterInterface</b> releases the interface index, so NDIS can reassign the index to another
    interface that is registered later. Do not confuse the interface index with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a> index, which persists after a computer
    restarts.</p>

<p>NDIS interface providers call the 
    <b>NdisIfDeregisterInterface</b> function to deregister a network interface and to indicate that the
    interface should be removed from the list of known interfaces on the computer.</p>

<p>An interface provider calls the 
    <b>NdisIfDeregisterInterface</b> function, for example, because the interface has been uninstalled.
    Interface providers do not call 
    <b>NdisIfDeregisterInterface</b> to indicate that an interface has changed state.</p>

<p><b>NdisIfDeregisterInterface</b> releases the interface index, so NDIS can reassign the index to another
    interface that is registered later. Do not confuse the interface index with the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a> index, which persists after a computer
    restarts.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Target platform</p>
</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547949">Irql_Interfaces_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562715">NdisIfRegisterInterface</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568747">NET_LUID</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisIfDeregisterInterface function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
