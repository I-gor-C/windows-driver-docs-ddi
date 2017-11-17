---
UID: NC.wdfobject.PFN_WDFOBJECTQUERY
title: PFN_WDFOBJECTQUERY
author: windows-driver-content
description: 
ms.assetid: 73b38c96-e180-4e1f-b9f7-4e015a1076fd
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfobject.h
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

# PFN_WDFOBJECTQUERY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFOBJECTQUERY PfnWdfobjectquery; 

// Definition

WDFAPI PfnWdfobjectquery 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFOBJECT Object
	CONST GUID
	ULONG QueryBufferLength
	PVOID QueryBuffer
)
{...}

PFN_WDFOBJECTQUERY 


```

## -parameters

### -param DriverGlobals: 
### -param Object: 
### -param GUID: 
### -param QueryBufferLength: 
### -param QueryBuffer: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also