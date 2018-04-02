---
UID: NF:ndis.NdisMCompleteDmaTransfer
title: NdisMCompleteDmaTransfer macro
author: windows-driver-content
description: The NdisMCompleteDmaTransfer function indicates that a system DMA transfer operation has completed. It resets the system DMA controller in preparation for further DMA transfers.
old-location: netvista\ndismcompletedmatransfer.htm
old-project: netvista
ms.assetid: 12a8062a-6d4b-4757-a076-56aeb5e4e48c
ms.author: windowsdriverdev
ms.date: 3/26/2018
ms.keywords: NdisMCompleteDmaTransfer, NdisMCompleteDmaTransfer macro [Network Drivers Starting with Windows Vista], dma_ref_bd601fef-cf06-42ff-9906-d3bf8edef72f.xml, ndis/NdisMCompleteDmaTransfer, netvista.ndismcompletedmatransfer
ms.prod: windows-hardware
ms.technology: windows-devices
ms.topic: macro
req.header: ndis.h
req.include-header: Ndis.h
req.target-type: Universal
req.target-min-winverclnt: Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisMCompleteDmaTransfer (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisMCompleteDmaTransfer (NDIS   5.1)) in Windows XP.
req.target-min-winversvr: 
req.kmdf-ver: 
req.umdf-ver: 
req.ddi-compliance: Irql_MCO_Function
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
-	NdisMCompleteDmaTransfer
product: Windows
targetos: Windows
req.typenames: NDIS_SHARED_MEMORY_USAGE, *PNDIS_SHARED_MEMORY_USAGE
---


# NdisMCompleteDmaTransfer function
The 
  <b>NdisMCompleteDmaTransfer</b> function indicates that a system DMA transfer operation has completed. It
  resets the system DMA controller in preparation for further DMA transfers.

## Syntax

```
void NdisMCompleteDmaTransfer(
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

<b>NdisMCompleteDmaTransfer</b> must be called with 
    <i>WriteToDevice</i> set to <b>TRUE</b> before the transferred data is considered present in the NIC's memory. 
    <b>NdisMCompleteDmaTransfer</b> must be called with 
    <i>WriteToDevice</i> set to <b>FALSE</b> before the transferred data can be read from host memory.

## Requirements
| &nbsp; | &nbsp; |
| ---- |:---- |
| **Windows version** | Supported for NDIS 6.0 and NDIS 5.1 drivers (see    NdisMCompleteDmaTransfer (NDIS   5.1)) in Windows Vista. Supported for NDIS 5.1 drivers (see    NdisMCompleteDmaTransfer (NDIS   5.1)) in Windows XP.  |
| **Target Platform** | Universal |
| **Header** | ndis.h (include Ndis.h) |
| **IRQL** | "<= DISPATCH_LEVEL" |
| **DDI compliance rules** | Irql_MCO_Function |

## See Also

<a href="https://msdn.microsoft.com/b146fa81-005b-4a6c-962d-4cb023ea790e">MiniportInitializeEx</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563646">NdisMRegisterDmaChannel</a>



<a href="https://msdn.microsoft.com/library/windows/hardware/ff563675">NdisMSetupDmaTransfer</a>