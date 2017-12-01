---
UID: NS.ndischimney._NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST
title: NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST
author: windows-driver-content
description: The NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure.
old-location: netvista\ndis_protocol_offload_block_list.htm
old-project: netvista
ms.assetid: 64febd55-1ab8-4e2e-b738-340167866333
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST, NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST, *PNDIS_PROTOCOL_OFFLOAD_BLOCK_LIST
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
req.alt-api: NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST
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

# NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>The NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure.</p>


## -syntax

````
typedef struct _NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST {
  NDIS_OBJECT_HEADER                       Header;
  struct _NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST  *NextBlock;
  struct _NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST  *DependentBlockList;
  NDIS_STATUS                              Status;
  PVOID                                    NdisReserved[3];
  PNDIS_OFFLOAD_HANDLE                     OffloadHandle;
  PVOID                                    ProtocolReserved[2];
  PVOID                                    MiniportReserved[2];
  PVOID                                    ImReserved[2];
  PVOID                                    Scratch[2];
  PVOID                                    SourceHandle;
  NDIS_PORT_NUMBER                         PortNumber;
  PNET_BUFFER_LIST                         NetBufferListChain;
} NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST, *PNDIS_PROTOCOL_OFFLOAD_BLOCK_LIST;
````


## -struct-fields
<dl>

### -field <b>Header</b>

<dd>
<p>The header of the NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure. The header is formatted as an 
     <a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a> structure. The
     NDIS_OBJECT_HEADER structure contains the revision number of the NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST
     structure, the type of offload state that immediately follows the NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST
     structure in memory, and the size of the NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure, including the
     header, in bytes. 
     </p>
<p>The 
     <b>Type</b> member of the NDIS_OBJECT_HEADER structure indicates the type of offload state, and by
     implication, the specific offload state structure (or structures) that immediately follow the
     NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure in memory.</p>
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
<p>Specifies all of the neighbor state, including the constant, cached, and delegated neighbor
       state. This state is formatted as a NEIGHBOR_OFFLOAD_STATE_CONST structure, followed by a
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
<p>Specifies all of the path state (IPv6), including the constant, cached, and delegated path
       state. This state is formatted as a PATH_OFFLOAD_STATE_CONST structure, followed by a
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
<p>Specifies all of the TCP state, including the constant, cached, and delegated TCP state. This
       state is formatted as a TCP_OFFLOAD_STATE_CONST structure, followed by a TCP_OFFLOAD_STATE_CACHED
       structure, followed by a TCP_OFFLOAD_STATE_DELEGATED structure.</p>
</dd>

### -field <a id="FilterReservedOffloadState"></a><a id="filterreservedoffloadstate"></a><a id="FILTERRESERVEDOFFLOADSTATE"></a><b>FilterReservedOffloadState</b>

<dd>
<p>Reserved for filter drivers.</p>
</dd>
</dl>
</dd>

### -field <b>NextBlock</b>

<dd>
<p>A pointer to the next NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure at the offload state layer
     (neighbor, path, or TCP) indicated by the 
     <b>Type</b> member of the 
     <b>Header</b> member. NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structures that are linked through 
     <b>NextBlock</b> pointers are always at the same layer of the offload state. A 
     <b>NextBlock</b> value of <b>NULL</b> indicates that there is no additional next
     NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure at this level.</p>
</dd>

### -field <b>DependentBlockList</b>

<dd>
<p>A pointer to an NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure that is at a dependent layer of the
     offload state (a higher layer in the offload state tree). 
     </p>
<p></p>
<dl>

### -field <a id="For_TCP_chimney_offload_"></a><a id="for_tcp_chimney_offload_"></a><a id="FOR_TCP_CHIMNEY_OFFLOAD_"></a>For TCP chimney offload:

<dd>
<p>The 
       <b>DependentBlockList</b> member of an NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure at the neighbor layer
       can point only to an NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure at the path layer. The 
       <b>DependentBlockList</b> member of an NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure at the path layer can
       point only to an NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure at the TCP layer. The 
       <b>DependentBlockList</b> member of an NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure at the TCP layer is
       always <b>NULL</b>.</p>
</dd>
</dl>
<p>A 
     <b>DependentBlockList</b> value of <b>NULL</b> indicates that there is no dependent
     NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure.</p>
</dd>

### -field <b>Status</b>

<dd>
<p>The completion status of an initiate offload, query offload, update offload, invalidate offload,
     or terminate offload operation that the offload target performed on the state associated with, or
     referenced by, the NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure. Depending on the operation, NDIS writes
     one of the following NDIS_STATUS values to the 
     <b>Status</b> member:
     </p>
<p></p>
<dl>

### -field <a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS

<dd>
<p>Initiate offload: The underlying offload target successfully offloaded the state associated with
       the NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure and the state associated with all of the immediately
       dependent PROTOCOL_MINIPORT_OFFLOAD_BLOCK_LIST structures.
       </p>
