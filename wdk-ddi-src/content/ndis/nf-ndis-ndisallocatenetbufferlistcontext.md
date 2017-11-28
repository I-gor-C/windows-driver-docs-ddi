---
UID: NF.ndis.NdisAllocateNetBufferListContext
title: NdisAllocateNetBufferListContext
author: windows-driver-content
description: Call the NdisAllocateNetBufferListContext function to allocate more context space in the NET_BUFFER_LIST_CONTEXT structure of a NET_BUFFER_LIST structure.
old-location: netvista\ndisallocatenetbufferlistcontext.htm
old-project: netvista
ms.assetid: 3bbad723-86bf-4206-9e51-52a66efaec20
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisAllocateNetBufferListContext
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
req.alt-api: NdisAllocateNetBufferListContext
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

# NdisAllocateNetBufferListContext function



## -description
<p>Call the 
  <b>NdisAllocateNetBufferListContext</b> function to allocate more context space in the 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568389">NET_BUFFER_LIST_CONTEXT</a> structure of a
  
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a> structure.</p>


## -syntax

````
NDIS_STATUS NdisAllocateNetBufferListContext(
  _In_ PNET_BUFFER_LIST NetBufferList,
  _In_ USHORT           ContextSize,
  _In_ USHORT           ContextBackFill,
  _In_ ULONG            PoolTag
);
````


## -parameters
<dl>

### -param <i>NetBufferList</i> [in]

<dd>
<p>A pointer to a previously allocated NET_BUFFER_LIST structure.</p>
</dd>

### -param <i>ContextSize</i> [in]

<dd>
<p>The amount of context space to allocate in the NET_BUFFER_LIST_CONTEXT structure. This amount must
     be a multiple of the value defined by MEMORY_ALLOCATION_ALIGNMENT.</p>
</dd>

### -param <i>ContextBackFill</i> [in]

<dd>
<p>The amount of memory, in addition to the value of 
     <i>ContextSize</i>, to allocate if NDIS must allocate memory to satisfy the request. This amount must be
     a multiple of the value defined by MEMORY_ALLOCATION_ALIGNMENT.</p>
</dd>

### -param <i>PoolTag</i> [in]

<dd>
<p>A kernel pool tag that NDIS uses to allocate the memory for the NET_BUFFER_LIST_CONTEXT structure,
     if allocation is required. The tag is a string, delimited by single quotation marks, with up to four
     characters, usually specified in reversed order. The kernel pool tag helps NDIS to identify the owner of
     the memory.</p>
</dd>
</dl>

## -returns
<p><b>NdisAllocateNetBufferListContext</b> returns one of the following:</p><dl>
<dt><b>NDIS_STATUS_SUCCESS</b></dt>
</dl><p><b>NdisAllocateNetBufferListContext</b> successfully allocated context space either by reducing the
       value of the 
       <b>Offset</b> member of the NET_BUFFER_LIST_CONTEXT structure or by allocating new memory.</p><dl>
<dt><b>NDIS_STATUS_RESOURCES</b></dt>
</dl><p><b>NdisAllocateNetBufferListContext</b> failed due to insufficient resources.</p><dl>
<dt><b>NDIS_STATUS_FAILURE</b></dt>
</dl><p><b>NdisAllocateNetBufferListContext</b> failed for reasons other than insufficient resources.</p>

<p> </p>

## -remarks
<p>If there is enough unused context space available in the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568389">NET_BUFFER_LIST_CONTEXT</a> structure to
    satisfy the request, 
    <b>NdisAllocateNetBufferListContext</b> simply reduces the value of the 
    <b>Offset</b> member in the NET_BUFFER_LIST_CONTEXT structure. Otherwise, NDIS allocates new memory for
    context space. You can specify 
    <i>ContextBackFill</i> to allocate extra memory so that the next call to 
    <b>NdisAllocateNetBufferListContext</b> does not have to allocate memory.</p>

<p>Call the 
    <a href="..\ndis\nf-ndis-ndisfreenetbufferlistcontext.md">
    NdisFreeNetBufferListContext</a> function to release the context space in the NET_BUFFER_LIST_CONTEXT
    structure that was allocated with 
    <b>NdisAllocateNetBufferListContext</b>.</p>

<p>If there is enough unused context space available in the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568389">NET_BUFFER_LIST_CONTEXT</a> structure to
    satisfy the request, 
    <b>NdisAllocateNetBufferListContext</b> simply reduces the value of the 
    <b>Offset</b> member in the NET_BUFFER_LIST_CONTEXT structure. Otherwise, NDIS allocates new memory for
    context space. You can specify 
    <i>ContextBackFill</i> to allocate extra memory so that the next call to 
    <b>NdisAllocateNetBufferListContext</b> does not have to allocate memory.</p>

<p>Call the 
    <a href="..\ndis\nf-ndis-ndisfreenetbufferlistcontext.md">
    NdisFreeNetBufferListContext</a> function to release the context space in the NET_BUFFER_LIST_CONTEXT
    structure that was allocated with 
    <b>NdisAllocateNetBufferListContext</b>.</p>

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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562587">NdisFreeNetBufferListContext</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisAllocateNetBufferListContext function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
