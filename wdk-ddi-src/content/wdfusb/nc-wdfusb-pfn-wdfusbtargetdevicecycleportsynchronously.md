---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICECYCLEPORTSYNCHRONOUSLY
title: PFN_WDFUSBTARGETDEVICECYCLEPORTSYNCHRONOUSLY
author: windows-driver-content
description: 
ms.assetid: c6142fe2-4c5c-477e-9642-70645f8d0877
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

# PFN_WDFUSBTARGETDEVICECYCLEPORTSYNCHRONOUSLY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICECYCLEPORTSYNCHRONOUSLY PfnWdfusbtargetdevicecycleportsynchronously; 

// Definition

WDFAPI PfnWdfusbtargetdevicecycleportsynchronously 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
)
{...}

PFN_WDFUSBTARGETDEVICECYCLEPORTSYNCHRONOUSLY 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also