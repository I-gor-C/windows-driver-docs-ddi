---
UID: NC.wdfdevice.PFN_WDFDEVICEASSIGNS0IDLESETTINGS
title: PFN_WDFDEVICEASSIGNS0IDLESETTINGS
author: windows-driver-content
description: 
ms.assetid: d52b8a39-6991-43de-9465-e14b47813769
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

# PFN_WDFDEVICEASSIGNS0IDLESETTINGS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEASSIGNS0IDLESETTINGS PfnWdfdeviceassigns0idlesettings; 

// Definition

WDFAPI PfnWdfdeviceassigns0idlesettings 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_DEVICE_POWER_POLICY_IDLE_SETTINGS Settings
)
{...}

PFN_WDFDEVICEASSIGNS0IDLESETTINGS 


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