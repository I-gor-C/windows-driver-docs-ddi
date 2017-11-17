---
UID: NC.wdm.PGET_DMA_DOMAIN
title: PGET_DMA_DOMAIN
author: windows-driver-content
description: 
ms.assetid: 5fa565ec-b932-4129-926d-15745e4a5964
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

# PGET_DMA_DOMAIN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_DMA_DOMAIN PgetDmaDomain; 

// Definition

HANDLE PgetDmaDomain 
(
	PDMA_ADAPTER DmaAdapter
)
{...}

PGET_DMA_DOMAIN 


```

## -parameters

### -param DmaAdapter: 



## -returns

Returns HANDLE that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also