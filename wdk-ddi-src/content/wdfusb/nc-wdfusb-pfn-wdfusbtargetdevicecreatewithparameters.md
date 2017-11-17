---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICECREATEWITHPARAMETERS
title: PFN_WDFUSBTARGETDEVICECREATEWITHPARAMETERS
author: windows-driver-content
description: 
ms.assetid: ef842f1a-088a-4b9c-8daa-e0287364fd36
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfusb.h
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

# PFN_WDFUSBTARGETDEVICECREATEWITHPARAMETERS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICECREATEWITHPARAMETERS PfnWdfusbtargetdevicecreatewithparameters; 

// Definition

WDFAPI PfnWdfusbtargetdevicecreatewithparameters 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_USB_DEVICE_CREATE_CONFIG Config
	PWDF_OBJECT_ATTRIBUTES Attributes
	WDFUSBDEVICE *UsbDevice
)
{...}

PFN_WDFUSBTARGETDEVICECREATEWITHPARAMETERS 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Config: 
### -param Attributes: 
### -param *UsbDevice: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also