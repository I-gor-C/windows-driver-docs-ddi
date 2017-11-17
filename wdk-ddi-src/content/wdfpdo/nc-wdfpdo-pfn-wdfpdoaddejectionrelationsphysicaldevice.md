---
UID: NC.wdfpdo.PFN_WDFPDOADDEJECTIONRELATIONSPHYSICALDEVICE
title: PFN_WDFPDOADDEJECTIONRELATIONSPHYSICALDEVICE
author: windows-driver-content
description: 
ms.assetid: 0364cc6f-4e3f-48f6-9ae2-f605b2191a0e
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfpdo.h
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

# PFN_WDFPDOADDEJECTIONRELATIONSPHYSICALDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPDOADDEJECTIONRELATIONSPHYSICALDEVICE PfnWdfpdoaddejectionrelationsphysicaldevice; 

// Definition

WDFAPI PfnWdfpdoaddejectionrelationsphysicaldevice 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PDEVICE_OBJECT PhysicalDevice
)
{...}

PFN_WDFPDOADDEJECTIONRELATIONSPHYSICALDEVICE 


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