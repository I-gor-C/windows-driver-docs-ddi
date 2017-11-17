---
UID: NC.d3dhal.LPD3DHAL_DRAWPRIMITIVESCB
title: LPD3DHAL_DRAWPRIMITIVESCB
author: windows-driver-content
description: 
ms.assetid: ddfd986c-1a86-4078-9872-88c5f3759207
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

# LPD3DHAL_DRAWPRIMITIVESCB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DHAL_DRAWPRIMITIVESCB Lpd3dhalDrawprimitivescb; 

// Definition

DWORD Lpd3dhalDrawprimitivescb 
(
	 LPD3DHAL_DRAWPRIMITIVESDATA
)
{...}

LPD3DHAL_DRAWPRIMITIVESCB 


```

## -parameters

### -param LPD3DHAL_DRAWPRIMITIVESDATA: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also