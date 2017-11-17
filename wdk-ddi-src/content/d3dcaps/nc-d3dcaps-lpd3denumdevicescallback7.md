---
UID: NC.d3dcaps.LPD3DENUMDEVICESCALLBACK7
title: LPD3DENUMDEVICESCALLBACK7
author: windows-driver-content
description: 
ms.assetid: ed52b250-6b73-4190-87fa-651c711276a5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: d3dcaps.h
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

# LPD3DENUMDEVICESCALLBACK7 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

LPD3DENUMDEVICESCALLBACK7 Lpd3denumdevicescallback7; 

// Definition

HRESULT Lpd3denumdevicescallback7 
(
	LPSTR lpDeviceDescription
	LPSTR lpDeviceName
	 LPD3DDEVICEDESC7
	 LPVOID
)
{...}

LPD3DENUMDEVICESCALLBACK7 


```

## -parameters

### -param lpDeviceDescription: 
### -param lpDeviceName: 
### -param LPD3DDEVICEDESC7: 
### -param LPVOID: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also