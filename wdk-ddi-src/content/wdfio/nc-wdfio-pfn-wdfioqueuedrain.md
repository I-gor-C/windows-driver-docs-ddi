---
UID: NC.wdfio.PFN_WDFIOQUEUEDRAIN
title: PFN_WDFIOQUEUEDRAIN
author: windows-driver-content
description: 
ms.assetid: 840c2e4b-a55e-4bb6-bb0a-360b8443eecd
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

# PFN_WDFIOQUEUEDRAIN callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOQUEUEDRAIN PfnWdfioqueuedrain; 

// Definition

WDFAPI PfnWdfioqueuedrain 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFQUEUE Queue
	PFN_WDF_IO_QUEUE_STATE DrainComplete
	WDFCONTEXT Context
)
{...}

PFN_WDFIOQUEUEDRAIN 


```

## -parameters

### -param DriverGlobals: 
### -param Queue: 
### -param DrainComplete: 
### -param Context: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also