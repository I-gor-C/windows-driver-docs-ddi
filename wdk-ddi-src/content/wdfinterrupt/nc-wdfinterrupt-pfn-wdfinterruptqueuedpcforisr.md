---
UID: NC.wdfinterrupt.PFN_WDFINTERRUPTQUEUEDPCFORISR
title: *PFN_WDFINTERRUPTQUEUEDPCFORISR
author: windows-driver-content
description: 
ms.assetid: 89c042da-55e5-4e11-a46f-1356542e0d38
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfinterrupt.h
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

# *PFN_WDFINTERRUPTQUEUEDPCFORISR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

*PFN_WDFINTERRUPTQUEUEDPCFORISR *PfnWdfinterruptqueuedpcforisr; 

// Definition

BOOLEAN *PfnWdfinterruptqueuedpcforisr 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFINTERRUPT Interrupt
)
{...}

*PFN_WDFINTERRUPTQUEUEDPCFORISR 


```

## -parameters

### -param DriverGlobals: 
### -param Interrupt: 



## -returns

Returns BOOLEAN that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also