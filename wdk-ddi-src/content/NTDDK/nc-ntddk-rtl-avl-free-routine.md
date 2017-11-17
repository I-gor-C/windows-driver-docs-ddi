---
UID: NC.ntddk.RTL_AVL_FREE_ROUTINE
title: RTL_AVL_FREE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 8ff919c5-49cb-4aa8-928e-4282fae6fd57
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

# RTL_AVL_FREE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RTL_AVL_FREE_ROUTINE RtlAvlFreeRoutine; 

// Definition

VOID RtlAvlFreeRoutine 
(
	_RTL_AVL_TABLE * Table
	__drv_freesMem(Mem)PVOID Buffer
)
{...}

RTL_AVL_FREE_ROUTINE PRTL_AVL_FREE_ROUTINE


```

## -parameters

### -param Table: 
### -param Buffer: 



## -returns

Returns VOID that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also