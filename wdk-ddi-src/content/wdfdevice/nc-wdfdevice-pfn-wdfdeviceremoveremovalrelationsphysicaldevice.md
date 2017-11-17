---
UID: NC.wdfdevice.PFN_WDFDEVICEREMOVEREMOVALRELATIONSPHYSICALDEVICE
title: PFN_WDFDEVICEREMOVEREMOVALRELATIONSPHYSICALDEVICE
author: windows-driver-content
description: 
ms.assetid: 836ecf6d-d807-4e0f-bb3c-278142b9123d
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

# PFN_WDFDEVICEREMOVEREMOVALRELATIONSPHYSICALDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEREMOVEREMOVALRELATIONSPHYSICALDEVICE PfnWdfdeviceremoveremovalrelationsphysicaldevice; 

// Definition

WDFAPI PfnWdfdeviceremoveremovalrelationsphysicaldevice 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PDEVICE_OBJECT PhysicalDevice
)
{...}

PFN_WDFDEVICEREMOVEREMOVALRELATIONSPHYSICALDEVICE 


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