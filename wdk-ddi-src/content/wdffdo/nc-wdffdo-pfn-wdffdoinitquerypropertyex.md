---
UID: NC.wdffdo.PFN_WDFFDOINITQUERYPROPERTYEX
title: PFN_WDFFDOINITQUERYPROPERTYEX
author: windows-driver-content
description: 
ms.assetid: 2452f3a8-6b14-485e-9189-5b6644e84f71
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

# PFN_WDFFDOINITQUERYPROPERTYEX callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFFDOINITQUERYPROPERTYEX PfnWdffdoinitquerypropertyex; 

// Definition

WDFAPI PfnWdffdoinitquerypropertyex 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PWDF_DEVICE_PROPERTY_DATA DeviceProperty
	ULONG BufferLength
	PVOID PropertyBuffer
	PULONG ResultLength
	PDEVPROPTYPE Type
)
{...}

PFN_WDFFDOINITQUERYPROPERTYEX 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param DeviceProperty: 
### -param BufferLength: 
### -param PropertyBuffer: 
### -param ResultLength: 
### -param Type: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also