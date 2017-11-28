---
UID: NS.ndis._NET_BUFFER_LIST~r1
title: NET_BUFFER_LIST
author: windows-driver-content
description: The NET_BUFFER_LIST structure specifies a linked list of NET_BUFFER structures.
old-location: netvista\net_buffer_list.htm
old-project: netvista
ms.assetid: 3b61a424-33f8-4b33-aaef-f68f0026ce27
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NET_BUFFER_LIST, NET_BUFFER_LIST, *PNET_BUFFER_LIST
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
req.alt-api: NET_BUFFER_LIST
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

# NET_BUFFER_LIST structure



## -description
<p>The NET_BUFFER_LIST structure specifies a linked list of 
  <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures.</p>


## -syntax

````
typedef struct _NET_BUFFER_LIST {
  NET_BUFFER_LIST_HEADER   NetBufferListHeader;
  PNET_BUFFER_LIST_CONTEXT Context;
  PNET_BUFFER_LIST         ParentNetBufferList;
  NDIS_HANDLE              NdisPoolHandle;
  PVOID                    NdisReserved[2];
  PVOID                    ProtocolReserved[4];
  PVOID                    MiniportReserved[2];
  PVOID                    Scratch;
  NDIS_HANDLE              SourceHandle;
  ULONG                    NblFlags;
  LONG                     ChildRefCount;
  ULONG                    Flags;
  NDIS_STATUS              Status;
  PVOID                    NetBufferListInfo[MaxNetBufferListInfo];
} NET_BUFFER_LIST, *PNET_BUFFER_LIST;
````


## -struct-fields
<dl>

### -field <b>NetBufferListHeader</b>

<dd>
<p>A 
     <a href="..\ndis\ns-ndis--net-buffer-list-header.md">
     NET_BUFFER_LIST_HEADER</a> structure.</p>
</dd>

### -field <b>Context</b>

<dd>
<p>A pointer to a 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff568389">NET_BUFFER_LIST_CONTEXT</a> structure.
      Protocol and miniport drivers use this structure to store information about the NET_BUFFER_LIST
      structure. Information stored in the NET_BUFFER_LIST_CONTEXT structure is opaque to NDIS and other
      drivers in the stack.</p>
<p>Use the following functions and macros to access data in the NET_BUFFER_LIST_CONTEXT structure:</p>
<dl>
<dd>
<p>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferlistcontext.md">
         NdisAllocateNetBufferListContext</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\nf-ndis-ndisfreenetbufferlistcontext.md">
         NdisFreeNetBufferListContext</a>
</p>
</dd>
<dd>
<p>
<a href="netvista.net_buffer_list_context_data_start">
         NET_BUFFER_LIST_CONTEXT_DATA_START</a>
</p>
</dd>
<dd>
<p>
<a href="netvista.net_buffer_list_context_data_size">
         NET_BUFFER_LIST_CONTEXT_DATA_SIZE</a>
</p>
</dd>
</dl>
</dd>

### -field <b>ParentNetBufferList</b>

<dd>
<p>If this NET_BUFFER_LIST structure is a clone of another NET_BUFFER_LIST structure, this member
     specifies a pointer to the parent NET_BUFFER_LIST structure. Otherwise, this parameter is <b>NULL</b>. A driver
     uses the 
     <a href="..\ndis\nf-ndis-ndisallocateclonenetbufferlist.md">
     NdisAllocateCloneNetBufferList</a> function to create a clone.</p>
</dd>

### -field <b>NdisPoolHandle</b>

<dd>
<p>A pool handle that identifies the NET_BUFFER_LIST pool from which the NET_BUFFER_LIST structure
     was allocated.</p>
</dd>

### -field <b>NdisReserved</b>

<dd>
<p>Reserved for use by NDIS.</p>
</dd>

### -field <b>ProtocolReserved</b>

<dd>
<p>Reserved for use by protocol drivers.</p>
</dd>

### -field <b>MiniportReserved</b>

<dd>
<p>Reserved for use by miniport drivers.</p>
</dd>

### -field <b>Scratch</b>

