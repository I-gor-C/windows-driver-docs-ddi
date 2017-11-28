---
UID: NF.ndis.NdisAllocateCloneNetBufferList
title: NdisAllocateCloneNetBufferList
author: windows-driver-content
description: Call the NdisAllocateCloneNetBufferList function to create a new clone NET_BUFFER_LIST structure.
old-location: netvista\ndisallocateclonenetbufferlist.htm
old-project: netvista
ms.assetid: 357605a1-5c57-44ed-97b3-f466f9a7182c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisAllocateCloneNetBufferList
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
req.alt-api: NdisAllocateCloneNetBufferList
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

# NdisAllocateCloneNetBufferList function



## -description
<p>Call the 
  <b>NdisAllocateCloneNetBufferList</b> function to create a new clone 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>


## -syntax

````
PNET_BUFFER_LIST NdisAllocateCloneNetBufferList(
  _In_     PNET_BUFFER_LIST OriginalNetBufferList,
  _In_opt_ NDIS_HANDLE      NetBufferListPoolHandle,
  _In_opt_ NDIS_HANDLE      NetBufferPoolHandle,
  _In_     ULONG            AllocateCloneFlags
);
````


## -parameters
<dl>

### -param <i>OriginalNetBufferList</i> [in]

<dd>
<p>A pointer to an existing <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>
</dd>

### -param <i>NetBufferListPoolHandle</i> [in, optional]

<dd>
<p>A handle that was obtained from a call to the 
     <a href="..\ndis\nf-ndis-ndisallocatenetbufferlistpool.md">
     NdisAllocateNetBufferListPool</a> function.</p>
</dd>

### -param <i>NetBufferPoolHandle</i> [in, optional]

<dd>
<p>A 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure pool handle that was
     previously returned from a call to 
     <a href="..\ndis\nf-ndis-ndisallocatenetbufferpool.md">
     NdisAllocateNetBufferPool</a>.</p>
</dd>

### -param <i>AllocateCloneFlags</i> [in]

<dd>
<p>NDIS flags that can be combined with an OR operation. The following flags are defined:
     </p>
<p></p>
<dl>

### -param <a id="NDIS_CLONE_FLAGS_RESERVED"></a><a id="ndis_clone_flags_reserved"></a>NDIS_CLONE_FLAGS_RESERVED

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -param <a id="NDIS_CLONE_FLAGS_USE_ORIGINAL_MDLS"></a><a id="ndis_clone_flags_use_original_mdls"></a>NDIS_CLONE_FLAGS_USE_ORIGINAL_MDLS

<dd>
<p>If this flag is set, NDIS does not allocate new MDLs for the cloned <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>. Instead,
       the cloned <b>NET_BUFFER_LIST</b> uses the same MDL chain as the original <b>NET_BUFFER_LIST</b>. If
       NDIS_CLONE_FLAGS_USE_ORIGINAL_MDLS is cleared, NDIS allocates new MDLs to reference the original data
       buffers.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p><b>NdisAllocateCloneNetBufferList</b> returns a pointer to the new clone <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure. If
     the allocation was unsuccessful, this pointer is <b>NULL</b>.</p>

## -remarks
<p>Call 
    <b>NdisAllocateCloneNetBufferList</b> to create a clone 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that you can use
    to send duplicate data on a separate data path.</p>

<p>Each <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure in the original <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure is only cloned from the start of the used data space, not the start of the entire data space. To get the offset from the beginning of the data space to the start of the used data space, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568383">NET_BUFFER_DATA_OFFSET</a>  macro.</p>

<p>If the cloned <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure should have attributes that are associated with a given pool,
    the caller must specify the pool handle in the 
    <i>NetBufferListPoolHandle</i> or 
    <i>NetBufferPoolHandle</i> parameter. For example, the 
    <b>ProtocolType</b> member of the <b>NET_BUFFER_LIST</b> structure is associated with the pool.</p>

<p>The clone <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure describes the same data that is described by the <b>NET_BUFFER_LIST</b>
    structure at 
    <i>OriginalNetBufferList</i>. NDIS does not copy the data that is described by the original MDLs to new
    data buffers. Instead, the cloned structures reference the original data buffers. The clone
    <b>NET_BUFFER_LIST</b> structure does not include an initial 
    <a href="..\ndis\ns-ndis--net-buffer-list-context.md">
    NET_BUFFER_LIST_CONTEXT</a> structure.</p>

<p>Call the 
    <a href="..\ndis\nf-ndis-ndisfreeclonenetbufferlist.md">
    NdisFreeCloneNetBufferList</a> function to free a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure and all of the associated
    structures and MDL chains that were allocated by calling 
    <b>NdisAllocateCloneNetBufferList</b>.</p>

<p>Call 
    <b>NdisAllocateCloneNetBufferList</b> to create a clone 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that you can use
    to send duplicate data on a separate data path.</p>

<p>Each <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure in the original <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure is only cloned from the start of the used data space, not the start of the entire data space. To get the offset from the beginning of the data space to the start of the used data space, use the <a href="https://msdn.microsoft.com/library/windows/hardware/ff568383">NET_BUFFER_DATA_OFFSET</a>  macro.</p>

<p>If the cloned <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure should have attributes that are associated with a given pool,
    the caller must specify the pool handle in the 
    <i>NetBufferListPoolHandle</i> or 
    <i>NetBufferPoolHandle</i> parameter. For example, the 
    <b>ProtocolType</b> member of the <b>NET_BUFFER_LIST</b> structure is associated with the pool.</p>

<p>The clone <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure describes the same data that is described by the <b>NET_BUFFER_LIST</b>
    structure at 
    <i>OriginalNetBufferList</i>. NDIS does not copy the data that is described by the original MDLs to new
    data buffers. Instead, the cloned structures reference the original data buffers. The clone
    <b>NET_BUFFER_LIST</b> structure does not include an initial 
    <a href="..\ndis\ns-ndis--net-buffer-list-context.md">
    NET_BUFFER_LIST_CONTEXT</a> structure.</p>

<p>Call the 
    <a href="..\ndis\nf-ndis-ndisfreeclonenetbufferlist.md">
    NdisFreeCloneNetBufferList</a> function to free a <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure and all of the associated
    structures and MDL chains that were allocated by calling 
    <b>NdisAllocateCloneNetBufferList</b>.</p>

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
<a href="..\ndis\nf-ndis-ndisallocatenetbufferlistpool.md">
   NdisAllocateNetBufferListPool</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561613">NdisAllocateNetBufferPool</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561841">NdisFreeCloneNetBufferList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568389">NET_BUFFER_LIST_CONTEXT</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisAllocateCloneNetBufferList function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
