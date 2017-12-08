---
UID: NS.ndis._NET_BUFFER
title: NET_BUFFER
author: windows-driver-content
description: The NET_BUFFER structure specifies data that is transmitted or received over the network.
old-location: netvista\net_buffer.htm
old-project: netvista
ms.assetid: 66a725f9-ae72-41b4-8840-63c9ff89ace7
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NET_BUFFER,
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
req.alt-api: NET_BUFFER
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

# NET_BUFFER structure



## -description
<p>The NET_BUFFER structure specifies data that is transmitted or received over the network.</p>


## -syntax

````
typedef struct _NET_BUFFER {
  NET_BUFFER_HEADER     NetBufferHeader;
  USHORT                ChecksumBias;
  USHORT                Reserved;
  NDIS_HANDLE           NdisPoolHandle;
  PVOID                 NdisReserved[2];
  PVOID                 ProtocolReserved[6];
  PVOID                 MiniportReserved[4];
  NDIS_PHYSICAL_ADDRESS DataPhysicalAddress;
#if (NDIS_SUPPORT_NDIS620)
  union {
    PNET_BUFFER_SHARED_MEMORY SharedMemoryInfo;
    PSCATTER_GATHER_LIST      ScatterGatherList;
  };
#endif 
} NET_BUFFER, *PNET_BUFFER;
````


## -struct-fields
<dl>

### -field NetBufferHeader

<dd>
<p>A 
     <a href="..\ndis\ns-ndis--net-buffer-header.md">NET_BUFFER_HEADER</a> structure.</p>
</dd>

### -field ChecksumBias

<dd>
<p>The number of bytes to skip over from the beginning of the data buffer when computing a checksum.
     This member is used by the TCP/IP protocol.</p>
</dd>

### -field Reserved

<dd>
<p>Reserved for future use.</p>
</dd>

### -field NdisPoolHandle

<dd>
<p>A pool handle that identifies the NET_BUFFER pool from which the NET_BUFFER structure was
     allocated.</p>
</dd>

### -field NdisReserved

<dd>
<p>Reserved for NDIS.</p>
</dd>

### -field ProtocolReserved

<dd>
<p>Reserved for use by protocol drivers. Protocol drivers and NDIS intermediate drivers can use this
     area for their own purposes. Intermediate drivers can use this member only if it is not already in
     use.</p>
</dd>

### -field MiniportReserved

<dd>
<p>Reserved for use by miniport drivers. Miniport drivers and NDIS intermediate drivers can use this
     area for their own purposes.</p>
</dd>

### -field DataPhysicalAddress

<dd>
<div class="alert"><b>Note</b>  The name of this member is 
      <b>NdisReserved1</b> for NDIS 6.0 drivers and is 
      <b>DataPhysicalAddress</b> for NDIS 6.1 and later drivers. For NDIS 6.0 drivers, this member is reserved
      for NDIS.</div>
<div> </div>
<p>The physical address of the data portion of a frame. This member should be to zero if the driver
      that allocated NET_BUFFER does not specify the address. This member is valid only if the
      NDIS_NBL_FLAGS_SPLIT_AT_UPPER_LAYER_PROTOCOL_HEADER or
      NDIS_NBL_FLAGS_SPLIT_AT_UPPER_LAYER_PROTOCOL_PAYLOAD flag is set in the 
      <b>NblFlags</b> member of the 
      <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure that is
      associated with the NET_BUFFER.</p>
<div class="alert"><b>Note</b>  A miniport driver can set the 
      <b>DataPhysicalAddress</b> member of the NET_BUFFER structure, even if the structure is not associated
      with a split frame. In this case, 
      <b>DataPhysicalAddress</b> contains the physical address of the header MDL.</div>
<div> </div>
</dd>

### -field SharedMemoryInfo

<dd>
<p>A pointer to an 
      <a href="..\ndis\ns-ndis--net-buffer-shared-memory.md">
      NET_BUFFER_SHARED_MEMORY</a> structure.</p>
</dd>

### -field ScatterGatherList

<dd>
<p>The SCATTER_GATHER_LIST structure describes a scatter/gather list for DMA.</p>
</dd>
</dl>

## -remarks
<p>NDIS drivers can call the following functions to allocate and initialize a NET_BUFFER structure:</p>

