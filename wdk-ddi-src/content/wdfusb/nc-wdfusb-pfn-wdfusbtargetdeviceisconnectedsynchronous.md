---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICEISCONNECTEDSYNCHRONOUS
title: PFN_WDFUSBTARGETDEVICEISCONNECTEDSYNCHRONOUS
author: windows-driver-content
description: 
ms.assetid: afbb6967-4ee8-4da5-a640-5f3b5f595601
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

# PFN_WDFUSBTARGETDEVICEISCONNECTEDSYNCHRONOUS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICEISCONNECTEDSYNCHRONOUS PfnWdfusbtargetdeviceisconnectedsynchronous; 

// Definition

WDFAPI PfnWdfusbtargetdeviceisconnectedsynchronous 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
)
{...}

PFN_WDFUSBTARGETDEVICEISCONNECTEDSYNCHRONOUS 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also