---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONGETBYTESTRANSFERRED
title: PFN_WDFDMATRANSACTIONGETBYTESTRANSFERRED
author: windows-driver-content
description: 
ms.assetid: 1cf5d31b-5212-420f-8f86-ea83f02d7945
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

# PFN_WDFDMATRANSACTIONGETBYTESTRANSFERRED callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONGETBYTESTRANSFERRED PfnWdfdmatransactiongetbytestransferred; 

// Definition

WDFAPI PfnWdfdmatransactiongetbytestransferred 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMATRANSACTION DmaTransaction
)
{...}

PFN_WDFDMATRANSACTIONGETBYTESTRANSFERRED 


```

## -parameters

### -param DriverGlobals: 
### -param DmaTransaction: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also