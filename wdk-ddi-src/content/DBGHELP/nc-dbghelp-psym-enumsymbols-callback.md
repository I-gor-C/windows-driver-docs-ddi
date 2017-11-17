---
UID: NC.dbghelp.PSYM_ENUMSYMBOLS_CALLBACK
title: PSYM_ENUMSYMBOLS_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 066bb62b-d190-4e5a-a0dc-49b89e3355b4
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

# PSYM_ENUMSYMBOLS_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYM_ENUMSYMBOLS_CALLBACK PsymEnumsymbolsCallback; 

// Definition

BOOL PsymEnumsymbolsCallback 
(
	PCSTR SymbolName
	ULONG SymbolAddress
	ULONG SymbolSize
	PVOID UserContext
)
{...}

PSYM_ENUMSYMBOLS_CALLBACK 


```

## -parameters

### -param SymbolName: 
### -param SymbolAddress: 
### -param SymbolSize: 
### -param UserContext: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also