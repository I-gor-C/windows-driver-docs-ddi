---
UID : NF:ndis.NdisMIndicateReceiveNetBufferLists
title : NdisMIndicateReceiveNetBufferLists function
author : windows-driver-content
description : Miniport drivers call the NdisMIndicateReceiveNetBufferLists function to indicate the receipt of data from the network.
old-location : netvista\ndismindicatereceivenetbufferlists.htm
old-project : netvista
ms.assetid : b87dba3e-c18f-4ea2-8bd5-ec3cdafc534b
ms.author : windowsdriverdev
ms.date : 1/18/2018
ms.keywords : NdisMIndicateReceiveNetBufferLists function [Network Drivers Starting with Windows Vista], ndis_sendrcv_ref_3ef0c38f-53f7-44a0-adfc-443132743f50.xml, NdisMIndicateReceiveNetBufferLists, netvista.ndismindicatereceivenetbufferlists, ndis/NdisMIndicateReceiveNetBufferLists
ms.prod : windows-hardware
ms.technology : windows-devices
ms.topic : function
req.header : ndis.h
req.include-header : Ndis.h
req.target-type : Universal
req.target-min-winverclnt : Supported in NDIS 6.0 and later.
req.target-min-winversvr : 
req.kmdf-ver : 
req.umdf-ver : 
req.ddi-compliance : Irql_SendRcv_Function
req.unicode-ansi : 
req.idl : 
req.max-support : 
req.namespace : 
req.assembly : 
req.type-library : 
req.lib : Ndis.lib
req.dll : 
req.irql : <= DISPATCH_LEVEL
topictype : 
apitype : 
apilocation : 
apiname : 
product : Windows
targetos : Windows
req.typenames : "*PNDIS_SHARED_MEMORY_USAGE, NDIS_SHARED_MEMORY_USAGE"
---


# NdisMIndicateReceiveNetBufferLists function
Miniport drivers call the 
  <b>NdisMIndicateReceiveNetBufferLists</b> function to indicate the receipt of data from the network.

## Syntax

````
VOID NdisMIndicateReceiveNetBufferLists(
  _In_ NDIS_HANDLE      MiniportAdapterHandle,
  _In_ PNET_BUFFER_LIST NetBufferLists,
  _In_ NDIS_PORT_NUMBER PortNumber,
  _In_ ULONG            NumberOfNetBufferLists,
  _In_ ULONG            ReceiveFlags
);
````

## Parameters

`MiniportAdapterHandle`

The miniport handle that NDIS passed to the 
     <mshelp:link keywords="netvista.miniportinitializeex" tabindex="0"><i>
     MiniportInitializeEx</i></mshelp:link> function.

`NetBufferList`

TBD

`PortNumber`

A port number that identifies a miniport adapter port. To assign a miniport adapter port number,
     call the 
     <a href="..\ndis\nf-ndis-ndismallocateport.md">NdisMAllocatePort</a> function. A zero
     value identifies the default port of a miniport adapter. Use the default port if the miniport driver has
     not allocated ports for the specified adapter.

`NumberOfNetBufferLists`

The number of <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structures that are in the linked list of structures at 
     <i>NetBufferLists</i> .

`ReceiveFlags`

Flags that define attributes for the send operation. The flags can be combined with an OR
     operation. To clear all the flags, set this member to zero. This function supports the following flags:


## Return Value

None

## Remarks

A miniport driver typically calls the 
    <b>NdisMIndicateReceiveNetBufferLists</b> function from its 
    <a href="..\ndis\nc-ndis-miniport_interrupt_dpc.md">MiniportInterruptDPC</a> function.
    When a miniport driver calls 
    <b>NdisMIndicateReceiveNetBufferLists</b>, it specifies a list of 
    <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structures in the 
    <i>NetBufferLists</i> parameter. NDIS passes the <b>NET_BUFFER_LIST</b> structures to the 
    <mshelp:link keywords="netvista.protocolreceivenetbufferlists" tabindex="0"><b>
    ProtocolReceiveNetBufferLists</b></mshelp:link> function of bound protocol drivers.

