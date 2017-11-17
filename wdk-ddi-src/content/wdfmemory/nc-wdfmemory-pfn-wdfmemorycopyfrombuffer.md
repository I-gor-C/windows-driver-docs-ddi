---
UID: NC.wdfmemory.PFN_WDFMEMORYCOPYFROMBUFFER
title: PFN_WDFMEMORYCOPYFROMBUFFER
author: windows-driver-content
description: 
ms.assetid: 061a2db3-86a9-42ac-b616-b8824495acdb
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

# PFN_WDFMEMORYCOPYFROMBUFFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFMEMORYCOPYFROMBUFFER PfnWdfmemorycopyfrombuffer; 

// Definition

WDFAPI PfnWdfmemorycopyfrombuffer 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFMEMORY DestinationMemory
	size_t DestinationOffset
	PVOID Buffer
	size_t NumBytesToCopyFrom
)
{...}

PFN_WDFMEMORYCOPYFROMBUFFER 


```

## -parameters

### -param DriverGlobals: 
### -param DestinationMemory: 
### -param DestinationOffset: 
### -param Buffer: 
### -param NumBytesToCopyFrom: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also