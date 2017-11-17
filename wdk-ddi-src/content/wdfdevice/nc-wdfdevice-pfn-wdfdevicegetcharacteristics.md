---
UID: NC.wdfdevice.PFN_WDFDEVICEGETCHARACTERISTICS
title: PFN_WDFDEVICEGETCHARACTERISTICS
author: windows-driver-content
description: 
ms.assetid: 7a6dd363-fad8-4a21-a345-748f12dfd2a9
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

# PFN_WDFDEVICEGETCHARACTERISTICS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEGETCHARACTERISTICS PfnWdfdevicegetcharacteristics; 

// Definition

WDFAPI PfnWdfdevicegetcharacteristics 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
)
{...}

PFN_WDFDEVICEGETCHARACTERISTICS 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also