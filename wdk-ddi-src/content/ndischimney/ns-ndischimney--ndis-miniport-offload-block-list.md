---
UID: NS.ndischimney._NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
title: NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
author: windows-driver-content
description: The NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure is the basic building block of a TCP chimney offload state tree. An offload state tree can contain one or more NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structures.
old-location: netvista\ndis_miniport_offload_block_list.htm
old-project: netvista
ms.assetid: ebc98e65-5d11-4c3d-aea1-dfad1434c093
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_MINIPORT_OFFLOAD_BLOCK_LIST, NDIS_MINIPORT_OFFLOAD_BLOCK_LIST, *PNDIS_MINIPORT_OFFLOAD_BLOCK_LIST
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: struct
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
req.alt-loc: ndischimney.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: 
req.iface: 
---

# NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>The NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure is the basic building block of a TCP chimney offload
  state tree. An offload state tree can contain one or more NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
  structures.</p>


## -syntax

````
typedef struct _NDIS_MINIPORT_OFFLOAD_BLOCK_LIST {
  NDIS_OBJECT_HEADER                       Header;
  struct _NDIS_MINIPORT_OFFLOAD_BLOCK_LIST  *NextBlock;
  struct _NDIS_MINIPORT_OFFLOAD_BLOCK_LIST  *DependentBlockList;
  NDIS_STATUS                              Status;
  PVOID                                    NdisReserved[2];
  PVOID                                    *MiniportOffloadContext;
  NDIS_HANDLE                              NdisOffloadHandle;
  PVOID                                    ProtocolReserved[2];
  PVOID                                    MiniportReserved[2];
  PVOID                                    ImReserved[2];
  PVOID                                    Scratch[2];
  PVOID                                    SourceHandle;
  NDIS_PORT_NUMBER                         PortNumber;
  PNET_BUFFER_LIST                         NetBufferListChain;
} NDIS_MINIPORT_OFFLOAD_BLOCK_LIST, *PNDIS_MINIPORT_OFFLOAD_BLOCK_LIST;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header of the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure. The header is formatted as an 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure. The
     NDIS_OBJECT_HEADER structure contains the revision number of the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
     structure, the type of offload state that immediately follows the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
     structure in memory, and the size of the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure, including the
     header, in bytes. 
     </p>
<p>The 
     <b>Type</b> member of the NDIS_OBJECT_HEADER structure indicates the type of offload state, and by
     implication, the specific offload state structure (or structures) that immediately follow the
     NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure in memory.</p>
<p>The following OFFLOAD_STATE_TYPE values are supported:</p>
<p></p>
<dl>

### -field <a id="NeighborOffloadConstState"></a><a id="neighboroffloadconststate"></a><a id="NEIGHBOROFFLOADCONSTSTATE"></a><b>NeighborOffloadConstState</b>

<dd>
<p>Specifies the constant neighbor state. This state is formatted as a 
       <a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-const.md">
       NEIGHBOR_OFFLOAD_STATE_CONST</a> structure.</p>
</dd>

### -field <a id="NeighborOffloadCachedState"></a><a id="neighboroffloadcachedstate"></a><a id="NEIGHBOROFFLOADCACHEDSTATE"></a><b>NeighborOffloadCachedState</b>

<dd>
<p>Specifies the cached neighbor state. This state is formatted as a 
       <a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-cached.md">
       NEIGHBOR_OFFLOAD_STATE_CACHED</a> structure.</p>
</dd>

### -field <a id="NeighborOffloadDelegatedState"></a><a id="neighboroffloaddelegatedstate"></a><a id="NEIGHBOROFFLOADDELEGATEDSTATE"></a><b>NeighborOffloadDelegatedState</b>

<dd>
<p>Specifies the delegated neighbor state. This state is formatted as a 
       <a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-delegated.md">
       NEIGHBOR_OFFLOAD_STATE_DELEGATED</a> structure.</p>
</dd>

### -field <a id="NeighborOffloadState"></a><a id="neighboroffloadstate"></a><a id="NEIGHBOROFFLOADSTATE"></a><b>NeighborOffloadState</b>

<dd>
<p>Specifies all of the neighbor state information, including the constant, cached, and delegated
       neighbor state. This state is formatted as a NEIGHBOR_OFFLOAD_STATE_CONST structure, followed by a
       NEIGHBOR_OFFLOAD_STATE_CACHED structure, followed by a NEIGHBOR_OFFLOAD_STATE_DELEGATED
       structure.</p>
