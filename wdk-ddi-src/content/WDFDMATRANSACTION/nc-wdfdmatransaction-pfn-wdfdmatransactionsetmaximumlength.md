---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONSETMAXIMUMLENGTH
title: PFN_WDFDMATRANSACTIONSETMAXIMUMLENGTH
author: windows-driver-content
description: 
ms.assetid: e6106824-5a32-475f-b892-82b2ba2ff41e
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

# PFN_WDFDMATRANSACTIONSETMAXIMUMLENGTH callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONSETMAXIMUMLENGTH PfnWdfdmatransactionsetmaximumlength; 

// Definition

WDFAPI PfnWdfdmatransactionsetmaximumlength 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMATRANSACTION DmaTransaction
	size_t MaximumLength
)
{...}

PFN_WDFDMATRANSACTIONSETMAXIMUMLENGTH 


```

## -parameters

### -param DriverGlobals: 
### -param DmaTransaction: 
### -param MaximumLength: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also