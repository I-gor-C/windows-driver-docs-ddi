---
UID: NC.wdfdevice.PFN_WDFDEVICECONFIGUREWDMIRPDISPATCHCALLBACK
title: PFN_WDFDEVICECONFIGUREWDMIRPDISPATCHCALLBACK
author: windows-driver-content
description: 
ms.assetid: 8451687a-5250-48e0-9863-3725392ee5cd
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

# PFN_WDFDEVICECONFIGUREWDMIRPDISPATCHCALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDEVICECONFIGUREWDMIRPDISPATCHCALLBACK PfnWdfdeviceconfigurewdmirpdispatchcallback; 

// Definition

WDFAPI PfnWdfdeviceconfigurewdmirpdispatchcallback 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	WDFDRIVER Driver
	UCHAR MajorFunction
	PFN_WDFDEVICE_WDM_IRP_DISPATCH EvtDeviceWdmIrpDisptach
	WDFCONTEXT DriverContext
)
{...}

PFN_WDFDEVICECONFIGUREWDMIRPDISPATCHCALLBACK 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param Driver: 
### -param MajorFunction: 
### -param EvtDeviceWdmIrpDisptach: 
### -param DriverContext: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also