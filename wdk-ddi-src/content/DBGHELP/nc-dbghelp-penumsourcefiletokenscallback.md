---
UID: NC.dbghelp.PENUMSOURCEFILETOKENSCALLBACK
title: PENUMSOURCEFILETOKENSCALLBACK
author: windows-driver-content
description: 
ms.assetid: 41bdd912-2879-4134-ae78-146723dbb6a7
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: dbghelp.h
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

# PENUMSOURCEFILETOKENSCALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PENUMSOURCEFILETOKENSCALLBACK Penumsourcefiletokenscallback; 

// Definition

BOOL Penumsourcefiletokenscallback 
(
	PVOID token
	size_t size
)
{...}

PENUMSOURCEFILETOKENSCALLBACK 


```

## -parameters

### -param token: 
### -param size: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also