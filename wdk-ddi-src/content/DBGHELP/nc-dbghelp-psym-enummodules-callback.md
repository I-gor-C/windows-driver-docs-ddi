---
UID: NC.dbghelp.PSYM_ENUMMODULES_CALLBACK
title: PSYM_ENUMMODULES_CALLBACK
author: windows-driver-content
description: 
ms.assetid: ddae0358-0e8e-45fb-ab5c-9ad15d52c905
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

# PSYM_ENUMMODULES_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYM_ENUMMODULES_CALLBACK PsymEnummodulesCallback; 

// Definition

BOOL PsymEnummodulesCallback 
(
	PCSTR ModuleName
	ULONG BaseOfDll
	PVOID UserContext
)
{...}

PSYM_ENUMMODULES_CALLBACK 


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