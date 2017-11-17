---
UID: NC.d3dhal.LPD3DHAL_CONTEXTDESTROYALLCB
title: LPD3DHAL_CONTEXTDESTROYALLCB
author: windows-driver-content
description: 
ms.assetid: 5c487580-a9ea-4d11-98e6-c4172da669c1
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

# LPD3DHAL_CONTEXTDESTROYALLCB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DHAL_CONTEXTDESTROYALLCB Lpd3dhalContextdestroyallcb; 

// Definition

DWORD Lpd3dhalContextdestroyallcb 
(
	 LPD3DHAL_CONTEXTDESTROYALLDATA
)
{...}

LPD3DHAL_CONTEXTDESTROYALLCB 


```

## -parameters

### -param LPD3DHAL_CONTEXTDESTROYALLDATA: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also