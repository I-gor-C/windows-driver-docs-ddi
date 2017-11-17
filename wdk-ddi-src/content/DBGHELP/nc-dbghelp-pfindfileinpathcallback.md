---
UID: NC.dbghelp.PFINDFILEINPATHCALLBACK
title: PFINDFILEINPATHCALLBACK
author: windows-driver-content
description: 
ms.assetid: 06576c19-1781-41fd-9913-2b644fd4569b
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

# PFINDFILEINPATHCALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFINDFILEINPATHCALLBACK Pfindfileinpathcallback; 

// Definition

BOOL Pfindfileinpathcallback 
(
	PCSTR filename
	PVOID context
)
{...}

PFINDFILEINPATHCALLBACK 


```

## -parameters

### -param filename: 
### -param context: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also