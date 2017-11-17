---
UID: NC.dbghelp.PSYM_ENUMSYMBOLS_CALLBACK64W
title: PSYM_ENUMSYMBOLS_CALLBACK64W
author: windows-driver-content
description: 
ms.assetid: b790bc6d-64eb-47ba-a190-e8a55679c845
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

# PSYM_ENUMSYMBOLS_CALLBACK64W callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYM_ENUMSYMBOLS_CALLBACK64W PsymEnumsymbolsCallback64w; 

// Definition

BOOL PsymEnumsymbolsCallback64w 
(
	PCWSTR SymbolName
	DWORD64 SymbolAddress
	ULONG SymbolSize
	PVOID UserContext
)
{...}

PSYM_ENUMSYMBOLS_CALLBACK64W 


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