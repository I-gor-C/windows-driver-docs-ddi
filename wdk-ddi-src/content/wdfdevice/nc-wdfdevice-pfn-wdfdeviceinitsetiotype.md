---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETIOTYPE
title: PFN_WDFDEVICEINITSETIOTYPE
author: windows-driver-content
description: 
ms.assetid: 15378e72-342f-4f57-8f34-f5d3f08a48e9
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

# PFN_WDFDEVICEINITSETIOTYPE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETIOTYPE PfnWdfdeviceinitsetiotype; 

// Definition

WDFAPI PfnWdfdeviceinitsetiotype 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	WDF_DEVICE_IO_TYPE IoType
)
{...}

PFN_WDFDEVICEINITSETIOTYPE 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param IoType: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also