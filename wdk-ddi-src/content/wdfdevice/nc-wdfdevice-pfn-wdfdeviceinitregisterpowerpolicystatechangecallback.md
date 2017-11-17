---
UID: NC.wdfdevice.PFN_WDFDEVICEINITREGISTERPOWERPOLICYSTATECHANGECALLBACK
title: PFN_WDFDEVICEINITREGISTERPOWERPOLICYSTATECHANGECALLBACK
author: windows-driver-content
description: 
ms.assetid: 10887c0d-faef-4d72-8848-75a8de670a9a
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

# PFN_WDFDEVICEINITREGISTERPOWERPOLICYSTATECHANGECALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITREGISTERPOWERPOLICYSTATECHANGECALLBACK PfnWdfdeviceinitregisterpowerpolicystatechangecallback; 

// Definition

WDFAPI PfnWdfdeviceinitregisterpowerpolicystatechangecallback 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	WDF_DEVICE_POWER_POLICY_STATE PowerPolicyState
	PFN_WDF_DEVICE_POWER_POLICY_STATE_CHANGE_NOTIFICATION EvtDevicePowerPolicyStateChange
	ULONG CallbackTypes
)
{...}

PFN_WDFDEVICEINITREGISTERPOWERPOLICYSTATECHANGECALLBACK 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param PowerPolicyState: 
### -param EvtDevicePowerPolicyStateChange: 
### -param CallbackTypes: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also