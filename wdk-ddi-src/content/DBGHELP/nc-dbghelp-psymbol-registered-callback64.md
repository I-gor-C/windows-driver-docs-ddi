---
UID: NC.dbghelp.PSYMBOL_REGISTERED_CALLBACK64
title: PSYMBOL_REGISTERED_CALLBACK64
author: windows-driver-content
description: 
ms.assetid: 53589bea-7c18-4149-b960-0ff73e7d8267
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

# PSYMBOL_REGISTERED_CALLBACK64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOL_REGISTERED_CALLBACK64 PsymbolRegisteredCallback64; 

// Definition

BOOL PsymbolRegisteredCallback64 
(
	HANDLE hProcess
	ULONG ActionCode
	ULONG64 CallbackData
	ULONG64 UserContext
)
{...}

PSYMBOL_REGISTERED_CALLBACK64 


```

## -parameters

### -param hProcess: 
### -param ActionCode: 
### -param CallbackData: 
### -param UserContext: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also