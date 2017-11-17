---
UID: NC.wdfdevice.PFN_WDFDEVICEINITREGISTERPOWERSTATECHANGECALLBACK
title: PFN_WDFDEVICEINITREGISTERPOWERSTATECHANGECALLBACK
author: windows-driver-content
description: 
ms.assetid: c59619e3-ff2a-48eb-bd46-b73dc75af290
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

# PFN_WDFDEVICEINITREGISTERPOWERSTATECHANGECALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITREGISTERPOWERSTATECHANGECALLBACK PfnWdfdeviceinitregisterpowerstatechangecallback; 

// Definition

WDFAPI PfnWdfdeviceinitregisterpowerstatechangecallback 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	WDF_DEVICE_POWER_STATE PowerState
	PFN_WDF_DEVICE_POWER_STATE_CHANGE_NOTIFICATION EvtDevicePowerStateChange
	ULONG CallbackTypes
)
{...}

PFN_WDFDEVICEINITREGISTERPOWERSTATECHANGECALLBACK 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param PowerState: 
### -param EvtDevicePowerStateChange: 
### -param CallbackTypes: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also