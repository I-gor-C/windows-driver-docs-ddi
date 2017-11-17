---
UID: NC.ucxcontroller.PFN_UCXIODEVICECONTROL
title: PFN_UCXIODEVICECONTROL
author: windows-driver-content
description: 
ms.assetid: 624280a6-aa91-409d-8d61-d416234e091d
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: ucxcontroller.h
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

# PFN_UCXIODEVICECONTROL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_UCXIODEVICECONTROL PfnUcxiodevicecontrol; 

// Definition

WDFAPI PfnUcxiodevicecontrol 
(
	PUCX_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	WDFREQUEST Request
	size_t OutputBufferLength
	size_t InputBufferLength
	ULONG IoControlCode
)
{...}

PFN_UCXIODEVICECONTROL 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Request: 
### -param OutputBufferLength: 
### -param InputBufferLength: 
### -param IoControlCode: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also