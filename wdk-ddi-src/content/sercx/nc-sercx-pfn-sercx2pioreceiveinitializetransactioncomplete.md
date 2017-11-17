---
UID: NC.sercx.PFN_SERCX2PIORECEIVEINITIALIZETRANSACTIONCOMPLETE
title: PFN_SERCX2PIORECEIVEINITIALIZETRANSACTIONCOMPLETE
author: windows-driver-content
description: 
ms.assetid: 65390b23-105b-4a3e-a7c1-f7558fe338b4
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

# PFN_SERCX2PIORECEIVEINITIALIZETRANSACTIONCOMPLETE callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_SERCX2PIORECEIVEINITIALIZETRANSACTIONCOMPLETE PfnSercx2pioreceiveinitializetransactioncomplete; 

// Definition

WDFAPI PfnSercx2pioreceiveinitializetransactioncomplete 
(
	PSERCX_DRIVER_GLOBALS DriverGlobals
	SERCX2PIORECEIVE PioReceive
	BOOLEAN InitSuccess
)
{...}

PFN_SERCX2PIORECEIVEINITIALIZETRANSACTIONCOMPLETE 


```

## -parameters

### -param DriverGlobals: 
### -param PioReceive: 
### -param InitSuccess: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also