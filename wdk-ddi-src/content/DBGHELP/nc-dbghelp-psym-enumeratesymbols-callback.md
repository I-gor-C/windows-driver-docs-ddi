---
UID: NC.dbghelp.PSYM_ENUMERATESYMBOLS_CALLBACK
title: PSYM_ENUMERATESYMBOLS_CALLBACK
author: windows-driver-content
description: 
ms.assetid: ae1128c4-6006-4900-8154-88044f168392
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

# PSYM_ENUMERATESYMBOLS_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYM_ENUMERATESYMBOLS_CALLBACK PsymEnumeratesymbolsCallback; 

// Definition

BOOL PsymEnumeratesymbolsCallback 
(
	PSYMBOL_INFO pSymInfo
	ULONG SymbolSize
	PVOID UserContext
)
{...}

PSYM_ENUMERATESYMBOLS_CALLBACK 


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