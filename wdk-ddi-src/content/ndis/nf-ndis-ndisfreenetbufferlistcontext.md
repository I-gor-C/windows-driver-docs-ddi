---
UID: NF.ndis.NdisFreeNetBufferListContext
title: NdisFreeNetBufferListContext
author: windows-driver-content
description: Call the NdisFreeNetBufferListContext function to release context space in the NET_BUFFER_LIST_CONTEXT structure of a NET_BUFFER_LIST structure.
old-location: netvista\ndisfreenetbufferlistcontext.htm
old-project: netvista
ms.assetid: e5554790-a7a2-4c0d-a6ae-585ea909cd3d
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NdisFreeNetBufferListContext
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
req.alt-api: NdisFreeNetBufferListContext
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

# NdisFreeNetBufferListContext function



## -description
<p>Call the 
  <b>NdisFreeNetBufferListContext</b> function to release context space in the 
  <a href="..\ndis\ns-ndis--net-buffer-list-context.md">NET_BUFFER_LIST_CONTEXT</a> structure of a
  
  <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure.</p>


## -syntax

````
VOID NdisFreeNetBufferListContext(
  _In_ PNET_BUFFER_LIST NetBufferList,
  _In_ USHORT           ContextSize
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
<p>The amount of context space to free.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p><b>NdisFreeNetBufferListContext</b> releases context space that was allocated in a previous call to 
    <a href="..\ndis\nf-ndis-ndisallocatenetbufferlistcontext.md">
    NdisAllocateNetBufferListContext</a>. If 
    <b>NdisAllocateNetBufferListContext</b> allocated memory to satisfy in the call to 
    <b>NdisAllocateNetBufferListContext</b>, 
    <b>NdisFreeNetBufferListContext</b> frees the allocated memory.</p>

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
<a href="devtest.ndis_irql_netbuffer_function">Irql_NetBuffer_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list-context.md">NET_BUFFER_LIST_CONTEXT</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferlistcontext.md">
   NdisAllocateNetBufferListContext</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisFreeNetBufferListContext function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
