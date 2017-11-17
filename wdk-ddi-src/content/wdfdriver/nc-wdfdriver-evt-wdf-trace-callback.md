---
UID: NC.wdfdriver.EVT_WDF_TRACE_CALLBACK
title: EVT_WDF_TRACE_CALLBACK
author: windows-driver-content
description: 
ms.assetid: 9acad71d-5842-496d-bee8-3aa4a0b6e734
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdriver.h
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

# EVT_WDF_TRACE_CALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

EVT_WDF_TRACE_CALLBACK EvtWdfTraceCallback; 

// Definition

NTSTATUS EvtWdfTraceCallback 
(
	UCHAR minorFunction
	PVOID dataPath
	ULONG bufferLength
	PVOID buffer
	PVOID context
	PULONG size
)
{...}

EVT_WDF_TRACE_CALLBACK PFN_WDF_TRACE_CALLBACK


```

## -parameters

### -param minorFunction: 
### -param dataPath: 
### -param bufferLength: 
### -param buffer: 
### -param context: 
### -param size: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also