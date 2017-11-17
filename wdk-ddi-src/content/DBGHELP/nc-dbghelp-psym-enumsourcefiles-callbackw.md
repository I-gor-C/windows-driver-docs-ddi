---
UID: NC.dbghelp.PSYM_ENUMSOURCEFILES_CALLBACKW
title: PSYM_ENUMSOURCEFILES_CALLBACKW
author: windows-driver-content
description: 
ms.assetid: bef0b494-0f83-4955-9bd4-5f80a2c2013a
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

# PSYM_ENUMSOURCEFILES_CALLBACKW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PSYM_ENUMSOURCEFILES_CALLBACKW PsymEnumsourcefilesCallbackw; 

// Definition

BOOL PsymEnumsourcefilesCallbackw 
(
	PSOURCEFILEW pSourceFile
	PVOID UserContext
)
{...}

PSYM_ENUMSOURCEFILES_CALLBACKW 


```

## -parameters

### -param pSourceFile: 
### -param UserContext: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also