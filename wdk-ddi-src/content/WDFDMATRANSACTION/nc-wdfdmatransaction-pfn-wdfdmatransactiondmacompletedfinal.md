---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONDMACOMPLETEDFINAL
title: PFN_WDFDMATRANSACTIONDMACOMPLETEDFINAL
author: windows-driver-content
description: 
ms.assetid: 40dd01f9-5846-48fc-a03e-111b2e887ed5
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

# PFN_WDFDMATRANSACTIONDMACOMPLETEDFINAL callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONDMACOMPLETEDFINAL PfnWdfdmatransactiondmacompletedfinal; 

// Definition

WDFAPI PfnWdfdmatransactiondmacompletedfinal 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMATRANSACTION DmaTransaction
	size_t FinalTransferredLength
	NTSTATUS *Status
)
{...}

PFN_WDFDMATRANSACTIONDMACOMPLETEDFINAL 


```

## -parameters

### -param DriverGlobals: 
### -param DmaTransaction: 
### -param FinalTransferredLength: 
### -param *Status: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also