<dd>
<p>Data that is defined by the current owner of the NET_BUFFER_LIST structure. The current owner,
     either NDIS or an NDIS driver, can use this member for their own purposes. When the NET_BUFFER_LIST
     structure is initially allocated, this member is <b>NULL</b>. After the current owner relinquishes ownership,
     NDIS or another driver can overwrite this member.</p>
</dd>

### -field <b>SourceHandle</b>

<dd>
<p>A handle that NDIS provided to the driver in a binding or attaching operation by using one of the
     following driver-supplied routines:
     </p>
<p></p>
<dl>

### -field <a id="Miniport_Driver"></a><a id="miniport_driver"></a><a id="MINIPORT_DRIVER"></a>Miniport Driver

<dd>
<p>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</p>
</dd>

### -field <a id="Protocol_Driver"></a><a id="protocol_driver"></a><a id="PROTOCOL_DRIVER"></a>Protocol Driver

<dd>
<p>
<a href="..\ndis\nc-ndis-protocol-bind-adapter-ex.md">ProtocolBindAdapterEx</a>
</p>
</dd>

### -field <a id="Filter_Driver"></a><a id="filter_driver"></a><a id="FILTER_DRIVER"></a>Filter Driver

<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff540442">FilterAttach</a>
</p>
</dd>
</dl>
<p>NDIS uses 
     <b>SourceHandle</b> to return the NET_BUFFER_LIST structure to the driver that sent the NET_BUFFER_LIST
     structure.</p>
</dd>

### -field <b>NblFlags</b>

<dd>
<p>This member contains flags that can be combined with a bitwise OR operation.
     </p>
<p>Use the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff564620">NdisTestNblFlag</a>, 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff564626">NdisTestNblFlags</a>, 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff564542">NdisSetNblFlag</a>, and 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff561630">NdisClearNblFlag</a> macros to access the
     flags.</p>
<p>Intermediate drivers and filter drivers can set the following flags if they do not modify data that
     is associated with a NET_BUFFER_LIST. For example, if the data did not change, NDIS might reuse the
     original information from which the NET_BUFFER_LIST was created.:</p>
<p></p>
<dl>

### -field <a id="NDIS_NBL_FLAGS_SEND_READ_ONLY"></a><a id="ndis_nbl_flags_send_read_only"></a>NDIS_NBL_FLAGS_SEND_READ_ONLY

<dd>
<p>If set, the NET_BUFFER_LIST structure and its data are read-only for send operations.</p>
</dd>

### -field <a id="NDIS_NBL_FLAGS_RECV_READ_ONLY"></a><a id="ndis_nbl_flags_recv_read_only"></a>NDIS_NBL_FLAGS_RECV_READ_ONLY

<dd>
<p>If set, the NET_BUFFER_LIST structure and its data are read-only for receive operations.</p>
</dd>
</dl>
<p>A driver can set the following flags even if it does not split the associated Ethernet frame:</p>
<p></p>
<dl>

### -field <a id="NDIS_NBL_FLAGS_IS_IPV4"></a><a id="ndis_nbl_flags_is_ipv4"></a>NDIS_NBL_FLAGS_IS_IPV4

<dd>
<p>All of the Ethernet frames in this NET_BUFFER_LIST structure are IPv4 frames. If this flag is
       set, the header-data split provider must not set the NDIS_NBL_FLAGS_IS_IPV6 flag.</p>
</dd>

### -field <a id="NDIS_NBL_FLAGS_IS_IPV6"></a><a id="ndis_nbl_flags_is_ipv6"></a>NDIS_NBL_FLAGS_IS_IPV6

<dd>
<p>All of the Ethernet frames in this NET_BUFFER_LIST structure are IPv6 frames. If this flag is
       set, the header-data split provider must not set the NDIS_NBL_FLAGS_IS_IPV4 flag.</p>
</dd>

### -field <a id="NDIS_NBL_FLAGS_IS_TCP"></a><a id="ndis_nbl_flags_is_tcp"></a>NDIS_NBL_FLAGS_IS_TCP

