---
UID: NF:ndis.NdisMSetupDmaTransfer
title: NdisMSetupDmaTransfer macro
author: windows-driver-content
description: The NdisMSetupDmaTransfer function sets up the host DMA controller for a DMA transfer.
old-location: netvista\ndismsetupdmatransfer.htm
old-project: netvista
ms.assetid: 2a7ebedd-0042-4624-9c9b-721cccfb0c4f
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: NdisMSetupDmaTransfer, NdisMSetupDmaTransfer macro [Network Drivers Starting with Windows Vista], dma_ref_b6de5799-dca5-4c30-aa3a-e20e1eac4f0f.xml, ndis/NdisMSetupDmaTransfer, netvista.ndismsetupdmatransfer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisMSetupDmaTransfer (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisMSetupDmaTransfer (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: Irql_Miniport_Driver_Function
req.unicode-ansi: 
req.idl: 
req.max-support: 
req.namespace: 
req.assembly: 
req.type-library: 
req.lib: 
req.dll: 
req.irql: "<= DISPATCH_LEVEL"
topic_type:
-	APIRef
-	kbSyntax
api_type:
-	HeaderDef
api_location:
-	ndis.h
api_name:
-	NdisMSetupDmaTransfer
product: Windows
targetos: Windows
req.typenames: NDIS_SHARED_MEMORY_USAGE, *PNDIS_SHARED_MEMORY_USAGE
---


# NdisMSetupDmaTransfer function
The 
  <b>NdisMSetupDmaTransfer</b> function sets up the host DMA controller for a DMA transfer.

## Syntax

```
void NdisMSetupDmaTransfer(
   _S,
   _H,
   _B,
   _O,
   _L,
   _M_
);
```

## Parameters

`_S`

TBD

`_H`

TBD

`_B`

TBD

`_O`

TBD

`_L`

TBD

`_M_`

TBD


## Return Value

None

## Remarks

Drivers of subordinate-DMA NICs call 
    <b>NdisMSetupDmaTransfer</b> in response to incoming send requests, for which the driver sets 
    <i>WriteToDevice</i> to <b>TRUE</b>. They set 
    <i>WriteToDevice</i> to <b>FALSE</b> when they transfer received data from the NIC to host memory.

The caller of 
    <b>NdisMSetupDmaTransfer</b> supplies a buffer descriptor mapping the host memory range that is the target
    of the transfer or that contains data for a download operation from the host to the NIC. To specify a
    transfer sized to suit the DMA constraints of the NIC, the caller can set up a subrange to be transferred
    with the 
    <i>Offset</i> and 
    <i>Length</i> parameters if necessary.

The caller must supply a buffer descriptor that specifies the host range into which received data will
    be transferred from the NIC when 
    <i>WriteToDevice</i> is <b>FALSE</b>. Otherwise, the buffer descriptor at 
    <i>Buffer</i> was chained to a packet descriptor input to the miniport driver's 
    <a href="https://msdn.microsoft.com/0bd5966d-66a6-4548-8c84-7cedced2cf40">
    MiniportSendNetBufferLists</a> function.

To improve performance for small transmit requests, such as a send request of less than 256 bytes in
    length, a miniport driver can copy the packet data into an internal staging buffer and pass a
    driver-allocated buffer descriptor mapping that buffer to 
    <b>NdisMSetupDmaTransfer</b>.

On return from 
    <b>NdisMSetupDmaTransfer</b>, the host DMA controller has been programmed for the transfer. The miniport
    driver then programs the NIC for the transfer operation.

When the transfer is complete, the miniport driver must call the 
    <a href="https://msdn.microsoft.com/12a8062a-6d4b-4757-a076-56aeb5e4e48c">
    NdisMCompleteDmaTransfer</a> function.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisMSetupDmaTransfer (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisMSetupDmaTransfer (NDIS   5.1)) in Windows XP.  |
| **Target Platform** | Universal |
| **Header** | ndis.h (include Ndis.h) |
| **IRQL** | "<= DISPATCH_LEVEL" |
| **DDI compliance rules** | Irql_Miniport_Driver_Function |

## See Also

<a href="https://msdn.microsoft.com/0bd5966d-66a6-4548-8c84-7cedced2cf40">MiniportSendNetBufferLists</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563564">NdisMCompleteDmaTransfer</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563646">NdisMRegisterDmaChannel</a>