---
UID: NC.sercx.PFN_SERCX2CUSTOMTRANSMITTRANSACTIONCLEANUPCOMPLETE
title: PFN_SERCX2CUSTOMTRANSMITTRANSACTIONCLEANUPCOMPLETE
author: windows-driver-content
description: 
ms.assetid: 9df978f1-3010-4ccb-81a4-037b7418af89
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

# PFN_SERCX2CUSTOMTRANSMITTRANSACTIONCLEANUPCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2CUSTOMTRANSMITTRANSACTIONCLEANUPCOMPLETE PfnSercx2customtransmittransactioncleanupcomplete; 

// Definition

WDFAPI PfnSercx2customtransmittransactioncleanupcomplete 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2CUSTOMTRANSMITTRANSACTION CustomTransmitTransaction
)
{...}

PFN_SERCX2CUSTOMTRANSMITTRANSACTIONCLEANUPCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param CustomTransmitTransaction: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also