<dd>
<p>All of the Ethernet frames in this NET_BUFFER_LIST structure are TCP frames. If this flag is
       set, the header-data split provider must not set the NDIS_NBL_FLAGS_IS_UDP flag, and the provider must
       set the NDIS_NBL_FLAGS_IS_IPV4 flag or the NDIS_NBL_FLAGS_IS_IPV6 flag.</p>
</dd>

### -field <a id="NDIS_NBL_FLAGS_IS_UDP"></a><a id="ndis_nbl_flags_is_udp"></a>NDIS_NBL_FLAGS_IS_UDP

<dd>
<p>All of the Ethernet frames in this NET_BUFFER_LIST structure are UDP frames. If this flag is
       set, the header-data split provider must not set the NDIS_NBL_FLAGS_IS_TCP flag, and the provider must
       set the NDIS_NBL_FLAGS_IS_IPV4 flag or the NDIS_NBL_FLAGS_IS_IPV6 flag.</p>
</dd>

### -field <a id="NDIS_NBL_FLAGS_IS_LOOPBACK_PACKET"></a><a id="ndis_nbl_flags_is_loopback_packet"></a>NDIS_NBL_FLAGS_IS_LOOPBACK_PACKET

<dd>
<p>All of the packets that are associated with this NET_BUFFER_LIST structure are loopback
       packets.</p>
</dd>
</dl>
<p>If the header-data split provider does not split the associated Ethernet frame, the miniport driver
     must indicate the NET_BUFFER_LIST structure with the following flags cleared:</p>
<p></p>
<dl>

### -field <a id="NDIS_NBL_FLAGS_HD_SPLIT"></a><a id="ndis_nbl_flags_hd_split"></a>NDIS_NBL_FLAGS_HD_SPLIT

<dd>
<p>The header and data are split in all of the Ethernet frames that are associated with this
       NET_BUFFER_LIST structure.</p>
</dd>

### -field <a id="NDIS_NBL_FLAGS_SPLIT_AT_UPPER_LAYER_PROTOCOL_HEADER"></a><a id="ndis_nbl_flags_split_at_upper_layer_protocol_header"></a>NDIS_NBL_FLAGS_SPLIT_AT_UPPER_LAYER_PROTOCOL_HEADER

<dd>
<p>All of the Ethernet frames in this NET_BUFFER_LIST are split at the beginning of the upper layer
       protocol header. If this flag is set, the header-data split provider must set the
       NDIS_NBL_FLAGS_IS_IPV4 flag or the NDIS_NBL_FLAGS_IS_IPV6 flag. Also, the provider can set the
       NDIS_NBL_FLAGS_IS_TCP flag or the NDIS_NBL_FLAGS_IS_UDP flag, but the provider must not set the
       NDIS_NBL_FLAGS_SPLIT_AT_UPPER_LAYER_PROTOCOL_PAYLOAD flag.</p>
</dd>

### -field <a id="NDIS_NBL_FLAGS_SPLIT_AT_UPPER_LAYER_PROTOCOL_PAYLOAD"></a><a id="ndis_nbl_flags_split_at_upper_layer_protocol_payload"></a>NDIS_NBL_FLAGS_SPLIT_AT_UPPER_LAYER_PROTOCOL_PAYLOAD

<dd>
<p>All of the Ethernet frames in this NET_BUFFER_LIST structure are split at the beginning of the
       TCP or UDP payload. If this flag is set, the header-data split provider must set the
       NDIS_NBL_FLAGS_IS_IPV4 flag or the NDIS_NBL_FLAGS_IS_IPV6 flag. Also, the provider must set the
       NDIS_NBL_FLAGS_IS_TCP flag or the NDIS_NBL_FLAGS_IS_UDP flag, but the provider must not set the
       NDIS_NBL_FLAGS_SPLIT_AT_UPPER_LAYER_PROTOCOL_HEADER flag.</p>
</dd>
</dl>
</dd>

### -field <b>ChildRefCount</b>

<dd>
<p>If this NET_BUFFER_LIST structure has clones (is a parent), this member specifies the number of
     outstanding clones. Otherwise, this member is zero.</p>
</dd>

