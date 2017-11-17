---
UID: NC.dbghelp.PFUNCTION_TABLE_ACCESS_ROUTINE
title: PFUNCTION_TABLE_ACCESS_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 6185f83d-97f5-4f09-86d0-edc7dfc76eb2
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

# PFUNCTION_TABLE_ACCESS_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFUNCTION_TABLE_ACCESS_ROUTINE PfunctionTableAccessRoutine; 

// Definition

PVOID PfunctionTableAccessRoutine 
(
	HANDLE hProcess
	DWORD AddrBase
)
{...}

PFUNCTION_TABLE_ACCESS_ROUTINE 


```

## -parameters

### -param hProcess: 
### -param AddrBase: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also