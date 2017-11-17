---
UID: NC.sercx.PFN_SERCX2PIOTRANSMITCLEANUPTRANSACTIONCOMPLETE
title: PFN_SERCX2PIOTRANSMITCLEANUPTRANSACTIONCOMPLETE
author: windows-driver-content
description: 
ms.assetid: 7634d0d1-370d-4f9f-805a-5d0ce54ca2e8
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

# PFN_SERCX2PIOTRANSMITCLEANUPTRANSACTIONCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2PIOTRANSMITCLEANUPTRANSACTIONCOMPLETE PfnSercx2piotransmitcleanuptransactioncomplete; 

// Definition

WDFAPI PfnSercx2piotransmitcleanuptransactioncomplete 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2PIOTRANSMIT PioTransmit
)
{...}

PFN_SERCX2PIOTRANSMITCLEANUPTRANSACTIONCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param PioTransmit: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also