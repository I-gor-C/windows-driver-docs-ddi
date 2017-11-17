---
UID: NC.dbghelp.PSYM_ENUMSYMBOLS_CALLBACK64
title: PSYM_ENUMSYMBOLS_CALLBACK64
author: windows-driver-content
description: 
ms.assetid: d2fb133c-5989-4528-b76d-6d9a8fa384ed
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

# PSYM_ENUMSYMBOLS_CALLBACK64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYM_ENUMSYMBOLS_CALLBACK64 PsymEnumsymbolsCallback64; 

// Definition

BOOL PsymEnumsymbolsCallback64 
(
	PCSTR SymbolName
	DWORD64 SymbolAddress
	ULONG SymbolSize
	PVOID UserContext
)
{...}

PSYM_ENUMSYMBOLS_CALLBACK64 


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