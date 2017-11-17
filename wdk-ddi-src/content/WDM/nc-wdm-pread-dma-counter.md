---
UID: NC.wdm.PREAD_DMA_COUNTER
title: PREAD_DMA_COUNTER
author: windows-driver-content
description: 
ms.assetid: e38c0946-3383-4673-8e33-8e4bb8335321
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

# PREAD_DMA_COUNTER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PREAD_DMA_COUNTER PreadDmaCounter; 

// Definition

ULONG PreadDmaCounter 
(
	PDMA_ADAPTER DmaAdapter
)
{...}

PREAD_DMA_COUNTER 


```

## -parameters

### -param DmaAdapter: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also