### -field <b>Flags</b>

<dd>
<p>Attributes of the NET_BUFFER_LIST structure. The following definitions specify a bit mask for a set
      of flags:</p>
<p></p>
<dl>

### -field <a id="NBL_FLAGS_PROTOCOL_RESERVED"></a><a id="nbl_flags_protocol_reserved"></a>NBL_FLAGS_PROTOCOL_RESERVED

<dd>
<p>This set is reserved for protocol drivers.</p>
<div class="alert"><b>Note</b>  Starting with NDIS 6.30, two additional bits are available for protocol use: 0x00000003.  A NDIS 6.30 protocol may use these bits if and only if <a href="https://msdn.microsoft.com/library/windows/hardware/ff562680">NdisGetVersion</a> returns a value greater than or equal to <b>NDIS_RUNTIME_VERSION_630</b>.  Protocols must not use these bits on earlier versions of NDIS, because prior to 6.30, NDIS uses them internally.</div>
<div> </div>
</dd>

### -field <a id="NBL_FLAGS_MINIPORT_RESERVED"></a><a id="nbl_flags_miniport_reserved"></a>NBL_FLAGS_MINIPORT_RESERVED

<dd>
<p>This set is reserved for miniport drivers.</p>
</dd>

### -field <a id="NBL_FLAGS_SCRATCH"></a><a id="nbl_flags_scratch"></a>NBL_FLAGS_SCRATCH

<dd>
<p>The current owner of the NET_BUFFER_LIST structure, either NDIS or an NDIS driver, can use this
        set. When the current owner relinquishes ownership, NDIS or another driver can overwrite these
        flags.</p>
</dd>

### -field <a id="NBL_FLAGS_NDIS_RESERVED"></a><a id="nbl_flags_ndis_reserved"></a>NBL_FLAGS_NDIS_RESERVED

<dd>
<p>This set is reserved for NDIS.</p>
</dd>
</dl>
</dd>

### -field <b>Status</b>

<dd>
<p>The final completion status of a network data operation on this NET_BUFFER_LIST structure.
     Miniport drivers write this value before calling the 
     <a href="..\ndis\nf-ndis-ndismsendnetbufferlistscomplete.md">
     NdisMSendNetBufferListsComplete</a> function. Miniport drivers specify one of the following values:
     </p>
<p></p>
<dl>

### -field <a id="NDIS_STATUS_SUCCESS"></a><a id="ndis_status_success"></a>NDIS_STATUS_SUCCESS

<dd>
<p>All the network data described by NET_BUFFER structures associated with this NET_BUFFER_LIST
       structure was successfully transmitted over the network.</p>
</dd>

### -field <a id="NDIS_STATUS_INVALID_LENGTH"></a><a id="ndis_status_invalid_length"></a>NDIS_STATUS_INVALID_LENGTH

<dd>
<p>The size of the data in some NET_BUFFER structures associated with this NET_BUFFER_LIST
       structure was too large for the underlying NIC.</p>
</dd>

### -field <a id="NDIS_STATUS_RESOURCES"></a><a id="ndis_status_resources"></a>NDIS_STATUS_RESOURCES

<dd>
<p>The send request for this NET_BUFFER_LIST structure failed due to insufficient resources.</p>
</dd>

### -field <a id="NDIS_STATUS_FAILURE"></a><a id="ndis_status_failure"></a>NDIS_STATUS_FAILURE

<dd>
<p>This send request for this NET_BUFFER_LIST structure failed due to some reason other than those
       stated in the previous three values.</p>
</dd>

### -field <a id="NDIS_STATUS_SEND_ABORTED"></a><a id="ndis_status_send_aborted"></a>NDIS_STATUS_SEND_ABORTED

<dd>
<p>NDIS called the 
       <a href="..\ndis\nc-ndis-miniport-cancel-send.md">MiniportCancelSend</a> function to
       cancel the send operation for this NET_BUFFER_LIST structure.</p>
</dd>

### -field <a id="NDIS_STATUS_RESET_IN_PROGRESS"></a><a id="ndis_status_reset_in_progress"></a>NDIS_STATUS_RESET_IN_PROGRESS

