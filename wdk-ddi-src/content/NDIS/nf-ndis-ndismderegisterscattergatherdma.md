---
UID: NF.ndis.NdisMDeregisterScatterGatherDma
title: NdisMDeregisterScatterGatherDma
author: windows-driver-content
description: Bus-master miniport drivers call NdisMDeregisterScatterGatherDma to release DMA resources that were allocated with the NdisMRegisterScatterGatherDma function.
old-location: netvista\ndismderegisterscattergatherdma.htm
ms.assetid: 44792a1f-c6d5-4491-a06d-e00e41e40059
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported in NDIS 6.0 and later.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMDeregisterScatterGatherDma
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Init_RegisterSG, Irql_Gather_DMA_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
ms.keywords: NdisMDeregisterScatterGatherDma
req.iface: 
---

# NdisMDeregisterScatterGatherDma function



## -description
<p>Bus-master miniport drivers call 
  <b>NdisMDeregisterScatterGatherDma</b> to release DMA resources that were allocated with the 
  <a href="https://msdn.microsoft.com/90ce64a2-9140-4b5f-88aa-b4f01a3d0c6f">
  NdisMRegisterScatterGatherDma</a> function.</p>


## -syntax

````
VOID NdisMDeregisterScatterGatherDma(
  _In_ NDIS_HANDLE NdisMiniportDmaHandle
);
````


## -parameters
<dl>

### -param <i>NdisMiniportDmaHandle</i> [in]

<dd>
<p>A handle to a context area that NDIS uses to manage a DMA resource. The caller obtained this
     handle by calling the 
     <b>NdisMRegisterScatterGatherDma</b> function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>An NDIS miniport driver calls 
    <b>NdisMDeregisterScatterGatherDma</b> from its 
    <a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a> function to release the
    DMA resources it allocated and initialized in a previous call to 
    <b>NdisMRegisterScatterGatherDma</b>.</p>

<p>An NDIS miniport driver calls 
    <b>NdisMDeregisterScatterGatherDma</b> from its 
    <a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a> function to release the
    DMA resources it allocated and initialized in a previous call to 
    <b>NdisMRegisterScatterGatherDma</b>.</p>

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
<p>PASSIVE_LEVEL</p>
</td>
</tr>
<tr>
<th width="30%">
<p>DDI compliance rules</p>
</th>
<td width="70%">
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547153">Init_RegisterSG</a>, <a href="https://msdn.microsoft.com/library/windows/hardware/ff547934">Irql_Gather_DMA_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/b8d452b4-bef3-4991-87cf-fac15bedfde4">MiniportHaltEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/90ce64a2-9140-4b5f-88aa-b4f01a3d0c6f">
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
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMDeregisterScatterGatherDma function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
