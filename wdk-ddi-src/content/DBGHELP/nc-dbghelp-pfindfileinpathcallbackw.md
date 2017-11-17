---
UID: NC.dbghelp.PFINDFILEINPATHCALLBACKW
title: PFINDFILEINPATHCALLBACKW
author: windows-driver-content
description: 
ms.assetid: 4ac8120c-9b50-4091-8bab-ccd91c51ad9d
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

# PFINDFILEINPATHCALLBACKW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFINDFILEINPATHCALLBACKW Pfindfileinpathcallbackw; 

// Definition

BOOL Pfindfileinpathcallbackw 
(
	PCWSTR filename
	PVOID context
)
{...}

PFINDFILEINPATHCALLBACKW 


```

## -parameters

### -param filename: 
### -param context: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also