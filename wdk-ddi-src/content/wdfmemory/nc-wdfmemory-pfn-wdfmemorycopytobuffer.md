---
UID: NC.wdfmemory.PFN_WDFMEMORYCOPYTOBUFFER
title: PFN_WDFMEMORYCOPYTOBUFFER
author: windows-driver-content
description: 
ms.assetid: f5a4a847-3b7a-45a8-b0c7-66082f4abbf6
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

# PFN_WDFMEMORYCOPYTOBUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFMEMORYCOPYTOBUFFER PfnWdfmemorycopytobuffer; 

// Definition

WDFAPI PfnWdfmemorycopytobuffer 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFMEMORY SourceMemory
	size_t SourceOffset
	PVOID Buffer
	size_t NumBytesToCopyTo
)
{...}

PFN_WDFMEMORYCOPYTOBUFFER 


```

## -parameters

### -param DriverGlobals: 
### -param SourceMemory: 
### -param SourceOffset: 
### -param Buffer: 
### -param NumBytesToCopyTo: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also