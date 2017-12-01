---
UID: NS.ndis._NET_BUFFER_SHARED_MEMORY
title: NET_BUFFER_SHARED_MEMORY
author: windows-driver-content
description: The NET_BUFFER_SHARED_MEMORY structure specifies a shared memory buffer that is associated with a NET_BUFFER structure.
old-location: netvista\net_buffer_shared_memory.htm
old-project: netvista
ms.assetid: 492bb1cd-fc3e-4e85-9074-32ebbf1fb837
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NET_BUFFER_SHARED_MEMORY,
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Windows
req.target-min-winverclnt: Supported in NDIS 6.20 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NET_BUFFER_SHARED_MEMORY
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

# NET_BUFFER_SHARED_MEMORY structure



## -description
<p>The NET_BUFFER_SHARED_MEMORY structure specifies a shared memory buffer that is associated with a 
  <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structure.</p>


## -syntax

````
typedef struct _NET_BUFFER_SHARED_MEMORY {
  PNET_BUFFER_SHARED_MEMORY NextSharedMemorySegment;
  ULONG                     SharedMemoryFlags;
  NDIS_HANDLE               SharedMemoryHandle;
  ULONG                     SharedMemoryOffset;
  ULONG                     SharedMemoryLength;
} NET_BUFFER_SHARED_MEMORY, *PNET_BUFFER_SHARED_MEMORY;
````


## -struct-fields
<dl>

### -field <b>NextSharedMemorySegment</b>

<dd>
<p>A pointer to the next NET_BUFFER_SHARED_MEMORY structure in a NULL-terminated linked list of such
     structures.</p>
</dd>

### -field <b>SharedMemoryFlags</b>

<dd>
<p>A ULONG value that contains shared memory flags. This member is reserved for future use.</p>
</dd>

### -field <b>SharedMemoryHandle</b>

<dd>
<p>An NDIS_HANDLE that contains an NDIS shared memory handle.</p>
</dd>

### -field <b>SharedMemoryOffset</b>

<dd>
<p>A ULONG value that contains the offset, in bytes, of the shared memory.</p>
</dd>

### -field <b>SharedMemoryLength</b>

<dd>
<p>A ULONG value for the length, in bytes, of the shared memory segment.</p>
</dd>
</dl>

## -remarks
<p>An NDIS 6.20 or later driver uses the NET_BUFFER_SHARED_MEMORY structure to describe a shared memory
    buffer. There can be a linked list of such shared memory buffers that are associated with a 
    <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structure. Virtual machine queue (VMQ)
    capable NICs use these shared memory buffers in the virtualization environment.</p>

<p>Use the 
    <a href="netvista.net_buffer_shared_mem_next_segment">
    NET_BUFFER_SHARED_MEM_NEXT_SEGMENT</a>, 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568420">NET_BUFFER_SHARED_MEM_FLAGS</a>, 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568421">NET_BUFFER_SHARED_MEM_HANDLE</a>, 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568727">NET_BUFFER_SHARED_MEM_OFFSET</a>,
    and 
    <a href="netvista.net_buffer_shared_mem_length">
    NET_BUFFER_SHARED_MEM_LENGTH</a> macros to access the NET_BUFFER_SHARED_MEMORY in a NET_BUFFER
    structure. The 
    <b>SharedMemoryInfo</b> member of the NET_BUFFER structure contains the first NET_BUFFER_SHARED_MEMORY
    structure in the linked list.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Version</p>
</th>
<td width="70%">
<p>Supported in NDIS 6.20 and later.</p>
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
<a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568420">NET_BUFFER_SHARED_MEM_FLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568421">NET_BUFFER_SHARED_MEM_HANDLE</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568725">NET_BUFFER_SHARED_MEM_LENGTH</a>
</dt>
<dt>
<a href="netvista.net_buffer_shared_mem_next_segment">
   NET_BUFFER_SHARED_MEM_NEXT_SEGMENT</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568727">NET_BUFFER_SHARED_MEM_OFFSET</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NET_BUFFER_SHARED_MEMORY structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
