---
UID: NC.ks.PFNKSPINPOWER
title: PFNKSPINPOWER
author: windows-driver-content
description: 
ms.assetid: 4c8e2951-0b27-4bc3-8c58-5f55edaaecb4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ks.h
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

# PFNKSPINPOWER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSPINPOWER Pfnkspinpower; 

// Definition

void Pfnkspinpower 
(
	PKSPIN Pin
	DEVICE_POWER_STATE State
)
{...}

PFNKSPINPOWER 


```

## -parameters

### -param Pin: 
### -param State: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also