---
UID: NC.d3dhal.LPD3DHAL_TEXTUREDESTROYCB
title: LPD3DHAL_TEXTUREDESTROYCB
author: windows-driver-content
description: 
ms.assetid: cf1a178d-2147-4614-9325-3f3ef412f4c9
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

# LPD3DHAL_TEXTUREDESTROYCB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DHAL_TEXTUREDESTROYCB Lpd3dhalTexturedestroycb; 

// Definition

DWORD Lpd3dhalTexturedestroycb 
(
	 LPD3DHAL_TEXTUREDESTROYDATA
)
{...}

LPD3DHAL_TEXTUREDESTROYCB 


```

## -parameters

### -param LPD3DHAL_TEXTUREDESTROYDATA: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also