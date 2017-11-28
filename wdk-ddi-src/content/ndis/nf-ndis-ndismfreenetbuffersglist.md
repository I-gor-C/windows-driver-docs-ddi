---
UID: NF.ndis.NdisMFreeNetBufferSGList
title: NdisMFreeNetBufferSGList
author: windows-driver-content
description: Bus-master miniport drivers call the NdisMFreeNetBufferSGList function to free scatter/gather list resources that were allocated by calling the NdisMAllocateNetBufferSGList function.
old-location: netvista\ndismfreenetbuffersglist.htm
old-project: netvista
ms.assetid: 22945e04-9feb-4f4b-9ca6-916dab372a64
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisMFreeNetBufferSGList
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
req.alt-api: NdisMFreeNetBufferSGList
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Gather_DMA_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: DISPATCH_LEVEL
req.iface: 
---

# NdisMFreeNetBufferSGList function



## -description
<p>Bus-master miniport drivers call the 
  <b>NdisMFreeNetBufferSGList</b> function to free scatter/gather list resources that were allocated by
  calling the 
  <a href="..\ndis\nf-ndis-ndismallocatenetbuffersglist.md">
  NdisMAllocateNetBufferSGList</a> function.</p>


## -syntax

````
VOID NdisMFreeNetBufferSGList(
  _In_ NDIS_HANDLE          NdisMiniportDmaHandle,
  _In_ PSCATTER_GATHER_LIST pSGL,
  _In_ PNET_BUFFER          NetBuffer
);
````


## -parameters
<dl>

### -param <i>NdisMiniportDmaHandle</i> [in]

<dd>
<p>A handle to a context area that NDIS uses to manage a DMA resource. The caller obtained this
     handle by calling the 
     <a href="..\ndis\nf-ndis-ndismregisterscattergatherdma.md">
     NdisMRegisterScatterGatherDma</a> function.</p>
</dd>

### -param <i>pSGL</i> [in]

<dd>
<p>A pointer to a miniport driver scatter/gather list buffer.</p>
</dd>

### -param <i>NetBuffer</i> [in]

<dd>
<p>A pointer to the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure associated with the
     specified scatter/gather list buffer.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>Bus-master miniport drivers must call the 
    <b>NdisMFreeNetBufferSGList</b> function to free a scatter/gather list. A miniport driver typically calls 
    <b>NdisMFreeNetBufferSGList</b> from its 
    <a href="..\ndis\nc-ndis-miniport-interrupt-dpc.md">MiniportInterruptDPC</a> function
    while it is handling a send complete interrupt or at any time that the driver no longer requires the
    scatter/gather list. Do not call 
    <b>NdisMFreeNetBufferSGList</b> while the driver or hardware is still accessing the memory that is
    described by the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure that is associated with the
    scatter/gather list.</p>

<p>Miniport drivers can free the buffer that was specified in the 
    <i>ScatterGatherListBuffer</i> parameter of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562776">NdisMAllocateNetBufferSGList</a> function after 
    <b>NdisMFreeNetBufferSGList</b> returns.</p>

<p>Before accessing received data, miniport drivers must call <b>NdisMFreeNetBufferSGList</b> to flush the memory cache.</p>

<p>Bus-master miniport drivers must call the 
    <b>NdisMFreeNetBufferSGList</b> function to free a scatter/gather list. A miniport driver typically calls 
    <b>NdisMFreeNetBufferSGList</b> from its 
    <a href="..\ndis\nc-ndis-miniport-interrupt-dpc.md">MiniportInterruptDPC</a> function
    while it is handling a send complete interrupt or at any time that the driver no longer requires the
    scatter/gather list. Do not call 
    <b>NdisMFreeNetBufferSGList</b> while the driver or hardware is still accessing the memory that is
    described by the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a> structure that is associated with the
    scatter/gather list.</p>

<p>Miniport drivers can free the buffer that was specified in the 
    <i>ScatterGatherListBuffer</i> parameter of the 
    <a href="https://msdn.microsoft.com/library/windows/hardware/ff562776">NdisMAllocateNetBufferSGList</a> function after 
    <b>NdisMFreeNetBufferSGList</b> returns.</p>

<p>Before accessing received data, miniport drivers must call <b>NdisMFreeNetBufferSGList</b> to flush the memory cache.</p>

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
<tr>
<th width="30%">
<p>IRQL</p>
</th>
<td width="70%">
<p>DISPATCH_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547934">Irql_Gather_DMA_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-interrupt-dpc.md">MiniportInterruptDPC</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff568376">NET_BUFFER</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff562776">NdisMAllocateNetBufferSGList</a>
</dt>
<dt>
<a href="..\ndis\nf-ndis-ndismregisterscattergatherdma.md">
   NdisMRegisterScatterGatherDma</a>
</dt>
<dt>
<a href="NULL">Allocating and Freeing Scatter/Gather Lists</a>
</dt>
<dt>
<a href="NULL">Miniport Driver Scatter/Gather DMA</a>
</dt>
<dt>
<a href="NULL">NDIS Scatter/Gather DMA</a>
</dt>
<dt>
<a href="NULL">Registering and Deregistering DMA Channels</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMFreeNetBufferSGList function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
