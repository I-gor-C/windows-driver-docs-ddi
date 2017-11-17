---
UID: NC.ks.PFNKSPINRESOLUTION
title: PFNKSPINRESOLUTION
author: windows-driver-content
description: 
ms.assetid: 752b5818-0d64-4709-882d-0cf065769614
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

# PFNKSPINRESOLUTION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSPINRESOLUTION Pfnkspinresolution; 

// Definition

void Pfnkspinresolution 
(
	PKSPIN Pin
	PKSRESOLUTION Resolution
)
{...}

PFNKSPINRESOLUTION 


```

## -parameters

### -param Pin: 
### -param Resolution: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also