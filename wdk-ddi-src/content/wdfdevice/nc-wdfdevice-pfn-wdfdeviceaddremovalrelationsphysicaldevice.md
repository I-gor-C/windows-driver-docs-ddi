---
UID: NC.wdfdevice.PFN_WDFDEVICEADDREMOVALRELATIONSPHYSICALDEVICE
title: PFN_WDFDEVICEADDREMOVALRELATIONSPHYSICALDEVICE
author: windows-driver-content
description: 
ms.assetid: 0e921578-7ff3-444c-ad24-b0dad5902c49
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

# PFN_WDFDEVICEADDREMOVALRELATIONSPHYSICALDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEADDREMOVALRELATIONSPHYSICALDEVICE PfnWdfdeviceaddremovalrelationsphysicaldevice; 

// Definition

WDFAPI PfnWdfdeviceaddremovalrelationsphysicaldevice 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PDEVICE_OBJECT PhysicalDevice
)
{...}

PFN_WDFDEVICEADDREMOVALRELATIONSPHYSICALDEVICE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param PhysicalDevice: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also