---
UID: NC.wdfdevice.PFN_WDFDEVICEALLOCANDQUERYINTERFACEPROPERTY
title: PFN_WDFDEVICEALLOCANDQUERYINTERFACEPROPERTY
author: windows-driver-content
description: 
ms.assetid: 535ae3ee-dc7b-4e06-8213-7bc9f64d088d
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

# PFN_WDFDEVICEALLOCANDQUERYINTERFACEPROPERTY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEALLOCANDQUERYINTERFACEPROPERTY PfnWdfdeviceallocandqueryinterfaceproperty; 

// Definition

WDFAPI PfnWdfdeviceallocandqueryinterfaceproperty 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_DEVICE_INTERFACE_PROPERTY_DATA PropertyData
	POOL_TYPE PoolType
	PWDF_OBJECT_ATTRIBUTES PropertyMemoryAttributes
	WDFMEMORY *PropertyMemory
	PDEVPROPTYPE Type
)
{...}

PFN_WDFDEVICEALLOCANDQUERYINTERFACEPROPERTY 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param PropertyData: 
### -param PoolType: 
### -param PropertyMemoryAttributes: 
### -param *PropertyMemory: 
### -param Type: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also