<p>
<a href="..\ndis\nf-ndis-ndisallocatenetbuffer.md">NdisAllocateNetBuffer</a>
</p>

<p>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferandnetbufferlist.md">
       NdisAllocateNetBufferAndNetBufferList</a>
</p>

<p>NDIS drivers can call the 
    <a href="..\ndis\nf-ndis-ndisallocatenetbufferlistpool.md">
    NdisAllocateNetBufferListPool</a> function and then set the 
    <b>fAllocateNetBuffer</b> member of the 
    <a href="..\ndis\ns-ndis--net-buffer-list-pool-parameters.md">NET_BUFFER_LIST_POOL_PARAMETERS</a> structure to <b>TRUE</b> when allocating a 
    <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure pool. In this
    case, a NET_BUFFER structure is preallocated with each NET_BUFFER_LIST structure that the driver
    allocates from the pool.</p>

<p>Chained to each NET_BUFFER structure are one or more buffer descriptors that map buffers that contain
    network packet data. These buffer descriptors are specified as an MDL chain in the 
    <b>NetBufferHeader</b> member. Such network packet data either was received or will be transmitted.</p>

<p>To access additional data space in the MDL chain, NDIS drivers can call the following functions:</p>

<p>
<a href="..\ndis\nf-ndis-ndisretreatnetbufferdatastart.md">
       NdisRetreatNetBufferDataStart</a>
</p>

<p>
<a href="..\ndis\nf-ndis-ndisretreatnetbufferlistdatastart.md">
       NdisRetreatNetBufferListDataStart</a>
</p>

<p>NDIS drivers typically use the 
    <b>MiniportReserved</b> or 
    <b>ProtocolReserved</b> members of the NET_BUFFER structure to maintain NET_BUFFER structure context
    information.</p>

<p>To access members of the NET_BUFFER structure, use the following macros and functions:</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568416">NET_BUFFER_NEXT_NB</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568386">NET_BUFFER_FIRST_MDL</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568383">NET_BUFFER_DATA_OFFSET</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568382">NET_BUFFER_DATA_LENGTH</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568417">NET_BUFFER_PROTOCOL_RESERVED</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568415">NET_BUFFER_MINIPORT_RESERVED</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568378">NET_BUFFER_CHECKSUM_BIAS</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568379">NET_BUFFER_CURRENT_MDL</a>
</p>

<p>
<a href="netvista.net_buffer_current_mdl_offset">
       NET_BUFFER_CURRENT_MDL_OFFSET</a>
</p>

<p>
<a href="..\ndis\nf-ndis-ndisgetpoolfromnetbuffer.md">NdisGetPoolFromNetBuffer</a>
</p>

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
<a href="..\ndis\nf-ndis-ndisallocatenetbuffer.md">NdisAllocateNetBuffer</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferandnetbufferlist.md">
   NdisAllocateNetBufferAndNetBufferList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferlistpool.md">
   NdisAllocateNetBufferListPool</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisgetpoolfromnetbuffer.md">NdisGetPoolFromNetBuffer</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismsendnetbufferlistscomplete.md">
   NdisMSendNetBufferListsComplete</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisretreatnetbufferdatastart.md">
   NdisRetreatNetBufferDataStart</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisretreatnetbufferlistdatastart.md">
   NdisRetreatNetBufferListDataStart</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568378">NET_BUFFER_CHECKSUM_BIAS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568379">NET_BUFFER_CURRENT_MDL</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568380">NET_BUFFER_CURRENT_MDL_OFFSET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568382">NET_BUFFER_DATA_LENGTH</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568383">NET_BUFFER_DATA_OFFSET</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568386">NET_BUFFER_FIRST_MDL</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-header.md">NET_BUFFER_HEADER</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="..\ndis\ns-ndis--net-buffer-list-pool-parameters.md">NET_BUFFER_LIST_POOL_PARAMETERS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568415">NET_BUFFER_MINIPORT_RESERVED</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568416">NET_BUFFER_NEXT_NB</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568417">NET_BUFFER_PROTOCOL_RESERVED</a>
</dt>
<dt>
<a href="..\wdm\ns-wdm--scatter-gather-list.md">SCATTER_GATHER_LIST</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NET_BUFFER structure%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