<p>Query, update, invalidate, or terminate offload: The offload target successfully performed the
       operation on the state associated with, or referenced by, the NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST
       structure.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_PARTIAL_SUCCESS"></a><a id="ndis_status_offload_partial_success"></a>NDIS_STATUS_OFFLOAD_PARTIAL_SUCCESS

<dd>
<p>Initiate offload: The underlying offload target successfully offloaded the state associated with
       the NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure, but failed to offload the state associated with one or
       more of the immediately dependent NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structures.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_FAILURE"></a><a id="ndis_status_failure"></a>NDIS_STATUS_FAILURE

<dd>
<p>Initiate offload: The underlying offload target failed to offload the state associated with the
       NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure. The cause of the failure cannot be categorized.
       </p>
<p>Query, update, invalidate, or terminate offload: The offload target failed to perform the operation
       on the state associated with, or referenced by, the NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST
       structure.</p>
</dd>

### -field <a id="NDIS_STATUS_RESOURCES"></a><a id="ndis_status_resources"></a>NDIS_STATUS_RESOURCES

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure because the offload target could not allocate sufficient
       host memory.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_TCP_ENTRIES"></a><a id="ndis_status_offload_tcp_entries"></a>NDIS_STATUS_OFFLOAD_TCP_ENTRIES

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure because the offload target could not allocate a TCP
       connection state object.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_PATH_ENTRIES"></a><a id="ndis_status_offload_path_entries"></a>NDIS_STATUS_OFFLOAD_PATH_ENTRIES

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure because the offload target could not allocate a path state
       object.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_NEIGHBOR_ENTRIES"></a><a id="ndis_status_offload_neighbor_entries"></a>NDIS_STATUS_OFFLOAD_NEIGHBOR_ENTRIES

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure because the offload target could not allocate a neighbor
       state object.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_HW_ADDRESS_ENTRIES"></a><a id="ndis_status_offload_hw_address_entries"></a>NDIS_STATUS_OFFLOAD_HW_ADDRESS_ENTRIES

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure because the host stack specified a non-<b>NULL</b><b>DlSourceAddress</b> member in the 
       <a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-const.md">
       NEIGHBOR_OFFLOAD_STATE_CONST</a> structure, and the offload target either does not support
       configurable source MAC addresses or cannot accept additional source MAC addresses.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_IP_ADDRESS_ENTRIES"></a><a id="ndis_status_offload_ip_address_entries"></a>NDIS_STATUS_OFFLOAD_IP_ADDRESS_ENTRIES

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure because the offload target could not allocate a data
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
       NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure because the offload target could not allocate enough TCP
       transmit buffers.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_TCP_RCV_BUFFER"></a><a id="ndis_status_offload_tcp_rcv_buffer"></a>NDIS_STATUS_OFFLOAD_TCP_RCV_BUFFER

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure because the offload target could not allocate enough TCP
       receive buffers.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_TCP_RCV_WINDOW"></a><a id="ndis_status_offload_tcp_rcv_window"></a>NDIS_STATUS_OFFLOAD_TCP_RCV_WINDOW

<dd>
<p>Initiate offload: The offload target failed to offload the state associated with the
       NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure because the 
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
       <b>VlanId</b> is nonzero and does not match one of the interface VLAN IDs.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>

### -field <a id="NDIS_STATUS_OFFLOAD_PATH_MTU"></a><a id="ndis_status_offload_path_mtu"></a>NDIS_STATUS_OFFLOAD_PATH_MTU

<dd>
<p>Initiate offload: The path MTU for the TCP connection is larger than the offload target
       supports.
       </p>
<p>Query, update, invalidate, or terminate offload: Not an allowed status value.</p>
</dd>
</dl>
</dd>

### -field <b>NdisReserved</b>

<dd>
<p>Reserved for use by NDIS.</p>
</dd>

### -field <b>OffloadHandle</b>

<dd>
<p>A pointer to an 
     <a href="..\ndischimney\ns-ndischimney--ndis-offload-handle.md">NDIS_OFFLOAD_HANDLE</a> structure. The
     NDIS_OFFLOAD_HANDLE structure represents a protocol or intermediate driver's context for an offloaded
     state object.</p>
</dd>

### -field <b>ProtocolReserved</b>

<dd>
<p>Reserved for use by protocol drivers, which can use this area for their own purposes.</p>
</dd>

### -field <b>MiniportReserved</b>

<dd>
<p>Reserved for use by offload targets or the miniport portion of an intermediate driver.</p>
</dd>

### -field <b>ImReserved</b>

<dd>
<p>Reserved for use by intermediate drivers, which can use this area for their own purposes.</p>
</dd>

### -field <b>Scratch</b>

<dd>
<p>The protocol driver or intermediate driver can use this area for internal tracking. The
     information in this area is valid only while the driver has ownership of the 
     <b>
     NDIS_PROTOCOL_OFFLOAD_BLOCK_LIS</b> T.</p>
