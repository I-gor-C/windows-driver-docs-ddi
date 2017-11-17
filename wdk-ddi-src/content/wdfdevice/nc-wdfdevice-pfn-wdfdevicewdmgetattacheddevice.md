---
UID: NC.wdfdevice.PFN_WDFDEVICEWDMGETATTACHEDDEVICE
title: PFN_WDFDEVICEWDMGETATTACHEDDEVICE
author: windows-driver-content
description: 
ms.assetid: 61fb0fd4-93c1-4ec8-8f78-e49b47cef5d7
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

# PFN_WDFDEVICEWDMGETATTACHEDDEVICE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEWDMGETATTACHEDDEVICE PfnWdfdevicewdmgetattacheddevice; 

// Definition

WDFAPI PfnWdfdevicewdmgetattacheddevice 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
)
{...}

PFN_WDFDEVICEWDMGETATTACHEDDEVICE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also