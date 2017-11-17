---
UID: NC.wdffdo.PFN_WDFFDOINITQUERYPROPERTY
title: PFN_WDFFDOINITQUERYPROPERTY
author: windows-driver-content
description: 
ms.assetid: 9b024cae-3110-48c5-8fa7-373d3a5d5164
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

# PFN_WDFFDOINITQUERYPROPERTY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFFDOINITQUERYPROPERTY PfnWdffdoinitqueryproperty; 

// Definition

WDFAPI PfnWdffdoinitqueryproperty 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	DEVICE_REGISTRY_PROPERTY DeviceProperty
	ULONG BufferLength
	PVOID PropertyBuffer
	PULONG ResultLength
)
{...}

PFN_WDFFDOINITQUERYPROPERTY 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param DeviceProperty: 
### -param BufferLength: 
### -param PropertyBuffer: 
### -param ResultLength: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also