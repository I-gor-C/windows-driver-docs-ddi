---
UID: NC.ndischimney.W_INITIATE_OFFLOAD_HANDLER
title: W_INITIATE_OFFLOAD_HANDLER
author: windows-driver-content
description: MiniportInitiateOffload offloads TCP chimney state from the host stack.
old-location: netvista\miniportinitiateoffload.htm
ms.assetid: f430642b-01bf-4ed7-bfea-e8dd8d5a8208
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: callback
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: MiniportInitiateOffload
req.alt-loc: Ndischimney.h
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
ms.keywords: BINARY_DATA, BINARY_DATA
req.iface: 
---

# W_INITIATE_OFFLOAD_HANDLER callback



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p><i>MiniportInitiateOffload</i> offloads TCP chimney state from the host stack.</p>


## -prototype

````
W_INITIATE_OFFLOAD_HANDLER MiniportInitiateOffload;

VOID MiniportInitiateOffload(
  _In_    NDIS_HANDLE                       MiniportAdapterContext,
  _Inout_ PNDIS_MINIPORT_OFFLOAD_BLOCK_LIST OffloadBlockList
)
{ ... }
````


## -parameters
<dl>

### -param <i>MiniportAdapterContext</i> [in]

<dd>
<p>The handle to an offload-target allocated context area in which the offload target maintains state
     information about this instance of the adapter. The miniport driver provided this handle to NDIS when it
     called 
     <a href="https://msdn.microsoft.com/861626af-23ea-40dc-a91a-7da42d4b0a1c">
     NdisMSetMiniportAttributes</a> from its 
     <a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">
     MiniportInitializeEx</a> function.</p>
</dd>

### -param <i>OffloadBlockList</i> [in, out]

<dd>
<p>A pointer to an 
     <a href="https://msdn.microsoft.com/ebc98e65-5d11-4c3d-aea1-dfad1434c093">
     NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a> structure that can be a stand-alone structure or the root of a
     linked list of such structures.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The 
    <i>MiniportInitiateOffload</i> function stores the 
    <i>OffloadBlockList</i> pointer and then returns. The offload target always completes the offload
    operation asynchronously by calling 
    <a href="https://msdn.microsoft.com/983b2e04-1563-4f2e-85a7-8fd93ec1cd8c">
    NdisMInitiateOffloadComplete</a>. The state tree pointed to by the 
    <i>OffloadBlockList</i> pointer is valid until the miniport driver calls 
    <b>NdisMInitiateOffloadComplete</b>.</p>

<p>After returning from its 
    <i>MiniportInitiateOffload</i> function, the offload target offloads state from the state tree. An
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure whose 
    <b>MiniportOffloadContext</b> member points to a memory location that contains a <b>NULL</b> value is followed by
    state to be offloaded. For more information, see 
    <a href="netvista.storing_and_referencing_offloaded_state">Storing and Referencing
    Offloaded State</a>. The 
    <b>Header</b> member of an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure contains a 
    <b>Type</b> member that specifies the type of offload state, and by implication, the 
    <a href="netvista.offload_state_structures">offload state structure</a> or structures,
    that immediately follow the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure in memory.</p>

<p>The offload target offloads the offload state associated with an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
    structure into an offload context area. For more information, see 
    <a href="netvista.storing_and_referencing_offloaded_state">Storing and Referencing
    Offloaded State</a>.</p>

<p>When offloading state, the offload target must traverse the state tree in 
    <a href="netvista.traversing_a_state_tree">depth-first/breadth-next fashion</a>. It
    is critical that an offload target offloads state in this way.</p>

<p>Some of the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structures in the state tree that are passed to the 
    <i>MiniportInitiateOffload</i> function can be placeholders or linking nodes that do not have accompanying
    state to be offloaded. For more information, see 
    <a href="netvista.placeholders__linkers__and_new_offloads">Placeholders, Linkers, and
    New Offloads</a>.</p>

