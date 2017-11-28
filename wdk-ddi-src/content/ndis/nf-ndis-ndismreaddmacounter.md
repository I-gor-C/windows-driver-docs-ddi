---
UID: NF.ndis.NdisMReadDmaCounter
title: NdisMReadDmaCounter
author: windows-driver-content
description: The NdisMReadDmaCounter function returns the current value of the system DMA controller's counter.
old-location: netvista\ndismreaddmacounter.htm
old-project: netvista
ms.assetid: bfce0f28-4cca-48a2-8836-2f77f4b6370a
ms.author: windowsdriverdev
ms.date: 11/22/2017
ms.keywords: NdisMReadDmaCounter
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see 
   NdisMReadDmaCounter (NDIS
   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   NdisMReadDmaCounter (NDIS
   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NdisMReadDmaCounter
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
req.irql: <= DISPATCH_LEVEL
req.iface: 
---

# NdisMReadDmaCounter function



## -description
<p>The 
  <b>NdisMReadDmaCounter</b> function returns the current value of the system DMA controller's counter.</p>


## -syntax

````
ULONG NdisMReadDmaCounter(
  _In_ NDIS_HANDLE MiniportDmaHandle
);
````


## -parameters
<dl>

### -param <i>MiniportDmaHandle</i> [in]

<dd>
<p>The handle returned when the miniport driver called the 
     <a href="https://msdn.microsoft.com/library/windows/hardware/ff563646">NdisMRegisterDmaChannel</a> function
     during initialization.</p>
</dd>
</dl>

## -returns
<p><b>NdisMReadDmaCounter</b> returns the number of bytes remaining in the current DMA transfer on the
     channel used by the NIC.</p>

## -remarks
<p>Miniport drivers of devices that use the system DMA controller's auto-initialize mode can call 
    <b>NdisMReadDmaCounter</b>.</p>

<p>Miniport drivers of devices that use the system DMA controller's auto-initialize mode can call 
    <b>NdisMReadDmaCounter</b>.</p>

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
   <a href="https://msdn.microsoft.com/0a8be1f7-1509-484b-9fd3-f2ea257dfe40">NdisMReadDmaCounter (NDIS
   5.1)</a>) in Windows Vista. Supported for NDIS 5.1 drivers (see 
   <b>NdisMReadDmaCounter (NDIS
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
<p>&lt;= DISPATCH_LEVEL</p>
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
<a href="https://msdn.microsoft.com/library/windows/hardware/ff563646">NdisMRegisterDmaChannel</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NdisMReadDmaCounter function%20 RELEASE:%20(11/22/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
