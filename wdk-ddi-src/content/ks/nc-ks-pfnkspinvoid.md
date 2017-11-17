---
UID: NC.ks.PFNKSPINVOID
title: PFNKSPINVOID
author: windows-driver-content
description: 
ms.assetid: f3478205-021f-4501-9da4-37c46c3d2cd3
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

# PFNKSPINVOID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSPINVOID Pfnkspinvoid; 

// Definition

void Pfnkspinvoid 
(
	PKSPIN Pin
)
{...}

PFNKSPINVOID 


```

## -parameters

### -param Pin: 



## -returns

Returns void that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also