---
UID: NC.wdfio.PFN_WDFIOQUEUEGETSTATE
title: PFN_WDFIOQUEUEGETSTATE
author: windows-driver-content
description: 
ms.assetid: cebdc855-f914-411e-a9d3-c8e1197bcee8
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfio.h
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

# PFN_WDFIOQUEUEGETSTATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOQUEUEGETSTATE PfnWdfioqueuegetstate; 

// Definition

WDFAPI PfnWdfioqueuegetstate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFQUEUE Queue
	PULONG QueueRequests
	PULONG DriverRequests
)
{...}

PFN_WDFIOQUEUEGETSTATE 


```

## -parameters

### -param DriverGlobals: 
### -param Queue: 
### -param QueueRequests: 
### -param DriverRequests: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also