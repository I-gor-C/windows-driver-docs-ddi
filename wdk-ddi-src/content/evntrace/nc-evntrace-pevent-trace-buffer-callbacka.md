---
UID: NC.evntrace.PEVENT_TRACE_BUFFER_CALLBACKA
title: PEVENT_TRACE_BUFFER_CALLBACKA
author: windows-driver-content
description: 
ms.assetid: 93d7fd89-ab7f-429f-8f3c-6f62458dc8c2
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

# PEVENT_TRACE_BUFFER_CALLBACKA callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PEVENT_TRACE_BUFFER_CALLBACKA PeventTraceBufferCallbacka; 

// Definition

ULONG PeventTraceBufferCallbacka 
(
	PEVENT_TRACE_LOGFILEA Logfile
)
{...}

PEVENT_TRACE_BUFFER_CALLBACKA 


```

## -parameters

### -param Logfile: 



## -returns

Returns ULONG that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also