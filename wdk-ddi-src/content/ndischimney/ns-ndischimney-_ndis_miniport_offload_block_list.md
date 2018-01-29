---
UID : NS:ndischimney._NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
title : _NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
author : windows-driver-content
description : The NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure is the basic building block of a TCP chimney offload state tree. An offload state tree can contain one or more NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structures.
old-location : netvista\ndis_miniport_offload_block_list.htm
old-project : netvista
ms.assetid : ebc98e65-5d11-4c3d-aea1-dfad1434c093
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : _NDIS_MINIPORT_OFFLOAD_BLOCK_LIST, NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure [Network Drivers Starting with Windows Vista], PNDIS_MINIPORT_OFFLOAD_BLOCK_LIST, NDIS_MINIPORT_OFFLOAD_BLOCK_LIST, PNDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure pointer [Network Drivers Starting with Windows Vista], *PNDIS_MINIPORT_OFFLOAD_BLOCK_LIST, ndischimney/PNDIS_MINIPORT_OFFLOAD_BLOCK_LIST, ndischimney/NDIS_MINIPORT_OFFLOAD_BLOCK_LIST, netvista.ndis_miniport_offload_block_list, tcp_chim_struct_34a99dea-527f-421e-a3a7-92a7c1f7d503.xml
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : struct
req.header : ndischimney.h
req.include-header : Ndischimney.h
req.target-type : Windows
req.target-min-winverclnt : 
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : 
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : 
req.dll : 
req.irql : 
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : NDIS_MINIPORT_OFFLOAD_BLOCK_LIST, *PNDIS_MINIPORT_OFFLOAD_BLOCK_LIST
---

# _NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]

The NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure is the basic building block of a TCP chimney offload
  state tree. An offload state tree can contain one or more NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
  structures.

## Syntax
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

## Members


`_NDIS_MINIPORT_OFFLOAD_BLOCK_LIST`



`DependentBlockList`

A pointer to an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure that is at a dependent layer of the
     offload state (a higher layer in the offload state tree). For TCP chimney offload: 
     
<ul>
<li>
The 
       <b>DependentBlockList</b> member of an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure at the neighbor layer
       can point only to an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure at the path layer.

</li>
<li>
The 
       <b>DependentBlockList</b> member of an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure at the path layer can
       point only to an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure at the TCP layer.

</li>
<li>
The 
       <b>DependentBlockList</b> member of an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure at the TCP layer is
       always <b>NULL</b>.

</li>
</ul>A 
     <b>DependentBlockList</b> value of <b>NULL</b> indicates that there is no dependent
     NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure.

`Header`

The header of the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure. The header is formatted as an 
     <a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a> structure. The
     NDIS_OBJECT_HEADER structure contains the revision number of the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
     structure, the type of offload state that immediately follows the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
     structure in memory, and the size of the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure, including the
     header, in bytes. 
     

The 
     <b>Type</b> member of the NDIS_OBJECT_HEADER structure indicates the type of offload state, and by
     implication, the specific offload state structure (or structures) that immediately follow the
     NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure in memory.

The following OFFLOAD_STATE_TYPE values are supported:

`ImReserved`

Reserved for use by intermediate drivers, which can use this area for their own purposes. Offload
     targets must not modify this value.

`MiniportOffloadContext`

A pointer to a memory location into which the offload target writes a PVOID value. The PVOID value
     references the offload context area in which the offload target stores the state associated with the
     NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure. If the state is a new state to be offloaded by the offload
     target, the memory location pointed to by 
     <b>MiniportOffloadContext</b> contains a <b>NULL</b> value. After offloading the state, the offload target
     writes a PVOID value to this memory location. The PVOID value supplied by the offload target references
     the offload context area into which the state was offloaded. If the 
     <b>MiniportOffloadContext</b> member itself is <b>NULL</b>, the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure is a
     placeholder in the offload state tree.

`MiniportReserved`

Reserved for use by offload targets, which can use this area for their own purposes, such as
     queuing up the offload state associated with the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure.

`NdisOffloadHandle`

The handle that the offload target supplies in subsequent calls to the 
     <mshelp:link keywords="netvista.ndistcpoffloadeventhandler" tabindex="0"><b>
     NdisTcpOffloadEventHandler</b></mshelp:link> function or the 
     <mshelp:link keywords="netvista.ndistcpoffloadreceivehandler" tabindex="0"><b>
     NdisTcpOffloadReceiveHandler</b></mshelp:link> function when making an indication on the offload state associated
     with this NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure.

`NdisReserved`

Reserved for use by NDIS.

`NetBufferListChain`

When the host stack specifies a <b>NULL</b> value, 
     <b>NetBufferListChain</b> is not significant and can be ignored by the offload target. 
     

