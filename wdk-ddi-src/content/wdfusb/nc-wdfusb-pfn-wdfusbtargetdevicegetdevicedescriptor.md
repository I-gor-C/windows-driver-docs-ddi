---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICEGETDEVICEDESCRIPTOR
title: PFN_WDFUSBTARGETDEVICEGETDEVICEDESCRIPTOR
author: windows-driver-content
description: 
ms.assetid: 52b922f7-5552-4e9b-8ee7-5c09059f22f9
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

# PFN_WDFUSBTARGETDEVICEGETDEVICEDESCRIPTOR callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICEGETDEVICEDESCRIPTOR PfnWdfusbtargetdevicegetdevicedescriptor; 

// Definition

WDFAPI PfnWdfusbtargetdevicegetdevicedescriptor 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
	PUSB_DEVICE_DESCRIPTOR UsbDeviceDescriptor
)
{...}

PFN_WDFUSBTARGETDEVICEGETDEVICEDESCRIPTOR 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param UsbDeviceDescriptor: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also