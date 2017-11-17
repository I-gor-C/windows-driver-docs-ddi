---
UID: NC.wdm.PFLUSH_DMA_BUFFER
title: PFLUSH_DMA_BUFFER
author: windows-driver-content
description: 
ms.assetid: bb7bf587-f480-487d-84c8-ed327316ce55
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

# PFLUSH_DMA_BUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFLUSH_DMA_BUFFER PflushDmaBuffer; 

// Definition

NTSTATUS PflushDmaBuffer 
(
	PDMA_ADAPTER DmaAdapter
	PMDL Mdl
	BOOLEAN ReadOperation
)
{...}

PFLUSH_DMA_BUFFER 


```

## -parameters

### -param DmaAdapter: 
### -param Mdl: 
### -param ReadOperation: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also