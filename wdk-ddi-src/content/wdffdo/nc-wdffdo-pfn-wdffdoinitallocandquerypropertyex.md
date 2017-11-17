---
UID: NC.wdffdo.PFN_WDFFDOINITALLOCANDQUERYPROPERTYEX
title: PFN_WDFFDOINITALLOCANDQUERYPROPERTYEX
author: windows-driver-content
description: 
ms.assetid: 0429cff0-a887-4179-b77b-2ac6e3e3a2bf
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

# PFN_WDFFDOINITALLOCANDQUERYPROPERTYEX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFFDOINITALLOCANDQUERYPROPERTYEX PfnWdffdoinitallocandquerypropertyex; 

// Definition

WDFAPI PfnWdffdoinitallocandquerypropertyex 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PWDF_DEVICE_PROPERTY_DATA DeviceProperty
	_Strict_type_match_ POOL_TYPE
	PWDF_OBJECT_ATTRIBUTES PropertyMemoryAttributes
	WDFMEMORY *PropertyMemory
	PDEVPROPTYPE Type
)
{...}

PFN_WDFFDOINITALLOCANDQUERYPROPERTYEX 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
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