---
UID: NC.wdffdo.PFN_WDFFDOINITALLOCANDQUERYPROPERTY
title: PFN_WDFFDOINITALLOCANDQUERYPROPERTY
author: windows-driver-content
description: 
ms.assetid: 13d78dc2-fa45-49fe-88ae-25f6048a921d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdffdo.h
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

# PFN_WDFFDOINITALLOCANDQUERYPROPERTY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFFDOINITALLOCANDQUERYPROPERTY PfnWdffdoinitallocandqueryproperty; 

// Definition

WDFAPI PfnWdffdoinitallocandqueryproperty 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	DEVICE_REGISTRY_PROPERTY DeviceProperty
	_Strict_type_match_ POOL_TYPE
	PWDF_OBJECT_ATTRIBUTES PropertyMemoryAttributes
	WDFMEMORY *PropertyMemory
)
{...}

PFN_WDFFDOINITALLOCANDQUERYPROPERTY 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param DeviceProperty: 
### -param POOL_TYPE: 
### -param PropertyMemoryAttributes: 
### -param *PropertyMemory: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also