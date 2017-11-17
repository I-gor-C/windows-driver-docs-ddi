---
UID: NC.d3dhal.LPD3DHAL_DRAWONEPRIMITIVECB
title: LPD3DHAL_DRAWONEPRIMITIVECB
author: windows-driver-content
description: 
ms.assetid: e67413a0-a087-48ab-8592-95d9a4f30c73
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

# LPD3DHAL_DRAWONEPRIMITIVECB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DHAL_DRAWONEPRIMITIVECB Lpd3dhalDrawoneprimitivecb; 

// Definition

DWORD Lpd3dhalDrawoneprimitivecb 
(
	 LPD3DHAL_DRAWONEPRIMITIVEDATA
)
{...}

LPD3DHAL_DRAWONEPRIMITIVECB 


```

## -parameters

### -param LPD3DHAL_DRAWONEPRIMITIVEDATA: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also