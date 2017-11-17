---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETDEVICETYPE
title: PFN_WDFDEVICEINITSETDEVICETYPE
author: windows-driver-content
description: 
ms.assetid: 5d273455-616b-4b4a-935b-0402abd1fb49
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

# PFN_WDFDEVICEINITSETDEVICETYPE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETDEVICETYPE PfnWdfdeviceinitsetdevicetype; 

// Definition

WDFAPI PfnWdfdeviceinitsetdevicetype 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	DEVICE_TYPE DeviceType
)
{...}

PFN_WDFDEVICEINITSETDEVICETYPE 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param DeviceType: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also