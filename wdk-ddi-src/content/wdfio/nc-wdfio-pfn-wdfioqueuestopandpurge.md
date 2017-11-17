---
UID: NC.wdfio.PFN_WDFIOQUEUESTOPANDPURGE
title: PFN_WDFIOQUEUESTOPANDPURGE
author: windows-driver-content
description: 
ms.assetid: 7452bf1d-ff93-4b46-9507-7e40fcce938d
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

# PFN_WDFIOQUEUESTOPANDPURGE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOQUEUESTOPANDPURGE PfnWdfioqueuestopandpurge; 

// Definition

WDFAPI PfnWdfioqueuestopandpurge 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFQUEUE Queue
	PFN_WDF_IO_QUEUE_STATE StopAndPurgeComplete
	WDFCONTEXT Context
)
{...}

PFN_WDFIOQUEUESTOPANDPURGE 


```

## -parameters

### -param DriverGlobals: 
### -param Queue: 
### -param StopAndPurgeComplete: 
### -param Context: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also