---
UID: NC.evntrace.PEVENT_TRACE_BUFFER_CALLBACKW
title: PEVENT_TRACE_BUFFER_CALLBACKW
author: windows-driver-content
description: 
ms.assetid: 45ce0d34-ea6e-4f50-9971-f646725e4df3
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: evntrace.h
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

# PEVENT_TRACE_BUFFER_CALLBACKW callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PEVENT_TRACE_BUFFER_CALLBACKW PeventTraceBufferCallbackw; 

// Definition

ULONG PeventTraceBufferCallbackw 
(
	PEVENT_TRACE_LOGFILEW Logfile
)
{...}

PEVENT_TRACE_BUFFER_CALLBACKW 


```

## -parameters

### -param Logfile: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also