<p>The offload target can receive buffered data from the host stack for a connection that is being
    offloaded. The offload target must copy this data into its own buffer before completing the offload
    operation. For more information about processing buffered receive data, see 
    <a href="netvista.handling_buffered_receive_data_during_and_after_an_offload_operation">
    Handling Buffered Receive Data During and After an Offload Operation</a>.</p>

<p>For each state object that it offloads, the offload target must also supply a PVOID value that
    references the offload context area in which the offload target stores the state object. The offload
    target writes this PVOID value to the memory location pointed to by the 
    <b>*MiniportOffloadContext</b> member of the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure associated with
    the state. If the offload target did not successfully offload the state associated with the
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure, it should not write a value to the memory location pointed to
    by the 
    <b>*MiniportOffloadContext</b> member. For more information, see 
    <a href="netvista.storing_and_referencing_offloaded_state">Storing and Referencing
    Offloaded State</a>.</p>

<p>The 
    <i>MiniportInitiateOffload</i> function stores the 
    <i>OffloadBlockList</i> pointer and then returns. The offload target always completes the offload
    operation asynchronously by calling 
    <a href="https://msdn.microsoft.com/983b2e04-1563-4f2e-85a7-8fd93ec1cd8c">
    NdisMInitiateOffloadComplete</a>. The state tree pointed to by the 
    <i>OffloadBlockList</i> pointer is valid until the miniport driver calls 
    <b>NdisMInitiateOffloadComplete</b>.</p>

<p>After returning from its 
    <i>MiniportInitiateOffload</i> function, the offload target offloads state from the state tree. An
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure whose 
    <b>MiniportOffloadContext</b> member points to a memory location that contains a <b>NULL</b> value is followed by
    state to be offloaded. For more information, see 
    <a href="netvista.storing_and_referencing_offloaded_state">Storing and Referencing
    Offloaded State</a>. The 
    <b>Header</b> member of an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure contains a 
    <b>Type</b> member that specifies the type of offload state, and by implication, the 
    <a href="netvista.offload_state_structures">offload state structure</a> or structures,
    that immediately follow the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure in memory.</p>

<p>The offload target offloads the offload state associated with an NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
    structure into an offload context area. For more information, see 
    <a href="netvista.storing_and_referencing_offloaded_state">Storing and Referencing
    Offloaded State</a>.</p>

<p>When offloading state, the offload target must traverse the state tree in 
    <a href="netvista.traversing_a_state_tree">depth-first/breadth-next fashion</a>. It
    is critical that an offload target offloads state in this way.</p>

<p>Some of the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structures in the state tree that are passed to the 
    <i>MiniportInitiateOffload</i> function can be placeholders or linking nodes that do not have accompanying
    state to be offloaded. For more information, see 
    <a href="netvista.placeholders__linkers__and_new_offloads">Placeholders, Linkers, and
    New Offloads</a>.</p>

<p>The offload target can receive buffered data from the host stack for a connection that is being
    offloaded. The offload target must copy this data into its own buffer before completing the offload
    operation. For more information about processing buffered receive data, see 
    <a href="netvista.handling_buffered_receive_data_during_and_after_an_offload_operation">
    Handling Buffered Receive Data During and After an Offload Operation</a>.</p>

<p>For each state object that it offloads, the offload target must also supply a PVOID value that
    references the offload context area in which the offload target stores the state object. The offload
    target writes this PVOID value to the memory location pointed to by the 
    <b>*MiniportOffloadContext</b> member of the NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure associated with
    the state. If the offload target did not successfully offload the state associated with the
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure, it should not write a value to the memory location pointed to
    by the 
    <b>*MiniportOffloadContext</b> member. For more information, see 
    <a href="netvista.storing_and_referencing_offloaded_state">Storing and Referencing
    Offloaded State</a>.</p>

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
<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563604">NdisMInitiateOffloadComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/ebc98e65-5d11-4c3d-aea1-dfad1434c093">
   NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563672">NdisMSetMiniportAttributes</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20W_INITIATE_OFFLOAD_HANDLER callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
