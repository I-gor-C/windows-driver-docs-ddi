---
UID: NC.wdfdmaenabler.PFN_WDFDMAENABLERCREATE
title: PFN_WDFDMAENABLERCREATE
author: windows-driver-content
description: 
ms.assetid: 3d19fbd0-b636-4308-83fa-19a7a4010953
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdmaenabler.h
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

# PFN_WDFDMAENABLERCREATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMAENABLERCREATE PfnWdfdmaenablercreate; 

// Definition

WDFAPI PfnWdfdmaenablercreate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PWDF_DMA_ENABLER_CONFIG Config
	PWDF_OBJECT_ATTRIBUTES Attributes
	WDFDMAENABLER *DmaEnablerHandle
)
{...}

PFN_WDFDMAENABLERCREATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Config: 
### -param Attributes: 
### -param *DmaEnablerHandle: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also