<dd>
<p>The miniport driver aborted the send request due to a reset.</p>
</dd>

### -field <a id="NDIS_STATUS_PAUSED"></a><a id="ndis_status_paused"></a>NDIS_STATUS_PAUSED

<dd>
<p>If a driver must reject send requests because it is paused, it sets the complete status in each
       affected NET_BUFFER_LIST to NDIS_STATUS_PAUSED.</p>
</dd>
</dl>
</dd>

### -field <b>NetBufferListInfo</b>

<dd>
<p>An array of values containing information that is common to all NET_BUFFER structures in the list.
     This information is often referred to as "out-of-band (OOB) data."</p>
<p>Use the 
     <a href="..\ndis\ne-ndis--ndis-net-buffer-list-info.md">
     NDIS_NET_BUFFER_LIST_INFO</a> enumeration values with the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a> macro to set and
     get values in the 
     <b>NetBufferListInfo</b> array.</p>
</dd>
</dl>

## -remarks
<p>NDIS drivers can call any of the following functions to allocate and initialize a NET_BUFFER_LIST
    structure:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561609">NdisAllocateNetBufferList</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferandnetbufferlist.md">
       NdisAllocateNetBufferAndNetBufferList</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\nf-ndis-ndisallocateclonenetbufferlist.md">
       NdisAllocateCloneNetBufferList</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\nf-ndis-ndisallocatefragmentnetbufferlist.md">
       NdisAllocateFragmentNetBufferList</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\nf-ndis-ndisallocatereassemblednetbufferlist.md">
       NdisAllocateReassembledNetBufferList</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561609">NdisAllocateNetBufferList</a>
</p>

<p>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferandnetbufferlist.md">
       NdisAllocateNetBufferAndNetBufferList</a>
</p>

<p>
<a href="..\ndis\nf-ndis-ndisallocateclonenetbufferlist.md">
       NdisAllocateCloneNetBufferList</a>
</p>

<p>
<a href="..\ndis\nf-ndis-ndisallocatefragmentnetbufferlist.md">
       NdisAllocateFragmentNetBufferList</a>
</p>

<p>
<a href="..\ndis\nf-ndis-ndisallocatereassemblednetbufferlist.md">
       NdisAllocateReassembledNetBufferList</a>
</p>

<p>All NET_BUFFER structures associated with a NET_BUFFER_LIST structure have the attributes that are
    specified by the 
    <b>NetBufferListInfo</b> and 
    <b>Context</b> members.</p>

<p>When a driver calls the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff564535">NdisSendNetBufferLists</a> or 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562616">NdisFSendNetBufferLists</a> function,
    it loses ownership of:</p>

<p>The specified NET_BUFFER_LIST structure.</p>

<p>The attached 
      <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structures and MDLs.</p>

<p>Any attached NDIS_REQUEST_CONTROLs.</p>

<p>All 
      <b>NetBufferListInfo</b> data that is associated with the NET_BUFFER_LIST structure.</p>

<p>The current owner of a list of NET_BUFFER_LIST structures can move a NET_BUFFER_LIST structure to
    another list. However, all NET_BUFFER structures associated with a NET_BUFFER_LIST structure should stay
    with the same NET_BUFFER_LIST structure. Only the driver that created the NET_BUFFER structures can move
    them to a different NET_BUFFER_LIST structure. The current owner cannot modify a NET_BUFFER structure's 
    <b>Next</b> member.</p>

<p>A list of NET_BUFFER_LIST structures is a simple singly linked and NULL-terminated list. To move a
    NET_BUFFER_LIST structure to a different list, make appropriate updates to the 
    <b>Next</b> members in both the source and destination lists.</p>

<p>To access members of the NET_BUFFER_LIST structure, use the following macros and functions:</p><dl>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568404">NET_BUFFER_LIST_NEXT_NBL</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568394">NET_BUFFER_LIST_FIRST_NB</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568395">NET_BUFFER_LIST_FLAGS</a>
</p>
</dd>
<dd>
<p>
<a href="netvista.net_buffer_list_miniport_reserved">
       NET_BUFFER_LIST_MINIPORT_RESERVED</a>
