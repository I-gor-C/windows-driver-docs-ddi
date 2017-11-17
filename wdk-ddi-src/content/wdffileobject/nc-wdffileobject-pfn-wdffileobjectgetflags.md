---
UID: NC.wdffileobject.PFN_WDFFILEOBJECTGETFLAGS
title: PFN_WDFFILEOBJECTGETFLAGS
author: windows-driver-content
description: 
ms.assetid: 8f35e846-fd8f-4a6a-8981-e5f988dd970d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdffileobject.h
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

# PFN_WDFFILEOBJECTGETFLAGS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFFILEOBJECTGETFLAGS PfnWdffileobjectgetflags; 

// Definition

WDFAPI PfnWdffileobjectgetflags 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFFILEOBJECT FileObject
)
{...}

PFN_WDFFILEOBJECTGETFLAGS 


```

## -parameters

### -param DriverGlobals: 
### -param FileObject: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also