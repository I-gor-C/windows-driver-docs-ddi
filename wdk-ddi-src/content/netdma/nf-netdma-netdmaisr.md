---
UID: NF.netdma.NetDmaIsr
title: NetDmaIsr
author: windows-driver-content
description: The NetDmaIsr function notifies the NetDMA interface that a DMA transfer interrupt has occurred on a DMA channel.
old-location: netvista\netdmaisr.htm
old-project: netvista
ms.assetid: 81aa5707-b614-429b-bd8e-0204eec74e0f
ms.author: windowsdriverdev
ms.date: 11/30/2017
ms.keywords: NetDmaIsr
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: function
req.header: netdma.h
req.include-header: Netdma.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NetDMA 1.0 drivers in Windows Vista.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: NetDmaIsr
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
req.irql: DEVICE_LEVEL
req.iface: 
---

# NetDmaIsr function



## -description

## -syntax

````
VOID NetDmaIsr(
  _In_  PVOID            NetDmaChannelHandle,
  _In_  PHYSICAL_ADDRESS DmaDescriptor,
  _Out_ PULONG           pCpuNumber
);
````


## -parameters
<dl>

### -param NetDmaChannelHandle [in]

<dd>
<p>A handle that identifies the DMA channel. The DMA provider driver received this handle from the
     NetDMA interface in a call to the 
     <a href="..\netdma\nc-netdma-dma-channel-allocate-handler.md">
     ProviderAllocateDmaChannel</a> function.</p>
</dd>

### -param DmaDescriptor [in]

<dd>
<p>The physical address of the DMA descriptor that is associated with the interrupt.</p>
</dd>

### -param pCpuNumber [out]

<dd>
<p>The number of the CPU that is associated with the interrupt DPC. The NetDMA interface writes this
     CPU number at the provided address before 
     <b>NetDmaIsr</b> returns.</p>
</dd>
</dl>

## -returns
<p>None</p>

## -remarks
<p>DMA provider drivers call the 
    <b>NetDmaIsr</b> function in their interrupt service routine (ISR).</p>

<p>If the NET_DMA_INTERRUPT_ON_COMPLETION flag in the 
    <b>ControlFlags</b> member of the 
    <a href="..\netdma\ns-netdma--net-dma-descriptor.md">NET_DMA_DESCRIPTOR</a> structure is set, the
    DMA engine should generate an interrupt for the DMA channel after it processes the DMA descriptor. When
    this flag is cleared, the DMA engine does not generate an interrupt.</p>

<p>A DMA provider driver should do as little work as possible in its ISR handler. The driver should defer
    I/O operations to the interrupt DPC handler.</p>

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
<p>DEVICE_LEVEL</p>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="..\netdma\ns-netdma--net-dma-descriptor.md">NET_DMA_DESCRIPTOR</a>
</dt>
<dt>
<a href="..\netdma\nc-netdma-dma-channel-allocate-handler.md">ProviderAllocateDmaChannel</a>
</dt>
</dl>
<p> </p>
<p> </p>
<p><a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [netvista\netvista]:%20NetDmaIsr function%20 RELEASE:%20(11/30/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a></p>
