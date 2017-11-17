---
UID: NC.wdfcompanion.PFN_WDFCOMPANIONCREATETASKQUEUE
title: PFN_WDFCOMPANIONCREATETASKQUEUE
author: windows-driver-content
description: 
ms.assetid: f8f9b59d-e210-49b5-ac77-d4eee5432966
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfcompanion.h
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

# PFN_WDFCOMPANIONCREATETASKQUEUE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCOMPANIONCREATETASKQUEUE PfnWdfcompanioncreatetaskqueue; 

// Definition

WDFAPI PfnWdfcompanioncreatetaskqueue 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFCOMPANION Companion
	PWDF_TASK_QUEUE_CONFIG Config
	PWDF_OBJECT_ATTRIBUTES QueueAttributes
	WDFTASKQUEUE *Queue
)
{...}

PFN_WDFCOMPANIONCREATETASKQUEUE 


```

## -parameters

### -param DriverGlobals: 
### -param Companion: 
### -param Config: 
### -param QueueAttributes: 
### -param *Queue: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also