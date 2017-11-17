---
UID: NC.d3dhal.LPD3DHAL_DRAWONEINDEXEDPRIMITIVECB
title: LPD3DHAL_DRAWONEINDEXEDPRIMITIVECB
author: windows-driver-content
description: 
ms.assetid: bbb0e6ff-4f87-4273-bce3-ac2e0d962c3e
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

# LPD3DHAL_DRAWONEINDEXEDPRIMITIVECB callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DHAL_DRAWONEINDEXEDPRIMITIVECB Lpd3dhalDrawoneindexedprimitivecb; 

// Definition

DWORD Lpd3dhalDrawoneindexedprimitivecb 
(
	 LPD3DHAL_DRAWONEINDEXEDPRIMITIVEDATA
)
{...}

LPD3DHAL_DRAWONEINDEXEDPRIMITIVECB 


```

## -parameters

### -param LPD3DHAL_DRAWONEINDEXEDPRIMITIVEDATA: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also