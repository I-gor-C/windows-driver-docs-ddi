---
UID: NC.dbghelp.PSYM_ENUMERATESYMBOLS_CALLBACKW
title: PSYM_ENUMERATESYMBOLS_CALLBACKW
author: windows-driver-content
description: 
ms.assetid: 2f4e17e0-9dbf-4247-a0d5-50baa14028bb
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

# PSYM_ENUMERATESYMBOLS_CALLBACKW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYM_ENUMERATESYMBOLS_CALLBACKW PsymEnumeratesymbolsCallbackw; 

// Definition

BOOL PsymEnumeratesymbolsCallbackw 
(
	PSYMBOL_INFOW pSymInfo
	ULONG SymbolSize
	PVOID UserContext
)
{...}

PSYM_ENUMERATESYMBOLS_CALLBACKW 


```

## -parameters

### -param pSymInfo: 
### -param SymbolSize: 
### -param UserContext: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also