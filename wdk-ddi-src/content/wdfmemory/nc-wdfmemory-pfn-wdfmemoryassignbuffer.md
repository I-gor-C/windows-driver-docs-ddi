---
UID: NC.wdfmemory.PFN_WDFMEMORYASSIGNBUFFER
title: PFN_WDFMEMORYASSIGNBUFFER
author: windows-driver-content
description: 
ms.assetid: b611b119-39bf-4ebc-9839-58cb3b012cf5
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfmemory.h
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

# PFN_WDFMEMORYASSIGNBUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFMEMORYASSIGNBUFFER PfnWdfmemoryassignbuffer; 

// Definition

WDFAPI PfnWdfmemoryassignbuffer 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFMEMORY Memory
	PVOID Buffer
	size_t BufferSize
)
{...}

PFN_WDFMEMORYASSIGNBUFFER 


```

## -parameters

### -param DriverGlobals: 
### -param Memory: 
### -param Buffer: 
### -param BufferSize: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also