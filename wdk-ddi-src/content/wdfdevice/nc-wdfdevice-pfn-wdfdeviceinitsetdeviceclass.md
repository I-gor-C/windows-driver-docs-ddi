---
UID: NC.wdfdevice.PFN_WDFDEVICEINITSETDEVICECLASS
title: PFN_WDFDEVICEINITSETDEVICECLASS
author: windows-driver-content
description: 
ms.assetid: c00cde6f-87eb-4c97-a428-3be449e87716
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

# PFN_WDFDEVICEINITSETDEVICECLASS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINITSETDEVICECLASS PfnWdfdeviceinitsetdeviceclass; 

// Definition

WDFAPI PfnWdfdeviceinitsetdeviceclass 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	CONST GUID
)
{...}

PFN_WDFDEVICEINITSETDEVICECLASS 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param GUID: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also