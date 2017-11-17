---
UID: NC.wdfdevice.PFN_WDFDEVICEREMOVEDEPENDENTUSAGEDEVICEOBJECT
title: PFN_WDFDEVICEREMOVEDEPENDENTUSAGEDEVICEOBJECT
author: windows-driver-content
description: 
ms.assetid: 3c975ab5-00ea-4f00-aa87-59e938e5efb3
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

# PFN_WDFDEVICEREMOVEDEPENDENTUSAGEDEVICEOBJECT callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEREMOVEDEPENDENTUSAGEDEVICEOBJECT PfnWdfdeviceremovedependentusagedeviceobject; 

// Definition

WDFAPI PfnWdfdeviceremovedependentusagedeviceobject 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PDEVICE_OBJECT DependentDevice
)
{...}

PFN_WDFDEVICEREMOVEDEPENDENTUSAGEDEVICEOBJECT 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param DependentDevice: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also