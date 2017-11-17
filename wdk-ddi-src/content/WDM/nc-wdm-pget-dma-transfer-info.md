---
UID: NC.wdm.PGET_DMA_TRANSFER_INFO
title: PGET_DMA_TRANSFER_INFO
author: windows-driver-content
description: 
ms.assetid: bb0f773a-d6cc-416e-bbab-e5069a247f27
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdm.h
req.include-header:
req.target-type:
req.target-min-winverclnt:
req.target-min-winversvr:
req.kmdf-ver:
req.umdf-ver:
req.lib:
req.dll:
req.irql: 
req.ddi-compliance:
req.alt-api:
req.alt-loc:
req.unicode-ansi:
req.idl:
req.max-support:
req.namespace:
req.assembly:
req.type-library:
---

# PGET_DMA_TRANSFER_INFO callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_DMA_TRANSFER_INFO PgetDmaTransferInfo; 

// Definition

NTSTATUS PgetDmaTransferInfo 
(
	PDMA_ADAPTER DmaAdapter
	PMDL Mdl
	ULONGLONG Offset
	ULONG Length
	BOOLEAN WriteOnly
	PDMA_TRANSFER_INFO TransferInfo
)
{...}

PGET_DMA_TRANSFER_INFO 


```

## -parameters

### -param DmaAdapter: 
### -param Mdl: 
### -param Offset: 
### -param Length: 
### -param WriteOnly: 
### -param TransferInfo: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also