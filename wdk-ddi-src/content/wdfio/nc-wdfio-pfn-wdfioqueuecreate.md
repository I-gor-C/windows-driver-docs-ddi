---
UID: NC.wdfio.PFN_WDFIOQUEUECREATE
title: PFN_WDFIOQUEUECREATE
author: windows-driver-content
description: 
ms.assetid: 43dc2685-7096-4ca5-aa29-942071bd90ca
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

# PFN_WDFIOQUEUECREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOQUEUECREATE PfnWdfioqueuecreate; 

// Definition

WDFAPI PfnWdfioqueuecreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_IO_QUEUE_CONFIG Config
	PWDF_OBJECT_ATTRIBUTES QueueAttributes
	WDFQUEUE *Queue
)
{...}

PFN_WDFIOQUEUECREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Config: 
### -param QueueAttributes: 
### -param *Queue: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also