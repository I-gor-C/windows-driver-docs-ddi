---
UID: NC.dbghelp.PSYMBOLSERVERCALLBACKPROC
title: PSYMBOLSERVERCALLBACKPROC
author: windows-driver-content
description: 
ms.assetid: 3888813f-19b2-44b1-a39f-0316d2304237
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

# PSYMBOLSERVERCALLBACKPROC callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERCALLBACKPROC Psymbolservercallbackproc; 

// Definition

BOOL Psymbolservercallbackproc 
(
	UINT_PTR action
	ULONG64 data
	ULONG64 context
)
{...}

PSYMBOLSERVERCALLBACKPROC 


```

## -parameters

### -param action: 
### -param data: 
### -param context: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also