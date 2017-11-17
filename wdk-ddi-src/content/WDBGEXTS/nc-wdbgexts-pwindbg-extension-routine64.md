---
UID: NC.wdbgexts.PWINDBG_EXTENSION_ROUTINE64
title: PWINDBG_EXTENSION_ROUTINE64
author: windows-driver-content
description: 
ms.assetid: 55be8a06-5487-4408-8f02-59de0c1ce428
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdbgexts.h
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

# PWINDBG_EXTENSION_ROUTINE64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_EXTENSION_ROUTINE64 PwindbgExtensionRoutine64; 

// Definition

VOID PwindbgExtensionRoutine64 
(
	HANDLE hCurrentProcess
	HANDLE hCurrentThread
	ULONG64 dwCurrentPc
	ULONG dwProcessor
	PCSTR lpArgumentString
)
{...}

PWINDBG_EXTENSION_ROUTINE64 


```

## -parameters

### -param hCurrentProcess: 
### -param hCurrentThread: 
### -param dwCurrentPc: 
### -param dwProcessor: 
### -param lpArgumentString: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also