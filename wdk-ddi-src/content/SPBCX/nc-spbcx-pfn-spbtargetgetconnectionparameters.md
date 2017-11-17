---
UID: NC.spbcx.PFN_SPBTARGETGETCONNECTIONPARAMETERS
title: PFN_SPBTARGETGETCONNECTIONPARAMETERS
author: windows-driver-content
description: 
ms.assetid: 2ec74bd8-7426-4f56-b850-79812ba2dcf4
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: spbcx.h
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

# PFN_SPBTARGETGETCONNECTIONPARAMETERS callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SPBTARGETGETCONNECTIONPARAMETERS PfnSpbtargetgetconnectionparameters; 

// Definition

WDFAPI PfnSpbtargetgetconnectionparameters 
(
	PSPB_DRIVER_GLOBALS DriverGlobals
	SPBTARGET Target
	SPB_CONNECTION_PARAMETERS *ConnectionParameters
)
{...}

PFN_SPBTARGETGETCONNECTIONPARAMETERS 


```

## -parameters

### -param DriverGlobals: 
### -param Target: 
### -param *ConnectionParameters: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also