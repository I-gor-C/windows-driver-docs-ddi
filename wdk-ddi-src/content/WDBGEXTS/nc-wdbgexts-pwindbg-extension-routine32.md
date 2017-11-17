---
UID: NC.wdbgexts.PWINDBG_EXTENSION_ROUTINE32
title: PWINDBG_EXTENSION_ROUTINE32
author: windows-driver-content
description: 
ms.assetid: a5854099-d020-493c-b33d-3808528f5c86
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

# PWINDBG_EXTENSION_ROUTINE32 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PWINDBG_EXTENSION_ROUTINE32 PwindbgExtensionRoutine32; 

// Definition

VOID PwindbgExtensionRoutine32 
(
	HANDLE hCurrentProcess
	HANDLE hCurrentThread
	ULONG dwCurrentPc
	ULONG dwProcessor
	PCSTR lpArgumentString
)
{...}

PWINDBG_EXTENSION_ROUTINE32 


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