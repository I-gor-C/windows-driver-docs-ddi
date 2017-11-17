---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONALLOCATERESOURCES
title: PFN_WDFDMATRANSACTIONALLOCATERESOURCES
author: windows-driver-content
description: 
ms.assetid: 758db1d1-230a-4b78-a372-20320b7c6ee1
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

# PFN_WDFDMATRANSACTIONALLOCATERESOURCES callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONALLOCATERESOURCES PfnWdfdmatransactionallocateresources; 

// Definition

WDFAPI PfnWdfdmatransactionallocateresources 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMATRANSACTION DmaTransaction
	WDF_DMA_DIRECTION DmaDirection
	ULONG RequiredMapRegisters
	PFN_WDF_RESERVE_DMA EvtReserveDmaFunction
	PVOID EvtReserveDmaContext
)
{...}

PFN_WDFDMATRANSACTIONALLOCATERESOURCES 


```

## -parameters

### -param DriverGlobals: 
### -param DmaTransaction: 
### -param DmaDirection: 
### -param RequiredMapRegisters: 
### -param EvtReserveDmaFunction: 
### -param EvtReserveDmaContext: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also