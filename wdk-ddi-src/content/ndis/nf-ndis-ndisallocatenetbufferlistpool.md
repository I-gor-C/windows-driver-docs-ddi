---
UID: NF.ndis.NdisAllocateNetBufferListPool
title: NdisAllocateNetBufferListPool function
author: windows-driver-content
description: Call the NdisAllocateNetBufferListPool function to allocate a pool of NET_BUFFER_LIST structures.
old-location: netvista\ndisallocatenetbufferlistpool.htm
old-project: netvista
ms.assetid: b117b472-0c26-41a9-b364-3d0cfbd26cc9
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisAllocateNetBufferListPool
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
req.alt-api: NdisAllocateNetBufferListPool
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

# NdisAllocateNetBufferListPool function



## -description
Call the 
  <b>NdisAllocateNetBufferListPool</b> function to allocate a pool of 
  <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures.



## -syntax

````
NDIS_HANDLE NdisAllocateNetBufferListPool(
  _In_opt_ NDIS_HANDLE                      NdisHandle,
  _In_     PNET_BUFFER_LIST_POOL_PARAMETERS Parameters
);
````


## -parameters

### -param NdisHandle [in, optional]

An NDIS handle that was obtained during caller initialization.


### -param Parameters [in]

A pointer to a <a href="netvista.net_buffer_list_pool_parameters">NET_BUFFER_LIST_POOL_PARAMETERS</a> structure that defines the parameters for the pool.


## -returns
<b>NdisAllocateNetBufferListPool</b> returns a handle to the NET_BUFFER_LIST structure pool that NDIS
     allocates. If the allocation was unsuccessful, this handle is <b>NULL</b>. This handle is a required parameter
     in subsequent calls to NDIS functions that allocate and free NET_BUFFER_LIST structures from this
     pool.


## -remarks
In most cases, a caller that allocates a 
    <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure will allocate and
    queue at least one 
    <a href="netvista.net_buffer">NET_BUFFER</a> structure on that NET_BUFFER_LIST
    structure. It is more efficient to preallocate NET_BUFFER structures when you allocate a pool of
    NET_BUFFER_LIST structures than allocating NET_BUFFER_LIST structures and NET_BUFFER structures
    separately.

You can call the 
    <b>NdisAllocateNetBufferListPool</b> function with the 
    <b>fAllocateNetBuffer</b> value set to <b>TRUE</b> when creating a NET_BUFFER_LIST structure pool. In this case,
    a NET_BUFFER structure is preallocated with each NET_BUFFER_LIST structure that the caller allocates from
    the pool. You can call the 
    <a href="netvista.ndisallocatenetbufferandnetbufferlist">
    NdisAllocateNetBufferAndNetBufferList</a> function or the 
    <a href="netvista.ndisallocatenetbufferlist">
    NdisAllocateNetBufferList</a> function to allocate NET_BUFFER_LIST structures from such a pool. Call 
    <b>NdisAllocateNetBufferAndNetBufferList</b> only if 
    <b>fAllocateNetBuffer</b> is <b>TRUE</b> and 
    <b>DataSize</b> is zero.

You can also call 
    <b>NdisAllocateNetBufferListPool</b> and set the 
    <b>DataSize</b> member to a nonzero value when creating a NET_BUFFER_LIST structure pool. In this case, a
    NET_BUFFER structure, MDL, and data are preallocated with each NET_BUFFER_LIST structure that the caller
    allocates from the pool.

NET_BUFFER structures, MDLs, and data buffers that are allocated with 
    <a href="netvista.ndisallocatenetbufferandnetbufferlist">
    NdisAllocateNetBufferAndNetBufferList</a> or 
    <a href="netvista.ndisallocatenetbufferlist">NdisAllocateNetBufferList</a> should
    not be freed separate from the NET_BUFFER_LIST structure. Such structures are freed with the
    NET_BUFFER_LIST structure when you call the 
    <a href="netvista.ndisfreenetbufferlist">NdisFreeNetBufferList</a> function.

Call the 
    <a href="netvista.ndisfreenetbufferlistpool">
    NdisFreeNetBufferListPool</a> function to free a NET_BUFFER_LIST structure pool.


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
<a href="netvista.ndisallocatenetbufferlist">NdisAllocateNetBufferList</a>
</dt>
<dt>
<a href="netvista.ndisallocatenetbufferandnetbufferlist">
   NdisAllocateNetBufferAndNetBufferList</a>
</dt>
<dt>
<a href="netvista.ndisfreenetbufferlist">NdisFreeNetBufferList</a>
</dt>
<dt>
<a href="netvista.ndisfreenetbufferlistpool">NdisFreeNetBufferListPool</a>
</dt>
<dt>
<a href="netvista.net_buffer">NET_BUFFER</a>
</dt>
<dt>
<a href="netvista.net_buffer_list">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="netvista.net_buffer_list_context">NET_BUFFER_LIST_CONTEXT</a>
</dt>
<dt>
<a href="netvista.net_buffer_list_pool_parameters">NET_BUFFER_LIST_POOL_PARAMETERS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisAllocateNetBufferListPool function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

