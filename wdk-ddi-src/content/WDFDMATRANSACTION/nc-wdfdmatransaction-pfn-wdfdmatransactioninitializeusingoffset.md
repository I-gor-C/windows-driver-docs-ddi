---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONINITIALIZEUSINGOFFSET
title: PFN_WDFDMATRANSACTIONINITIALIZEUSINGOFFSET
author: windows-driver-content
description: 
ms.assetid: efca488c-6c64-4cc1-a407-7a2ba6abed2b
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

# PFN_WDFDMATRANSACTIONINITIALIZEUSINGOFFSET callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONINITIALIZEUSINGOFFSET PfnWdfdmatransactioninitializeusingoffset; 

// Definition

WDFAPI PfnWdfdmatransactioninitializeusingoffset 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMATRANSACTION DmaTransaction
	PFN_WDF_PROGRAM_DMA EvtProgramDmaFunction
	WDF_DMA_DIRECTION DmaDirection
	PMDL Mdl
	size_t Offset
	size_t Length
)
{...}

PFN_WDFDMATRANSACTIONINITIALIZEUSINGOFFSET 


```

## -parameters

### -param DriverGlobals: 
### -param DmaTransaction: 
### -param EvtProgramDmaFunction: 
### -param DmaDirection: 
### -param Mdl: 
### -param Offset: 
### -param Length: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also