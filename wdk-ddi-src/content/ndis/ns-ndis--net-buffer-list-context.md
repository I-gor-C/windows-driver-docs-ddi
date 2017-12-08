---
UID: NS.ndis._NET_BUFFER_LIST_CONTEXT
title: NET_BUFFER_LIST_CONTEXT
author: windows-driver-content
description: The NET_BUFFER_LIST_CONTEXT structure stores context information for a NET_BUFFER_LIST structure.
old-location: netvista\net_buffer_list_context.htm
old-project: netvista
ms.assetid: e5d70be6-daa5-4d2e-94fd-5739edd8821e
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NET_BUFFER_LIST_CONTEXT,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NET_BUFFER_LIST_CONTEXT
req.alt-loc: ndis.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: See Remarks section
req.iface: 
---

# NET_BUFFER_LIST_CONTEXT structure



## -description
<p>The NET_BUFFER_LIST_CONTEXT structure stores context information for a 
  <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure.</p>


## -syntax

````
typedef struct _NET_BUFFER_LIST_CONTEXT {
  PNET_BUFFER_LIST_CONTEXT Next;
  USHORT                   Size;
  USHORT                   Offset;
  UCHAR                    ContextData[];
} NET_BUFFER_LIST_CONTEXT, *PNET_BUFFER_LIST_CONTEXT;
````


## -struct-fields
<dl>

### -field Next

<dd>
<p>A pointer to the next NET_BUFFER_LIST_CONTEXT structure in a linked list of
     NET_BUFFER_LIST_CONTEXT structures.</p>
</dd>

### -field Size

<dd>
<p>The size, in bytes, of the entire context space in the NET_BUFFER_LIST_CONTEXT structure,
     including the used and unused context space.</p>
</dd>

### -field Offset

<dd>
<p>The offset, in bytes, from the beginning of the context data buffer to the start of the context
     data in the NET_BUFFER_LIST_CONTEXT structure. The 
     <b>Offset</b> member also specifies the size in bytes of the unused context space in the
     NET_BUFFER_LIST_CONTEXT structure.</p>
</dd>

### -field ContextData

<dd>
<p>The context data buffer. The context data can include any information that a driver
     requires.</p>
</dd>
</dl>

## -remarks
<p>Every 
    <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure can include a
    preallocated NET_BUFFER_LIST_CONTEXT structure. As a NET_BUFFER_LIST structure travels through the driver
    stack, the linked list of NET_BUFFER_LIST_CONTEXT structures can expand to accommodate additional data
    space for each driver.</p>

<p>Drivers should use the following NDIS macros and functions to access and manipulate members in a
    NET_BUFFER_LIST_CONTEXT structure:</p>

<p>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferlistcontext.md">
       NdisAllocateNetBufferListContext</a>
</p>

<p>
<a href="..\ndis\nf-ndis-ndisfreenetbufferlistcontext.md">
       NdisFreeNetBufferListContext</a>
</p>

<p>
<a href="netvista.net_buffer_list_context_data_start">
       NET_BUFFER_LIST_CONTEXT_DATA_START</a>
</p>

<p>
<a href="netvista.net_buffer_list_context_data_size">
       NET_BUFFER_LIST_CONTEXT_DATA_SIZE</a>
</p>

<p>The 
    <b>ContextData</b> member of the NET_BUFFER_LIST_CONTEXT structure specifies the data portion of the
    NET_BUFFER_LIST_CONTEXT structure. To improve system performance, a driver should preallocate any
    required context data space when the driver allocates a NET_BUFFER_LIST structure pool. To preallocate
    this data space, a driver calls the 
    <a href="..\ndis\nf-ndis-ndisallocatenetbufferlistpool.md">
    NdisAllocateNetBufferListPool</a> function and then specifies the amount of data space required in the 
    <i>ContextSize</i> parameter. Preallocation of this data space saves NDIS from allocating memory in the
    receive and send paths.</p>

<p>The 
    <b>Offset</b> member specifies the amount of unused context space in the NET_BUFFER_LIST_CONTEXT
    structure. The 
    <b>Offset</b> member also indicates the offset from the beginning of the 
    <b>ContextData</b> member to the start of the used context data space.</p>

<p>NDIS drivers call the 
    <a href="..\ndis\nf-ndis-ndisallocatenetbufferlistcontext.md">
    NdisAllocateNetBufferListContext</a> function to allocate contiguous buffer space in the
    NET_BUFFER_LIST_CONTEXT structure. If necessary, NDIS allocates a new NET_BUFFER_LIST_CONTEXT structure
    with additional space to honor the request. NDIS drivers call the 
    <a href="..\ndis\nf-ndis-ndisfreenetbufferlistcontext.md">
    NdisFreeNetBufferListContext</a> function to free the buffer space.</p>

<p>Use the 
    <a href="netvista.net_buffer_list_context_data_size">
    NET_BUFFER_LIST_CONTEXT_DATA_SIZE</a> macro to obtain the size of the used context space. Use the 
    <a href="netvista.net_buffer_list_context_data_start">
    NET_BUFFER_LIST_CONTEXT_DATA_START</a> macro to get the starting address of the used context space.</p>

<p>For more information on how to use net buffers, see 
    <a href="netvista.net_buffer_architecture">NET_BUFFER Architecture</a>.</p>

## -requirements
<table>
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
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferlistcontext.md">
   NdisAllocateNetBufferListContext</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferlistpool.md">
   NdisAllocateNetBufferListPool</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisfreenetbufferlistcontext.md">NdisFreeNetBufferListContext</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="netvista.net_buffer_list_context_data_start">
   NET_BUFFER_LIST_CONTEXT_DATA_START</a>
</dt>
<dt>
<a href="netvista.net_buffer_list_context_data_size">
   NET_BUFFER_LIST_CONTEXT_DATA_SIZE</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NET_BUFFER_LIST_CONTEXT structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
