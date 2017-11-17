---
UID: NC.wdfdevice.PFN_WDFDEVICEASSIGNINTERFACEPROPERTY
title: PFN_WDFDEVICEASSIGNINTERFACEPROPERTY
author: windows-driver-content
description: 
ms.assetid: 5bacbf70-d70f-4bf3-b69c-13d4dc6829ba
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

# PFN_WDFDEVICEASSIGNINTERFACEPROPERTY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEASSIGNINTERFACEPROPERTY PfnWdfdeviceassigninterfaceproperty; 

// Definition

WDFAPI PfnWdfdeviceassigninterfaceproperty 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_DEVICE_INTERFACE_PROPERTY_DATA PropertyData
	DEVPROPTYPE Type
	ULONG BufferLength
	PVOID PropertyBuffer
)
{...}

PFN_WDFDEVICEASSIGNINTERFACEPROPERTY 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param PropertyData: 
### -param Type: 
### -param BufferLength: 
### -param PropertyBuffer: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also