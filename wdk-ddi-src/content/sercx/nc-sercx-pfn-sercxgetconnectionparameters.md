---
UID: NC.sercx.PFN_SERCXGETCONNECTIONPARAMETERS
title: PFN_SERCXGETCONNECTIONPARAMETERS
author: windows-driver-content
description: 
ms.assetid: 9346592f-d198-440d-866a-8997a63af882
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: sercx.h
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

# PFN_SERCXGETCONNECTIONPARAMETERS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCXGETCONNECTIONPARAMETERS PfnSercxgetconnectionparameters; 

// Definition

WDFAPI PfnSercxgetconnectionparameters 
(
	PSER_DRIVER_GLOBALS DriverGlobals
	WDFDEVICE Device
	PVOID *ConnectionParameters
)
{...}

PFN_SERCXGETCONNECTIONPARAMETERS 


```

## -parameters

### -param DriverGlobals: 
### -param Device: 
### -param *ConnectionParameters: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also