---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONGETREQUEST
title: PFN_WDFDMATRANSACTIONGETREQUEST
author: windows-driver-content
description: 
ms.assetid: 5756d46b-8730-498c-a222-c7a278adae55
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

# PFN_WDFDMATRANSACTIONGETREQUEST callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONGETREQUEST PfnWdfdmatransactiongetrequest; 

// Definition

WDFAPI PfnWdfdmatransactiongetrequest 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMATRANSACTION DmaTransaction
)
{...}

PFN_WDFDMATRANSACTIONGETREQUEST 


```

## -parameters

### -param DriverGlobals: 
### -param DmaTransaction: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also