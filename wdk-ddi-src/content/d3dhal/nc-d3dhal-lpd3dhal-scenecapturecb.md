---
UID: NC.d3dhal.LPD3DHAL_SCENECAPTURECB
title: LPD3DHAL_SCENECAPTURECB
author: windows-driver-content
description: 
ms.assetid: ae7bbe51-b57b-4439-9f7c-bbe1f98464da
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dhal.h
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

# LPD3DHAL_SCENECAPTURECB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DHAL_SCENECAPTURECB Lpd3dhalScenecapturecb; 

// Definition

DWORD Lpd3dhalScenecapturecb 
(
	 LPD3DHAL_SCENECAPTUREDATA
)
{...}

LPD3DHAL_SCENECAPTURECB 


```

## -parameters

### -param LPD3DHAL_SCENECAPTUREDATA: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also