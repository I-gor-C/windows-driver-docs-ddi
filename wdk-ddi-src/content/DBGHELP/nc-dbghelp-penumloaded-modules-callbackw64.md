---
UID: NC.dbghelp.PENUMLOADED_MODULES_CALLBACKW64
title: PENUMLOADED_MODULES_CALLBACKW64
author: windows-driver-content
description: 
ms.assetid: 8ca7fd1c-1764-46f9-aba2-24d791a2f87a
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

# PENUMLOADED_MODULES_CALLBACKW64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PENUMLOADED_MODULES_CALLBACKW64 PenumloadedModulesCallbackw64; 

// Definition

BOOL PenumloadedModulesCallbackw64 
(
	PCWSTR ModuleName
	DWORD64 ModuleBase
	ULONG ModuleSize
	PVOID UserContext
)
{...}

PENUMLOADED_MODULES_CALLBACKW64 


```

## -parameters

### -param ModuleName: 
### -param ModuleBase: 
### -param ModuleSize: 
### -param UserContext: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also