</dd>

### -field <b>SourceHandle</b>

<dd>
<p>This member is not significant for a protocol or intermediate driver. A protocol or intermediate
      driver must not modify this member.</p>
<p>When propagating the completion of a state-manipulation operation, an intermediate driver copies the
      
      <b>SourceHandle</b> that it stored in its IM call entry to the 
      <b>SourceHandle</b> member of the 
      <a href="..\ndischimney\ns-ndischimney--ndis-miniport-offload-block-list.md">
      NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a> structure that it passes to the NdisMXxxComplete function.</p>
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
<p>When the protocol or intermediate driver specifies a <b>NULL</b> value, 
      <b>NetBufferListChain</b> is not significant and can be ignored by the underlying driver or offload
      target.</p>
<p>When a protocol or intermediate driver specifies a non-<b>NULL</b> value, 
      <b>NetBufferListChain</b> points to a 
      <a href="..\ndis\ns-ndis--net-buffer-list.md">NET_BUFFER_LIST</a> structure that can be a
      stand-alone structure or the first structure in a linked list of such structures. Each NET_BUFFER_LIST
      structure in the linked list describes one 
      <a href="..\ndis\ns-ndis--net-buffer.md">NET_BUFFER</a> structure. The NET_BUFFER structure
      maps to a chain of memory descriptor lists (MDLs). The NET_BUFFER_LIST and associated structures are
      locked so that they remain resident in physical memory. However, they are not mapped into system
      memory.</p>
<p>The MDLs associated with the NET_BUFFER structures contain data that is being conveyed as part of a
      state-manipulation operation or the completion of such an operation. At present, the linked list can
      contain just one type of data: outstanding send data. For more information about send data, see 
      <a href="netvista.handling_outstanding_send_data_during_and_after_an_offload_operation">Handling
      Outstanding Send Data During and After an Offload Operation</a>.</p>
<p>An offload target or intermediate driver can pass outstanding send data to the overlying driver or
      host stack when terminating the offload of a TCP connection. In this case, the offload target specifies
      a non-<b>NULL</b> value for the 
      <b>NetBufferListChain</b> member when calling the 
      <a href="..\ndischimney\nf-ndischimney-ndismterminateoffloadcomplete.md">
      NdisMTerminateOffloadComplete</a> function. If the offload target is not passing send data for a TCP
      connection that is being terminated, it specifies a <b>NULL</b> value for the 
      <b>NetBufferListChain</b> member.</p>
</dd>
</dl>

## -remarks
<p>An intermediate driver creates an NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure from an 
    <a href="..\ndischimney\ns-ndischimney--ndis-miniport-offload-block-list.md">
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a> structure when 
    <a href="netvista.propagating_state_manipulation_operations">propagating a
    state-manipulation operation</a>. When 
    <a href="netvista.propagating_the_completion_of_a_state_manipulation_operation">
    propagating the completion of such an operation</a>, an intermediate driver uses an
    NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure to construct an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
    structure.</p>

<p>An NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure can be immediately followed in memory by an 
    <a href="netvista.offload_state_structures">offload state structure</a> that contains
    the state to be (or that has been) offloaded, queried, updated, invalidated, or terminated. The 
    <b>Type</b> member of the NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure's 
    <b>Header</b> specifies the type of offload state, and by implication, the specific offload state
    structure (or structures) that follow the NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure in memory.</p>

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
<a href="..\ndischimney\nf-ndischimney-ndisinitiateoffload.md">NdisInitiateOffload</a>
</dt>
<dt>
<a href="..\ndischimney\nf-ndischimney-ndisinvalidateoffload.md">NdisInvalidateOffload</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismallocateport.md">NdisMAllocatePort</a>
</dt>
<dt>
<a href="..\ntddndis\ns-ntddndis--ndis-object-header.md">NDIS_OBJECT_HEADER</a>
</dt>
<dt>
<a href="netvista.ndisqueryoffload">NdisQueryOffload</a>
</dt>
<dt>
<a href="..\ndischimney\nf-ndischimney-ndisterminateoffload.md">NdisTerminateOffload</a>
</dt>
<dt>
<a href="..\ndischimney\nf-ndischimney-ndisupdateoffload.md">NdisUpdateOffload</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-cached.md">NEIGHBOR_OFFLOAD_STATE_CACHED</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-const.md">NEIGHBOR_OFFLOAD_STATE_CONST</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-delegated.md">
   NEIGHBOR_OFFLOAD_STATE_DELEGATED</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-initiate-offload-complete-handler.md">
   ProtocolInitiateOffloadComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-invalidate-offload-complete-handler.md">
   ProtocolInvalidateOffloadComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-query-offload-complete-handler.md">
   ProtocolQueryOffloadComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-terminate-offload-complete-handler.md">
   ProtocolTerminateOffloadComplete</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-update-offload-complete-handler.md">
   ProtocolUpdateOffloadComplete</a>
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
