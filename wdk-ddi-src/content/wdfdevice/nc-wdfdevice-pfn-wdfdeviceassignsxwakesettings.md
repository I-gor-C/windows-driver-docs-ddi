---
UID: NC.wdfdevice.PFN_WDFDEVICEASSIGNSXWAKESETTINGS
title: PFN_WDFDEVICEASSIGNSXWAKESETTINGS
author: windows-driver-content
description: 
ms.assetid: 2d24dc91-4ae9-44b0-b19a-c469eb6e369b
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

# PFN_WDFDEVICEASSIGNSXWAKESETTINGS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEASSIGNSXWAKESETTINGS PfnWdfdeviceassignsxwakesettings; 

// Definition

WDFAPI PfnWdfdeviceassignsxwakesettings 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_DEVICE_POWER_POLICY_WAKE_SETTINGS Settings
)
{...}

PFN_WDFDEVICEASSIGNSXWAKESETTINGS 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Settings: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also