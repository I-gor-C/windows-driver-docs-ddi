---
UID: NC.wdfmemory.PFN_WDFMEMORYCREATEFROMLOOKASIDE
title: PFN_WDFMEMORYCREATEFROMLOOKASIDE
author: windows-driver-content
description: 
ms.assetid: 139087fe-04ba-428c-aa16-a8f872c6a322
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfmemory.h
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

# PFN_WDFMEMORYCREATEFROMLOOKASIDE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFMEMORYCREATEFROMLOOKASIDE PfnWdfmemorycreatefromlookaside; 

// Definition

WDFAPI PfnWdfmemorycreatefromlookaside 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFLOOKASIDE Lookaside
	WDFMEMORY *Memory
)
{...}

PFN_WDFMEMORYCREATEFROMLOOKASIDE 


```

## -parameters

### -param DriverGlobals: 
### -param Lookaside: 
### -param *Memory: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also