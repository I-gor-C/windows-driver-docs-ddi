---
UID: NC.wdm.PFREE_MAP_REGISTERS
title: PFREE_MAP_REGISTERS
author: windows-driver-content
description: The FreeMapRegisters routine releases a set of map registers that were saved from a call to AllocateAdapterChannel.
old-location: kernel\freemapregisters.htm
old-project: kernel
ms.assetid: 0326229f-cf02-4368-bc32-7fbed118714b
ms.author: windowsdriverdev
ms.date: 12/7/2017
ms.keywords: _WDI_TYPE_PMK_NAME, WDI_TYPE_PMK_NAME, *PWDI_TYPE_PMK_NAME
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: callback
req.header: wdm.h
req.include-header: Wdm.h, Ntddk.h, Ntifs.h
req.target-type: Desktop
req.target-min-winverclnt: Available starting with Windows 2000.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.alt-api: FreeMapRegisters
req.alt-loc: wdm.h
req.ddi-compliance: IrqlDispatch, IrqlDispatch(storport)
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: DISPATCH_LEVEL
req.product: Windows 10 or later.
---

# PFREE_MAP_REGISTERS callback



## -description
The <b>FreeMapRegisters</b> routine releases a set of map registers that were saved from a call to <a href="..\wdm\nc-wdm-pallocate_adapter_channel.md">AllocateAdapterChannel</a>. 



## -prototype

````
PFREE_MAP_REGISTERS FreeMapRegisters;

VOID FreeMapRegisters(
  _In_ PDMA_ADAPTER DmaAdapter,
  _In_ PVOID        MapRegisterBase,
  _In_ ULONG        NumberOfMapRegisters
)
{ ... }
````


## -parameters

### -param DmaAdapter [in]

Pointer to the <a href="kernel.dma_adapter">DMA_ADAPTER</a> structure returned by <a href="kernel.iogetdmaadapter">IoGetDmaAdapter</a> that represents the bus-master adapter or DMA controller.


### -param MapRegisterBase [in]

Specifies the map registers allocated for the DMA operation.  The system passes this value  to the driver's <a href="..\wdm\nc-wdm-driver_control.md">AdapterControl</a> routine.


### -param NumberOfMapRegisters [in]

Specifies the number of map registers to be released. This value must match the number specified in an earlier call to <a href="..\wdm\nc-wdm-pallocate_adapter_channel.md">AllocateAdapterChannel</a>.


## -returns
None


## -remarks
<b>FreeMapRegisters</b>
           is not a system routine that can be called directly by name. This routine is only callable by pointer from the address returned in a 
          <a href="kernel.dma_operations">DMA_OPERATIONS</a>
           structure. Drivers obtain the address of this routine by calling <a href="kernel.iogetdmaadapter">IoGetDmaAdapter</a>.

When the driver of a bus-master device has completed the current packet-based DMA transfer request, it calls <b>FreeMapRegisters</b> to release the map registers previously allocated by a call to <a href="..\wdm\nc-wdm-pallocate_adapter_channel.md">AllocateAdapterChannel</a> and retained because its <i>AdapterControl</i> routine returned <b>DeallocateObjectKeepRegisters</b>. The driver must call <b>FreeMapRegisters</b> after calling <a href="..\wdm\nc-wdm-pflush_adapter_buffers.md">FlushAdapterBuffers</a>. 


## -requirements
<table>
<tr>
<th width="30%">
Target platform

</th>
<td width="70%">
<dl>
<dt>Desktop</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
Version

</th>
<td width="70%">
Available starting with Windows 2000.

</td>
</tr>
<tr>
<th width="30%">
Header

</th>
<td width="70%">
<dl>
<dt>Wdm.h (include Wdm.h, Ntddk.h, or Ntifs.h)</dt>
</dl>
</td>
</tr>
<tr>
<th width="30%">
IRQL

</th>
<td width="70%">
DISPATCH_LEVEL

</td>
</tr>
<tr>
<th width="30%">
DDI compliance rules

</th>
<td width="70%">
<a href="devtest.wdm_irqldispatch">IrqlDispatch</a>, <a href="devtest.storport_irqldispatch">IrqlDispatch(storport)</a>
</td>
</tr>
</table>

## -see-also
<dl>
<dt>
<a href="kernel.dma_adapter">DMA_ADAPTER</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-pallocate_adapter_channel.md">AllocateAdapterChannel</a>
</dt>
<dt>
<a href="kernel.iogetdmaadapter">IoGetDmaAdapter</a>
</dt>
<dt>
<a href="..\wdm\nc-wdm-pmap_transfer.md">MapTransfer</a>
</dt>
<dt>
<a href="kernel.dma_operations">DMA_OPERATIONS</a>
</dt>
</dl>
 

 

<a href="mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback [kernel\kernel]:%20PFREE_MAP_REGISTERS callback function%20 RELEASE:%20(12/7/2017)&amp;body=%0A%0APRIVACY STATEMENT%0A%0AWe use your feedback to improve the documentation. We don't use your email address for any other purpose, and we'll remove your email address from our system after the issue that you're reporting is fixed. While we're working to fix this issue, we might send you an email message to ask for more info. Later, we might also send you an email message to let you know that we've addressed your feedback.%0A%0AFor more info about Microsoft's privacy policy, see http://privacy.microsoft.com/en-us/default.aspx." title="Send comments about this topic to Microsoft">Send comments about this topic to Microsoft</a>

