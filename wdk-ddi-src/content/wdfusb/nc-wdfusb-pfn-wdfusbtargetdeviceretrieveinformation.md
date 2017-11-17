---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICERETRIEVEINFORMATION
title: PFN_WDFUSBTARGETDEVICERETRIEVEINFORMATION
author: windows-driver-content
description: 
ms.assetid: 9c7cfd66-8bee-4338-9d0c-fd6187f1bc39
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

# PFN_WDFUSBTARGETDEVICERETRIEVEINFORMATION callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICERETRIEVEINFORMATION PfnWdfusbtargetdeviceretrieveinformation; 

// Definition

WDFAPI PfnWdfusbtargetdeviceretrieveinformation 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
	PWDF_USB_DEVICE_INFORMATION Information
)
{...}

PFN_WDFUSBTARGETDEVICERETRIEVEINFORMATION 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param Information: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also