---
UID: NC.wdfdevice.PFN_WDFDEVICESETFAILED
title: PFN_WDFDEVICESETFAILED
author: windows-driver-content
description: 
ms.assetid: ef6bc597-5c44-4f9c-9bfb-a71cfb0caaa1
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

# PFN_WDFDEVICESETFAILED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICESETFAILED PfnWdfdevicesetfailed; 

// Definition

WDFAPI PfnWdfdevicesetfailed 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	WDF_DEVICE_FAILED_ACTION FailedAction
)
{...}

PFN_WDFDEVICESETFAILED 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param FailedAction: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also