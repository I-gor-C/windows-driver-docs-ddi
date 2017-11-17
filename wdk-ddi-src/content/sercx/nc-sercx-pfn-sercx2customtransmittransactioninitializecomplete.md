---
UID: NC.sercx.PFN_SERCX2CUSTOMTRANSMITTRANSACTIONINITIALIZECOMPLETE
title: PFN_SERCX2CUSTOMTRANSMITTRANSACTIONINITIALIZECOMPLETE
author: windows-driver-content
description: 
ms.assetid: 805381cc-4d21-468e-b3d4-c13cba575374
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

# PFN_SERCX2CUSTOMTRANSMITTRANSACTIONINITIALIZECOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2CUSTOMTRANSMITTRANSACTIONINITIALIZECOMPLETE PfnSercx2customtransmittransactioninitializecomplete; 

// Definition

WDFAPI PfnSercx2customtransmittransactioninitializecomplete 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2CUSTOMTRANSMITTRANSACTION CustomTransmitTransaction
	BOOLEAN InitSuccess
)
{...}

PFN_SERCX2CUSTOMTRANSMITTRANSACTIONINITIALIZECOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param CustomTransmitTransaction: 
### -param InitSuccess: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also