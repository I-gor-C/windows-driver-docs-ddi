---
UID: NC.ntddk.RTL_GENERIC_COMPARE_ROUTINE
title: RTL_GENERIC_COMPARE_ROUTINE
author: windows-driver-content
description: 
ms.assetid: 4fdeac37-b2ef-463a-9b1d-b9e099e86abc
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

# RTL_GENERIC_COMPARE_ROUTINE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

RTL_GENERIC_COMPARE_ROUTINE RtlGenericCompareRoutine; 

// Definition

RTL_GENERIC_COMPARE_RESULTS RtlGenericCompareRoutine 
(
	_RTL_GENERIC_TABLE * Table
	PVOID FirstStruct
	PVOID SecondStruct
)
{...}

RTL_GENERIC_COMPARE_ROUTINE PRTL_GENERIC_COMPARE_ROUTINE


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