</dd>

### -field <a id="Ip4OffloadConstState"></a><a id="ip4offloadconststate"></a><a id="IP4OFFLOADCONSTSTATE"></a><b>Ip4OffloadConstState</b>

<dd>
<p>Specifies the constant path state (IPv4). This state is formatted as a 
       <a href="..\ndischimney\ns-ndischimney--path-offload-state-const.md">
       PATH_OFFLOAD_STATE_CONST</a> structure.</p>
</dd>

### -field <a id="Ip4OffloadCachedState"></a><a id="ip4offloadcachedstate"></a><a id="IP4OFFLOADCACHEDSTATE"></a><b>Ip4OffloadCachedState</b>

<dd>
<p>Specifies the cached path state (IPv4). This state is formatted as a 
       <a href="..\ndischimney\ns-ndischimney--path-offload-state-cached.md">
       PATH_OFFLOAD_STATE_CACHED</a> structure.</p>
</dd>

### -field <a id="Ip4OffloadDelegatedState"></a><a id="ip4offloaddelegatedstate"></a><a id="IP4OFFLOADDELEGATEDSTATE"></a><b>Ip4OffloadDelegatedState</b>

<dd>
<p>Specifies the delegated path state (IPv4). This state is formatted as a 
       <a href="..\ndischimney\ns-ndischimney--path-offload-state-delegated.md">
       PATH_OFFLOAD_STATE_DELEGATED</a> structure. Currently there is no delegated path state. The
       PATH_OFFLOAD_STATE_DELEGATED structure does not contain any variables.</p>
</dd>

### -field <a id="Ip4OffloadState"></a><a id="ip4offloadstate"></a><a id="IP4OFFLOADSTATE"></a><b>Ip4OffloadState</b>

<dd>
<p>Specifies all of the path state (IPv4), including the constant, cached, and delegated path
       state. This state is formatted as a PATH_OFFLOAD_STATE_CONST structure, followed by a
       PATH_OFFLOAD_STATE_CACHED structure, followed by a PATH_OFFLOAD_STATE_DELEGATED structure.</p>
</dd>

### -field <a id="Ip6OffloadConstState"></a><a id="ip6offloadconststate"></a><a id="IP6OFFLOADCONSTSTATE"></a><b>Ip6OffloadConstState</b>

<dd>
<p>Specifies the constant path state (IPv6). This state is formatted as a PATH_OFFLOAD_STATE_CONST
       structure.</p>
</dd>

### -field <a id="Ip6OffloadCachedState"></a><a id="ip6offloadcachedstate"></a><a id="IP6OFFLOADCACHEDSTATE"></a><b>Ip6OffloadCachedState</b>

<dd>
<p>Specifies the cached path state (IPv6). This state is formatted as a PATH_OFFLOAD_STATE_CACHED
       structure.</p>
</dd>

### -field <a id="Ip6OffloadDelegatedState"></a><a id="ip6offloaddelegatedstate"></a><a id="IP6OFFLOADDELEGATEDSTATE"></a><b>Ip6OffloadDelegatedState</b>

<dd>
<p>Specifies the delegated path state (IPv6). This state is formatted as a
       PATH_OFFLOAD_STATE_DELEGATED structure. Currently, there is no delegated path state. The
       PATH_OFFLOAD_STATE_DELEGATED structure does not contain any variables.</p>
</dd>

### -field <a id="Ip6OffloadState"></a><a id="ip6offloadstate"></a><a id="IP6OFFLOADSTATE"></a><b>Ip6OffloadState</b>

<dd>
<p>Specifies all of the path state information(IPv6), including the constant, cached, and delegated
       path state. This state is formatted as a PATH_OFFLOAD_STATE_CONST structure, followed by a
       PATH_OFFLOAD_STATE_CACHED structure, followed by a PATH_OFFLOAD_STATE_DELEGATED structure.</p>
</dd>

### -field <a id="TcpOffloadConstState"></a><a id="tcpoffloadconststate"></a><a id="TCPOFFLOADCONSTSTATE"></a><b>TcpOffloadConstState</b>

<dd>
<p>Specifies the constant TCP state. This state is formatted as a 
       <a href="..\ndischimney\ns-ndischimney--tcp-offload-state-const.md">
       TCP_OFFLOAD_STATE_CONST</a> structure.</p>
</dd>

### -field <a id="TcpOffloadCachedState"></a><a id="tcpoffloadcachedstate"></a><a id="TCPOFFLOADCACHEDSTATE"></a><b>TcpOffloadCachedState</b>

