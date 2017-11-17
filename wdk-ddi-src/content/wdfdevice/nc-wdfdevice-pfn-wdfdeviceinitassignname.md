---
UID: NC.wdfdevice.PFN_WDFDEVICEINITASSIGNNAME
title: PFN_WDFDEVICEINITASSIGNNAME
author: windows-driver-content
description: 
ms.assetid: ba602902-ee47-4058-8b8b-b7a2294f1f96
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

# PFN_WDFDEVICEINITASSIGNNAME callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITASSIGNNAME PfnWdfdeviceinitassignname; 

// Definition

WDFAPI PfnWdfdeviceinitassignname 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PCUNICODE_STRING DeviceName
)
{...}

PFN_WDFDEVICEINITASSIGNNAME 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param DeviceName: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also