---
UID: NC.wdfdevice.PFN_WDFDEVICEGETDEVICEPOWERPOLICYSTATE
title: PFN_WDFDEVICEGETDEVICEPOWERPOLICYSTATE
author: windows-driver-content
description: 
ms.assetid: 523b37e8-e3a6-4276-855f-e971df4c72ef
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

# PFN_WDFDEVICEGETDEVICEPOWERPOLICYSTATE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEGETDEVICEPOWERPOLICYSTATE PfnWdfdevicegetdevicepowerpolicystate; 

// Definition

WDFAPI PfnWdfdevicegetdevicepowerpolicystate 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
)
{...}

PFN_WDFDEVICEGETDEVICEPOWERPOLICYSTATE 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also