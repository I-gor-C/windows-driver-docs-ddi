---
UID: NC.sercx.PFN_SERCX2PIOTRANSMITREADY
title: PFN_SERCX2PIOTRANSMITREADY
author: windows-driver-content
description: 
ms.assetid: 43447f96-e1d2-4b21-9d30-c3211f52f162
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

# PFN_SERCX2PIOTRANSMITREADY callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2PIOTRANSMITREADY PfnSercx2piotransmitready; 

// Definition

WDFAPI PfnSercx2piotransmitready 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2PIOTRANSMIT PioTransmit
)
{...}

PFN_SERCX2PIOTRANSMITREADY 


```

## -parameters

### -param DriverGlobals: 
### -param PioTransmit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also