</p>
</dd>
<dd>
<p>
<a href="netvista.net_buffer_list_context_data_start">
       NET_BUFFER_LIST_CONTEXT_DATA_START</a>
</p>
</dd>
<dd>
<p>
<a href="netvista.net_buffer_list_context_data_size">
       NET_BUFFER_LIST_CONTEXT_DATA_SIZE</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a>
</p>
</dd>
<dd>
<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568411">NET_BUFFER_LIST_STATUS</a>
</p>
</dd>
<dd>
<p>
<a href="netvista.net_buffer_list_protocol_reserved">
       NET_BUFFER_LIST_PROTOCOL_RESERVED</a>
</p>
</dd>
<dd>
<p>
<a href="..\ndis\nf-ndis-ndisgetpoolfromnetbufferlist.md">
       NdisGetPoolFromNetBufferList</a>
</p>
</dd>
</dl><p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568404">NET_BUFFER_LIST_NEXT_NBL</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568394">NET_BUFFER_LIST_FIRST_NB</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568395">NET_BUFFER_LIST_FLAGS</a>
</p>

<p>
<a href="netvista.net_buffer_list_miniport_reserved">
       NET_BUFFER_LIST_MINIPORT_RESERVED</a>
</p>

<p>
<a href="netvista.net_buffer_list_context_data_start">
       NET_BUFFER_LIST_CONTEXT_DATA_START</a>
</p>

<p>
<a href="netvista.net_buffer_list_context_data_size">
       NET_BUFFER_LIST_CONTEXT_DATA_SIZE</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a>
</p>

<p>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568411">NET_BUFFER_LIST_STATUS</a>
</p>

<p>
<a href="netvista.net_buffer_list_protocol_reserved">
       NET_BUFFER_LIST_PROTOCOL_RESERVED</a>
</p>

<p>
<a href="..\ndis\nf-ndis-ndisgetpoolfromnetbufferlist.md">
       NdisGetPoolFromNetBufferList</a>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff566569">NDIS_NET_BUFFER_LIST_INFO</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocateclonenetbufferlist.md">
   NdisAllocateCloneNetBufferList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatefragmentnetbufferlist.md">
   NdisAllocateFragmentNetBufferList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561609">NdisAllocateNetBufferList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferandnetbufferlist.md">
   NdisAllocateNetBufferAndNetBufferList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatereassemblednetbufferlist.md">
   NdisAllocateReassembledNetBufferList</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561623">NdisCancelSendNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff561630">NdisClearNblFlag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562587">NdisFreeNetBufferListContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562623">NdisGeneratePartialCancelId</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562659">NdisGetPoolFromNetBufferList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndisallocatenetbufferlistcontext.md">
   NdisAllocateNetBufferListContext</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564535">NdisSendNetBufferLists</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564542">NdisSetNblFlag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564620">NdisTestNblFlag</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff564626">NdisTestNblFlags</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568389">NET_BUFFER_LIST_CONTEXT</a>
</dt>
<dt>
<a href="netvista.net_buffer_list_context_data_size">
   NET_BUFFER_LIST_CONTEXT_DATA_SIZE</a>
</dt>
<dt>
<a href="netvista.net_buffer_list_context_data_start">
   NET_BUFFER_LIST_CONTEXT_DATA_START</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568394">NET_BUFFER_LIST_FIRST_NB</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568395">NET_BUFFER_LIST_FLAGS</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568400">NET_BUFFER_LIST_HEADER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568401">NET_BUFFER_LIST_INFO</a>
</dt>
<dt>
<a href="netvista.net_buffer_list_miniport_reserved">
   NET_BUFFER_LIST_MINIPORT_RESERVED</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568404">NET_BUFFER_LIST_NEXT_NBL</a>
</dt>
<dt>
<a href="netvista.net_buffer_list_protocol_reserved">
   NET_BUFFER_LIST_PROTOCOL_RESERVED</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568411">NET_BUFFER_LIST_STATUS</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NET_BUFFER_LIST structure%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
