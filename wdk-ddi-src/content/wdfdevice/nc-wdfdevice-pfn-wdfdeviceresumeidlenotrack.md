---
UID: NC.wdfdevice.PFN_WDFDEVICERESUMEIDLENOTRACK
title: PFN_WDFDEVICERESUMEIDLENOTRACK
author: windows-driver-content
description: 
ms.assetid: f4e4fe98-acd7-4f6b-93c4-de1baadb4140
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdevice.h
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

# PFN_WDFDEVICERESUMEIDLENOTRACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICERESUMEIDLENOTRACK PfnWdfdeviceresumeidlenotrack; 

// Definition

WDFAPI PfnWdfdeviceresumeidlenotrack 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
)
{...}

PFN_WDFDEVICERESUMEIDLENOTRACK 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also