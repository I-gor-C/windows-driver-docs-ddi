---
UID: NC.sercx.PFN_SERCX2PIOTRANSMITDRAINFIFOCOMPLETE
title: PFN_SERCX2PIOTRANSMITDRAINFIFOCOMPLETE
author: windows-driver-content
description: 
ms.assetid: a7727329-b974-4400-871c-67567da79171
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

# PFN_SERCX2PIOTRANSMITDRAINFIFOCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2PIOTRANSMITDRAINFIFOCOMPLETE PfnSercx2piotransmitdrainfifocomplete; 

// Definition

WDFAPI PfnSercx2piotransmitdrainfifocomplete 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2PIOTRANSMIT PioTransmit
)
{...}

PFN_SERCX2PIOTRANSMITDRAINFIFOCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param PioTransmit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also