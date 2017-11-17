---
UID: NF.ndis.NdisAllocateNetBufferPool
title: NdisAllocateNetBufferPool
author: windows-driver-content
description: Call the NdisAllocateNetBufferPool function to allocate a pool of NET_BUFFER structures.
old-location: netvista\ndisallocatenetbufferpool.htm
ms.assetid: bc27758a-a793-48a1-a6ab-bd193aa9c61a
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
req.alt-api: NdisAllocateNetBufferPool
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
ms.keywords: NdisAllocateNetBufferPool
req.iface: 
---

# NdisAllocateNetBufferPool function



## -description
<p>Call the
  <b>NdisAllocateNetBufferPool</b> function to allocate a pool of 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures.</p>


## -syntax

````
NDIS_HANDLE NdisAllocateNetBufferPool(
  _In_opt_ NDIS_HANDLE                 NdisHandle,
  _In_     PNET_BUFFER_POOL_PARAMETERS Parameters
);
````


## -parameters
<dl>

### -param <i>NdisHandle</i> [in, optional]

<dd>
<p>An NDIS handle that was obtained during caller initialization.</p>
</dd>

### -param <i>Parameters</i> [in]

<dd>
<p>A pointer to a NET_BUFFER_POOL_PARAMETERS structure that defines the parameters for the pool. The
     structure is defined as follows:
     </p>
<div class="code"><span codelanguage=""><table>
<tr>
<th></th>
</tr>
<tr>
<td>
<pre>typedef struct _NET_BUFFER_POOL_PARAMETERS {
  NDIS_OBJECT_HEADER  Header;
  ULONG  PoolTag;
  ULONG  DataSize;
} NET_BUFFER_POOL_PARAMETERS, *PNET_BUFFER_POOL_PARAMETERS;</pre>
</td>
</tr>
</table></span></div>
<p>This structure includes the following members:</p>
<p></p>
<dl>

### -param <a id="Header"></a><a id="header"></a><a id="HEADER"></a><b>Header</b>

<dd>
<p>The 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff566588">NDIS_OBJECT_HEADER</a> structure for the
       NET_BUFFER_POOL_PARAMETERS structure. Set the 
       <b>Type</b> member of the structure that 
       <b>Header</b> specifies to NDIS_OBJECT_TYPE_DEFAULT, the 
       <b>Revision</b> member to NET_BUFFER_POOL_PARAMETERS_REVISION_1, and the 
       <b>Size</b> member to NDIS_SIZEOF_NET_BUFFER_POOL_PARAMETERS_REVISION_1.</p>
</dd>

### -param <a id="PoolTag"></a><a id="pooltag"></a><a id="POOLTAG"></a><b>PoolTag</b>

<dd>
<p>A kernel pool tag that the caller uses when it allocates 
       <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures from this pool. The tag
       is a string, delimited by single quotation marks, with up to four characters, usually specified in
       reverse order. The kernel pool tag helps NDIS to identify the owner of the NET_BUFFER structures that
       are allocated from this pool.</p>
</dd>

### -param <a id="DataSize"></a><a id="datasize"></a><a id="DATASIZE"></a><b>DataSize</b>

<dd>
<p>The default data size for data buffers associated with this pool. The caller must set this value
       if it calls the 
       <a href="https://msdn.microsoft.com/cfac9061-a685-4e67-aaa2-ca43b7e36cfa">
       NdisAllocateNetBufferMdlAndData</a> function. NDIS uses this value to set the size of the data
       buffer that it allocates for the NET_BUFFER structure. If the caller does not use this feature, this
       value should be set to zero.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p><b>NdisAllocateNetBufferPool</b> returns a handle to the NET_BUFFER structure pool that NDIS allocates.
     If the allocation was unsuccessful, this handle is <b>NULL</b>. This handle is a required parameter in
     subsequent calls to NDIS functions that allocate and free NET_BUFFER structures from this pool.</p>

## -remarks
<p>Call the following functions to allocate 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures from the NET_BUFFER
    structure pool.</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561607">NdisAllocateNetBuffer</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/cfac9061-a685-4e67-aaa2-ca43b7e36cfa">
       NdisAllocateNetBufferMdlAndData</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561607">NdisAllocateNetBuffer</a>
</p>

<p>
<a href="https://msdn.microsoft.com/cfac9061-a685-4e67-aaa2-ca43b7e36cfa">
       NdisAllocateNetBufferMdlAndData</a>
</p>

<p>You can call 
    <b>NdisAllocateNetBufferPool</b> and set the 
    <b>DataSize</b> value when creating a NET_BUFFER structure pool. In this case, MDL and data are
    preallocated with each NET_BUFFER structure that the caller allocates from the pool. You must call the 
    <b>NdisAllocateNetBufferMdlAndData</b> function to allocate NET_BUFFER structures from such a pool.</p>

<p>MDL and data buffers that are allocated with 
    <b>NdisAllocateNetBufferMdlAndData</b> should not be freed separate from the NET_BUFFER structure. Such
    structures are freed with the NET_BUFFER structure when you call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562582">NdisFreeNetBuffer</a> function.</p>

<p>Call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562592">NdisFreeNetBufferPool</a> function to
    free NET_BUFFER structure pools that are created with 
    <b>NdisAllocateNetBufferPool</b>.</p>

<p>Call the following functions to allocate 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures from the NET_BUFFER
    structure pool.</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561607">NdisAllocateNetBuffer</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/cfac9061-a685-4e67-aaa2-ca43b7e36cfa">
       NdisAllocateNetBufferMdlAndData</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561607">NdisAllocateNetBuffer</a>
</p>

<p>
<a href="https://msdn.microsoft.com/cfac9061-a685-4e67-aaa2-ca43b7e36cfa">
       NdisAllocateNetBufferMdlAndData</a>
</p>

<p>You can call 
    <b>NdisAllocateNetBufferPool</b> and set the 
    <b>DataSize</b> value when creating a NET_BUFFER structure pool. In this case, MDL and data are
    preallocated with each NET_BUFFER structure that the caller allocates from the pool. You must call the 
    <b>NdisAllocateNetBufferMdlAndData</b> function to allocate NET_BUFFER structures from such a pool.</p>

<p>MDL and data buffers that are allocated with 
    <b>NdisAllocateNetBufferMdlAndData</b> should not be freed separate from the NET_BUFFER structure. Such
    structures are freed with the NET_BUFFER structure when you call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562582">NdisFreeNetBuffer</a> function.</p>

<p>Call the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562592">NdisFreeNetBufferPool</a> function to
    free NET_BUFFER structure pools that are created with 
    <b>NdisAllocateNetBufferPool</b>.</p>

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
<a href="https://msdn.microsoft.com/cfac9061-a685-4e67-aaa2-ca43b7e36cfa">
   NdisAllocateNetBufferMdlAndData</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562582">NdisFreeNetBuffer</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562592">NdisFreeNetBufferPool</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568388">NET_BUFFER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisAllocateNetBufferPool function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
