---
UID: NC.dbghelp.PENUMLOADED_MODULES_CALLBACK64
title: PENUMLOADED_MODULES_CALLBACK64
author: windows-driver-content
description: 
ms.assetid: 2ed13728-160c-4b3e-a678-d492bcad8b58
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

# PENUMLOADED_MODULES_CALLBACK64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PENUMLOADED_MODULES_CALLBACK64 PenumloadedModulesCallback64; 

// Definition

BOOL PenumloadedModulesCallback64 
(
	PCSTR ModuleName
	DWORD64 ModuleBase
	ULONG ModuleSize
	PVOID UserContext
)
{...}

PENUMLOADED_MODULES_CALLBACK64 


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