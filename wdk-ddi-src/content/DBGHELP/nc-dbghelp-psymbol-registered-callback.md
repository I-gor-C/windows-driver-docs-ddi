---
UID: NC.dbghelp.PSYMBOL_REGISTERED_CALLBACK
title: PSYMBOL_REGISTERED_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 25c1d9f4-5a7d-4d55-8159-d7763212d094
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

# PSYMBOL_REGISTERED_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYMBOL_REGISTERED_CALLBACK PsymbolRegisteredCallback; 

// Definition

BOOL PsymbolRegisteredCallback 
(
	HANDLE hProcess
	ULONG ActionCode
	PVOID CallbackData
	PVOID UserContext
)
{...}

PSYMBOL_REGISTERED_CALLBACK 


```

## -parameters

### -param hProcess: 
### -param ActionCode: 
### -param CallbackData: 
### -param UserContext: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also