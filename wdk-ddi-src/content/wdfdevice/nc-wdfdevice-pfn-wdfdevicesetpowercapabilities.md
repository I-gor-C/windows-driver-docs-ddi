---
UID: NC.wdfdevice.PFN_WDFDEVICESETPOWERCAPABILITIES
title: PFN_WDFDEVICESETPOWERCAPABILITIES
author: windows-driver-content
description: 
ms.assetid: 6e8094f8-4381-4260-97e4-d4a851f07001
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

# PFN_WDFDEVICESETPOWERCAPABILITIES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICESETPOWERCAPABILITIES PfnWdfdevicesetpowercapabilities; 

// Definition

WDFAPI PfnWdfdevicesetpowercapabilities 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_DEVICE_POWER_CAPABILITIES PowerCapabilities
)
{...}

PFN_WDFDEVICESETPOWERCAPABILITIES 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param PowerCapabilities: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also