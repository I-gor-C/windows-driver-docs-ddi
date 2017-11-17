---
UID: NC.wdfdevice.PFN_WDFDEVICEWDMGETPHYSICALDEVICE
title: PFN_WDFDEVICEWDMGETPHYSICALDEVICE
author: windows-driver-content
description: 
ms.assetid: fc9c83cf-3830-4b41-a410-c7f272042fa0
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

# PFN_WDFDEVICEWDMGETPHYSICALDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEWDMGETPHYSICALDEVICE PfnWdfdevicewdmgetphysicaldevice; 

// Definition

WDFAPI PfnWdfdevicewdmgetphysicaldevice 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
)
{...}

PFN_WDFDEVICEWDMGETPHYSICALDEVICE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also