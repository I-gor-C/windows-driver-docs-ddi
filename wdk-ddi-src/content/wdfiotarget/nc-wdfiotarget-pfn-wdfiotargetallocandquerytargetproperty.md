---
UID: NC.wdfiotarget.PFN_WDFIOTARGETALLOCANDQUERYTARGETPROPERTY
title: PFN_WDFIOTARGETALLOCANDQUERYTARGETPROPERTY
author: windows-driver-content
description: 
ms.assetid: 87857a7e-6480-4902-a8d8-e532936470c6
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfiotarget.h
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

# PFN_WDFIOTARGETALLOCANDQUERYTARGETPROPERTY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETALLOCANDQUERYTARGETPROPERTY PfnWdfiotargetallocandquerytargetproperty; 

// Definition

WDFAPI PfnWdfiotargetallocandquerytargetproperty 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
	DEVICE_REGISTRY_PROPERTY DeviceProperty
	_Strict_type_match_ POOL_TYPE
	PWDF_OBJECT_ATTRIBUTES PropertyMemoryAttributes
	WDFMEMORY *PropertyMemory
)
{...}

PFN_WDFIOTARGETALLOCANDQUERYTARGETPROPERTY 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 
### -param DeviceProperty: 
### -param POOL_TYPE: 
### -param PropertyMemoryAttributes: 
### -param *PropertyMemory: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also