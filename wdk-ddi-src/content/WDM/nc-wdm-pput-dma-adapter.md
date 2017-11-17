---
UID: NC.wdm.PPUT_DMA_ADAPTER
title: PPUT_DMA_ADAPTER
author: windows-driver-content
description: 
ms.assetid: 015d9700-4c99-42a8-af1d-4da88e9bdac3
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

# PPUT_DMA_ADAPTER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PPUT_DMA_ADAPTER PputDmaAdapter; 

// Definition

VOID PputDmaAdapter 
(
	PDMA_ADAPTER DmaAdapter
)
{...}

PPUT_DMA_ADAPTER 


```

## -parameters

### -param DmaAdapter: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also