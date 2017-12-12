---
UID: NF.ndis.NdisMIndicateReceiveNetBufferLists
title: NdisMIndicateReceiveNetBufferLists function
author: windows-driver-content
description: Miniport drivers call the NdisMIndicateReceiveNetBufferLists function to indicate the receipt of data from the network.
old-location: netvista\ndismindicatereceivenetbufferlists.htm
old-project: netvista
ms.assetid: b87dba3e-c18f-4ea2-8bd5-ec3cdafc534b
ms.author: windowsdriverdev
ms.date: 12/8/2017
ms.keywords: NdisMIndicateReceiveNetBufferLists
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
req.alt-api: NdisMIndicateReceiveNetBufferLists
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_SendRcv_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: <= DISPATCH_LEVEL
---

# NdisMIndicateReceiveNetBufferLists function



## -description
Miniport drivers call the 
  <b>NdisMIndicateReceiveNetBufferLists</b> function to indicate the receipt of data from the network.



## -syntax

````
VOID NdisMIndicateReceiveNetBufferLists(
  _In_ NDIS_HANDLE      MiniportAdapterHandle,
  _In_ PNET_BUFFER_LIST NetBufferLists,
  _In_ NDIS_PORT_NUMBER PortNumber,
  _In_ ULONG            NumberOfNetBufferLists,
  _In_ ULONG            ReceiveFlags
);
````


## -parameters

### -param MiniportAdapterHandle [in]

The miniport handle that NDIS passed to the 
     <a href="..\ndis\nc-ndis-miniport_initialize.md">
     MiniportInitializeEx</a> function.


### -param NetBufferLists [in]

A linked list of 
     <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures that the
     miniport driver allocated.


### -param PortNumber [in]

A port number that identifies a miniport adapter port. To assign a miniport adapter port number,
     call the 
     <a href="netvista.ndismallocateport">NdisMAllocatePort</a> function. A zero
     value identifies the default port of a miniport adapter. Use the default port if the miniport driver has
     not allocated ports for the specified adapter.


### -param NumberOfNetBufferLists [in]

The number of <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures that are in the linked list of structures at 
     <i>NetBufferLists</i> .


### -param ReceiveFlags [in]

Flags that define attributes for the send operation. The flags can be combined with an OR
     operation. To clear all the flags, set this member to zero. This function supports the following flags:
     




### -param NDIS_RECEIVE_FLAGS_DISPATCH_LEVEL

Specifies that the current IRQL is DISPATCH_LEVEL. For more information about this flag, see 
       <a href="netvista.dispatch_irql_tracking">Dispatch IRQL Tracking</a>.


### -param NDIS_RECEIVE_FLAGS_RESOURCES

Specifies that the miniport driver reclaims ownership of the <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures and any
       attached <a href="netvista.net_buffer">NET_BUFFER</a> structures immediately after the call to 
       <b>NdisMIndicateReceiveNetBufferLists</b> returns.


### -param NDIS_RECEIVE_FLAGS_SINGLE_ETHER_TYPE

Specifies that all of the <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures in the list at 
       <i>NetBufferLists</i> have the same protocol type (EtherType).


### -param NDIS_RECEIVE_FLAGS_SINGLE_VLAN

Specifies that all of the <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures in the list at 
       <i>NetBufferLists</i> belong to the same VLAN.


### -param NDIS_RECEIVE_FLAGS_PERFECT_FILTERED

Specifies that all of the <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures in the list at 
       <i>NetBufferLists</i> include only data that matches the packet filter and multicast address list that are
       assigned to the miniport adapter.


### -param NDIS_RECEIVE_FLAGS_SINGLE_QUEUE

Specifies that all the <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures in the list at 
       <i>NetBufferLists</i> belong to the same VM queue. A miniport driver must set this flag for all receive
       indications on a queue if the <b>NDIS_RECEIVE_QUEUE_PARAMETERS_PER_QUEUE_RECEIVE_INDICATION</b> flag was set
       in the 
       <b>Flags</b> member of the 
       <a href="netvista.ndis_receive_queue_parameters">
       NDIS_RECEIVE_QUEUE_PARAMETERS</a> structure when that queue was allocated.


### -param NDIS_RECEIVE_FLAGS_SHARED_MEMORY_INFO_VALID

