---
UID: NC.dbghelp.PGET_MODULE_BASE_ROUTINE64
title: PGET_MODULE_BASE_ROUTINE64
author: windows-driver-content
description: 
ms.assetid: cec02488-28aa-4625-ae34-1012b9bbc108
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

# PGET_MODULE_BASE_ROUTINE64 callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_MODULE_BASE_ROUTINE64 PgetModuleBaseRoutine64; 

// Definition

DWORD64 PgetModuleBaseRoutine64 
(
	HANDLE hProcess
	DWORD64 Address
)
{...}

PGET_MODULE_BASE_ROUTINE64 


```

## -parameters

### -param hProcess: 
### -param Address: 



## -returns

Returns DWORD64 that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also