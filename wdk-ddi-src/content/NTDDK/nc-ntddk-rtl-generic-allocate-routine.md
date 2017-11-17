---
UID: NC.ntddk.RTL_GENERIC_ALLOCATE_ROUTINE
title: RTL_GENERIC_ALLOCATE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: da10b281-98cc-44d9-93c9-3891ffe639da
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ntddk.h
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

# RTL_GENERIC_ALLOCATE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RTL_GENERIC_ALLOCATE_ROUTINE RtlGenericAllocateRoutine; 

// Definition

PVOID RtlGenericAllocateRoutine 
(
	_RTL_GENERIC_TABLE * Table
	CLONG ByteSize
)
{...}

RTL_GENERIC_ALLOCATE_ROUTINE PRTL_GENERIC_ALLOCATE_ROUTINE


```

## -parameters

### -param Table: 
### -param ByteSize: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also