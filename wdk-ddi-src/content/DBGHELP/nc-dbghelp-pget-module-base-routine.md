---
UID: NC.dbghelp.PGET_MODULE_BASE_ROUTINE
title: PGET_MODULE_BASE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: d861798d-ec57-49bf-b296-15ef405e8890
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

# PGET_MODULE_BASE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PGET_MODULE_BASE_ROUTINE PgetModuleBaseRoutine; 

// Definition

DWORD PgetModuleBaseRoutine 
(
	HANDLE hProcess
	DWORD Address
)
{...}

PGET_MODULE_BASE_ROUTINE 


```

## -parameters

### -param hProcess: 
### -param Address: 



## -returns

Returns DWORD that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also