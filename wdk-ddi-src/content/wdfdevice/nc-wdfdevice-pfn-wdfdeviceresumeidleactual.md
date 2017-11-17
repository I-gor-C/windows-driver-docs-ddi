---
UID: NC.wdfdevice.PFN_WDFDEVICERESUMEIDLEACTUAL
title: PFN_WDFDEVICERESUMEIDLEACTUAL
author: windows-driver-content
description: 
ms.assetid: d822b8b9-a65d-4934-8c0a-dbe526b64a32
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

# PFN_WDFDEVICERESUMEIDLEACTUAL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICERESUMEIDLEACTUAL PfnWdfdeviceresumeidleactual; 

// Definition

WDFAPI PfnWdfdeviceresumeidleactual 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PVOID Tag
	LONG Line
	PCCH File
)
{...}

PFN_WDFDEVICERESUMEIDLEACTUAL 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Tag: 
### -param Line: 
### -param File: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also