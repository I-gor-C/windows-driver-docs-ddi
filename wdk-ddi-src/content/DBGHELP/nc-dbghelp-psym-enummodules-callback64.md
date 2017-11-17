---
UID: NC.dbghelp.PSYM_ENUMMODULES_CALLBACK64
title: PSYM_ENUMMODULES_CALLBACK64
author: windows-driver-content
description: 
ms.assetid: 89451680-1f2e-4bb8-9ae8-1dbde528f7b2
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

# PSYM_ENUMMODULES_CALLBACK64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYM_ENUMMODULES_CALLBACK64 PsymEnummodulesCallback64; 

// Definition

BOOL PsymEnummodulesCallback64 
(
	PCSTR ModuleName
	DWORD64 BaseOfDll
	PVOID UserContext
)
{...}

PSYM_ENUMMODULES_CALLBACK64 


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