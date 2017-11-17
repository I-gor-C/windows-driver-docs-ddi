---
UID: NC.wdfdmaenabler.PFN_WDFDMAENABLERWDMGETDMAADAPTER
title: PFN_WDFDMAENABLERWDMGETDMAADAPTER
author: windows-driver-content
description: 
ms.assetid: a03817b1-29e0-474e-b2bc-1f7fb4cf822e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdmaenabler.h
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

# PFN_WDFDMAENABLERWDMGETDMAADAPTER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMAENABLERWDMGETDMAADAPTER PfnWdfdmaenablerwdmgetdmaadapter; 

// Definition

WDFAPI PfnWdfdmaenablerwdmgetdmaadapter 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMAENABLER DmaEnabler
	WDF_DMA_DIRECTION DmaDirection
)
{...}

PFN_WDFDMAENABLERWDMGETDMAADAPTER 


```

## -parameters

### -param DriverGlobals: 
### -param DmaEnabler: 
### -param DmaDirection: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also