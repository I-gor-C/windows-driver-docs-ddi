---
UID: NC.dbghelp.PSYM_ENUMMODULES_CALLBACKW64
title: PSYM_ENUMMODULES_CALLBACKW64
author: windows-driver-content
description: 
ms.assetid: 2ebc68b0-84dd-4f6e-87ee-be9b3d7cff72
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

# PSYM_ENUMMODULES_CALLBACKW64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYM_ENUMMODULES_CALLBACKW64 PsymEnummodulesCallbackw64; 

// Definition

BOOL PsymEnummodulesCallbackw64 
(
	PCWSTR ModuleName
	DWORD64 BaseOfDll
	PVOID UserContext
)
{...}

PSYM_ENUMMODULES_CALLBACKW64 


```

## -parameters

### -param ModuleName: 
### -param BaseOfDll: 
### -param UserContext: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also