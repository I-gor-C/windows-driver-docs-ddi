---
UID: NF.ndis.NdisIfDeregisterInterface
title: NdisIfDeregisterInterface function
author: windows-driver-content
description: The NdisIfDeregisterInterface function deregisters an NDIS network interface that was previously registered by a call to the NdisIfRegisterInterface function.
old-location: netvista\ndisifderegisterinterface.htm
old-project: netvista
ms.assetid: 696d0870-966e-44ac-859e-d530dd6c76b8
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisIfDeregisterInterface
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
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
---

# NdisIfDeregisterInterface function



## -description
The 
  <b>NdisIfDeregisterInterface</b> function deregisters an NDIS network interface that was previously
  registered by a call to the 
  <a href="netvista.ndisifregisterinterface">
  NdisIfRegisterInterface</a> function.



## -syntax

````
VOID NdisIfDeregisterInterface(
  _In_ NET_IFINDEX IfIndex
);
````


## -parameters

### -param IfIndex [in]

An index that identifies the network interface to deregister. The interface provider obtained this
     index from a previous call to the 
     <a href="netvista.ndisifregisterinterface">
     NdisIfRegisterInterface</a> function.


## -returns
None


## -remarks
NDIS interface providers call the 
    <b>NdisIfDeregisterInterface</b> function to deregister a network interface and to indicate that the
    interface should be removed from the list of known interfaces on the computer.

An interface provider calls the 
    <b>NdisIfDeregisterInterface</b> function, for example, because the interface has been uninstalled.
    Interface providers do not call 
    <b>NdisIfDeregisterInterface</b> to indicate that an interface has changed state.

<b>NdisIfDeregisterInterface</b> releases the interface index, so NDIS can reassign the index to another
    interface that is registered later. Do not confuse the interface index with the 
    <a href="netvista.net_luid">NET_LUID</a> index, which persists after a computer
    restarts.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported in NDIS 6.0 and later.

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
PASSIVE_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.ndis_irql_interfaces_function">Irql_Interfaces_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.ndisifregisterinterface">NdisIfRegisterInterface</a>
</dt>
<dt>
<a href="netvista.net_luid">NET_LUID</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisIfDeregisterInterface function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

