---
UID: NC.wdfobject.PFN_WDFOBJECTGETTYPEDCONTEXTWORKER
title: PFN_WDFOBJECTGETTYPEDCONTEXTWORKER
author: windows-driver-content
description: 
ms.assetid: 7fb3eccd-5685-4041-83a4-362756deaf43
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

# PFN_WDFOBJECTGETTYPEDCONTEXTWORKER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFOBJECTGETTYPEDCONTEXTWORKER PfnWdfobjectgettypedcontextworker; 

// Definition

WDFAPI PfnWdfobjectgettypedcontextworker 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFOBJECT Handle
	PCWDF_OBJECT_CONTEXT_TYPE_INFO TypeInfo
)
{...}

PFN_WDFOBJECTGETTYPEDCONTEXTWORKER 


```

## -parameters

### -param DriverGlobals: 
### -param Handle: 
### -param TypeInfo: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also