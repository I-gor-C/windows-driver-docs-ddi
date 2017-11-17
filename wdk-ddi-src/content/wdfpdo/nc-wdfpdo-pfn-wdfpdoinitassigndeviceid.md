---
UID: NC.wdfpdo.PFN_WDFPDOINITASSIGNDEVICEID
title: PFN_WDFPDOINITASSIGNDEVICEID
author: windows-driver-content
description: 
ms.assetid: 137a70f3-4187-427d-bbe0-d8aad59fe309
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

# PFN_WDFPDOINITASSIGNDEVICEID callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFPDOINITASSIGNDEVICEID PfnWdfpdoinitassigndeviceid; 

// Definition

WDFAPI PfnWdfpdoinitassigndeviceid 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	PWDFDEVICE_INIT DeviceInit
	PCUNICODE_STRING DeviceID
)
{...}

PFN_WDFPDOINITASSIGNDEVICEID 


```

## -parameters

### -param DriverGlobals: 
### -param DeviceInit: 
### -param DeviceID: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also