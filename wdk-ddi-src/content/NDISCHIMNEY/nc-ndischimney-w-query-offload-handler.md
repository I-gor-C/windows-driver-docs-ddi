---
UID: NC.ndischimney.W_QUERY_OFFLOAD_HANDLER
title: W_QUERY_OFFLOAD_HANDLER
author: windows-driver-content
description: The MiniportQueryOffload function queries previously offloaded TCP chimney state objects.
old-location: netvista\miniportqueryoffload.htm
ms.assetid: a583c4cb-53c1-4eff-bcfe-c962f736b1f8
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
req.alt-api: MiniportQueryOffload
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

# W_QUERY_OFFLOAD_HANDLER callback



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>The 
  <i>MiniportQueryOffload</i> function queries previously offloaded TCP chimney state objects.</p>


## -prototype

````
W_QUERY_OFFLOAD_HANDLER MiniportQueryOffload;

VOID MiniportQueryOffload(
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
     information about this instance of the adapter. The offload target provided this handle to NDIS when it
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
     NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a> structure, which can be the root of a linked list of such
     structures. These structures identify the offloaded state that is being queried.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The 
    <i>MiniportQueryOffload</i> function can query any TCP chimney state that has been offloaded to the
    offload target.</p>

<p>The 
    <i>MiniportQueryOffload</i> function stores the 
    <i>OffloadBlockList</i> pointer and then returns. The offload target always completes the query operation
    asynchronously by calling the 
    <a href="https://msdn.microsoft.com/7bcc6610-0c48-4a7f-b8fa-be372af201ba">
    NdisMQueryOffloadStateComplete</a> function. The 
    <i>OffloadBlockList</i> pointer points to an 
    <a href="https://msdn.microsoft.com/ebc98e65-5d11-4c3d-aea1-dfad1434c093">
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a> structure that can either be a stand-alone structure or the root
    node in an 
    <a href="NULL">offload state tree</a>. The state tree is valid
    until the offload target calls the 
    <b>NdisMQueryOffloadStateComplete</b> function.</p>

<p>After returning from the 
    <i>MiniportQueryOffload</i> function, the miniport driver fills in the 
    <a href="netvista.offload_state_structures">offload state structure</a> that is
    associated with each NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure in the state tree pointed to by the 
    <i>OffloadBlockList</i> pointer. To each of these offload state structures, the miniport driver writes the
    current value of each variable in the structure.</p>

<p>Before calling the 
    <b>NdisMQueryOffloadStateComplete</b> function, the offload target must write either of the following
    NDIS_STATUS values to the 
    <b>Status</b> member of each NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure in the state tree:</p>

<p>NDIS_STATUS_SUCCESS
     </p>

<p>The offload target successfully queried the state objects.</p>

<p>NDIS_STATUS_FAILURE
     </p>

<p>The query operation did not succeed. The host stack will terminate the state objects that could not
     be queried.</p>

<p>The 
    <i>MiniportQueryOffload</i> function can query any TCP chimney state that has been offloaded to the
    offload target.</p>

<p>The 
    <i>MiniportQueryOffload</i> function stores the 
    <i>OffloadBlockList</i> pointer and then returns. The offload target always completes the query operation
    asynchronously by calling the 
    <a href="https://msdn.microsoft.com/7bcc6610-0c48-4a7f-b8fa-be372af201ba">
    NdisMQueryOffloadStateComplete</a> function. The 
    <i>OffloadBlockList</i> pointer points to an 
    <a href="https://msdn.microsoft.com/ebc98e65-5d11-4c3d-aea1-dfad1434c093">
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a> structure that can either be a stand-alone structure or the root
    node in an 
    <a href="NULL">offload state tree</a>. The state tree is valid
    until the offload target calls the 
    <b>NdisMQueryOffloadStateComplete</b> function.</p>

<p>After returning from the 
    <i>MiniportQueryOffload</i> function, the miniport driver fills in the 
    <a href="netvista.offload_state_structures">offload state structure</a> that is
    associated with each NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure in the state tree pointed to by the 
    <i>OffloadBlockList</i> pointer. To each of these offload state structures, the miniport driver writes the
    current value of each variable in the structure.</p>

<p>Before calling the 
    <b>NdisMQueryOffloadStateComplete</b> function, the offload target must write either of the following
    NDIS_STATUS values to the 
    <b>Status</b> member of each NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure in the state tree:</p>

<p>NDIS_STATUS_SUCCESS
     </p>

<p>The offload target successfully queried the state objects.</p>

<p>NDIS_STATUS_FAILURE
     </p>

<p>The query operation did not succeed. The host stack will terminate the state objects that could not
     be queried.</p>

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
<a href="https://msdn.microsoft.com/ebc98e65-5d11-4c3d-aea1-dfad1434c093">
   NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563672">NdisMSetMiniportAttributes</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/7bcc6610-0c48-4a7f-b8fa-be372af201ba">
   NdisMQueryOffloadStateComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20W_QUERY_OFFLOAD_HANDLER callback function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
