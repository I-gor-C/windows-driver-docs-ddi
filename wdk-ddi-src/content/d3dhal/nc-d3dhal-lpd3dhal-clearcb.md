---
UID: NC.d3dhal.LPD3DHAL_CLEARCB
title: LPD3DHAL_CLEARCB
author: windows-driver-content
description: 
ms.assetid: efe042da-08d4-40e3-b47f-9e75c68f0e11
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

# LPD3DHAL_CLEARCB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DHAL_CLEARCB Lpd3dhalClearcb; 

// Definition

DWORD Lpd3dhalClearcb 
(
	 LPD3DHAL_CLEARDATA
)
{...}

LPD3DHAL_CLEARCB 


```

## -parameters

### -param LPD3DHAL_CLEARDATA: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also