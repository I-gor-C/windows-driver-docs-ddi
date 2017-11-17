---
UID: NC.wdfworkitem.PFN_WDFWORKITEMENQUEUE
title: PFN_WDFWORKITEMENQUEUE
author: windows-driver-content
description: 
ms.assetid: 76360083-72c4-4bfd-b4df-4b17e7562cd0
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfworkitem.h
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

# PFN_WDFWORKITEMENQUEUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFWORKITEMENQUEUE PfnWdfworkitemenqueue; 

// Definition

WDFAPI PfnWdfworkitemenqueue 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFWORKITEM WorkItem
)
{...}

PFN_WDFWORKITEMENQUEUE 


```

## -parameters

### -param DriverGlobals: 
### -param WorkItem: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also