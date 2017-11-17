---
UID: NC.dbghelp.PENUMLOADED_MODULES_CALLBACK
title: PENUMLOADED_MODULES_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 32601dbc-9470-48f5-a6a4-9f84f13d6eea
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

# PENUMLOADED_MODULES_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PENUMLOADED_MODULES_CALLBACK PenumloadedModulesCallback; 

// Definition

BOOL PenumloadedModulesCallback 
(
	PCSTR ModuleName
	ULONG ModuleBase
	ULONG ModuleSize
	PVOID UserContext
)
{...}

PENUMLOADED_MODULES_CALLBACK 


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