---
UID: NC.wdfdevice.PFN_WDFDEVICEENQUEUEREQUEST
title: PFN_WDFDEVICEENQUEUEREQUEST
author: windows-driver-content
description: 
ms.assetid: 7573f6f4-ac0f-4b3a-a536-20dcba9f79c4
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

# PFN_WDFDEVICEENQUEUEREQUEST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEENQUEUEREQUEST PfnWdfdeviceenqueuerequest; 

// Definition

WDFAPI PfnWdfdeviceenqueuerequest 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	WDFREQUEST Request
)
{...}

PFN_WDFDEVICEENQUEUEREQUEST 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Request: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also