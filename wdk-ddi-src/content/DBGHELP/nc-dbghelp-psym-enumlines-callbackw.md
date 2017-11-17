---
UID: NC.dbghelp.PSYM_ENUMLINES_CALLBACKW
title: PSYM_ENUMLINES_CALLBACKW
author: windows-driver-content
description: 
ms.assetid: 8322acb1-3a75-4f4d-995d-69956e742e4c
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

# PSYM_ENUMLINES_CALLBACKW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYM_ENUMLINES_CALLBACKW PsymEnumlinesCallbackw; 

// Definition

BOOL PsymEnumlinesCallbackw 
(
	PSRCCODEINFOW LineInfo
	PVOID UserContext
)
{...}

PSYM_ENUMLINES_CALLBACKW 


```

## -parameters

### -param LineInfo: 
### -param UserContext: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also