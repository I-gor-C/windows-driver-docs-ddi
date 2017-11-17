---
UID: NC.d3dhal.LPD3DHAL_CLEAR2CB
title: LPD3DHAL_CLEAR2CB
author: windows-driver-content
description: 
ms.assetid: 53840f49-a428-429d-a110-056f4a016154
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

# LPD3DHAL_CLEAR2CB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DHAL_CLEAR2CB Lpd3dhalClear2cb; 

// Definition

DWORD Lpd3dhalClear2cb 
(
	 LPD3DHAL_CLEAR2DATA
)
{...}

LPD3DHAL_CLEAR2CB 


```

## -parameters

### -param LPD3DHAL_CLEAR2DATA: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also