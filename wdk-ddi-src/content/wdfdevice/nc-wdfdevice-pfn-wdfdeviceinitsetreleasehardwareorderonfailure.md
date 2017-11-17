---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETRELEASEHARDWAREORDERONFAILURE
title: PFN_WDFDEVICEINITSETRELEASEHARDWAREORDERONFAILURE
author: windows-driver-content
description: 
ms.assetid: 0f106b20-1565-4e0e-937a-74476c84ba01
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

# PFN_WDFDEVICEINITSETRELEASEHARDWAREORDERONFAILURE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETRELEASEHARDWAREORDERONFAILURE PfnWdfdeviceinitsetreleasehardwareorderonfailure; 

// Definition

WDFAPI PfnWdfdeviceinitsetreleasehardwareorderonfailure 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	WDF_RELEASE_HARDWARE_ORDER_ON_FAILURE ReleaseHardwareOrderOnFailure
)
{...}

PFN_WDFDEVICEINITSETRELEASEHARDWAREORDERONFAILURE 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param ReleaseHardwareOrderOnFailure: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also