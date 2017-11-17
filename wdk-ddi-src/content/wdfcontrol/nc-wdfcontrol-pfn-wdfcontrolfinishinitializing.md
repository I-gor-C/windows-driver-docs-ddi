---
UID: NC.wdfcontrol.PFN_WDFCONTROLFINISHINITIALIZING
title: PFN_WDFCONTROLFINISHINITIALIZING
author: windows-driver-content
description: 
ms.assetid: b6801db6-799c-4d3e-9eda-d3963f82ac18
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfcontrol.h
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

# PFN_WDFCONTROLFINISHINITIALIZING callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFCONTROLFINISHINITIALIZING PfnWdfcontrolfinishinitializing; 

// Definition

WDFAPI PfnWdfcontrolfinishinitializing 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
)
{...}

PFN_WDFCONTROLFINISHINITIALIZING 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also