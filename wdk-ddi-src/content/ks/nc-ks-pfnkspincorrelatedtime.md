---
UID: NC.ks.PFNKSPINCORRELATEDTIME
title: PFNKSPINCORRELATEDTIME
author: windows-driver-content
description: 
ms.assetid: ca5c5b2d-9893-4416-9c55-be9850b5e511
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

# PFNKSPINCORRELATEDTIME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSPINCORRELATEDTIME Pfnkspincorrelatedtime; 

// Definition

LONGLONG Pfnkspincorrelatedtime 
(
	PKSPIN Pin
	PLONGLONG SystemTime
)
{...}

PFNKSPINCORRELATEDTIME 


```

## -parameters

### -param Pin: 
### -param SystemTime: 



## -returns

Returns LONGLONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also