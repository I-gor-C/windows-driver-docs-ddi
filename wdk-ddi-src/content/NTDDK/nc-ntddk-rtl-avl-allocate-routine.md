---
UID: NC.ntddk.RTL_AVL_ALLOCATE_ROUTINE
title: RTL_AVL_ALLOCATE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: e6c19a6d-ffcf-4a01-8f04-bc0e50312dd9
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

# RTL_AVL_ALLOCATE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RTL_AVL_ALLOCATE_ROUTINE RtlAvlAllocateRoutine; 

// Definition

PVOID RtlAvlAllocateRoutine 
(
	_RTL_AVL_TABLE * Table
	CLONG ByteSize
)
{...}

RTL_AVL_ALLOCATE_ROUTINE PRTL_AVL_ALLOCATE_ROUTINE


```

## -parameters

### -param Table: 
### -param ByteSize: 



## -returns

Returns PVOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also