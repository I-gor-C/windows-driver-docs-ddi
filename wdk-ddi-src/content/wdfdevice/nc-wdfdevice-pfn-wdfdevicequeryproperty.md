---
UID: NC.wdfdevice.PFN_WDFDEVICEQUERYPROPERTY
title: PFN_WDFDEVICEQUERYPROPERTY
author: windows-driver-content
description: 
ms.assetid: a54c58a9-3960-4e02-bed0-df30ef7b3759
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

# PFN_WDFDEVICEQUERYPROPERTY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEQUERYPROPERTY PfnWdfdevicequeryproperty; 

// Definition

WDFAPI PfnWdfdevicequeryproperty 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	DEVICE_REGISTRY_PROPERTY DeviceProperty
	ULONG BufferLength
	PVOID PropertyBuffer
	PULONG ResultLength
)
{...}

PFN_WDFDEVICEQUERYPROPERTY 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param DeviceProperty: 
### -param BufferLength: 
### -param PropertyBuffer: 
### -param ResultLength: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also