---
UID: NC.wdfdevice.PFN_WDFDEVICEALLOCANDQUERYPROPERTY
title: PFN_WDFDEVICEALLOCANDQUERYPROPERTY
author: windows-driver-content
description: 
ms.assetid: 6aace1fc-d8f6-4117-a5c0-d51310e9ae67
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

# PFN_WDFDEVICEALLOCANDQUERYPROPERTY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEALLOCANDQUERYPROPERTY PfnWdfdeviceallocandqueryproperty; 

// Definition

WDFAPI PfnWdfdeviceallocandqueryproperty 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	DEVICE_REGISTRY_PROPERTY DeviceProperty
	_Strict_type_match_ POOL_TYPE
	PWDF_OBJECT_ATTRIBUTES PropertyMemoryAttributes
	WDFMEMORY *PropertyMemory
)
{...}

PFN_WDFDEVICEALLOCANDQUERYPROPERTY 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param DeviceProperty: 
### -param POOL_TYPE: 
### -param PropertyMemoryAttributes: 
### -param *PropertyMemory: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also