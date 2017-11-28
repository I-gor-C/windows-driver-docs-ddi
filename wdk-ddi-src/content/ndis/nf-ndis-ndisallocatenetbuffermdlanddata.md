---
UID: NF.ndis.NdisAllocateNetBufferMdlAndData
title: NdisAllocateNetBufferMdlAndData
author: windows-driver-content
description: NDIS drivers call the NdisAllocateNetBufferMdlAndData function to allocate a NET_BUFFER structure along with the associated MDL and data.
old-location: netvista\ndisallocatenetbuffermdlanddata.htm
old-project: netvista
ms.assetid: cfac9061-a685-4e67-aaa2-ca43b7e36cfa
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisAllocateNetBufferMdlAndData
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
req.alt-api: NdisAllocateNetBufferMdlAndData
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
req.iface: 
---

# NdisAllocateNetBufferMdlAndData function



## -description
<p>NDIS drivers call the 
  <b>NdisAllocateNetBufferMdlAndData</b> function to allocate a NET_BUFFER structure along with the associated
  MDL and data.</p>


## -syntax

````
PNET_BUFFER NdisAllocateNetBufferMdlAndData(
  _In_ NDIS_HANDLE PoolHandle
);
````


## -parameters
<dl>

### -param <i>PoolHandle</i> [in]

<dd>
<p>A NET_BUFFER structure pool handle that was previously returned from a call to the 
     <b>NdisAllocateNetBufferPool</b> function.</p>
</dd>
</dl>

## -returns
<p><b>NdisAllocateNetBufferMdlAndData</b> returns a pointer to the NET_BUFFER structure that NDIS allocated.
     If the allocation was unsuccessful, this pointer is <b>NULL</b>.</p>

## -remarks
<p>The caller must call the 
    <b>NdisAllocateNetBufferPool</b> function and specify the maximum size of the data buffers. Given this
    value, NDIS can preallocate buffers for the caller.</p>

<p>This function allocates a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure, MDL and data in a single
    memory buffer. This is useful to achieve high performance when NET_BUFFER structures are frequently
    allocated and freed. The caller should not call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561607">NdisAllocateNetBuffer</a> to allocate
    NET_BUFFERs out of NET_BUFFER pools which contain data.</p>

<p>NDIS uses the 
    <i>PoolHandle</i> parameter to get a block of memory, and then creates the NET_BUFFER, MDL, and data
    buffer.</p>

<p>To free the NET_BUFFER and associated information, call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562582">NdisFreeNetBuffer</a> function.</p>

<p>The caller must call the 
    <b>NdisAllocateNetBufferPool</b> function and specify the maximum size of the data buffers. Given this
    value, NDIS can preallocate buffers for the caller.</p>

<p>This function allocates a 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure, MDL and data in a single
    memory buffer. This is useful to achieve high performance when NET_BUFFER structures are frequently
    allocated and freed. The caller should not call 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff561607">NdisAllocateNetBuffer</a> to allocate
    NET_BUFFERs out of NET_BUFFER pools which contain data.</p>

<p>NDIS uses the 
    <i>PoolHandle</i> parameter to get a block of memory, and then creates the NET_BUFFER, MDL, and data
    buffer.</p>

<p>To free the NET_BUFFER and associated information, call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562582">NdisFreeNetBuffer</a> function.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547985">Irql_NetBuffer_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561607">NdisAllocateNetBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562582">NdisFreeNetBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisAllocateNetBufferMdlAndData function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
