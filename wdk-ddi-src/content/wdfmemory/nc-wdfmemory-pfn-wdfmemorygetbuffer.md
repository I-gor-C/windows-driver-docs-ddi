---
UID: NC.wdfmemory.PFN_WDFMEMORYGETBUFFER
title: PFN_WDFMEMORYGETBUFFER
author: windows-driver-content
description: 
ms.assetid: 9dcb0d03-38cf-4ed1-b0c9-73a6925b70cc
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

# PFN_WDFMEMORYGETBUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFMEMORYGETBUFFER PfnWdfmemorygetbuffer; 

// Definition

WDFAPI PfnWdfmemorygetbuffer 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFMEMORY Memory
	size_t *BufferSize
)
{...}

PFN_WDFMEMORYGETBUFFER 


```

## -parameters

### -param DriverGlobals: 
### -param Memory: 
### -param *BufferSize: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also