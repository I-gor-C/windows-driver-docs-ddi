---
UID: NC.d3dhal.LPD3DHAL_GETSTATECB
title: LPD3DHAL_GETSTATECB
author: windows-driver-content
description: 
ms.assetid: f350956f-2297-4e12-8c35-fef6094cf813
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

# LPD3DHAL_GETSTATECB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DHAL_GETSTATECB Lpd3dhalGetstatecb; 

// Definition

DWORD Lpd3dhalGetstatecb 
(
	 LPD3DHAL_GETSTATEDATA
)
{...}

LPD3DHAL_GETSTATECB 


```

## -parameters

### -param LPD3DHAL_GETSTATEDATA: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also