---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONSETTRANSFERCOMPLETECALLBACK
title: PFN_WDFDMATRANSACTIONSETTRANSFERCOMPLETECALLBACK
author: windows-driver-content
description: 
ms.assetid: 9800e228-e315-410a-9f46-e115faa99044
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

# PFN_WDFDMATRANSACTIONSETTRANSFERCOMPLETECALLBACK callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONSETTRANSFERCOMPLETECALLBACK PfnWdfdmatransactionsettransfercompletecallback; 

// Definition

WDFAPI PfnWdfdmatransactionsettransfercompletecallback 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMATRANSACTION DmaTransaction
	PFN_WDF_DMA_TRANSACTION_DMA_TRANSFER_COMPLETE DmaCompletionRoutine
	PVOID DmaCompletionContext
)
{...}

PFN_WDFDMATRANSACTIONSETTRANSFERCOMPLETECALLBACK 


```

## -parameters

### -param DriverGlobals: 
### -param DmaTransaction: 
### -param DmaCompletionRoutine: 
### -param DmaCompletionContext: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also