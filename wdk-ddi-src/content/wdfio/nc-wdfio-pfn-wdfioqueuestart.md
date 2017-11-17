---
UID: NC.wdfio.PFN_WDFIOQUEUESTART
title: PFN_WDFIOQUEUESTART
author: windows-driver-content
description: 
ms.assetid: 9b37f186-4b7a-43d9-b989-79aa7daeef53
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

# PFN_WDFIOQUEUESTART callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOQUEUESTART PfnWdfioqueuestart; 

// Definition

WDFAPI PfnWdfioqueuestart 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFQUEUE Queue
)
{...}

PFN_WDFIOQUEUESTART 


```

## -parameters

### -param DriverGlobals: 
### -param Queue: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also