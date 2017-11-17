---
UID: NC.d3dhal.LPD3DHAL_VALIDATETEXTURESTAGESTATECB
title: LPD3DHAL_VALIDATETEXTURESTAGESTATECB
author: windows-driver-content
description: 
ms.assetid: 7adc3379-c64e-4837-aba3-74b9c93f2c6e
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

# LPD3DHAL_VALIDATETEXTURESTAGESTATECB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DHAL_VALIDATETEXTURESTAGESTATECB Lpd3dhalValidatetexturestagestatecb; 

// Definition

DWORD Lpd3dhalValidatetexturestagestatecb 
(
	 LPD3DHAL_VALIDATETEXTURESTAGESTATEDATA
)
{...}

LPD3DHAL_VALIDATETEXTURESTAGESTATECB 


```

## -parameters

### -param LPD3DHAL_VALIDATETEXTURESTAGESTATEDATA: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also