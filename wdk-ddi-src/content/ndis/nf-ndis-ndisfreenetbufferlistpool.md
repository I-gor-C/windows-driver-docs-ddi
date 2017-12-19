---
UID: NF.ndis.NdisFreeNetBufferListPool
title: NdisFreeNetBufferListPool function
author: windows-driver-content
description: Call the NdisFreeNetBufferListPool function to free a NET_BUFFER_LIST structure pool.
old-location: netvista\ndisfreenetbufferlistpool.htm
old-project: NetVista
ms.assetid: 811df5ea-f5e6-4986-adc0-c5fa95e5f072
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: NdisFreeNetBufferListPool
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisFreeNetBufferListPool
req.alt-loc: ndis.sys
req.ddi-compliance: Irql_NetBuffer_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: Ndis.sys
req.irql: <= DISPATCH_LEVEL
---

# NdisFreeNetBufferListPool function



## -description
Call the 
  <b>NdisFreeNetBufferListPool</b> function to free a 
  <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure pool.



## -syntax

````
VOID NdisFreeNetBufferListPool(
  _In_ NDIS_HANDLE PoolHandle
);
````


## -parameters

### -param PoolHandle [in]

A handle that was obtained from a call to the 
     <a href="netvista.ndisallocatenetbufferlistpool">
     NdisAllocateNetBufferListPool</a> function.


## -returns
None


## -remarks
Before freeing a 
    <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure pool, you must
    free all the NET_BUFFER_LIST structures in the pool. To free a NET_BUFFER_LIST structure, call the 
    <a href="netvista.ndisfreenetbufferlist">NdisFreeNetBufferList</a> function.


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
DLL

</th>
<td width="70%">
<dl>
<dt>Ndis.sys</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.ndis_irql_netbuffer_function">Irql_NetBuffer_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="netvista.net_buffer_list">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="netvista.ndisallocatenetbufferlistpool">
   NdisAllocateNetBufferListPool</a>
</dt>
<dt>
<a href="netvista.ndisfreenetbufferlist">NdisFreeNetBufferList</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NdisFreeNetBufferListPool function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

