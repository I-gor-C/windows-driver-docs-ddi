---
UID: NC.dbghelp.PSYMBOL_FUNCENTRY_CALLBACK
title: PSYMBOL_FUNCENTRY_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 5ee46479-0fbd-433f-b015-26703fff84f0
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

# PSYMBOL_FUNCENTRY_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOL_FUNCENTRY_CALLBACK PsymbolFuncentryCallback; 

// Definition

PVOID PsymbolFuncentryCallback 
(
	HANDLE hProcess
	DWORD AddrBase
	PVOID UserContext
)
{...}

PSYMBOL_FUNCENTRY_CALLBACK 


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