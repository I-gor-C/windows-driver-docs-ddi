---
UID: NC.sercx.PFN_SERCX2PIOTRANSMITINITIALIZETRANSACTIONCOMPLETE
title: PFN_SERCX2PIOTRANSMITINITIALIZETRANSACTIONCOMPLETE
author: windows-driver-content
description: 
ms.assetid: bd609a64-ff55-42f8-9fd9-2f9527b6b040
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

# PFN_SERCX2PIOTRANSMITINITIALIZETRANSACTIONCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2PIOTRANSMITINITIALIZETRANSACTIONCOMPLETE PfnSercx2piotransmitinitializetransactioncomplete; 

// Definition

WDFAPI PfnSercx2piotransmitinitializetransactioncomplete 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2PIOTRANSMIT PioTransmit
	BOOLEAN InitSuccess
)
{...}

PFN_SERCX2PIOTRANSMITINITIALIZETRANSACTIONCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param PioTransmit: 
### -param InitSuccess: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also