---
UID: NC.wdfdevice.PFN_WDFDEVICEQUERYPROPERTYEX
title: PFN_WDFDEVICEQUERYPROPERTYEX
author: windows-driver-content
description: 
ms.assetid: e9c6eefe-056d-4e5f-aefa-9b0c724f5627
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

# PFN_WDFDEVICEQUERYPROPERTYEX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEQUERYPROPERTYEX PfnWdfdevicequerypropertyex; 

// Definition

WDFAPI PfnWdfdevicequerypropertyex 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_DEVICE_PROPERTY_DATA DeviceProperty
	ULONG BufferLength
	PVOID PropertyBuffer
	PULONG RequiredSize
	PDEVPROPTYPE Type
)
{...}

PFN_WDFDEVICEQUERYPROPERTYEX 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param DeviceProperty: 
### -param BufferLength: 
### -param PropertyBuffer: 
### -param RequiredSize: 
### -param Type: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also