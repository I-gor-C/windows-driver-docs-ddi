---
UID: NF.netdma.NetDmaInterruptDpc
title: NetDmaInterruptDpc
author: windows-driver-content
description: The NetDmaInterruptDpc function notifies the NetDMA interface that a DMA transfer deferred procedure call (DPC) has completed on a DMA channel.
old-location: netvista\netdmainterruptdpc.htm
ms.assetid: 93d7e4dd-70ee-4490-bffd-9b07511ee9fe
ms.author: windowsdriverdev
ms.date: 11/1/2017
ms.topic: function
ms.prod: windows-hardware
ms.technology: netvista
req.header: netdma.h
req.include-header: Netdma.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NetDMA 1.0 drivers in Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NetDmaInterruptDpc
req.alt-loc: netdma.h
req.ddi-compliance: 
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
ms.keywords: NetDmaInterruptDpc
req.iface: 
---

# NetDmaInterruptDpc function



## -description

## -syntax

````
VOID NetDmaInterruptDpc(
  _In_     PVOID            NetDmaChannelHandle,
  _In_opt_ PHYSICAL_ADDRESS DmaDescriptor
);
````


## -parameters
<dl>

### -param <i>NetDmaChannelHandle</i> [in]

<dd>
<p>A handle that identifies the DMA channel. The DMA provider driver received this handle from NetDMA
     in a call to the 
     <a href="https://msdn.microsoft.com/42bc0e08-3d85-424f-aaa4-4df788d3706a">
     ProviderAllocateDmaChannel</a> function.</p>
</dd>

### -param <i>DmaDescriptor</i> [in, optional]

<dd>
<p>A pointer to the last DMA descriptor that was processed.</p>
</dd>
</dl>

## -returns
<p>None.</p>

## -remarks
<p>DMA providers call the 
    <b>NetDmaInterruptDpc</b> function in their DPC handler.</p>

<p>DMA providers call the 
    <b>NetDmaInterruptDpc</b> function in their DPC handler.</p>

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
<p>Supported for NetDMA 1.0 drivers in Windows Vista.</p>
</td>
</tr>
<tr>
<th width="30%">
<p>Header</p>
</th>
<td width="70%">
<dl>
<dt>Netdma.h (include Netdma.h)</dt>
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
</table>

## -see-also
<dl>
<dt>
<a href="https://msdn.microsoft.com/42bc0e08-3d85-424f-aaa4-4df788d3706a">ProviderAllocateDmaChannel</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NetDmaInterruptDpc function%20 RELEASE:%20(11/1/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
