---
UID: NC.ntddk.RTL_AVL_COMPARE_ROUTINE
title: RTL_AVL_COMPARE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 84bac0d6-956d-43d9-8656-642b118ab9d5
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

# RTL_AVL_COMPARE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RTL_AVL_COMPARE_ROUTINE RtlAvlCompareRoutine; 

// Definition

RTL_GENERIC_COMPARE_RESULTS RtlAvlCompareRoutine 
(
	_RTL_AVL_TABLE * Table
	PVOID FirstStruct
	PVOID SecondStruct
)
{...}

RTL_AVL_COMPARE_ROUTINE PRTL_AVL_COMPARE_ROUTINE


```

## -parameters

### -param Table: 
### -param FirstStruct: 
### -param SecondStruct: 



## -returns

Returns RTL_GENERIC_COMPARE_RESULTS that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also