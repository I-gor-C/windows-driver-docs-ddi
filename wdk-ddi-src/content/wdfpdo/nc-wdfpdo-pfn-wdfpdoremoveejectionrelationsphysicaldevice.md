---
UID: NC.wdfpdo.PFN_WDFPDOREMOVEEJECTIONRELATIONSPHYSICALDEVICE
title: PFN_WDFPDOREMOVEEJECTIONRELATIONSPHYSICALDEVICE
author: windows-driver-content
description: 
ms.assetid: ff12959b-87af-4c3e-bb2c-c25f3f16dabd
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

# PFN_WDFPDOREMOVEEJECTIONRELATIONSPHYSICALDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPDOREMOVEEJECTIONRELATIONSPHYSICALDEVICE PfnWdfpdoremoveejectionrelationsphysicaldevice; 

// Definition

WDFAPI PfnWdfpdoremoveejectionrelationsphysicaldevice 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PDEVICE_OBJECT PhysicalDevice
)
{...}

PFN_WDFPDOREMOVEEJECTIONRELATIONSPHYSICALDEVICE 


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