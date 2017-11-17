---
UID: NC.dbghelp.PFUNCTION_TABLE_ACCESS_ROUTINE64
title: PFUNCTION_TABLE_ACCESS_ROUTINE64
author: windows-driver-content
description: 
ms.assetid: d2e95de6-2e3b-4f8f-a756-04312cc0284f
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

# PFUNCTION_TABLE_ACCESS_ROUTINE64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFUNCTION_TABLE_ACCESS_ROUTINE64 PfunctionTableAccessRoutine64; 

// Definition

PVOID PfunctionTableAccessRoutine64 
(
	HANDLE ahProcess
	DWORD64 AddrBase
)
{...}

PFUNCTION_TABLE_ACCESS_ROUTINE64 


```

## -parameters

### -param ahProcess: 
### -param AddrBase: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also