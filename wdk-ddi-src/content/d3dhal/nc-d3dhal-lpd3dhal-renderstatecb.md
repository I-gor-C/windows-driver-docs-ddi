---
UID: NC.d3dhal.LPD3DHAL_RENDERSTATECB
title: LPD3DHAL_RENDERSTATECB
author: windows-driver-content
description: 
ms.assetid: 1afda3f1-6773-4658-87a0-f4db5acb5729
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

# LPD3DHAL_RENDERSTATECB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DHAL_RENDERSTATECB Lpd3dhalRenderstatecb; 

// Definition

DWORD Lpd3dhalRenderstatecb 
(
	 LPD3DHAL_RENDERSTATEDATA
)
{...}

LPD3DHAL_RENDERSTATECB 


```

## -parameters

### -param LPD3DHAL_RENDERSTATEDATA: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also