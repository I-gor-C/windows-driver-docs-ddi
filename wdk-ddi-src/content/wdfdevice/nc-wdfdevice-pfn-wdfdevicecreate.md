---
UID: NC.wdfdevice.PFN_WDFDEVICECREATE
title: PFN_WDFDEVICECREATE
author: windows-driver-content
description: 
ms.assetid: 3b2606b6-4b72-4039-ad3c-e46223a12dc4
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

# PFN_WDFDEVICECREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICECREATE PfnWdfdevicecreate; 

// Definition

WDFAPI PfnWdfdevicecreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT *DeviceInit
	PWDF_OBJECT_ATTRIBUTES DeviceAttributes
	WDFDEVICE *Device
)
{...}

PFN_WDFDEVICECREATE 


```

## -parameters

### -param DriverGlobals: 
### -param *DeviceInit: 
### -param DeviceAttributes: 
### -param *Device: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also