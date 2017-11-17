---
UID: NC.d3dhal.LPD3DHAL_TEXTURECREATECB
title: LPD3DHAL_TEXTURECREATECB
author: windows-driver-content
description: 
ms.assetid: 55834924-0106-4527-8865-2c7ba4c143da
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

# LPD3DHAL_TEXTURECREATECB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DHAL_TEXTURECREATECB Lpd3dhalTexturecreatecb; 

// Definition

DWORD Lpd3dhalTexturecreatecb 
(
	 LPD3DHAL_TEXTURECREATEDATA
)
{...}

LPD3DHAL_TEXTURECREATECB 


```

## -parameters

### -param LPD3DHAL_TEXTURECREATEDATA: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also