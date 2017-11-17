---
UID: NC.wdfiotarget.PFN_WDFIOTARGETQUERYTARGETPROPERTY
title: PFN_WDFIOTARGETQUERYTARGETPROPERTY
author: windows-driver-content
description: 
ms.assetid: ff3b4dd9-2c0f-4914-91dd-c8075457ce91
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

# PFN_WDFIOTARGETQUERYTARGETPROPERTY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFIOTARGETQUERYTARGETPROPERTY PfnWdfiotargetquerytargetproperty; 

// Definition

WDFAPI PfnWdfiotargetquerytargetproperty 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFIOTARGET IoTarget
	DEVICE_REGISTRY_PROPERTY DeviceProperty
	ULONG BufferLength
	PVOID PropertyBuffer
	PULONG ResultLength
)
{...}

PFN_WDFIOTARGETQUERYTARGETPROPERTY 


```

## -parameters

### -param DriverGlobals: 
### -param IoTarget: 
### -param DeviceProperty: 
### -param BufferLength: 
### -param PropertyBuffer: 
### -param ResultLength: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also