When the host stack specifies a non-<b>NULL</b> value, 
     <b>NetBufferListChain</b> points to a 
     <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structure that can be a
     stand-alone structure or the first structure in a linked list of such structures. Each NET_BUFFER_LIST
     structure in the linked list describes one 
     <a href="..\ndis\ns-ndis-_net_buffer.md">NET_BUFFER</a> structure. The NET_BUFFER structure
     maps to a chain of memory descriptor lists (MDLs). The NET_BUFFER_LIST and associated structures are
     locked so that they remain resident in physical memory. However, they are not mapped into system
     memory.

The MDLs associated with the NET_BUFFER structures contain data that the host stack is passing to the
     offload target as part of the offload operation. The offload target completes such data asynchronously
     back to the host stack by calling the appropriate 
     <b>NdisTcpOffload<i>Xxx</i>Complete</b> function. At present, the linked list can contain just one type of data:
     outstanding send data. For more information, see 
     <a href="https://docs.microsoft.com/en-us/windows-hardware/drivers/network/handling-outstanding-send-data-during-and-after-an-offload-operation">Handling Outstanding Send Data During and After an Offload Operation</a>.

An offload target can pass outstanding send data to the host stack when terminating the offload of a
     TCP connection. In this case, the offload target specifies a non-<b>NULL</b> value for the 
     <b>NetBufferListChain</b> member when calling the 
     <mshelp:link keywords="netvista.ndismterminateoffloadcomplete" tabindex="0"><b>
     NdisMTerminateOffloadComplete</b></mshelp:link> function. If the offload target is not passing send data for a TCP
     connection that is being terminated, it must specify a <b>NULL</b> value for the 
     <b>NetBufferListChain</b> member.

`NextBlock`

A pointer to the next NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure at the offload state layer
     (neighbor, path, or TCP) indicated by the 
     <b>Type</b> member of the 
     <b>Header</b> member. NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structures that are linked through 
     <b>NextBlock</b> pointers are always at the same layer of the offload state. A 
     <b>NextBlock</b> value of <b>NULL</b> indicates that there is no additional next
     NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure at this level.

`PortNumber`

A port number that identifies a miniport adapter port. To assign a miniport adapter port number,
     call the 
     <a href="..\ndis\nf-ndis-ndismallocateport.md">NdisMAllocatePort</a> function. A zero
     value identifies the default port of a miniport adapter. Use the default port if the miniport driver has
     not allocated ports for the specified adapter.

`ProtocolReserved`

Reserved for use by protocol drivers, which can use this area for their own purposes. Offload
     targets must not modify this value.

`Scratch`

The offload target can use this area for internal tracking. The information in this area is valid
     only while the offload target has ownership of the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST.

`SourceHandle`

This member is not significant for an offload target. An offload target must not modify this
     member.

`Status`

The completion status of an initiate offload, query offload, update offload, invalidate offload,
     or terminate offload operation that the offload target performed on the state associated with, or
     referenced by, the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure. Depending on the operation, the offload
     target writes one of the following NDIS_STATUS values to the 
     <b>Status</b> member:

## Remarks
NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structures can be linked together to build the framework of a TCP
    chimney 
    <a href="https://msdn.microsoft.com/c96608bd-5e8f-499b-872a-b6f7f33c9e0c">offload state tree</a>.

Through NDIS, the host stack passes an 
    <i>OffloadBlockList</i> pointer, which references an offload state tree to one of the following functions
    of an offload target:
<ul>
<li>

<a href="..\ndischimney\nc-ndischimney-w_initiate_offload_handler.md">MiniportInitiateOffload</a>


</li>
<li>

<a href="..\ndischimney\nc-ndischimney-w_query_offload_handler.md">MiniportQueryOffload</a>


</li>
<li>

<a href="..\ndischimney\nc-ndischimney-w_update_offload_handler.md">MiniportUpdateOffload</a>


</li>
<li>

<a href="..\ndischimney\nc-ndischimney-w_invalidate_offload_handler.md">MiniportInvalidateOffload</a>


</li>
<li>

<a href="..\ndischimney\nc-ndischimney-w_terminate_offload_handler.md">MiniportTerminateOffload</a>


</li>
</ul>The offload target returns the tree to the host stack by passing the same pointer to the corresponding
    completion function:
<ul>
<li>

<mshelp:link keywords="netvista.ndisminitiateoffloadcomplete" tabindex="0"><b>
       NdisMInitiateOffloadComplete</b></mshelp:link>


</li>
<li>

<mshelp:link keywords="netvista.ndismqueryoffloadstatecomplete" tabindex="0"><b>
       NdisMQueryOffloadStateComplete</b></mshelp:link>


</li>
<li>

<a href="..\ndischimney\nf-ndischimney-ndismupdateoffloadcomplete.md">NdisMUpdateOffloadComplete</a>


</li>
<li>

<mshelp:link keywords="netvista.ndisminvalidateoffloadcomplete" tabindex="0"><b>
       NdisMInvalidateOffloadComplete</b></mshelp:link>


