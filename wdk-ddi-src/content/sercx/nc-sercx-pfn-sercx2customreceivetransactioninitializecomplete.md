---
UID: NC.sercx.PFN_SERCX2CUSTOMRECEIVETRANSACTIONINITIALIZECOMPLETE
title: PFN_SERCX2CUSTOMRECEIVETRANSACTIONINITIALIZECOMPLETE
author: windows-driver-content
description: 
ms.assetid: ddcfc15e-867e-40d6-9c2c-0cf3c5faa4bc
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

# PFN_SERCX2CUSTOMRECEIVETRANSACTIONINITIALIZECOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2CUSTOMRECEIVETRANSACTIONINITIALIZECOMPLETE PfnSercx2customreceivetransactioninitializecomplete; 

// Definition

WDFAPI PfnSercx2customreceivetransactioninitializecomplete 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2CUSTOMRECEIVETRANSACTION CustomReceiveTransaction
	BOOLEAN InitSuccess
)
{...}

PFN_SERCX2CUSTOMRECEIVETRANSACTIONINITIALIZECOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param CustomReceiveTransaction: 
### -param InitSuccess: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also