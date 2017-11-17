---
UID: NC.ntpoapi.PROCESSOR_IDLE_HANDLER
title: PROCESSOR_IDLE_HANDLER
author: windows-driver-content
description: 
ms.assetid: a9aea945-6fd8-45c3-a80b-19f3631f0e58
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntpoapi.h
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

# PROCESSOR_IDLE_HANDLER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PROCESSOR_IDLE_HANDLER ProcessorIdleHandler; 

// Definition

NTSTATUS ProcessorIdleHandler 
(
	ULONG_PTR Context
	PPROCESSOR_IDLE_TIMES IdleTimes
)
{...}

PROCESSOR_IDLE_HANDLER 


```

## -parameters

### -param Context: 
### -param IdleTimes: 



## -returns

Returns NTSTATUS that ...
Return STATUS_SUCCESS if the operation succeeds. Otherwise, return an appropriate NTSTATUS Values error code. For more information, see [XREF-LINK:NTSTATUS Values].

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also