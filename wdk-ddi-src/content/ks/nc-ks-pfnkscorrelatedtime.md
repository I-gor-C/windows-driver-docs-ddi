---
UID: NC.ks.PFNKSCORRELATEDTIME
title: PFNKSCORRELATEDTIME
author: windows-driver-content
description: 
ms.assetid: f83ee122-c84e-4bb2-b5de-05cde31bc1c4
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

# PFNKSCORRELATEDTIME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFNKSCORRELATEDTIME Pfnkscorrelatedtime; 

// Definition

LONGLONG Pfnkscorrelatedtime 
(
	PVOID Context
	PLONGLONG SystemTime
)
{...}

PFNKSCORRELATEDTIME 


```

## -parameters

### -param Context: 
### -param SystemTime: 



## -returns

Returns LONGLONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also