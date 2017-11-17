---
UID: NC.dbghelp.PFIND_DEBUG_FILE_CALLBACKW
title: PFIND_DEBUG_FILE_CALLBACKW
author: windows-driver-content
description: 
ms.assetid: acb30fe0-9690-4045-8bbf-c056af0faa39
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

# PFIND_DEBUG_FILE_CALLBACKW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFIND_DEBUG_FILE_CALLBACKW PfindDebugFileCallbackw; 

// Definition

BOOL PfindDebugFileCallbackw 
(
	HANDLE FileHandle
	PCWSTR FileName
	PVOID CallerData
)
{...}

PFIND_DEBUG_FILE_CALLBACKW 


```

## -parameters

### -param FileHandle: 
### -param FileName: 
### -param CallerData: 



## -returns

Returns BOOL that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also