---
UID: NC.wdfdevice.PFN_WDFDEVICEWDMASSIGNPOWERFRAMEWORKSETTINGS
title: PFN_WDFDEVICEWDMASSIGNPOWERFRAMEWORKSETTINGS
author: windows-driver-content
description: 
ms.assetid: f887c7a2-47ff-4d98-908a-9c7303b6222e
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

# PFN_WDFDEVICEWDMASSIGNPOWERFRAMEWORKSETTINGS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEWDMASSIGNPOWERFRAMEWORKSETTINGS PfnWdfdevicewdmassignpowerframeworksettings; 

// Definition

WDFAPI PfnWdfdevicewdmassignpowerframeworksettings 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_POWER_FRAMEWORK_SETTINGS PowerFrameworkSettings
)
{...}

PFN_WDFDEVICEWDMASSIGNPOWERFRAMEWORKSETTINGS 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param PowerFrameworkSettings: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also