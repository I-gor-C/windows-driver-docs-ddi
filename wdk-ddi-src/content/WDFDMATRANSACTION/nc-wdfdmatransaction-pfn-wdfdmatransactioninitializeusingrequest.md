---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONINITIALIZEUSINGREQUEST
title: PFN_WDFDMATRANSACTIONINITIALIZEUSINGREQUEST
author: windows-driver-content
description: 
ms.assetid: ca6bec2f-e2a3-4460-a751-1fcf71c1df31
ms.author: windowsdriverdev
ms.date: 
ms.topic: callback
ms.prod: windows-hardware
ms.technology: windows-devices
req.header: wdfdmatransaction.h
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

# PFN_WDFDMATRANSACTIONINITIALIZEUSINGREQUEST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONINITIALIZEUSINGREQUEST PfnWdfdmatransactioninitializeusingrequest; 

// Definition

WDFAPI PfnWdfdmatransactioninitializeusingrequest 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMATRANSACTION DmaTransaction
	WDFREQUEST Request
	PFN_WDF_PROGRAM_DMA EvtProgramDmaFunction
	WDF_DMA_DIRECTION DmaDirection
)
{...}

PFN_WDFDMATRANSACTIONINITIALIZEUSINGREQUEST 


```

## -parameters

### -param DriverGlobals: 
### -param DmaTransaction: 
### -param Request: 
### -param EvtProgramDmaFunction: 
### -param DmaDirection: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also