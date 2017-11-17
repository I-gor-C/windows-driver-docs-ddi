---
UID: NC.d3dhal.LPD3DHAL_SETRENDERTARGETCB
title: LPD3DHAL_SETRENDERTARGETCB
author: windows-driver-content
description: 
ms.assetid: 921c6173-974a-442d-a8a5-5ee66f018727
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

# LPD3DHAL_SETRENDERTARGETCB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DHAL_SETRENDERTARGETCB Lpd3dhalSetrendertargetcb; 

// Definition

DWORD Lpd3dhalSetrendertargetcb 
(
	 LPD3DHAL_SETRENDERTARGETDATA
)
{...}

LPD3DHAL_SETRENDERTARGETCB 


```

## -parameters

### -param LPD3DHAL_SETRENDERTARGETDATA: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also