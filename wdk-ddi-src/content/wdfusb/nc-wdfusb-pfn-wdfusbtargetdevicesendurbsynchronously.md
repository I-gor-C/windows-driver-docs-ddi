---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICESENDURBSYNCHRONOUSLY
title: PFN_WDFUSBTARGETDEVICESENDURBSYNCHRONOUSLY
author: windows-driver-content
description: 
ms.assetid: e977387a-654f-47ac-b1b5-783ffb7e8667
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

# PFN_WDFUSBTARGETDEVICESENDURBSYNCHRONOUSLY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICESENDURBSYNCHRONOUSLY PfnWdfusbtargetdevicesendurbsynchronously; 

// Definition

WDFAPI PfnWdfusbtargetdevicesendurbsynchronously 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
	WDFREQUEST Request
	PWDF_REQUEST_SEND_OPTIONS RequestOptions
	PURB Urb
)
{...}

PFN_WDFUSBTARGETDEVICESENDURBSYNCHRONOUSLY 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param Request: 
### -param RequestOptions: 
### -param Urb: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also