Miniport drivers must set the 
    <b>SourceHandle</b> member of each <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structure to the same value as the 
    <i>MiniportAdapterHandle</i> parameter.

If a miniport driver calls 
    <b>NdisMIndicateReceiveNetBufferLists</b> and clears the <b>NDIS_RECEIVE_FLAG_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter, NDIS returns the indicated <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structures to the miniport
    driver's 
    <mshelp:link keywords="netvista.miniportreturnnetbufferlists" tabindex="0"><i>
    MiniportReturnNetBufferLists</i></mshelp:link> function. In this case, the miniport driver must not reclaim the
    <b>NET_BUFFER_LIST</b> structures until NDIS returns the <b>NET_BUFFER_LIST</b> structures to the miniport driver's 
    <i>MiniportReturnNetBufferLists</i> function.

If a miniport driver calls 
    <b>NdisMIndicateReceiveNetBufferLists</b> and sets the <b>NDIS_RECEIVE_FLAG_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter, this indicates that the miniport driver must regain ownership of the
    <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structures immediately. In this case, NDIS does not call the miniport driver's 
    <i>MiniportReturnNetBufferLists</i> function to return the <b>NET_BUFFER_LIST</b> structures. Instead, NDIS
    returns the <b>NET_BUFFER_LIST</b> structures to the miniport driver upon return from 
    <b>NdisMIndicateReceiveNetBufferLists</b>. The miniport driver should reclaim the <b>NET_BUFFER_LIST</b>
    structures immediately after 
    <b>NdisMIndicateReceiveNetBufferLists</b> returns. To reclaim the <b>NET_BUFFER_LIST</b> structures, a miniport
    driver can call its own 
    <mshelp:link keywords="netvista.miniportreturnnetbufferlists" tabindex="0"><i>
    MiniportReturnNetBufferLists</i></mshelp:link> function.

Setting the <b>NDIS_RECEIVE_FLAG_RESOURCES</b> flag in the 
    <i>ReceiveFlags</i> parameter forces the protocol drivers to copy the network data and release the
    <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structures to the miniport driver. Driver writers should design their miniport drivers
    with enough preallocated <b>NET_BUFFER_LIST</b> structures to avoid unnecessary copying.

The caller of 
    <b>NdisMIndicateReceiveNetBufferLists</b> must properly initialize the <a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a> structures,
    attached 
    <a href="..\ndis\ns-ndis-_net_buffer.md">NET_BUFFER</a> structures, and any attached MDLs.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows Driver kit version** |  |
| **Target platform** | Universal |
| **Minimum KMDF version** |  |
| **Minimum UMDF version** |  |
| **Header** | ndis.h (include Ndis.h) |
| **Library** |  |
| **IRQL** | <= DISPATCH_LEVEL |
| **DDI compliance rules** | Irql_SendRcv_Function |

## See Also

<a href="..\ndis\nf-ndis-ndismallocateport.md">NdisMAllocatePort</a>

<a href="..\ndis\ns-ndis-_net_buffer.md">NET_BUFFER</a>

<a href="..\ndis\nc-ndis-miniport_initialize.md">MiniportInitializeEx</a>

<mshelp:link keywords="netvista.protocolreceivenetbufferlists" tabindex="0"><b>
   ProtocolReceiveNetBufferLists</b></mshelp:link>

<a href="..\ndis\ns-ndis-_net_buffer_list.md">NET_BUFFER_LIST</a>

<a href="..\ntddndis\ns-ntddndis-_ndis_receive_queue_parameters.md">NDIS_RECEIVE_QUEUE_PARAMETERS</a>

<a href="..\ndis\nc-ndis-miniport_interrupt_dpc.md">MiniportInterruptDPC</a>

<mshelp:link keywords="netvista.miniportreturnnetbufferlists" tabindex="0"><i>
   MiniportReturnNetBufferLists</i></mshelp:link>

 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMIndicateReceiveNetBufferLists function%20 RELEASE:%20(1/18/2018)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>