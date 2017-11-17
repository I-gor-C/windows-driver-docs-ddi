---
UID: NC.dbghelp.PSYM_ENUMSYMBOLS_CALLBACKW
title: PSYM_ENUMSYMBOLS_CALLBACKW
author: windows-driver-content
description: 
ms.assetid: 9ffc660e-3a0e-4b61-93fb-32d1e87f0ad5
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

# PSYM_ENUMSYMBOLS_CALLBACKW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYM_ENUMSYMBOLS_CALLBACKW PsymEnumsymbolsCallbackw; 

// Definition

BOOL PsymEnumsymbolsCallbackw 
(
	PCWSTR SymbolName
	ULONG SymbolAddress
	ULONG SymbolSize
	PVOID UserContext
)
{...}

PSYM_ENUMSYMBOLS_CALLBACKW 


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