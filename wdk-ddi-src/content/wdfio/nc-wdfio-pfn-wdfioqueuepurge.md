---
UID: NC.wdfio.PFN_WDFIOQUEUEPURGE
title: PFN_WDFIOQUEUEPURGE
author: windows-driver-content
description: 
ms.assetid: 1ba50fbd-ed23-411c-bcb3-5b9fad450e9d
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

# PFN_WDFIOQUEUEPURGE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOQUEUEPURGE PfnWdfioqueuepurge; 

// Definition

WDFAPI PfnWdfioqueuepurge 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFQUEUE Queue
	PFN_WDF_IO_QUEUE_STATE PurgeComplete
	WDFCONTEXT Context
)
{...}

PFN_WDFIOQUEUEPURGE 


```

## -parameters

### -param DriverGlobals: 
### -param Queue: 
### -param PurgeComplete: 
### -param Context: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also