<dd>
<p>Specifies the cached TCP state. This state is formatted as a 
       <a href="..\ndischimney\ns-ndischimney--tcp-offload-state-cached.md">
       TCP_OFFLOAD_STATE_CACHED</a> structure.</p>
</dd>

### -field <a id="TcpOffloadDelegatedState"></a><a id="tcpoffloaddelegatedstate"></a><a id="TCPOFFLOADDELEGATEDSTATE"></a><b>TcpOffloadDelegatedState</b>

<dd>
<p>Specifies the delegated TCP state. This state is formatted as a 
       <a href="..\ndischimney\ns-ndischimney--tcp-offload-state-delegated.md">
       TCP_OFFLOAD_STATE_DELEGATED</a> structure.</p>
</dd>

### -field <a id="TcpOffloadResourceState"></a><a id="tcpoffloadresourcestate"></a><a id="TCPOFFLOADRESOURCESTATE"></a><b>TcpOffloadResourceState</b>

<dd>
<p>Reserved. This OFFLOAD_STATE_TYPE value, as well as the TCP_OFFLOAD_RESOURCE_STATE structure,
       are currently not used.</p>
</dd>

### -field <a id="TcpOffloadState"></a><a id="tcpoffloadstate"></a><a id="TCPOFFLOADSTATE"></a><b>TcpOffloadState</b>

<dd>
<p>Specifies all of the TCP state information, including the constant, cached, and delegated TCP
       state. This state is formatted as a TCP_OFFLOAD_STATE_CONST structure, followed by a
       TCP_OFFLOAD_STATE_CACHED structure, followed by a TCP_OFFLOAD_STATE_DELEGATED structure.</p>
</dd>

### -field <a id="FilterReservedOffloadState"></a><a id="filterreservedoffloadstate"></a><a id="FILTERRESERVEDOFFLOADSTATE"></a><b>FilterReservedOffloadState</b>

<dd>
<p>Reserved for filter drivers.</p>
</dd>
</dl>
</dd>

### -field <b>NextBlock</b>

<dd>
<p>A pointer to the next NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure at the offload state layer
     (neighbor, path, or TCP) indicated by the 
     <b>Type</b> member of the 
     <b>Header</b> member. NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structures that are linked through 
     <b>NextBlock</b> pointers are always at the same layer of the offload state. A 
     <b>NextBlock</b> value of <b>NULL</b> indicates that there is no additional next
     NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure at this level.</p>
</dd>

### -field <b>DependentBlockList</b>

<dd>
<p>A pointer to an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure that is at a dependent layer of the
     offload state (a higher layer in the offload state tree). For TCP chimney offload: 
     </p>
<ul>
<li>
<p>The 
       <b>DependentBlockList</b> member of an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure at the neighbor layer
       can point only to an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure at the path layer.</p>
</li>
<li>
<p>The 
       <b>DependentBlockList</b> member of an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure at the path layer can
       point only to an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure at the TCP layer.</p>
</li>
<li>
<p>The 
       <b>DependentBlockList</b> member of an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure at the TCP layer is
       always <b>NULL</b>.</p>
</li>
</ul>
<p>A 
     <b>DependentBlockList</b> value of <b>NULL</b> indicates that there is no dependent
     NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure.</p>
</dd>

### -field <b>Status</b>

<dd>
<p>The completion status of an initiate offload, query offload, update offload, invalidate offload,
     or terminate offload operation that the offload target performed on the state associated with, or
     referenced by, the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure. Depending on the operation, the offload
     target writes one of the following NDIS_STATUS values to the 
     <b>Status</b> member:
     </p>
<p></p>
<dl>

### -field <a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS

<dd>
<p>Initiate offload: The offload target successfully offloaded the state associated with the
       NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure and the state associated with all of the immediately
       dependent NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structures.
       </p>
<p>Query, update, invalidate, or terminate offload: The offload target successfully performed the
       operation on the state associated with, or referenced by, the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
       structure.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_PARTIAL_SUCCESS"></a><a id="ndis_status_offload_partial_success"></a>NDIS_STATUS_OFFLOAD_PARTIAL_SUCCESS

<dd>
<p>Initiate offload: The offload target successfully offloaded the state associated with the
       NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure, but failed to offload the state associated with one or
       more of the immediately dependent NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structures.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_FAILURE"></a><a id="ndis_status_failure"></a>NDIS_STATUS_FAILURE

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure. The cause of the failure cannot be categorized.
       </p>
