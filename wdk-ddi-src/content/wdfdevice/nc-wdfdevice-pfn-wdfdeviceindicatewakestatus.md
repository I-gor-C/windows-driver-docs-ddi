---
UID: NC.wdfdevice.PFN_WDFDEVICEINDICATEWAKESTATUS
title: PFN_WDFDEVICEINDICATEWAKESTATUS
author: windows-driver-content
description: 
ms.assetid: 055ab063-0be3-46cc-b305-890b633be306
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

# PFN_WDFDEVICEINDICATEWAKESTATUS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICEINDICATEWAKESTATUS PfnWdfdeviceindicatewakestatus; 

// Definition

WDFAPI PfnWdfdeviceindicatewakestatus 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	NTSTATUS WaitWakeStatus
)
{...}

PFN_WDFDEVICEINDICATEWAKESTATUS 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param WaitWakeStatus: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also