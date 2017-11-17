---
UID: NC.extsfns.EXT_GET_HANDLE_TRACE
title: EXT_GET_HANDLE_TRACE
author: windows-driver-content
description: 
ms.assetid: d2bf7255-1327-42ac-a739-5f19b2c9e004
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: extsfns.h
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

# EXT_GET_HANDLE_TRACE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EXT_GET_HANDLE_TRACE ExtGetHandleTrace; 

// Definition

HRESULT ExtGetHandleTrace 
(
	PDEBUG_CLIENT Client
	ULONG TraceType
	ULONG StartIndex
	PULONG64 HandleValue
	PULONG64 StackFunctions
	ULONG StackTraceSize
)
{...}

EXT_GET_HANDLE_TRACE 


```

## -parameters

### -param Client: 
### -param TraceType: 
### -param StartIndex: 
### -param HandleValue: 
### -param StackFunctions: 
### -param StackTraceSize: 



## -returns

Returns HRESULT that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also