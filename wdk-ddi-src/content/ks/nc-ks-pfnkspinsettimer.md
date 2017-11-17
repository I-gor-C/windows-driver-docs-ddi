---
UID: NC.ks.PFNKSPINSETTIMER
title: PFNKSPINSETTIMER
author: windows-driver-content
description: 
ms.assetid: f40e13f1-a861-4e66-b918-d5d04ec8ae26
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

# PFNKSPINSETTIMER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSPINSETTIMER Pfnkspinsettimer; 

// Definition

BOOLEAN Pfnkspinsettimer 
(
	PKSPIN Pin
	PKTIMER Timer
	LARGE_INTEGER DueTime
	PKDPC Dpc
)
{...}

PFNKSPINSETTIMER 


```

## -parameters

### -param Pin: 
### -param Timer: 
### -param DueTime: 
### -param Dpc: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also