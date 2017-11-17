---
UID: NC.dbghelp.PSYMBOL_FUNCENTRY_CALLBACK64
title: PSYMBOL_FUNCENTRY_CALLBACK64
author: windows-driver-content
description: 
ms.assetid: 720bc9ed-59f9-498a-aa05-b0bab0107aaf
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

# PSYMBOL_FUNCENTRY_CALLBACK64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOL_FUNCENTRY_CALLBACK64 PsymbolFuncentryCallback64; 

// Definition

PVOID PsymbolFuncentryCallback64 
(
	HANDLE hProcess
	ULONG64 AddrBase
	ULONG64 UserContext
)
{...}

PSYMBOL_FUNCENTRY_CALLBACK64 


```

## -parameters

### -param hProcess: 
### -param AddrBase: 
### -param UserContext: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also