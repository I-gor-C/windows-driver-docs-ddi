---
UID: NC.wdfdevice.PFN_WDFDEVICEQUERYINTERFACEPROPERTY
title: PFN_WDFDEVICEQUERYINTERFACEPROPERTY
author: windows-driver-content
description: 
ms.assetid: c87bdb5f-c8d7-4bc0-a3f4-898ef7a11e84
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

# PFN_WDFDEVICEQUERYINTERFACEPROPERTY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEQUERYINTERFACEPROPERTY PfnWdfdevicequeryinterfaceproperty; 

// Definition

WDFAPI PfnWdfdevicequeryinterfaceproperty 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_DEVICE_INTERFACE_PROPERTY_DATA PropertyData
	ULONG BufferLength
	PVOID PropertyBuffer
	PULONG ResultLength
	PDEVPROPTYPE Type
)
{...}

PFN_WDFDEVICEQUERYINTERFACEPROPERTY 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param PropertyData: 
### -param BufferLength: 
### -param PropertyBuffer: 
### -param ResultLength: 
### -param Type: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also