---
UID: NC.d3dhal.LPD3DHAL_TEXTURESWAPCB
title: LPD3DHAL_TEXTURESWAPCB
author: windows-driver-content
description: 
ms.assetid: e986caf6-dd85-4285-baba-3571184d847e
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

# LPD3DHAL_TEXTURESWAPCB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DHAL_TEXTURESWAPCB Lpd3dhalTextureswapcb; 

// Definition

DWORD Lpd3dhalTextureswapcb 
(
	 LPD3DHAL_TEXTURESWAPDATA
)
{...}

LPD3DHAL_TEXTURESWAPCB 


```

## -parameters

### -param LPD3DHAL_TEXTURESWAPDATA: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also