---
UID: NC.wdfdevice.PFN_WDFDEVICEASSIGNPROPERTY
title: PFN_WDFDEVICEASSIGNPROPERTY
author: windows-driver-content
description: 
ms.assetid: 975c20a1-f5d5-4e52-8e0a-93ae0076335a
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

# PFN_WDFDEVICEASSIGNPROPERTY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEASSIGNPROPERTY PfnWdfdeviceassignproperty; 

// Definition

WDFAPI PfnWdfdeviceassignproperty 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_DEVICE_PROPERTY_DATA DeviceProperty
	DEVPROPTYPE Type
	ULONG Size
	PVOID Data
)
{...}

PFN_WDFDEVICEASSIGNPROPERTY 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param DeviceProperty: 
### -param Type: 
### -param Size: 
### -param Data: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also