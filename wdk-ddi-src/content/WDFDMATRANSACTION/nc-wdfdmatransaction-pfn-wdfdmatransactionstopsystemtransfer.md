---
UID: NC.wdfdmatransaction.PFN_WDFDMATRANSACTIONSTOPSYSTEMTRANSFER
title: PFN_WDFDMATRANSACTIONSTOPSYSTEMTRANSFER
author: windows-driver-content
description: 
ms.assetid: 7dd183b1-fa97-43ee-b676-b6ce09a8838a
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

# PFN_WDFDMATRANSACTIONSTOPSYSTEMTRANSFER callback function

## -description

Implemented by the client driver to ... 

## -prototype

```
//Declaration

PFN_WDFDMATRANSACTIONSTOPSYSTEMTRANSFER PfnWdfdmatransactionstopsystemtransfer; 

// Definition

WDFAPI PfnWdfdmatransactionstopsystemtransfer 
(
	PWDF_DRIVER_GLOBALS DriverGlobals
	WDFDMATRANSACTION DmaTransaction
)
{...}

PFN_WDFDMATRANSACTIONSTOPSYSTEMTRANSFER 


```

## -parameters

### -param DriverGlobals: 
### -param DmaTransaction: 



## -returns

Returns WDFAPI that ...

## -remarks

Register your implementation of this callback function by setting the appropriate member of <!-- REPLACE ME --> and then calling <!-- REPLACE ME -->.


## -see-also