<p>Query, update, invalidate, or terminate offload: The offload target failed to perform the operation
       on the state associated with, or referenced by, the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
       structure.</p>
</dd>

### -field <a id="NDIS_STATUS_RESOURCES"></a><a id="ndis_status_resources"></a>NDIS_STATUS_RESOURCES

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure because the offload target could not allocate sufficient
       host memory.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_TCP_ENTRIES"></a><a id="ndis_status_offload_tcp_entries"></a>NDIS_STATUS_OFFLOAD_TCP_ENTRIES

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure because the offload target could not allocate a TCP
       connection state object.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_PATH_ENTRIES"></a><a id="ndis_status_offload_path_entries"></a>NDIS_STATUS_OFFLOAD_PATH_ENTRIES

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure because the offload target could not allocate a path state
       object.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_NEIGHBOR_ENTRIES"></a><a id="ndis_status_offload_neighbor_entries"></a>NDIS_STATUS_OFFLOAD_NEIGHBOR_ENTRIES

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure because the offload target could not allocate a neighbor
       state object.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_HW_ADDRESS_ENTRIES"></a><a id="ndis_status_offload_hw_address_entries"></a>NDIS_STATUS_OFFLOAD_HW_ADDRESS_ENTRIES

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure because the host stack specified a non-<b>NULL</b><b>DlSourceAddress</b> member in the 
       <a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-const.md">
       NEIGHBOR_OFFLOAD_STATE_CONST</a> structure, and the offload target either does not support
       configurable source MAC addresses or cannot accept additional source MAC addresses.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_IP_ADDRESS_ENTRIES"></a><a id="ndis_status_offload_ip_address_entries"></a>NDIS_STATUS_OFFLOAD_IP_ADDRESS_ENTRIES

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure because the offload target could not allocate a data
       structure for the source IP address that is referenced by the 
       <b>SourceAddress</b> pointer in the 
       <a href="..\ndischimney\ns-ndischimney--path-offload-state-const.md">
       PATH_OFFLOAD_STATE_CONST</a> structure.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_TCP_XMIT_BUFFER"></a><a id="ndis_status_offload_tcp_xmit_buffer"></a>NDIS_STATUS_OFFLOAD_TCP_XMIT_BUFFER

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure because the offload target could not allocate enough TCP
       transmit buffers.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_TCP_RCV_BUFFER"></a><a id="ndis_status_offload_tcp_rcv_buffer"></a>NDIS_STATUS_OFFLOAD_TCP_RCV_BUFFER

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure because the offload target could not allocate enough TCP
       receive buffers.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_TCP_RCV_WINDOW"></a><a id="ndis_status_offload_tcp_rcv_window"></a>NDIS_STATUS_OFFLOAD_TCP_RCV_WINDOW

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure because the 
       <b>InitialRcvWnd</b> member specified in the 
       <a href="..\ndischimney\ns-ndischimney--tcp-offload-state-cached.md">
       TCP_OFFLOAD_STATE_CACHED</a> structure is larger than the offload target can support.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_VLAN_ENTRIES"></a><a id="ndis_status_offload_vlan_entries"></a>NDIS_STATUS_OFFLOAD_VLAN_ENTRIES

<dd>
<p>Initiate offload: The offload target has run out of resources for tracking additional VLAN IDs. 
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_VLAN_MISMATCH"></a><a id="ndis_status_offload_vlan_mismatch"></a>NDIS_STATUS_OFFLOAD_VLAN_MISMATCH

<dd>
<p>Initiate offload: The neighbor 
       <b>VlanId</b> is non-zero and does not match one of the interface VLAN IDs.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_PATH_MTU"></a><a id="ndis_status_offload_path_mtu"></a>NDIS_STATUS_OFFLOAD_PATH_MTU

<dd>
<p>The path MTU for the TCP connection is larger than the offload target supports.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>
</dl>
</dd>

### -field <b>NdisReserved</b>

<dd>
<p>Reserved for use by NDIS.</p>
</dd>

### -field <b>MiniportOffloadContext</b>

<dd>
<p>A pointer to a memory location into which the offload target writes a PVOID value. The PVOID value
     references the offload context area in which the offload target stores the state associated with the
     NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure. If the state is a new state to be offloaded by the offload
     target, the memory location pointed to by 
     <b>MiniportOffloadContext</b> contains a <b>NULL</b> value. After offloading the state, the offload target
     writes a PVOID value to this memory location. The PVOID value supplied by the offload target references
     the offload context area into which the state was offloaded. If the 
     <b>MiniportOffloadContext</b> member itself is <b>NULL</b>, the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure is a
     placeholder in the offload state tree.</p>
