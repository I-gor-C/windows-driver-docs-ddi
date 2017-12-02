---
UID: NF.ndischimney.NdisMInitiateOffloadComplete
title: NdisMInitiateOffloadComplete
author: windows-driver-content
description: An offload target calls the NdisMInitiateOffloadComplete function to complete an offload operation that was initiated by a previous call to the MiniportInitiateOffload function.
old-location: netvista\ndisminitiateoffloadcomplete.htm
old-project: netvista
ms.assetid: 983b2e04-1563-4f2e-85a7-8fd93ec1cd8c
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NdisMInitiateOffloadComplete
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Universal
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMInitiateOffloadComplete
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
req.irql: Any level
req.iface: 
---

# NdisMInitiateOffloadComplete function



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>An offload target calls the 
  <b>NdisMInitiateOffloadComplete</b> function to complete an offload operation that was initiated by a
  previous call to the 
  <a href="..\ndischimney\nc-ndischimney-w-initiate-offload-handler.md">
  MiniportInitiateOffload</a> function.</p>


## -syntax

````
VOID NdisMInitiateOffloadComplete(
  _In_ NDIS_HANDLE                       NdisMiniportHandle,
  _In_ PNDIS_MINIPORT_OFFLOAD_BLOCK_LIST OffloadBlockList
);
````


## -parameters
<dl>

### -param NdisMiniportHandle [in]

<dd>
<p>The handle that the offload target obtained in a previous call to 
     <a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">
     NdisMRegisterMiniportDriver</a>.</p>
</dd>

### -param OffloadBlockList [in]

<dd>
<p>A pointer to an 
     <a href="..\ndischimney\ns-ndischimney--ndis-miniport-offload-block-list.md">
     NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a> structure. The offload target obtained this pointer as an input
     parameter to its 
     <a href="..\ndischimney\nc-ndischimney-w-initiate-offload-handler.md">
     MiniportInitiateOffload</a> function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Before calling 
    <b>NdisMInitiateOffloadComplete</b>, the offload target must write one of the following NDIS_STATUS
    values to the 
    <b>Status</b> member of each 
    <a href="..\ndischimney\ns-ndischimney--ndis-miniport-offload-block-list.md">
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a> structure in the state tree passed to the offload target's 
    <i>MiniportInitiateOffload</i> function:</p>

<p>NDIS_STATUS_SUCCESS</p>

<p>NDIS_STATUS_PARTIAL_SUCCESS</p>

<p>NDIS_STATUS_RESOURCES</p>

<p>NDIS_STATUS_OFFLOAD_TCP_ENTRIES</p>

<p>NDIS_STATUS_OFFLOAD_PATH_ENTRIES</p>

<p>NDIS_STATUS_OFFLOAD_NEIGHBOR_ENTRIES</p>

<p>NDIS_STATUS_OFFLOAD_HW_ADDRESS_ENTRIES</p>

<p>NDIS_STATUS_OFFLOAD_IP_ADDRESS_ENTRIES</p>

<p>NDIS_STATUS_OFFLOAD_TCP_XMIT_BUFFER</p>

<p>NDIS_STATUS_OFFLOAD_TCP_RCV_BUFFER</p>

<p>NDIS_STATUS_OFFLOAD_TCP_RCV_WINDOW</p>

<p>NDIS_STATUS_OFFLOAD_VLAN_ENTRIES</p>

<p>NDIS_STATUS_OFFLOAD_PATH_MTU</p>

<p>NDIS_STATUS_FAILURE</p>

<p>For more information, see 
    <a href="netvista.returning_completion_status_of_an_initiate_offload_operation">
    Returning Completion Status of an Initiate Offload Operation</a>.</p>

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
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Ndischimney.h (include Ndischimney.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>Any level</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndischimney\nc-ndischimney-w-initiate-offload-handler.md">MiniportInitiateOffload</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--ndis-miniport-offload-block-list.md">
   NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismregisterminiportdriver.md">NdisMRegisterMiniportDriver</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-receive-indicate.md">NdisTcpOffloadReceiveHandler</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-ndis-tcp-offload-event-indicate.md">NdisTcpOffloadEventHandler</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff569816">OID_TCP_TASK_OFFLOAD</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMInitiateOffloadComplete function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
