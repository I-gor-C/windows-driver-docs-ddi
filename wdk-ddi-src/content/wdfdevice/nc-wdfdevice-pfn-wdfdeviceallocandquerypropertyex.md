---
UID: NC.wdfdevice.PFN_WDFDEVICEALLOCANDQUERYPROPERTYEX
title: PFN_WDFDEVICEALLOCANDQUERYPROPERTYEX
author: windows-driver-content
description: 
ms.assetid: d277b419-be2a-4cc3-948d-89a9044ed4a7
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

# PFN_WDFDEVICEALLOCANDQUERYPROPERTYEX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEALLOCANDQUERYPROPERTYEX PfnWdfdeviceallocandquerypropertyex; 

// Definition

WDFAPI PfnWdfdeviceallocandquerypropertyex 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_DEVICE_PROPERTY_DATA DeviceProperty
	_Strict_type_match_ POOL_TYPE
	PWDF_OBJECT_ATTRIBUTES PropertyMemoryAttributes
	WDFMEMORY *PropertyMemory
	PDEVPROPTYPE Type
)
{...}

PFN_WDFDEVICEALLOCANDQUERYPROPERTYEX 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param DeviceProperty: 
### -param POOL_TYPE: 
### -param PropertyMemoryAttributes: 
### -param *PropertyMemory: 
### -param Type: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also