</dd>

### -field <b>NdisOffloadHandle</b>

<dd>
<p>The handle that the offload target supplies in subsequent calls to the 
     <a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-event-indicate.md">
     NdisTcpOffloadEventHandler</a> function or the 
     <a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-receive-indicate.md">
     NdisTcpOffloadReceiveHandler</a> function when making an indication on the offload state associated
     with this NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure.</p>
</dd>

### -field <b>ProtocolReserved</b>

<dd>
<p>Reserved for use by protocol drivers, which can use this area for their own purposes. Offload
     targets must not modify this value.</p>
</dd>

### -field <b>MiniportReserved</b>

<dd>
<p>Reserved for use by offload targets, which can use this area for their own purposes, such as
     queuing up the offload state associated with the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure.</p>
</dd>

### -field <b>ImReserved</b>

<dd>
<p>Reserved for use by intermediate drivers, which can use this area for their own purposes. Offload
     targets must not modify this value.</p>
</dd>

### -field <b>Scratch</b>

<dd>
<p>The offload target can use this area for internal tracking. The information in this area is valid
     only while the offload target has ownership of the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST.</p>
</dd>

### -field <b>SourceHandle</b>

<dd>
<p>This member is not significant for an offload target. An offload target must not modify this
     member.</p>
</dd>

### -field <b>PortNumber</b>

<dd>
<p>A port number that identifies a miniport adapter port. To assign a miniport adapter port number,
     call the 
     <a href="..\ndis\nf-ndis-ndismallocateport.md">NdisMAllocatePort</a> function. A zero
     value identifies the default port of a miniport adapter. Use the default port if the miniport driver has
     not allocated ports for the specified adapter.</p>
</dd>

### -field <b>NetBufferListChain</b>

<dd>
<p>When the host stack specifies a <b>NULL</b> value, 
     <b>NetBufferListChain</b> is not significant and can be ignored by the offload target. 
     </p>
<p>When the host stack specifies a non-<b>NULL</b> value, 
     <b>NetBufferListChain</b> points to a 
     <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure that can be a
     stand-alone structure or the first structure in a linked list of such structures. Each NET_BUFFER_LIST
     structure in the linked list describes one 
     <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structure. The NET_BUFFER structure
     maps to a chain of memory descriptor lists (MDLs). The NET_BUFFER_LIST and associated structures are
     locked so that they remain resident in physical memory. However, they are not mapped into system
     memory.</p>
<p>The MDLs associated with the NET_BUFFER structures contain data that the host stack is passing to the
     offload target as part of the offload operation. The offload target completes such data asynchronously
     back to the host stack by calling the appropriate 
     <b>NdisTcpOffload<i>Xxx</i>Complete</b> function. At present, the linked list can contain just one type of data:
     outstanding send data. For more information, see 
     <a href="NULL">Handling Outstanding Send Data During and After an Offload Operation</a>.</p>
<p>An offload target can pass outstanding send data to the host stack when terminating the offload of a
     TCP connection. In this case, the offload target specifies a non-<b>NULL</b> value for the 
     <b>NetBufferListChain</b> member when calling the 
     <a href="..\ndischimney\nf-ndischimney-ndismterminateoffloadcomplete.md">
     NdisMTerminateOffloadComplete</a> function. If the offload target is not passing send data for a TCP
     connection that is being terminated, it must specify a <b>NULL</b> value for the 
     <b>NetBufferListChain</b> member.</p>
</dd>
</dl>

## -remarks
<p>NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structures can be linked together to build the framework of a TCP
    chimney 
    <a href="NULL">offload state tree</a>.</p>

<p>Through NDIS, the host stack passes an 
    <i>OffloadBlockList</i> pointer, which references an offload state tree to one of the following functions
    of an offload target:</p>

<p>
<a href="..\ndischimney\nc-ndischimney-w-initiate-offload-handler.md">MiniportInitiateOffload</a>
</p>

<p>
<a href="..\ndischimney\nc-ndischimney-w-query-offload-handler.md">MiniportQueryOffload</a>
</p>

<p>
<a href="..\ndischimney\nc-ndischimney-w-update-offload-handler.md">MiniportUpdateOffload</a>
</p>

