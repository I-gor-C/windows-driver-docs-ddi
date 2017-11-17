---
UID: NC.video.PVIDEO_HW_START_DMA
title: PVIDEO_HW_START_DMA
author: windows-driver-content
description: 
ms.assetid: 53858704-6922-4e82-8052-5240e944cd13
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: video.h
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

# PVIDEO_HW_START_DMA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PVIDEO_HW_START_DMA PvideoHwStartDma; 

// Definition

HW_DMA_RETURN PvideoHwStartDma 
(
	PVOID HwDeviceExtension
	PDMA pDma
)
{...}

PVIDEO_HW_START_DMA 


```

## -parameters

### -param HwDeviceExtension: 
### -param pDma: 



## -returns

Returns HW_DMA_RETURN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also