Specifies that all the <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures in the list at 
       <i>NetBufferLists</i> contain shared memory information that is valid. When this flag is set on a
       received <b>NET_BUFFER_LIST</b>, NDIS treats the shared memory information as valid. When this flag is not
       set, NDIS and drivers ignore the shared memory information. For example, intermediate drivers that
       modify packet data can use this flag to determine if data should be copied. Miniport drivers can use
       the flag to determine how to free the memory that is associated with a VM queue when a queue is
       deleted.


### -param NDIS_RECEIVE_FLAGS_MORE_NBLS

Reserved.

</dd>
</dl>

## -returns
None


## -remarks
A miniport driver typically calls the 
    <b>NdisMIndicateReceiveNetBufferLists</b> function from its 
    <a href="..\ndis\nc-ndis-miniport_interrupt_dpc.md">MiniportInterruptDPC</a> function.
    When a miniport driver calls 
    <b>NdisMIndicateReceiveNetBufferLists</b>, it specifies a list of 
    <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures in the 
    <i>NetBufferLists</i> parameter. NDIS passes the <b>NET_BUFFER_LIST</b> structures to the 
    <a href="..\ndis\nc-ndis-protocol_receive_net_buffer_lists.md">
    ProtocolReceiveNetBufferLists</a> function of bound protocol drivers.

Miniport drivers must set the 
    <b>SourceHandle</b> member of each <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structure to the same value as the 
    <i>MiniportAdapterHandle</i> parameter.

If a miniport driver calls 
    <b>NdisMIndicateReceiveNetBufferLists</b> and clears the <b>NDIS_RECEIVE_FLAG_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter, NDIS returns the indicated <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures to the miniport
    driver's 
    <a href="..\ndis\nc-ndis-miniport_return_net_buffer_lists.md">
    MiniportReturnNetBufferLists</a> function. In this case, the miniport driver must not reclaim the
    <b>NET_BUFFER_LIST</b> structures until NDIS returns the <b>NET_BUFFER_LIST</b> structures to the miniport driver's 
    <i>MiniportReturnNetBufferLists</i> function.

If a miniport driver calls 
    <b>NdisMIndicateReceiveNetBufferLists</b> and sets the <b>NDIS_RECEIVE_FLAG_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter, this indicates that the miniport driver must regain ownership of the
    <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures immediately. In this case, NDIS does not call the miniport driver's 
    <i>MiniportReturnNetBufferLists</i> function to return the <b>NET_BUFFER_LIST</b> structures. Instead, NDIS
    returns the <b>NET_BUFFER_LIST</b> structures to the miniport driver upon return from 
    <b>NdisMIndicateReceiveNetBufferLists</b>. The miniport driver should reclaim the <b>NET_BUFFER_LIST</b>
    structures immediately after 
    <b>NdisMIndicateReceiveNetBufferLists</b> returns. To reclaim the <b>NET_BUFFER_LIST</b> structures, a miniport
    driver can call its own 
    <a href="..\ndis\nc-ndis-miniport_return_net_buffer_lists.md">
    MiniportReturnNetBufferLists</a> function.

Setting the <b>NDIS_RECEIVE_FLAG_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter forces the protocol drivers to copy the network data and release the
    <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures to the miniport driver. Driver writers should design their miniport drivers
    with enough preallocated <b>NET_BUFFER_LIST</b> structures to avoid unnecessary copying.

The caller of 
    <b>NdisMIndicateReceiveNetBufferLists</b> must properly initialize the <a href="netvista.net_buffer_list">NET_BUFFER_LIST</a> structures,
    attached 
    <a href="netvista.net_buffer">NET_BUFFER</a> structures, and any attached MDLs.


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt><a href="http://go.microsoft.com/fwlink/p/?linkid=531356" target="_blank">Universal</a></dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Supported in NDIS 6.0 and later.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Ndis.h (include Ndis.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Library

</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
&lt;= DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.ndis_irql_sendrcv_function">Irql_SendRcv_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_interrupt_dpc.md">MiniportInterruptDPC</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport_return_net_buffer_lists.md">
   MiniportReturnNetBufferLists</a>
</dt>
<dt>
<a href="netvista.ndis_receive_queue_parameters">NDIS_RECEIVE_QUEUE_PARAMETERS</a>
</dt>
<dt>
<a href="netvista.ndismallocateport">NdisMAllocatePort</a>
</dt>
<dt>
<a href="netvista.net_buffer">NET_BUFFER</a>
</dt>
<dt>
<a href="netvista.net_buffer_list">NET_BUFFER_LIST</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-protocol_receive_net_buffer_lists.md">
   ProtocolReceiveNetBufferLists</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMIndicateReceiveNetBufferLists function%20 RELEASE:%20(12/8/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

