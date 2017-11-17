---
UID: NC.wdfobject.PFN_WDFOBJECTCONTEXTGETOBJECT
title: PFN_WDFOBJECTCONTEXTGETOBJECT
author: windows-driver-content
description: 
ms.assetid: a6a32a0f-5ea2-4a2b-926f-96dba56d11c4
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

# PFN_WDFOBJECTCONTEXTGETOBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFOBJECTCONTEXTGETOBJECT PfnWdfobjectcontextgetobject; 

// Definition

WDFAPI PfnWdfobjectcontextgetobject 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PVOID ContextPointer
)
{...}

PFN_WDFOBJECTCONTEXTGETOBJECT 


```

## -parameters

### -param DriverGlobals: 
### -param ContextPointer: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also