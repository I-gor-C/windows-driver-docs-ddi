---
UID: NC.wdfdevice.PFN_WDFDEVICESETSTATICSTOPREMOVE
title: PFN_WDFDEVICESETSTATICSTOPREMOVE
author: windows-driver-content
description: 
ms.assetid: 1f5052b9-54fc-4a0d-96e2-394e46d5fd61
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

# PFN_WDFDEVICESETSTATICSTOPREMOVE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICESETSTATICSTOPREMOVE PfnWdfdevicesetstaticstopremove; 

// Definition

WDFAPI PfnWdfdevicesetstaticstopremove 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	BOOLEAN Stoppable
)
{...}

PFN_WDFDEVICESETSTATICSTOPREMOVE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Stoppable: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also