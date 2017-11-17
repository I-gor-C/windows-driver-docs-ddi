---
UID: NC.wdfdevice.PFN_WDFDEVICESETDEVICESTATE
title: PFN_WDFDEVICESETDEVICESTATE
author: windows-driver-content
description: 
ms.assetid: ac62b856-661d-4cd7-a680-01083df4e3b5
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

# PFN_WDFDEVICESETDEVICESTATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICESETDEVICESTATE PfnWdfdevicesetdevicestate; 

// Definition

WDFAPI PfnWdfdevicesetdevicestate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_DEVICE_STATE DeviceState
)
{...}

PFN_WDFDEVICESETDEVICESTATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param DeviceState: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also