</li>
<li>

<mshelp:link keywords="netvista.ndismterminateoffloadcomplete" tabindex="0"><b>
       NdisMTerminateOffloadComplete</b></mshelp:link>


</li>
</ul>An NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure can be immediately followed in memory by an 
    <a href="https://msdn.microsoft.com/en-us/library/windows/hardware/ff570939">offload state structure</a> that contains
    state to be offloaded, queried, updated, invalidated, or terminated. The 
    <b>Type</b> member of the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure's 
    <b>Header</b> specifies the type of offload state, and by implication, the specific offload state
    structure (or structures) that follow the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure in memory.

The host stack and offload target use the 
    <b>*MiniportOffloadContext</b> and 
    <b>NdisOffloadHandle</b> members of an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure to reference offloaded
    state. For more information, see 
    <mshelp:link keywords="netvista.storing_and_referencing_offloaded_state" tabindex="0">Storing and Referencing
    Offloaded State</mshelp:link>.

An NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure can perform one of several functions in an offload state
    tree. It can function as a placeholder, a linker, or it can convey new state to be offloaded by the
    offload target. For more information, see 
    <mshelp:link keywords="netvista.placeholders__linkers__and_new_offloads" tabindex="0">Placeholders, Linkers, and
    New Offloads</mshelp:link>.

Before completing an initiate offload, query offload, update offload, invalidate offload, or terminate
    offload operation, an offload target must write the completion status to the 
    <b>Status</b> member of each NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure in the state tree.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ndischimney.h (include Ndischimney.h) |

## See Also

<a href="..\ndischimney\nc-ndischimney-ndis_tcp_offload_receive_indicate.md">NdisTcpOffloadReceiveHandler</a>

<mshelp:link keywords="netvista.ndismqueryoffloadstatecomplete" tabindex="0"><b>
   NdisMQueryOffloadStateComplete</b></mshelp:link>

<a href="..\ndischimney\nc-ndischimney-w_query_offload_handler.md">MiniportQueryOffload</a>

<a href="..\ndischimney\ns-ndischimney-_path_offload_state_const.md">PATH_OFFLOAD_STATE_CONST</a>

<mshelp:link keywords="netvista.neighbor_offload_state_delegated" tabindex="0"><b>
   NEIGHBOR_OFFLOAD_STATE_DELEGATED</b></mshelp:link>

<a href="..\ndischimney\nc-ndischimney-w_update_offload_handler.md">MiniportUpdateOffload</a>

<a href="..\ndis\nf-ndis-ndismallocateport.md">NdisMAllocatePort</a>

<a href="..\ndischimney\nf-ndischimney-ndisminitiateoffloadcomplete.md">NdisMInitiateOffloadComplete</a>

<a href="..\ndischimney\nc-ndischimney-ndis_tcp_offload_event_indicate.md">NdisTcpOffloadEventHandler</a>

<mshelp:link keywords="netvista.ndismterminateoffloadcomplete" tabindex="0"><b>
   NdisMTerminateOffloadComplete</b></mshelp:link>

<a href="..\ndischimney\ns-ndischimney-_tcp_offload_state_const.md">TCP_OFFLOAD_STATE_CONST</a>

<a href="..\ndischimney\ns-ndischimney-_path_offload_state_delegated.md">PATH_OFFLOAD_STATE_DELEGATED</a>

<a href="..\ndischimney\nc-ndischimney-w_initiate_offload_handler.md">MiniportInitiateOffload</a>

<a href="..\ndischimney\nf-ndischimney-ndismupdateoffloadcomplete.md">NdisMUpdateOffloadComplete</a>

<a href="..\ndischimney\ns-ndischimney-_tcp_offload_state_delegated.md">TCP_OFFLOAD_STATE_DELEGATED</a>

<a href="..\ndischimney\ns-ndischimney-_path_offload_state_cached.md">PATH_OFFLOAD_STATE_CACHED</a>

<a href="..\ndischimney\nc-ndischimney-w_invalidate_offload_handler.md">MiniportInvalidateOffload</a>

<a href="..\ndischimney\ns-ndischimney-_neighbor_offload_state_cached.md">NEIGHBOR_OFFLOAD_STATE_CACHED</a>

<mshelp:link keywords="netvista.ndisminvalidateoffloadcomplete" tabindex="0"><b>
   NdisMInvalidateOffloadComplete</b></mshelp:link>

<a href="..\ntddndis\ns-ntddndis-_ndis_object_header.md">NDIS_OBJECT_HEADER</a>

<a href="..\ndischimney\nc-ndischimney-w_terminate_offload_handler.md">MiniportTerminateOffload</a>

<a href="..\ndischimney\ns-ndischimney-_tcp_offload_state_cached.md">TCP_OFFLOAD_STATE_CACHED</a>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>