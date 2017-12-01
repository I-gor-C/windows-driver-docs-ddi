---
UID: NC.ndischimney.INDICATE_OFFLOAD_EVENT_HANDLER
title: INDICATE_OFFLOAD_EVENT_HANDLER
author: windows-driver-content
description: NDIS calls a protocol driver's or intermediate driver's ProtocolIndicateOffloadEvent function to post an indication that was initiated by an underlying driver's or offload target's call to the NdisMOffloadEventIndicate function.
old-location: netvista\protocolindicateoffloadevent.htm
old-project: netvista
ms.assetid: 608c1c7c-1eb3-4d86-9471-313fce2df00e
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.keywords: BINARY_DATA, BINARY_DATA
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: ndischimney.h
req.include-header: Ndischimney.h
req.target-type: Windows
req.target-min-winverclnt: 
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: ProtocolIndicateOffloadEvent
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
req.irql: 
req.iface: 
---

# INDICATE_OFFLOAD_EVENT_HANDLER callback



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>NDIS calls a protocol driver's or intermediate driver's 
  <i>ProtocolIndicateOffloadEvent</i> function to post an indication that was initiated by an underlying
  driver's or offload target's call to the 
  <a href="..\ndischimney\nf-ndischimney-ndismoffloadeventindicate.md">
  NdisMOffloadEventIndicate</a> function.</p>


## -prototype

````
INDICATE_OFFLOAD_EVENT_HANDLER ProtocolIndicateOffloadEvent;

VOID ProtocolIndicateOffloadEvent(
  _In_ NDIS_HANDLE                       ProtocolBindingContext,
  _In_ PNDIS_PROTOCOL_OFFLOAD_BLOCK_LIST OffloadBlockList,
  _In_ ULONG                             IndicationCode
)
{ ... }
````


## -parameters
<dl>

### -param <i>ProtocolBindingContext</i> [in]

<dd>
<p>A handle to a context area that was allocated by the protocol driver. The driver maintains the per
     binding context information in this context area. The driver supplied this handle to NDIS when the
     driver called the 
     <a href="..\ndis\nf-ndis-ndisopenadapterex.md">NdisOpenAdapterEx</a> function.</p>
</dd>

### -param <i>OffloadBlockList</i> [in]

<dd>
<p>A pointer to an 
     <a href="..\ndischimney\ns-ndischimney--ndis-protocol-offload-block-list.md">
     NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST</a> structure. This structure identifies the offloaded state object
     on which the indication is being made. Note that there is only one NDIS_MINIPORT_OFFLOAD_BLOCK_LIST
     structure. There is not a linked list of such structures. 
     </p>
<p>The underlying offload target supplies a valid 
     <i>OffloadBlockList</i> pointer when making a 
     <b>NeighborReachabilityQuery</b> indication. In this case, the offload target supplies a 
     <a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-const.md">
     NEIGHBOR_OFFLOAD_STATE_CONST</a> structure, a 
     <a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-cached.md">
     NEIGHBOR_OFFLOAD_STATE_CACHED</a> structure, and a 
     <a href="..\ndischimney\ns-ndischimney--neighbor-offload-state-delegated.md">
     NEIGHBOR_OFFLOAD_STATE_DELEGATED</a> structure (in that order) immediately following the
     NDIS_MINIPORT_OFFLOAD_BLOCK_LIST structure referenced by the 
     <i>OffloadBlockList</i> pointer.</p>
</dd>

### -param <i>IndicationCode</i> [in]

<dd>
<p>The event being indicated as one of the following INDICATE_OFFLOAD_EVENT values:
     </p>
<p></p>
<dl>

### -param <a id="NeighborReachabilityQuery"></a><a id="neighborreachabilityquery"></a><a id="NEIGHBORREACHABILITYQUERY"></a><b>NeighborReachabilityQuery</b>

<dd>
<p>Indicates that a neighbor cache entry (NCE) has become stale. For more information about NCEs,
       see RFC 2461.</p>
</dd>

### -param <a id="NeighborReachabilityInDoubt"></a><a id="neighborreachabilityindoubt"></a><a id="NEIGHBORREACHABILITYINDOUBT"></a><b>NeighborReachabilityInDoubt</b>

<dd>
<p>Reserved.</p>
</dd>
</dl>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The implementation of this function for intermediate drivers is to be determined.</p>

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
<a href="..\ndischimney\ns-ndischimney--ndis-protocol-offload-block-list.md">
   NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST</a>
</dt>
<dt>
<a href="..\ndischimney\nf-ndischimney-ndismoffloadeventindicate.md">NdisMOffloadEventIndicate</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20INDICATE_OFFLOAD_EVENT_HANDLER callback function%20 RELEASE:%20(11/28/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
