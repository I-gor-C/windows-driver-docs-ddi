---
UID: NC.wdfusb.PFN_WDFUSBTARGETDEVICERETRIEVECURRENTFRAMENUMBER
title: PFN_WDFUSBTARGETDEVICERETRIEVECURRENTFRAMENUMBER
author: windows-driver-content
description: 
ms.assetid: a508f9a1-650b-429d-8ea6-83ee2a512e5b
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

# PFN_WDFUSBTARGETDEVICERETRIEVECURRENTFRAMENUMBER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFUSBTARGETDEVICERETRIEVECURRENTFRAMENUMBER PfnWdfusbtargetdeviceretrievecurrentframenumber; 

// Definition

WDFAPI PfnWdfusbtargetdeviceretrievecurrentframenumber 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFUSBDEVICE UsbDevice
	PULONG CurrentFrameNumber
)
{...}

PFN_WDFUSBTARGETDEVICERETRIEVECURRENTFRAMENUMBER 


```

## -parameters

### -param DriverGlobals: 
### -param UsbDevice: 
### -param CurrentFrameNumber: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also