---
UID: NF.ndischimney.NdisUpdateOffload
title: NdisUpdateOffload
author: windows-driver-content
description: A protocol or intermediate driver calls the NdisUpdateOffload function to update previously offloaded TCP chimney state objects.
old-location: netvista\ndisupdateoffload.htm
old-project: netvista
ms.assetid: 1e85357d-9fe2-406b-bc1a-69e4357a0f8b
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisUpdateOffload
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
req.alt-api: NdisUpdateOffload
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: 
req.iface: 
---

# NdisUpdateOffload function



## -description
<p class="CCE_Message">[The TCP chimney offload feature is deprecated and should not be used.]</p>
<p>A protocol or intermediate driver calls the 
  <b>NdisUpdateOffload</b> function to update previously offloaded TCP chimney state objects.</p>


## -syntax

````
VOID NdisUpdateOffload(
  _In_ NDIS_HANDLE                       NdisBindingHandle,
  _In_ PNDIS_PROTOCOL_OFFLOAD_BLOCK_LIST OffloadBlockList
);
````


## -parameters
<dl>

### -param <i>NdisBindingHandle</i> [in]

<dd>
<p>The handle that NDIS provided at the 
     <i>NdisBindingHandle</i> parameter of 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>. This handle
     identifies the binding between the caller and the underlying intermediate driver or offload
     target.</p>
</dd>

### -param <i>OffloadBlockList</i> [in]

<dd>
<p>A pointer to an 
     <a href="..\ndischimney\ns-ndischimney--ndis-protocol-offload-block-list.md">
     NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST</a> structure that can be a stand-alone structure or the root of a
     linked list of such structures. These structures identify the offloaded state objects that are being
     updated.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>An intermediate driver calls the 
    <b>NdisUpdateOffload</b> function to propagate an update offload operation that was initiated by the host
    stack. For more information, see 
    <a href="netvista.propagating_state_manipulation_operations">Propagating
    State-Manipulation Operations</a>.</p>

<p>From the 
    <a href="..\ndischimney\ns-ndischimney--ndis-miniport-offload-block-list.md">
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a> structure that was passed to its 
    <a href="..\ndischimney\nc-ndischimney-w-update-offload-handler.md">MiniportUpdateOffload</a> function,
    the intermediate driver constructs an NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure. For more information,
    see 
    <a href="netvista.reusing_an_ndis_miniport_offload_block_list_structure">Reusing an
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST Structure</a>. The intermediate driver passes a pointer (the 
    <i>OffloadBlockList</i> parameter) to this NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure when calling the 
    <b>NdisUpdateOffload</b> function.</p>

<p>An intermediate driver calls the 
    <b>NdisUpdateOffload</b> function to propagate an update offload operation that was initiated by the host
    stack. For more information, see 
    <a href="netvista.propagating_state_manipulation_operations">Propagating
    State-Manipulation Operations</a>.</p>

<p>From the 
    <a href="..\ndischimney\ns-ndischimney--ndis-miniport-offload-block-list.md">
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a> structure that was passed to its 
    <a href="..\ndischimney\nc-ndischimney-w-update-offload-handler.md">MiniportUpdateOffload</a> function,
    the intermediate driver constructs an NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure. For more information,
    see 
    <a href="netvista.reusing_an_ndis_miniport_offload_block_list_structure">Reusing an
    NDIS_MINIPORT_OFFLOAD_BLOCK_LIST Structure</a>. The intermediate driver passes a pointer (the 
    <i>OffloadBlockList</i> parameter) to this NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST structure when calling the 
    <b>NdisUpdateOffload</b> function.</p>

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
<p>Library</p>
</th>
<td width="70%">
<dl>
<dt>Ndis.lib</dt>
</dl>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndischimney\nc-ndischimney-w-update-offload-handler.md">MiniportUpdateOffload</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--ndis-miniport-offload-block-list.md">
   NDIS_MINIPORT_OFFLOAD_BLOCK_LIST</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563694">NdisMUpdateOffloadComplete</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563715">NdisOpenAdapterEx</a>
</dt>
<dt>
<a href="..\ndischimney\ns-ndischimney--ndis-protocol-offload-block-list.md">
   NDIS_PROTOCOL_OFFLOAD_BLOCK_LIST</a>
</dt>
<dt>
<a href="..\ndischimney\nc-ndischimney-update-offload-complete-handler.md">
   ProtocolUpdateOffloadComplete</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisUpdateOffload function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
