---
UID: NF.ndis.NdisAllocateReassembledNetBufferList
title: NdisAllocateReassembledNetBufferList
author: windows-driver-content
description: Call the NdisAllocateReassembledNetBufferList function to reassemble a fragmented NET_BUFFER_LIST structure.
old-location: netvista\ndisallocatereassemblednetbufferlist.htm
old-project: netvista
ms.assetid: 6a7fcb43-93bf-4351-8198-1d788b1bcc8c
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisAllocateReassembledNetBufferList
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
req.alt-api: NdisAllocateReassembledNetBufferList
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

# NdisAllocateReassembledNetBufferList function



## -description
<p>Call the 
  <b>NdisAllocateReassembledNetBufferList</b> function to reassemble a fragmented 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>


## -syntax

````
PNET_BUFFER_LIST NdisAllocateReassembledNetBufferList(
  _In_     PNET_BUFFER_LIST FragmentedNetBufferList,
  _In_opt_ NDIS_HANDLE      NetBufferAndNetBufferListPoolHandle,
  _In_     ULONG            StartOffset,
  _In_     ULONG            DataOffsetDelta,
  _In_     ULONG            DataBackFill,
  _In_     ULONG            AllocateReassembleFlags
);
````


## -parameters
<dl>

### -param <i>FragmentedNetBufferList</i> [in]

<dd>
<p>A pointer to the NET_BUFFER_LIST structure to reassemble.</p>
</dd>

### -param <i>NetBufferAndNetBufferListPoolHandle</i> [in, optional]

<dd>
<p>A NET_BUFFER_LIST structure pool handle that was previously returned from the 
     <a href="..\ndis\nf-ndis-ndisallocatenetbufferlistpool.md">
     NdisAllocateNetBufferListPool</a> function. The 
     <b>fAllocateNetBuffer</b> member of the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/hh205394">NET_BUFFER_LIST_POOL_PARAMETERS</a> structure that the caller passed to 
     <b>NdisAllocateNetBufferListPool</b> must have been set to <b>TRUE</b>, and the 
     <b>DataSize</b> member set to zero. If this parameter is <b>NULL</b>, NDIS uses an internal pool.</p>
</dd>

### -param <i>StartOffset</i> [in]

<dd>
<p>The amount of data to skip at the beginning of each source 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure. This amount is in addition
     to the value that is specified in the 
     <b>DataOffset</b> member of the NET_BUFFER structure.</p>
</dd>

### -param <i>DataOffsetDelta</i> [in]

<dd>
<p>The number of bytes of 
     <i>used data space</i> to add to in the reassembled NET_BUFFER structure.</p>
</dd>

### -param <i>DataBackFill</i> [in]

<dd>
<p>If allocation of 
     <i>unused data space</i> (backfill space) is required, this parameter specifies the number of bytes of 
     <i>unused data space</i> in addition to 
     <i>DataOffsetDelta</i> to allocate.</p>
</dd>

### -param <i>AllocateReassembleFlags</i> [in]

<dd>
<p>NDIS flags that can be combined with an OR operation. Set this parameter to zero. There are
     currently no flags defined for this function.</p>
</dd>
</dl>

## -returns
<p>If the reassemble operation succeeds, 
     <b>NdisAllocateReassembledNetBufferList</b> returns a reassembled NET_BUFFER_LIST structure. If the
     operation fails, it returns <b>NULL</b>.</p>

## -remarks
<p><b>NdisAllocateReassembledNetBufferList</b> allocates, initializes, and returns a new 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that includes one 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure and one MDL chain. The new
    NET_BUFFER_LIST structure describes the same data as the fragmented source NET_BUFFER_LIST structure that
    the driver passed at 
    <i>FragmentedNetBufferList</i>. After skipping the number of bytes specified in 
    <i>StartOffset</i> in every fragmented NET_BUFFER structure, NDIS concatenates the remaining data in each
    fragmented NET_BUFFER structure into one reassembled NET_BUFFER structure. Reassembled NET_BUFFER_LIST
    structures do not include an initial 
    <a href="..\ndis\ns-ndis--net-buffer-list-context.md">
    NET_BUFFER_LIST_CONTEXT</a> structure.</p>

<p>Call the 
    <a href="..\ndis\nf-ndis-ndisfreereassemblednetbufferlist.md">
    NdisFreeReassembledNetBufferList</a> function to free a reassembled NET_BUFFER_LIST structure and all
    of the associated NET_BUFFER structures and MDL chains.</p>

<p><b>NdisAllocateReassembledNetBufferList</b> allocates, initializes, and returns a new 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure that includes one 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure and one MDL chain. The new
    NET_BUFFER_LIST structure describes the same data as the fragmented source NET_BUFFER_LIST structure that
    the driver passed at 
    <i>FragmentedNetBufferList</i>. After skipping the number of bytes specified in 
    <i>StartOffset</i> in every fragmented NET_BUFFER structure, NDIS concatenates the remaining data in each
    fragmented NET_BUFFER structure into one reassembled NET_BUFFER structure. Reassembled NET_BUFFER_LIST
    structures do not include an initial 
    <a href="..\ndis\ns-ndis--net-buffer-list-context.md">
    NET_BUFFER_LIST_CONTEXT</a> structure.</p>

<p>Call the 
    <a href="..\ndis\nf-ndis-ndisfreereassemblednetbufferlist.md">
    NdisFreeReassembledNetBufferList</a> function to free a reassembled NET_BUFFER_LIST structure and all
    of the associated NET_BUFFER structures and MDL chains.</p>

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
<a href="..\ndis\nf-ndis-ndisfreereassemblednetbufferlist.md">
   NdisFreeReassembledNetBufferList</a>
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
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/hh205394">NET_BUFFER_LIST_POOL_PARAMETERS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisAllocateReassembledNetBufferList function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
