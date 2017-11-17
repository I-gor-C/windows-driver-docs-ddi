---
UID: NC.ks.PFNKSPINCANCELTIMER
title: PFNKSPINCANCELTIMER
author: windows-driver-content
description: 
ms.assetid: b28d556f-f534-4d8f-93c6-b483ad889e08
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

# PFNKSPINCANCELTIMER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSPINCANCELTIMER Pfnkspincanceltimer; 

// Definition

BOOLEAN Pfnkspincanceltimer 
(
	PKSPIN Pin
	PKTIMER Timer
)
{...}

PFNKSPINCANCELTIMER 


```

## -parameters

### -param Pin: 
### -param Timer: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also