---
UID: NC.wdfobject.PFN_WDFOBJECTALLOCATECONTEXT
title: PFN_WDFOBJECTALLOCATECONTEXT
author: windows-driver-content
description: 
ms.assetid: 48e24b55-939b-46f7-968a-3a6656879ff2
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

# PFN_WDFOBJECTALLOCATECONTEXT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFOBJECTALLOCATECONTEXT PfnWdfobjectallocatecontext; 

// Definition

WDFAPI PfnWdfobjectallocatecontext 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFOBJECT Handle
	PWDF_OBJECT_ATTRIBUTES ContextAttributes
	PVOID *Context
)
{...}

PFN_WDFOBJECTALLOCATECONTEXT 


```

## -parameters

### -param DriverGlobals: 
### -param Handle: 
### -param ContextAttributes: 
### -param *Context: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also