---
UID: NC.dbghelp.PSYMBOLSERVERPINGPROCWEX
title: PSYMBOLSERVERPINGPROCWEX
author: windows-driver-content
description: 
ms.assetid: 3687409a-d6f4-4144-b617-85e05ee3c270
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

# PSYMBOLSERVERPINGPROCWEX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOLSERVERPINGPROCWEX Psymbolserverpingprocwex; 

// Definition

BOOL Psymbolserverpingprocwex 
(
	 PCWSTR
)
{...}

PSYMBOLSERVERPINGPROCWEX 


```

## -parameters

### -param PCWSTR: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also