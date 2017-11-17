---
UID: NC.ucxusbdevice.PFN_UCXUSBDEVICECREATE
title: PFN_UCXUSBDEVICECREATE
author: windows-driver-content
description: 
ms.assetid: 32b07b4f-d275-43f1-8505-36e62477eb4b
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxusbdevice.h
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

# PFN_UCXUSBDEVICECREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCXUSBDEVICECREATE PfnUcxusbdevicecreate; 

// Definition

WDFAPI PfnUcxusbdevicecreate 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	UCXCONTROLLER Controller
	PUCXUSBDEVICE_INIT *UsbDeviceInit
	PWDF_OBJECT_ATTRIBUTES Attributes
	UCXUSBDEVICE *UsbDevice
)
{...}

PFN_UCXUSBDEVICECREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Controller: 
### -param *UsbDeviceInit: 
### -param Attributes: 
### -param *UsbDevice: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also