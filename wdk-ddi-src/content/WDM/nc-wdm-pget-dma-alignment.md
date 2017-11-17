---
UID: NC.wdm.PGET_DMA_ALIGNMENT
title: PGET_DMA_ALIGNMENT
author: windows-driver-content
description: 
ms.assetid: 32b44dc7-3af0-4b50-be05-fcba48130eb8
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

# PGET_DMA_ALIGNMENT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_DMA_ALIGNMENT PgetDmaAlignment; 

// Definition

ULONG PgetDmaAlignment 
(
	PDMA_ADAPTER DmaAdapter
)
{...}

PGET_DMA_ALIGNMENT 


```

## -parameters

### -param DmaAdapter: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also