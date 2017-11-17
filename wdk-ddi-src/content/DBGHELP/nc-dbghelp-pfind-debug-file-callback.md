---
UID: NC.dbghelp.PFIND_DEBUG_FILE_CALLBACK
title: PFIND_DEBUG_FILE_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 9ebe2d64-9645-4359-8a48-4bdd40973586
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

# PFIND_DEBUG_FILE_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFIND_DEBUG_FILE_CALLBACK PfindDebugFileCallback; 

// Definition

BOOL PfindDebugFileCallback 
(
	HANDLE FileHandle
	PCSTR FileName
	PVOID CallerData
)
{...}

PFIND_DEBUG_FILE_CALLBACK 


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