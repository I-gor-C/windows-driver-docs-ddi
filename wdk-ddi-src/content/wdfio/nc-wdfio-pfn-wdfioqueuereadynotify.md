---
UID: NC.wdfio.PFN_WDFIOQUEUEREADYNOTIFY
title: PFN_WDFIOQUEUEREADYNOTIFY
author: windows-driver-content
description: 
ms.assetid: 5e5669dc-80ef-41f4-9daa-8001b786b7a4
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

# PFN_WDFIOQUEUEREADYNOTIFY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOQUEUEREADYNOTIFY PfnWdfioqueuereadynotify; 

// Definition

WDFAPI PfnWdfioqueuereadynotify 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFQUEUE Queue
	PFN_WDF_IO_QUEUE_STATE QueueReady
	WDFCONTEXT Context
)
{...}

PFN_WDFIOQUEUEREADYNOTIFY 


```

## -parameters

### -param DriverGlobals: 
### -param Queue: 
### -param QueueReady: 
### -param Context: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also