<p>
<a href="..\ndischimney\nc-ndischimney-w-invalidate-offload-handler.md">MiniportInvalidateOffload</a>
</p>

<p>
<a href="..\ndischimney\nc-ndischimney-w-terminate-offload-handler.md">MiniportTerminateOffload</a>
</p>

<p>The offload target returns the tree to the host stack by passing the same pointer to the corresponding
    completion function:</p>

<p>
<a href="..\ndischimney\nf-ndischimney-ndisminitiateoffloadcomplete.md">
       NdisMInitiateOffloadComplete</a>
</p>

<p>
<a href="..\ndischimney\nf-ndischimney-ndismqueryoffloadstatecomplete.md">
       NdisMQueryOffloadStateComplete</a>
</p>

<p>
<a href="..\ndischimney\nf-ndischimney-ndismupdateoffloadcomplete.md">NdisMUpdateOffloadComplete</a>
</p>

<p>
<a href="..\ndischimney\nf-ndischimney-ndisminvalidateoffloadcomplete.md">
       NdisMInvalidateOffloadComplete</a>
</p>

<p>
<a href="..\ndischimney\nf-ndischimney-ndismterminateoffloadcomplete.md">
       NdisMTerminateOffloadComplete</a>
</p>

<p>An NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure can be immediately followed in memory by an 
    <a href="netvista.offload_state_structures">offload state structure</a> that contains
    state to be offloaded, queried, updated, invalidated, or terminated. The 
    <b>Type</b> member of the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure's 
    <b>Header</b> specifies the type of offload state, and by implication, the specific offload state
    structure (or structures) that follow the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure in memory.</p>

<p>The host stack and offload target use the 
    <b>*MiniportOffloadContext</b> and 
    <b>NdisOffloadHandle</b> members of an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure to reference offloaded
    state. For more information, see 
    <a href="netvista.storing_and_referencing_offloaded_state">Storing and Referencing
    Offloaded State</a>.</p>

<p>An NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure can perform one of several functions in an offload state
    tree. It can function as a placeholder, a linker, or it can convey new state to be offloaded by the
    offload target. For more information, see 
    <a href="netvista.placeholders__linkers__and_new_offloads">Placeholders, Linkers, and
    New Offloads</a>.</p>

<p>Before completing an initiate offload, query offload, update offload, invalidate offload, or terminate
    offload operation, an offload target must write the completion status to the 
    <b>Status</b> member of each NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure in the state tree.</p>

## -requirements
<table>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndischimney.h (include Ndischimney.h)</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndischimney\nc-ndischimney-w-initiate-offload-handler.md">MiniportInitiateOffload</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-w-invalidate-offload-handler.md">MiniportInvalidateOffload</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-w-query-offload-handler.md">MiniportQueryOffload</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-w-terminate-offload-handler.md">MiniportTerminateOffload</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-w-update-offload-handler.md">MiniportUpdateOffload</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-cached.md">NEIGHBOR_OFFLOAD_STATE_CACHED</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-delegated.md">
   NEIGHBOR_OFFLOAD_STATE_DELEGATED</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismallocateport.md">NdisMAllocatePort</a>
</dt>
<dt>
<a href="..\ndischimney\nf-ndischimney-ndisminitiateoffloadcomplete.md">NdisMInitiateOffloadComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nf-ndischimney-ndisminvalidateoffloadcomplete.md">
   NdisMInvalidateOffloadComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nf-ndischimney-ndismqueryoffloadstatecomplete.md">
   NdisMQueryOffloadStateComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nf-ndischimney-ndismterminateoffloadcomplete.md">
   NdisMTerminateOffloadComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nf-ndischimney-ndismupdateoffloadcomplete.md">NdisMUpdateOffloadComplete</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-event-indicate.md">NdisTcpOffloadEventHandler</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-receive-indicate.md">NdisTcpOffloadReceiveHandler</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--path-offload-state-cached.md">PATH_OFFLOAD_STATE_CACHED</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--path-offload-state-const.md">PATH_OFFLOAD_STATE_CONST</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--path-offload-state-delegated.md">PATH_OFFLOAD_STATE_DELEGATED</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--tcp-offload-state-cached.md">TCP_OFFLOAD_STATE_CACHED</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--tcp-offload-state-const.md">TCP_OFFLOAD_STATE_CONST</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--tcp-offload-state-delegated.md">TCP_OFFLOAD_STATE_DELEGATED</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
