---
UID: NF.ndis.NdisFreeNetBufferPool
title: NdisFreeNetBufferPool function
author: windows-driver-content
description: Call the NdisFreeNetBufferPool function to free NET_BUFFER structure pools that are created with the NdisAllocateNetBufferPool function.
old-location: netvista\ndisfreenetbufferpool.htm
old-project: NetVista
ms.assetid: e1ea63d1-9322-44c7-8196-2fe1a7b6a220
ms.author: windowsdriverdev
ms.date: 12/14/2017
ms.keywords: NdisFreeNetBufferPool
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
req.alt-api: NdisFreeNetBufferPool
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_NetBuffer_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
---

# NdisFreeNetBufferPool function



## -description
Call the 
  <b>NdisFreeNetBufferPool</b> function to free 
  <a href="netvista.net_buffer">NET_BUFFER</a> structure pools that are created with
  the 
  <a href="netvista.ndisallocatenetbufferpool">
  NdisAllocateNetBufferPool</a> function.



## -syntax

````
VOID NdisFreeNetBufferPool(
  _In_ NDIS_HANDLE PoolHandle
);
````


## -parameters

### -param PoolHandle [in]

The pool handle for the NET_BUFFER structure pool to be freed.


## -returns
None


## -remarks
You should free all the 
    <a href="netvista.net_buffer">NET_BUFFER</a> structures in a pool before freeing
    the NET_BUFFER structure pool. Call the 
    <a href="netvista.ndisfreenetbuffer">NdisFreeNetBuffer</a> function to free each
    NET_BUFFER structure.


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
<a href="netvista.net_buffer">NET_BUFFER</a>
</dt>
<dt>
<a href="netvista.ndisallocatenetbufferpool">NdisAllocateNetBufferPool</a>
</dt>
<dt>
<a href="netvista.ndisfreenetbuffer">NdisFreeNetBuffer</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [NetVista\netvista]:%20NdisFreeNetBufferPool function%20 RELEASE:%20(12/14/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

