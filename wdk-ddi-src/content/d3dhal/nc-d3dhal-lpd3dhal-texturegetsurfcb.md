---
UID: NC.d3dhal.LPD3DHAL_TEXTUREGETSURFCB
title: LPD3DHAL_TEXTUREGETSURFCB
author: windows-driver-content
description: 
ms.assetid: ec3f63d8-3635-454a-86e9-1fcfd082b79d
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

# LPD3DHAL_TEXTUREGETSURFCB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DHAL_TEXTUREGETSURFCB Lpd3dhalTexturegetsurfcb; 

// Definition

DWORD Lpd3dhalTexturegetsurfcb 
(
	 LPD3DHAL_TEXTUREGETSURFDATA
)
{...}

LPD3DHAL_TEXTUREGETSURFCB 


```

## -parameters

### -param LPD3DHAL_TEXTUREGETSURFDATA: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also