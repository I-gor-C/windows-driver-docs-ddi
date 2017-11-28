---
UID: NF.ndis.NdisMDeregisterDmaChannel
title: NdisMDeregisterDmaChannel
author: windows-driver-content
description: The NdisMDeregisterDmaChannel function releases a miniport driver's claim on a DMA channel for a NIC.
old-location: netvista\ndismderegisterdmachannel.htm
old-project: netvista
ms.assetid: 1581cbfd-bdab-40ed-9978-f60ec220c17a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisMDeregisterDmaChannel
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisMDeregisterDmaChannel (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisMDeregisterDmaChannel (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMDeregisterDmaChannel
req.alt-loc: ndis.lib,ndis.dll
req.ddi-compliance: Irql_Miniport_Driver_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: Ndis.lib
req.dll: 
req.irql: PASSIVE_LEVEL
req.iface: 
---

# NdisMDeregisterDmaChannel function



## -description
<p>The 
  <b>NdisMDeregisterDmaChannel</b> function releases a miniport driver's claim on a DMA channel for a
  NIC.</p>


## -syntax

````
VOID NdisMDeregisterDmaChannel(
  _In_ NDIS_HANDLE MiniportDmaHandle
);
````


## -parameters
<dl>

### -param <i>MiniportDmaHandle</i> [in]

<dd>
<p>The DMA handle returned by the 
     <a href="..\ndis\nf-ndis-ndismregisterdmachannel.md">
     NdisMRegisterDmaChannel</a> function.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>The caller should consider 
    <i>MiniportDmaHandle</i> invalid as soon as it is passed to 
    <b>NdisMDeregisterDmaChannel</b>. This function releases the NIC's claim on the DMA channel in the
    registry.</p>

<p><b>NdisMDeregisterDmaChannel</b> can be called only from a miniport driver's 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> and 
    <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> functions.</p>

<p>The caller should consider 
    <i>MiniportDmaHandle</i> invalid as soon as it is passed to 
    <b>NdisMDeregisterDmaChannel</b>. This function releases the NIC's claim on the DMA channel in the
    registry.</p>

<p><b>NdisMDeregisterDmaChannel</b> can be called only from a miniport driver's 
    <a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a> and 
    <a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a> functions.</p>

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
<p>Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   <a href="https://msdn.microsoft.com/4f9a99d2-6090-46f2-8c92-7893f6d91cdf">NdisMDeregisterDmaChannel (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisMDeregisterDmaChannel (NDIS
   5.1)</b>) in Windows XP.</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff547979">Irql_Miniport_Driver_Function</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\ndis\nc-ndis-miniport-halt.md">MiniportHaltEx</a>
</dt>
<dt>
<a href="..\ndis\nc-ndis-miniport-initialize.md">MiniportInitializeEx</a>
</dt>
<dt>
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563646">NdisMRegisterDmaChannel</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMDeregisterDmaChannel function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
